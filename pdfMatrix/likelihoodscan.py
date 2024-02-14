
import sys
import os
import ROOT
import array
import argparse 
import numpy as np
from scipy import interpolate, optimize

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default="", help="ROOT input file")
parser.add_argument("--label", type=str, default="", help="Label")
parser.add_argument("-o", "--outName", type=str, default="", help="Output name")
parser.add_argument("--outFolder", type=str, default="", help='Output dir')
args = parser.parse_args()


def findCrossing(xv, yv, left=True, flip=125, cross=1.):
    x = np.array(xv)
    y = np.array(yv)
    minx = x[np.argmin(y)]
    interp_fn = interpolate.interp1d(x, y, 'quadratic')
    interp_fn2 = lambda x: interp_fn(x)-1 # 68% CL
    unc_m, unc_p = optimize.newton(interp_fn2, minx-5), optimize.newton(interp_fn2, minx+5)
    
    unc_avg = 0.5*(abs(minx-unc_m) + abs(unc_p-minx))
    #print(unc_m, unc_p, unc_avg, minx)
    return unc_m, unc_p, unc_avg, minx

def analyzeMass(fInName, outDir, outName, label):
    #print(fInName, outDir, outName, label)
    if not os.path.exists(outDir): os.makedirs(outDir)

    fIn = ROOT.TFile(fInName, "READ")
    t = fIn.Get("fitresults")

    xv, yv = [], []
    yMin_, xMin_ = 1e9, 1e9
    for i in range(1, t.GetEntries()): # first one is Hessian?
        t.GetEntry(i)
        mass = getattr(t, "massShiftW100MeV")*100.
        xv.append(mass)
        deltaNLL = t.dnllval*2.  # t.nllvalfull
        if deltaNLL < yMin_:
            yMin_ = deltaNLL
            xMin_ = mass
        yv.append(deltaNLL)
        #print(mass, deltaNLL, t.nllval, t.nllvalfull)
    yv = [k - yMin_ for k in yv] # DeltaNLL
    xv, yv = zip(*sorted(zip(xv, yv)))
    g_nll = ROOT.TGraph(len(xv), array.array('d', xv), array.array('d', yv))

    # bestfit = minimum
    unc_m, unc_p, unc, x_min = findCrossing(xv, yv, left=True)

    # TF1 for Hessian unc
    t.GetEntry(0)
    x_min_hess = t.massShiftW100MeV_noi*100.
    unc_hess = t.massShiftW100MeV_noi_err*100.
    a_ = 1./(unc_hess**2)
    g_nll_hess = ROOT.TF1("parabola_func", f"{a_}*(x-{x_min_hess})*(x-{x_min_hess})", x_min_hess-3*unc_hess, x_min_hess+3*unc_hess)
    g_nll_hess.SetLineColor(ROOT.kBlue)
    g_nll_hess.SetLineWidth(2)


    #############################################
    c = ROOT.TCanvas("c", "c", 1000, 1000)
    c.SetTopMargin(0.055)
    c.SetRightMargin(0.05)
    c.SetLeftMargin(0.15)
    c.SetBottomMargin(0.11)
    c.SetGrid()


    g_nll.GetXaxis().SetTitle("m_{W} (GeV)")
    #g_nll.GetXaxis().SetRangeUser(-15, 15)
    
    g_nll.SetMarkerStyle(20)
    g_nll.SetMarkerColor(ROOT.kRed)
    g_nll.SetMarkerSize(1)
    g_nll.SetLineColor(ROOT.kRed)
    g_nll.SetLineWidth(2)

    g_nll.GetXaxis().SetTitleFont(43)
    g_nll.GetXaxis().SetTitleSize(40)
    g_nll.GetXaxis().SetLabelFont(43)
    g_nll.GetXaxis().SetLabelSize(35)
    g_nll.GetXaxis().SetTitleOffset(1.2*g_nll.GetXaxis().GetTitleOffset())
    g_nll.GetXaxis().SetLabelOffset(1.2*g_nll.GetXaxis().GetLabelOffset())
    g_nll.GetYaxis().SetTitle("-2#DeltaNLL")

    g_nll.GetYaxis().SetTitleFont(43)
    g_nll.GetYaxis().SetTitleSize(40)
    g_nll.GetYaxis().SetLabelFont(43)
    g_nll.GetYaxis().SetLabelSize(35)

    g_nll.GetYaxis().SetTitleOffset(1.7*g_nll.GetYaxis().GetTitleOffset())
    g_nll.GetYaxis().SetLabelOffset(1.4*g_nll.GetYaxis().GetLabelOffset())
    
    #g_nll.Draw("HIST")
    g_nll.Draw("ALP")
    g_nll_hess.Draw("L SAME")

    leg = ROOT.TLegend(.20, 0.78, 0.85, .92)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.03)
    leg.SetMargin(0.15)
    leg.SetBorderSize(1)
    leg.SetHeader(label)
    leg.AddEntry(g_nll, "Likelihood scan m_{W} = %.2f #pm %.2f MeV" % (x_min, unc), "LP")
    leg.AddEntry(g_nll_hess, "Hessian m_{W} = %.2f #pm %.2f MeV" % (x_min_hess, unc_hess), "LP")
    leg.Draw()

    c.Modify()
    c.Update()
    c.Draw()
    c.SaveAs(f"{outDir}/{outName}.png")
    c.SaveAs(f"{outDir}/{outName}.pdf")


def main():
    analyzeMass(args.input, args.outFolder, args.outName, args.label)

if __name__ == "__main__":
    main()
