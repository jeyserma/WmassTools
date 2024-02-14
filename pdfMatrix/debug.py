import narf
import narf.combineutils
import os

import numpy as np
import boost_histogram as bh
import hist
import wremnants.histselections as histselections
import mplhep as hep

import matplotlib as mpl
mpl.use('Agg') # batch mode
import matplotlib.pyplot as plt

s = hist.tag.Slicer()

font = {'size': 22}
mpl.rc('font', **font)



def get_hists(debug, ch="ch0", proc="Wmunu"):
    hist_nom = debug.nominal_hists[ch]
    hist_systs = debug.syst_hists[ch]

    hist_nom = hist_nom[{'processes': proc}]
    hist_systs = hist_systs[{'processes': proc}]

    return hist_nom, hist_systs


def plot_hist(hist_nom_, hist_systs_, syst_name="massShiftW100MeV", out_dir="./", charge="combined"):
    print(syst_name)
    if charge=="combined": q = s[::hist.sum]
    elif charge=="plus": q=1j
    elif charge=="minus": q=-1j 
    hist_nom = hist_nom_[{'charge': q}]
    h_up_mass = hist_systs_[{'DownUp': 'Up', 'systs': "massShiftW100MeV", 'charge': q}]
    h_dw_mass = hist_systs_[{'DownUp': 'Down', 'systs': "massShiftW100MeV", 'charge': q}]

    h_up = hist_systs_[{'DownUp': 'Up', 'systs': syst_name, 'charge': q}]
    h_dw = hist_systs_[{'DownUp': 'Down', 'systs': syst_name, 'charge': q}]

    hist_nom = histselections.unrolledHist(hist_nom)
    h_up = histselections.unrolledHist(h_up)
    h_dw = histselections.unrolledHist(h_dw)
    h_up_mass = histselections.unrolledHist(h_up_mass)
    h_dw_mass = histselections.unrolledHist(h_dw_mass)

    bin_edges = hist_nom.axes[0].edges

    fig, (ax_main, ax_ratio) = plt.subplots(
        nrows=2, sharex=True, gridspec_kw={"height_ratios": [2, 1], "hspace": 0}, figsize=(15, 10)
    )

    #ax_main.hist(hist_nom.axes[0].centers, bins=hist_nom.axes[0].edges, weights=hist_nom.view(), color='lightblue', linewidth=1.2)
    ax_main.plot(hist_nom.axes[0].centers, hist_nom.view(), color="black", linestyle='-')

    ax_main.set_xlim(0, 1440)
    ax_main.set_ylabel("Events")
    ax_main.set_title(f'Variation {syst_name}')
    #ax_main.legend()

    ratio_up = h_up / hist_nom
    ratio_dw = h_dw / hist_nom
    ratio_up_mass = h_up_mass / hist_nom
    ratio_dw_mass = h_dw_mass / hist_nom
    ratio_up_mass = (ratio_up_mass - 1.)*0.1 + 1.
    ratio_dw_mass = (ratio_dw_mass - 1.)*0.1 + 1.
    ax_ratio.axhline(y=1, color='black', linestyle='-')
    plt_mass, = ax_ratio.plot(ratio_up_mass.axes[0].centers, ratio_up_mass.view(), color="gray", linestyle='-')
    ax_ratio.plot(ratio_dw_mass.axes[0].centers, ratio_dw_mass.view(), color="gray", linestyle='-')
    plt_up, = ax_ratio.plot(ratio_up.axes[0].centers, ratio_up.view(), color="blue", linestyle='-')
    plt_dw, = ax_ratio.plot(ratio_dw.axes[0].centers, ratio_dw.view(), color="red", linestyle='-')


    ax_ratio.set_xlabel(r"Unrolled $p_{T}-\eta$")
    ax_ratio.set_ylabel("Ratio")
    ax_main.legend([plt_mass, plt_up, plt_dw],['10 MeV mass variation', 'Up variation', 'Down variation'], loc="upper right")

    plt.savefig(f"{out_dir}/{syst_name}.png")
    plt.close(fig)


def main():

    pdfs = ["msht20", "msht20an3lo", "ct18", "herapdf20"]
    charges = ["combined", "plus", "minus"]
    tags = ["Lin", "Quadr", "Avg", "None"]
    baseDir = "/home/submit/jaeyserm/public_html/wmass/systs_pdf/"
    
    pdfs = ["msht20an3lo", "ct18", "herapdf20"]
    tags = ["None"]
    baseDir = "/home/submit/jaeyserm/public_html/wmass/systs_pdf/"
    
    for tag in tags:
        for pdf in pdfs:
            filename = f"/scratch/submit/cms/jaeyserm/CombineStudies/pdfMatrix//mw_pdfOnly_sym{tag}_symHess/WMass_eta_pt_charge_{pdf}//WMass.hdf5"
            indata = narf.combineutils.FitInputData(filename)
            debug = narf.combineutils.FitDebugData(indata)

            proc = "Wmunu"
            hist_nom, hist_systs = get_hists(debug)
            for syst_name in debug.nonzeroSysts(procs="Wmunu"):
                syst_name=syst_name.decode('ASCII')
                print(syst_name)
                #if not ("resumFOScale" in syst_name or "QCDscale" in syst_name):
                #    continue
                for charge in charges:
                    out_dir = f"{baseDir}/{pdf}/sym{tag}_symHess/W_{charge}/"
                    print(out_dir)
                    if not os.path.exists(out_dir):
                        os.makedirs(out_dir)
                    plot_hist(hist_nom, hist_systs, syst_name=syst_name, out_dir=out_dir, charge=charge)

if __name__ == "__main__":
    main()