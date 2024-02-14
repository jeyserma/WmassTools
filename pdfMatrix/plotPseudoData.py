import narf
import narf.combineutils
import os
import argparse

import numpy as np
import boost_histogram as bh
import hist
import wremnants.histselections as histselections
from utilities import boostHistHelpers as hh,common
import mplhep as hep

import matplotlib as mpl
mpl.use('Agg') # batch mode
import matplotlib.pyplot as plt

s = hist.tag.Slicer()

font = {'size': 22}
mpl.rc('font', **font)






def get_hists(debug, ch="ch0", proc="Wmunu"):
    hist_nom_ = debug.nominal_hists[ch]
    hist_nom = hist_nom_[{'processes': proc}]
    hist_bkgs = hist_nom_[{'processes':  [x for x in hist_nom_.axes["processes"] if x != proc]}]
    hist_bkgs = hist_bkgs[..., hist.sum]

    hist_systs = debug.syst_hists[ch]
    hist_systs = hist_systs[{'processes': proc}]

    hist_obs = debug.data_obs_hists[ch]

    hist_obs = hist_obs + hist_bkgs*(-1.)
    return hist_nom, hist_systs, hist_obs


def plot_hist(hist_nom_, hist_systs_, hist_obs_, syst_name="massShiftW100MeV", out_dir="./", out_name="", source_pdf="", target_pdf="", charge="combined"):
    if charge=="combined": q = s[::hist.sum]
    elif charge=="plus": q=1j
    elif charge=="minus": q=-1j 
    hist_nom = hist_nom_[{'charge': q}]
    hist_obs = hist_obs_[{'charge': q}]
    hist_systs = hist_systs_[{'charge': q}]
    h_up_mass = hist_systs_[{'DownUp': 'Up', 'systs': "massShiftW100MeV", 'charge': q}]
    h_dw_mass = hist_systs_[{'DownUp': 'Down', 'systs': "massShiftW100MeV", 'charge': q}]

    print(source_pdf, target_pdf)
    print(hist_systs)
    hist_systs_noAS = hist_systs[{'systs':  [x for x in hist_systs.axes["systs"] if x not in ["massShiftW100MeV", "pdfAlphaS", "pdfAlphaSSymAvg", "pdfAlphaSSymDiff"]]}]
    
    hist_systs_AS = hist_systs[{'systs':  [x for x in hist_systs.axes["systs"] if x in ["pdfAlphaS", "as", "pdfAlphaSSymAvg", "pdfAlphaSSymDiff", "asSymAvg", "asSymDiff"]]}] # as for nnpdf31, to be checked
    #if 'pdfAlphaS' in hist_systs.axes["systs"]:
    #    hist_systs_AS = hist_systs[{'systs': 'pdfAlphaS'}]
    #else:
    #    hist_systs_AS = hist_nom*0.


    h_up = hist_systs_noAS[{'DownUp': 'Up'}]
    h_dw = hist_systs_noAS[{'DownUp': 'Down'}]
    h_up, x = hh.rssHist(h_up, 'systs') # sum in quadrature -- need to remove massShift?
    y, h_dw = hh.rssHist(h_dw, 'systs')
    
    h_up_AS = hist_systs_AS[{'DownUp': 'Up'}]
    h_dw_AS = hist_systs_AS[{'DownUp': 'Down'}]
    h_up_AS, x = hh.rssHist(h_up_AS, 'systs')
    y, h_dw_AS = hh.rssHist(h_dw_AS, 'systs')

    hist_nom = histselections.unrolledHist(hist_nom)
    hist_obs = histselections.unrolledHist(hist_obs)
    h_up_mass = histselections.unrolledHist(h_up_mass)
    h_dw_mass = histselections.unrolledHist(h_dw_mass)

    h_up = histselections.unrolledHist(h_up)
    h_dw = histselections.unrolledHist(h_dw)
    
    h_up_AS = histselections.unrolledHist(h_up_AS)
    h_dw_AS = histselections.unrolledHist(h_dw_AS)

    bin_edges = hist_nom.axes[0].edges

    fig, (ax_main, ax_ratio) = plt.subplots(
        nrows=2, sharex=True, gridspec_kw={"height_ratios": [2, 1], "hspace": 0}, figsize=(15, 10)
    )

    plt_nom, = ax_main.plot(hist_nom.axes[0].centers, hist_nom.view(), color="black", linestyle='-')
    #ax_main.plot(hist_obs.axes[0].centers, hist_obs.view(), color="red", linestyle='-')

    ax_main.set_xlim(0, 1440)
    ax_main.set_ylabel("Events")
    ax_main.set_title(f'{source_pdf} $\\rightarrow$ {target_pdf}')
    #ax_main.legend()

    ratio = hist_obs / hist_nom
    ratio_up = h_up / hist_nom
    ratio_dw = h_dw / hist_nom
    ratio_up_AS = h_up_AS / hist_nom
    ratio_dw_AS = h_dw_AS / hist_nom
    ratio_up_mass = h_up_mass / hist_nom
    ratio_dw_mass = h_dw_mass / hist_nom
    ratio_up_mass = (ratio_up_mass - 1.)*0.1 + 1.
    ratio_dw_mass = (ratio_dw_mass - 1.)*0.1 + 1.
    ax_ratio.axhline(y=1, color='black', linestyle='-')
    plt_mass, = ax_ratio.plot(ratio_up_mass.axes[0].centers, ratio_up_mass.view(), color="gray", linestyle='-')
    ax_ratio.plot(ratio_dw_mass.axes[0].centers, ratio_dw_mass.view(), color="gray", linestyle='-')
    plt_ratio, = ax_ratio.plot(ratio.axes[0].centers, ratio.view(), color="violet", linestyle='-')
    plt_up, = ax_ratio.plot(ratio_up.axes[0].centers, ratio_up.view(), color="red", linestyle='-')
    plt_dw, = ax_ratio.plot(ratio_dw.axes[0].centers, ratio_dw.view(), color="red", linestyle='-')
    plt_up_AS, = ax_ratio.plot(ratio_up_AS.axes[0].centers, ratio_up_AS.view(), color="blue", linestyle='-')
    plt_dw_AS, = ax_ratio.plot(ratio_dw_AS.axes[0].centers, ratio_dw_AS.view(), color="blue", linestyle='-')

    ax_ratio.set_xlabel(r"Unrolled $p_{T}-\eta$ bins")
    ax_ratio.set_ylabel("Ratio")
    ax_main.legend([plt_mass, plt_ratio, plt_nom, plt_up, plt_up_AS],['10 MeV mass variation', f"Pseudo: {target_pdf}", f"Nominal: {source_pdf}", "PDF unc.", "AlphaS unc."], loc="upper right")

    
    out_ = f"{out_dir}/{out_name}_{charge}.png"
    print(out_)
    plt.savefig(out_)
    plt.savefig(out_.replace("/mw_", "/mw_pdfOnly_"))
    plt.close(fig)


def main(args):
    inflationFactor = args.inflationFactor
    fitType = args.postfix

    charges = ["combined", "plus", "minus"]
    pdf_tags = ["msht20", "nnpdf40", "ct18", "nnpdf31", "pdf4lhc21", "herapdf20", "msht20an3lo"]
    pdf_names = ["pdfMSHT20", "pdfNNPDF40", "pdfCT18", "pdfNNPDF31", "pdfPDF4LHC21", "pdfHERAPDF20", "pdfMSHT20an3lo"]
    tags = ["None"]
    baseDir = "/home/submit/jaeyserm/public_html/wmass/pdfMatrix/pseudoDataPlots"
    
    combine_dir = "/scratch/submit/cms/jaeyserm/CombineStudies/pdfMatrix/"
    web_dir = "/work/submit/jaeyserm/public_html/wmass/fits/pdfMatrix/"
    
    if inflationFactor == 1.:
        combine_dir = f"{combine_dir}/mw_pdfOnly_{fitType}"
        web_dir = f"{web_dir}/mw_{fitType}" 
    else:
        t = str(inflationFactor).replace(".", "p")
        combine_dir = f"{combine_dir}/mw_infl_{t}_pdfOnly_{fitType}"
        web_dir = f"{web_dir}/mw_infl_{t}_{fitType}" 
    
    for pdf_source in pdf_tags:
        for pdf_target in pdf_tags:
            filename = f"{combine_dir}/WMass_eta_pt_charge_{pdf_source}//WMass.hdf5"
            pdf_target_name = pdf_names[pdf_tags.index(pdf_target)]
            indata = narf.combineutils.FitInputData(filename, pseudodata=f"{pdf_target_name}_pdfVar")
            
            debug = narf.combineutils.FitDebugData(indata)
            hist_nom, hist_systs, hist_obs = get_hists(debug)

            out_dir = f"{web_dir}/{pdf_source}/{pdf_target}/"
            if not os.path.isdir(out_dir):
                    os.makedirs(out_dir)
            for charge in charges: 
                plot_hist(hist_nom, hist_systs, hist_obs, out_dir=out_dir, out_name="pseudodata", source_pdf=pdf_source, target_pdf=pdf_target, charge=charge)
                

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inflationFactor", type=float, default=1.0, help="PDF inflation factor")
    parser.add_argument("--postfix", type=str, default="symNone", help='Postfix')
    args = parser.parse_args()

    main(args)