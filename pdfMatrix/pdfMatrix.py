import os
import argparse 
import itertools
import glob

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", type=str, help="Calculation mode", default="", choices=["histmaker", "combine", "fit", "fitth", "matrixl", "matrixh", "summary", "impacts", "lscan", "diagnostics", "matrixext", "check"])
parser.add_argument("--fitType", type=str, help="Fit type", default="mw", choices=["mw", "wlike", "mw_agn"])

parser.add_argument("--histmaker_dir", type=str, default="/scratch/submit/cms/jaeyserm/Analysis/new/", help='output folder for combine files')
parser.add_argument("--combine_dir", type=str, default="/scratch/submit/cms/jaeyserm/CombineStudies/pdfMatrix/", help='output folder for combine files')
parser.add_argument("--web_dir", type=str, default="/work/submit/jaeyserm/public_html/wmass/fits/pdfMatrix/", help='output folder for combine files')


parser.add_argument("--inflationFactor", type=float, default=1.0, help="PDF inflation factor")

parser.add_argument("-d", "--debug", action='store_true', help="Debug mode - do not execute commands")
parser.add_argument("-p", "--pdfOnly", action='store_true', help="Do fit with PDF+AS uncertainties only")
parser.add_argument("-n", "--nohup", action='store_true', help="Run fits in background using nohup")
parser.add_argument("--skipCheckDir", action='store_true', help="Make directory")


parser.add_argument("--nThreads", type=int, default=1, help="Number of threads")

parser.add_argument("--postfix", type=str, default="", help='Postfix')

parser.add_argument("--fit_pdf_source", type=str, default="", help='Source PDF')
parser.add_argument("--fit_pdf_target", type=str, default="", help='Target PDF')

parser.add_argument("-s", "--scan", action='store_true', help="Run likelihood scan")
parser.add_argument("-x", "--xsec", action='store_true', help="Let xsec float")

args = parser.parse_args()

#print("add saturated")
#quit()
def exe(cmd):
    if args.debug:
        print(cmd)
    else:
        os.system(cmd)

if __name__ == "__main__":

    pdf_tags = ["msht20", "nnpdf40", "ct18", "ct18z", "nnpdf31", "pdf4lhc21", "herapdf20", "msht20an3lo"]
    pdf_names = ["pdfMSHT20", "pdfNNPDF40", "pdfCT18", "pdfCT18Z", "pdfNNPDF31", "pdfPDF4LHC21", "pdfHERAPDF20", "pdfMSHT20an3lo"]
    isW = "mw" in args.fitType
    histmaker_output = "mw_with_mu_eta_pt_scetlib_dyturboCorr" if isW else "mz_wlike_with_mu_eta_pt_scetlib_dyturboCorr"
    inflationFactor = args.inflationFactor

    t = str(args.inflationFactor).replace(".", "p")
    combine_dir = f"{args.combine_dir}/{args.fitType}_infl_{t}"
    web_dir = f"{args.web_dir}/{args.fitType}_infl_{t}"

    if args.pdfOnly:
        combine_dir += "_pdfOnly"
        web_dir += "_pdfOnly"
    if args.postfix:
        combine_dir += f"_{args.postfix}"
        web_dir += f"_{args.postfix}"
    if args.xsec:
        combine_dir += f"_xsec"
        web_dir += f"_xsec"

    if not os.path.isdir(combine_dir) and not args.skipCheckDir:
        print(f"Combine directory {combine_dir} does not exist")
        quit()
    else:
        if not os.path.isdir(combine_dir):
            os.makedirs(combine_dir)

    if not os.path.isdir(web_dir):
        os.makedirs(web_dir)

    perms_set = set(tuple([pdf] + pdf_tags[:i] + pdf_tags[i+1:]) for i, pdf in enumerate(pdf_tags))
    pdf_perms = [list(t) for t in perms_set]


    if args.mode == "histmaker":
        print(f"Run {args.histmaker} histmaker")


    if args.mode == "combine":
        if os.path.isdir(combine_dir) and len(os.listdir(combine_dir)) != 0 and not args.skipCheckDir:
            print(f"Combine directory {combine_dir} not empty")
            quit()

        for pdfs in pdf_perms:
            base_pdf = pdfs[0]
            pseudo_pdfs = pdfs
            base_pdf_name = pdf_names[pdf_tags.index(base_pdf)]
            pseudo_pdf_names = [pdf_names[pdf_tags.index(pdf)] for pdf in pseudo_pdfs]

            if "_agn" in args.fitType and base_pdf != "msht20":
                continue # only msht20 as central one for agn

            # {args.histmaker_dir}/{histmaker_output}_{base_pdf}_symmHess.hdf5
            cmd = f"python3 scripts/combine/setupCombine.py -i {args.histmaker_dir}/{histmaker_output}_{base_pdf}_symHess.hdf5 -o {combine_dir} --pseudoData {' '.join(pseudo_pdf_names)} -p {base_pdf} --hdf5 --scalePdf {inflationFactor} --pseudoDataAxes pdfVar "
            if "_agn" in args.fitType:
                # --theoryAgnosticBandSize 2
                #cmd += f" --theoryAgnostic --poiAsNoi --sparse  --noPDFandQCDtheorySystOnSignal  " # cfg0 all unc #  --doStatOnly --filterProcGroups Wmunu
                #cmd += f" --theoryAgnostic --poiAsNoi --sparse  " # cfg2 all unc # cfg2
                cmd += f" --theoryAgnostic --poiAsNoi --sparse  --noPDFandQCDtheorySystOnSignal" # cfg1 #  --noPDFandQCDtheorySystOnSignal --doStatOnly
                #cmd += f" --theoryAgnostic --poiAsNoi --sparse --excludeNuisances '.*' --keepNuisances '^(.*{base_pdf_name[3:]}.*|.*Weight{'W' if isW else 'Z'}.*|.*Shift{'W' if isW else 'Z'}.*|.*norm{'W' if isW else 'Z'}.*|.*yieldsTheoryAgnostic.*|.*Alpha.*)$'  "
            if args.pdfOnly:
                if "_agn" in args.fitType:
                    cmd += f" --excludeNuisances '.*' --keepNuisances '^(.*Weight{'W' if isW else 'Z'}.*|.*Shift{'W' if isW else 'Z'}.*|.*norm{'W' if isW else 'Z'}.*|.*yieldsTheoryAgnostic.*|.*Alpha.*)$' "  
                    #cmd += f" --excludeNuisances '.*' --keepNuisances '^(.*{base_pdf_name[3:]}.*|.*Weight{'W' if isW else 'Z'}.*|.*Shift{'W' if isW else 'Z'}.*|.*norm{'W' if isW else 'Z'}.*|.*yieldsTheoryAgnostic.*|.*Alpha.*)$' "  
                    # no PDF unc for agn, only the norms and mass shift
                else:
                    cmd += f" --excludeNuisances '.*' --keepNuisances '^(.*{base_pdf_name[3:]}.*|.*Weight{'W' if isW else 'Z'}.*|.*Shift{'W' if isW else 'Z'}.*|.*Alpha.*)$' "
            
            if args.xsec:
                cmd += " --fitXsec "
            
            exe(cmd)

    if args.mode == "fit":
        for pdfs in pdf_perms:
            base_pdf = pdfs[0]
            pseudo_pdfs = pdfs
            if "_agn" in args.fitType and base_pdf != "msht20":
                continue # only msht20 as central one for agn
            #if base_pdf != "herapdf20":
            # fit_pdf_source
            if args.fit_pdf_source and args.fit_pdf_source != base_pdf:
                continue
            #    continue
            for pseudo_pdf in pseudo_pdfs:
                pseudo_pdf_name = pdf_names[pdf_tags.index(pseudo_pdf)]
                if args.fit_pdf_target and args.fit_pdf_target != pseudo_pdf:
                    continue
                working_dir = glob.glob(f"{combine_dir}/*{base_pdf}")[0]
                scan = " --scan massShiftW100MeV_noi --scanRange 2 " if args.scan else ""
                if args.nohup:
                    cmd = f"nohup combinetf.py --saveHists --computeHistErrors --doImpacts --binByBinStat {working_dir}/{'WMass' if isW else 'ZMassWLike'}.hdf5 -p {pseudo_pdf_name}_pdfVar {scan} -o {working_dir}/fit_{pseudo_pdf}.root --nThreads {args.nThreads} --fitverbose 10 > {working_dir}/fit_{pseudo_pdf}.log &"
                else:
                    cmd = f"combinetf.py --saveHists --computeHistErrors --doImpacts --binByBinStat {working_dir}/{'WMass' if isW else 'ZMassWLike'}.hdf5 -p {pseudo_pdf_name}_pdfVar {scan} -o {working_dir}/fit_{pseudo_pdf}.root --fitverbose 10"
                #print(cmd)
                exe(cmd)


    if args.mode == "fitth":
        tag = "scetlib" # scetlib minnlo
        combine_dir = combine_dir.replace("pdfMatrix", "pdfMatrix_scetlib")
        base_pdf = "msht20an3lo"

        for pseudo_pdf in pdf_tags:
            pseudo_pdf_name = pdf_names[pdf_tags.index(pseudo_pdf)]
            print(f"{combine_dir}/*{base_pdf}")
            working_dir = glob.glob(f"{combine_dir}/*{base_pdf}_{tag}")[0]
            if args.nohup:
                cmd = f"nohup combinetf.py --saveHists --computeHistErrors --doImpacts --binByBinStat {working_dir}/{'WMass' if isW else 'ZMassWLike'}.hdf5 -p {pseudo_pdf_name} -o {working_dir}/fit_{pseudo_pdf}.root  --nThreads 15 --fitverbose 10 > {working_dir}/fit_{pseudo_pdf}.log &"
            else:
                cmd = f"combinetf.py --saveHists --computeHistErrors --doImpacts --binByBinStat {working_dir}/{'WMass' if isW else 'ZMassWLike'}.hdf5 -p {pseudo_pdf_name} -o {working_dir}/fit_{pseudo_pdf}.root --fitverbose 10"
            exe(cmd)

    if args.mode == "matrixls":
        import uproot
        from utilities.io_tools import combinetf_input

        t = f"\\begin{{tabular}}{{l|{'c'*len(pdf_tags)}}} \n"
        t += f"Model + & \multicolumn{{{len(pdf_tags)}}}{{c}}{{Pseudodata}}  \\\ \n"
        t += f"Uncertainty & {' & '.join([p[3:] for p in pdf_names])} \\\ \n"
        t += "\hline \n"
        for base_pdf in pdf_tags:
            if "_agn" in args.fitType and base_pdf != "msht20":
                continue # only msht20 as central one for agn
            #if base_pdf != "herapdf20":
            #    continue
            l = pdf_names[pdf_tags.index(base_pdf)][3:]
            base_pdf_name = pdf_names[pdf_tags.index(base_pdf)]
            for pseudo_pdf in pdf_tags:
                working_dir = glob.glob(f"{combine_dir}/*{base_pdf}")[0]
                fitresult = combinetf_input.get_fitresult(f"{working_dir}/fit_{pseudo_pdf}.root")
                pois = combinetf_input.get_poi_names(fitresult, poi_type=None)
                impacts, labels, _ = combinetf_input.read_impacts_poi(fitresult, True, add_total=True, poi=pois[0], normalize=False)
                labels = list(labels)
                if "_agn" in args.fitType:
                    unc_tot = impacts[labels.index('Total')]*100.
                    unc_pdf = impacts[labels.index('normXsecW')]*100.
                else:
                    unc_tot = impacts[labels.index('Total')]*100.
                    unc_pdf = impacts[labels.index(base_pdf_name)]*100. # including AS +"NoAlphaS"
                
                pulls, constraints, pulls_prefit = combinetf_input.get_pulls_and_constraints(f"{working_dir}/fit_{pseudo_pdf}.root", [f"massShift{'W' if isW else 'Z'}100MeV"])
                pull = 100.*pulls[0]
                if abs(pull) > unc_pdf:
                    #l += ' & \\cellcolor{{red!25}} ${:.1f} \pm {:.1f}$'.format(pull, unc)
                    l += ' & \\cellcolor{{red!25}} ${:.1f} \pm {:.1f} ({:.1f})$'.format(pull, unc_pdf, unc_tot)
                else:
                    if base_pdf == pseudo_pdf:
                        #l += ' & \\cellcolor{{lightgray!25}} ${:.1f} \pm {:.1f}$'.format(pull, unc)
                        l += ' & \\cellcolor{{lightgray!25}} ${:.1f} \pm {:.1f} ({:.1f})$'.format(pull, unc_pdf, unc_tot)
                    else:
                        #l += ' & ${:.1f} \pm {:.1f}$'.format(pull, unc)
                        l += ' & ${:.1f} \pm {:.1f} ({:.1f})$'.format(pull, unc_pdf, unc_tot)
            l += " \\\ \n"
            t += l
        t += "\\end{tabular}"
        print(t)

    if args.mode == "matrixh":
        import uproot
        from utilities.io_tools import combinetf_input

        t = '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        body, html {
            font: 16px Arial;
            text-align: center;
            padding = 0;
            margin = 0;
        }
        table, th, td {
          border: 1px solid black;
          border-style:solid;
          border-collapse:collapse;
        }
        table {
            margin: 0 auto;
            margin-top: 0px;
        }
        a {
            color: black;
            text-decoration: none;
        }
        </style>
        </head>
        <body>
        '''
        
        t += f"<table cellpadding=\"10px\" cellspacing=\"\">\n"
        t += f"<tr><td></td><td colspan=\"{len(pdf_tags)}\">Pseudodata &ndash; {args.postfix} &ndash; inflation {args.inflationFactor}</td></tr>\n"
        t += f"<tr><td>Model</td><td width=\"135px\">{'</td><td>'.join([p[3:] for p in pdf_names])}</td></tr>\n"

        for base_pdf in pdf_tags:
            n = pdf_names[pdf_tags.index(base_pdf)][3:]
            t += f"<tr><td>{n}</td>\n"
            base_pdf_name = pdf_names[pdf_tags.index(base_pdf)]
            for pseudo_pdf in pdf_tags:
                working_dir = glob.glob(f"{combine_dir}/*{base_pdf}")[0]
                fitresult = combinetf_input.get_fitresult(f"{working_dir}/fit_{pseudo_pdf}.root")  
                if args.xsec:
                    pois = combinetf_input.get_poi_names(fitresult, poi_type="mu")
                
                else:
                    pois = combinetf_input.get_poi_names(fitresult, poi_type=None)
                impacts, labels, _ = combinetf_input.read_impacts_poi(fitresult, True, add_total=True, poi=pois[0], normalize=False)
                labels = list(labels)

                unc_tot = impacts[labels.index('Total')]*100.
                unc_pdf = impacts[labels.index(base_pdf_name)]*100. # including AS +"NoAlphaS"
                
                pulls, constraints, pulls_prefit = combinetf_input.get_pulls_and_constraints(f"{working_dir}/fit_{pseudo_pdf}.root", [f"massShift{'W' if isW else 'Z'}100MeV"])
                unc_tot_mw = 100.*constraints[0] ## should be equal to unc_tot
                pull = 100.*pulls[0]
                
                if args.xsec:
                    unc_pdf = unc_tot_mw # no pdf unc for xsec
                
                style = "background-color: Tomato;" if abs(pull) > unc_pdf else ""
                style += "background-color: LightGray;" if base_pdf == pseudo_pdf else ""
                sign = "" if pull >= 0 else "&minus;"
                
                
                f = web_dir.replace("/work/submit/jaeyserm/public_html/", "http://submit08.mit.edu/~jaeyserm/")
                url = f"{f}/{base_pdf}/{pseudo_pdf}/"
                t += "<td style=\"{}\"><a href=\"{}\" target=\"_blank\">{}{:.1f} &pm; {:.1f} ({:.1f})</a></td>\n".format(style, url, sign, abs(pull), unc_pdf, unc_tot_mw)

            t += '</tr>\n'
        
        t += "</table></html>\n"
        print(t)
        with open(f"{web_dir}/table.html", "w") as tf:
            tf.write(t)


    if args.mode == "summary":
        import uproot
        from utilities.io_tools import combinetf_input

        t = '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        body, html {
            font: 16px Arial;
            text-align: center;
            padding = 0;
            margin = 0;
        }
        table, th, td {
          border: 1px solid black;
          border-style:solid;
          border-collapse:collapse;
        }
        table {
            margin: 0 auto;
            margin-top: 0px;
        }
        a {
            color: black;
            text-decoration: none;
        }
        </style>
        </head>
        <body>
        '''
        
        t += f"<table cellpadding=\"10px\" cellspacing=\"\">\n"
        t += f"<tr><td></td><td colspan=\"{len(pdf_tags)}\">Pseudodata &ndash; {args.postfix} &ndash; inflation {args.inflationFactor}</td></tr>\n"
        t += f"<tr><td>Model</td><td width=\"135px\">{'</td><td>'.join([p[3:] for p in pdf_names])}</td></tr>\n"

        for base_pdf in pdf_tags:
            n = pdf_names[pdf_tags.index(base_pdf)][3:]
            t += f"<tr><td>{n}</td>\n"
            base_pdf_name = pdf_names[pdf_tags.index(base_pdf)]
            for pseudo_pdf in pdf_tags:
                for infl in [1, 1.5, 2, 2.5, 3]:
                    if infl == 1.:
                        combine_dir_ = f"{args.combine_dir}/{args.fitType}"
                    else:
                        t = str(infl).replace(".", "p")
                        combine_dir_ = f"{args.combine_dir}/{args.fitType}_infl_{t}"

                    working_dir = glob.glob(f"{combine_dir_}/*{base_pdf}")[0]
                    fitresult = combinetf_input.get_fitresult(f"{working_dir}/fit_{pseudo_pdf}.root")  
                    if args.xsec:
                        pois = combinetf_input.get_poi_names(fitresult, poi_type="mu")
                    
                    else:
                        pois = combinetf_input.get_poi_names(fitresult, poi_type=None)
                    impacts, labels, _ = combinetf_input.read_impacts_poi(fitresult, True, add_total=True, poi=pois[0], normalize=False)
                    labels = list(labels)

                    unc_tot = impacts[labels.index('Total')]*100.
                    unc_pdf = impacts[labels.index(base_pdf_name)]*100. # including AS +"NoAlphaS"
                    
                    pulls, constraints, pulls_prefit = combinetf_input.get_pulls_and_constraints(f"{working_dir}/fit_{pseudo_pdf}.root", [f"massShift{'W' if isW else 'Z'}100MeV"])
                    unc_tot_mw = 100.*constraints[0] ## should be equal to unc_tot
                    pull = 100.*pulls[0]
                    
                    if args.xsec:
                        unc_pdf = unc_tot_mw # no pdf unc for xsec
                    
                    style = "background-color: Tomato;" if abs(pull) > unc_pdf else ""
                    style += "background-color: LightGray;" if base_pdf == pseudo_pdf else ""
                    sign = "" if pull >= 0 else "&minus;"
                    
                
                f = web_dir.replace("/work/submit/jaeyserm/public_html/", "http://submit08.mit.edu/~jaeyserm/")
                url = f"{f}/{base_pdf}/{pseudo_pdf}/"
                t += "<td style=\"{}\"><a href=\"{}\" target=\"_blank\">{}{:.1f} &pm; {:.1f} ({:.1f})</a></td>\n".format(style, url, sign, abs(pull), unc_pdf, unc_tot_mw)

            t += '</tr>\n'
        
        t += "</table></html>\n"
        print(t)
        with open(f"{web_dir}/table.html", "w") as tf:
            tf.write(t)


    if args.mode == "matrixth":
        import uproot
        from utilities.io_tools import combinetf_input
        combine_dir = combine_dir.replace("pdfMatrix", "pdfMatrix_scetlib")
        base_pdf = "msht20an3lo"
        tag = "minnlo" # scetlib minnlo

        t = f"\\begin{{tabular}}{{l|{'c'*len(pdf_tags)}}} \n"
        t += f"Model + & \multicolumn{{{len(pdf_tags)}}}{{c}}{{Pseudodata}}  \\\ \n"
        t += f"Uncertainty & {' & '.join([p[3:] for p in pdf_names])} \\\ \n"
        t += "\hline \n"


        l = pdf_names[pdf_tags.index(base_pdf)][3:]
        base_pdf_name = pdf_names[pdf_tags.index(base_pdf)]
        for pseudo_pdf in pdf_tags:
            working_dir = glob.glob(f"{combine_dir}/*{base_pdf}_{tag}")[0]
            fitresult = combinetf_input.get_fitresult(f"{working_dir}/fit_{pseudo_pdf}.root")
            pois = combinetf_input.get_poi_names(fitresult, poi_type=None)
            impacts, labels, _ = combinetf_input.read_impacts_poi(fitresult, True, add_total=True, poi=pois[0], normalize=False)
            labels = list(labels)

            unc_tot = impacts[labels.index('Total')]
            unc_pdf = impacts[labels.index(base_pdf_name)] # including AS +"NoAlphaS"
            unc_pdf = 100.*unc_pdf
            unc_tot = 100.*unc_tot
                
            pulls, constraints = combinetf_input.get_pulls_and_constraints(f"{working_dir}/fit_{pseudo_pdf}.root", [f"massShift{'W' if isW else 'Z'}100MeV"])
            pull = 100.*pulls[0]
            if abs(pull) > unc_pdf:
                #l += ' & \\cellcolor{{red!25}} ${:.1f} \pm {:.1f}$'.format(pull, unc)
                l += ' & \\cellcolor{{red!25}} ${:.1f} \pm {:.1f} ({:.1f})$'.format(pull, unc_pdf, unc_tot)
            else:
                if base_pdf == pseudo_pdf:
                    #l += ' & \\cellcolor{{lightgray!25}} ${:.1f} \pm {:.1f}$'.format(pull, unc)
                    l += ' & \\cellcolor{{lightgray!25}} ${:.1f} \pm {:.1f} ({:.1f})$'.format(pull, unc_pdf, unc_tot)
                else:
                    #l += ' & ${:.1f} \pm {:.1f}$'.format(pull, unc)
                    l += ' & ${:.1f} \pm {:.1f} ({:.1f})$'.format(pull, unc_pdf, unc_tot)
        l += " \\\ \n"
        t += l
        t += "\\end{tabular}"
        print(t)

    if args.mode == "matrixext":
        import uproot
        import numpy as np
        from utilities.io_tools import combinetf_input

        t = f"\\begin{{tabular}}{{l|{'c'*len(pdf_tags)}}} \n"
        t += f"Model + & \multicolumn{{{len(pdf_tags)}}}{{c}}{{Pseudodata}}  \\\ \n"
        t += f"Uncertainty & {' & '.join([p[3:] for p in pdf_names])} \\\ \n"
        t += "\hline \n"
        table = np.zeros((len(pdf_tags), len(pdf_tags)))
        for i, base_pdf in enumerate(pdf_tags):
            row = []
            if "_agn" in args.fitType and base_pdf != "msht20":
                continue # only msht20 as central one for agn
            #if base_pdf != "herapdf20":
            #    continue
            l = pdf_names[pdf_tags.index(base_pdf)][3:]
            if base_pdf in ["msht20", "nnpdf40", "ct18"]: l = f"\\cellcolor{{green!25}} {pdf_names[pdf_tags.index(base_pdf)][3:]}"
            base_pdf_name = pdf_names[pdf_tags.index(base_pdf)]
            for j, pseudo_pdf in enumerate(pdf_tags):
                working_dir = glob.glob(f"{combine_dir}/*{base_pdf}")[0]
                fitresult = combinetf_input.get_fitresult(f"{working_dir}/fit_{pseudo_pdf}.root")
                pois = combinetf_input.get_poi_names(fitresult, poi_type=None)
                impacts, labels, _ = combinetf_input.read_impacts_poi(fitresult, True, add_total=True, poi=pois[0], normalize=False)
                labels = list(labels)
                if "_agn" in args.fitType:
                    unc_tot = impacts[labels.index('Total')]
                    unc = 100.*unc_tot
                else:
                    unc_tot = impacts[labels.index('Total')]
                    unc_pdf = impacts[labels.index(base_pdf_name)] # including AS +"NoAlphaS"
                    unc = 100.*unc_pdf
                
                pulls, constraints = combinetf_input.get_pulls_and_constraints(f"{working_dir}/fit_{pseudo_pdf}.root", [f"massShift{'W' if isW else 'Z'}100MeV"])
                pull = 100.*pulls[0]
                if abs(pull) > unc:
                    l += ' & \\cellcolor{{red!25}} ${:.1f} \pm {:.1f}$'.format(pull, unc)
                else:
                    if base_pdf == pseudo_pdf:
                        l += ' & \\cellcolor{{lightgray!25}} ${:.1f} \pm {:.1f}$'.format(pull, unc)
                    else:
                        l += ' & ${:.1f} \pm {:.1f}$'.format(pull, unc)
                table[i][j] = pull
            l += " \\\ \n"
            t += l
        
        t += "\hline \n"
        t += "\\cellcolor{green!25} Spread "
        for i, pseudo_pdf in enumerate(pdf_tags):
            spread = abs(np.min(table[:3, i]) - np.max(table[:3, i]))
            t += " & ${:.1f}$ ".format(spread)
        t += " \\\ \n"
        
        t += "\hline \n"
        t += "Spread (all) "
        for i, pseudo_pdf in enumerate(pdf_tags):
            spread = abs(np.min(table[:, i]) - np.max(table[:, i]))
            t += " & ${:.1f}$ ".format(spread)
        t += " \\\ \n"
            
        t += "\\end{tabular}"
        print(t)


    if args.mode == "impacts":
        for pdfs in pdf_perms:
            base_pdf = pdfs[0]
            pseudo_pdfs = pdfs
            if "_agn" in args.fitType and base_pdf != "msht20":
                continue # only msht20 as central one for agn
                
            out_dir = f"{web_dir}/{base_pdf}"
            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)
  
            for pseudo_pdf in pseudo_pdfs:
                pseudo_pdf_name = pdf_names[pdf_tags.index(pseudo_pdf)]
                working_dir = glob.glob(f"{combine_dir}/*{base_pdf}")[0]
                cmd = f"python3 scripts/combine/pullsAndImpacts.py --oneSidedImpacts -f {working_dir}/fit_{pseudo_pdf}.hdf5 --grouping max -t utilities/styles/nuisance_translate.json output --outFolder {out_dir} -o {pseudo_pdf}.png --otherExtensions html pdf -n 50"
                exe(cmd)

    if args.mode == "lscan":
        for pdfs in pdf_perms:
            base_pdf = pdfs[0]
            pseudo_pdfs = pdfs

            for pseudo_pdf in pseudo_pdfs:
                pseudo_pdf_name = pdf_names[pdf_tags.index(pseudo_pdf)]
                working_dir = glob.glob(f"{combine_dir}/*{base_pdf}")[0]
                if not os.path.exists(f"{working_dir}/fit_{pseudo_pdf}.root"):
                    print(f"ERROR {working_dir}/fit_{pseudo_pdf}.root")
                    continue
                out_dir = f"{web_dir}/{base_pdf}/{pseudo_pdf}/"
                if not os.path.isdir(out_dir):
                    os.makedirs(out_dir)
                cmd = f"python3 ../scripts/likelihoodscan.py -i {working_dir}/fit_{pseudo_pdf}.root --label='{base_pdf} #rightarrow {pseudo_pdf}' --outFolder {out_dir} -o {pseudo_pdf}"
                exe(cmd)

    if args.mode == "check":
        import ROOT
        ROOT.gErrorIgnoreLevel = 6001
        for pdfs in pdf_perms:
            base_pdf = pdfs[0]
            pseudo_pdfs = pdfs

            for pseudo_pdf in pseudo_pdfs:
                pseudo_pdf_name = pdf_names[pdf_tags.index(pseudo_pdf)]
                try:
                    working_dir = glob.glob(f"{combine_dir}/*{base_pdf}")[0]
                    fIn = ROOT.TFile(f"{working_dir}/fit_{pseudo_pdf}.root")
                    t = fIn.Get("fitresults")
                    if t.GetEntries() == 0:
                        #print(t.GetEntries())
                        raise
                    #t.GetEntries()
                    #print(t.GetEntries())
                    #if t.GetEntries > 5:
                    #    pass
                except Exception as e:
                    ifl = f"--inflationFactor {args.inflationFactor}" if args.inflationFactor else ''
                    print(f"python3 ../scripts/pdfMatrix.py --skipCheckDir {'--pdfOnly' if args.pdfOnly else ''} {ifl} --fitType {args.fitType} --mode fit --postfix {args.postfix} --nohup --nThreads 10 --fit_pdf_source {base_pdf} --fit_pdf_target {pseudo_pdf} &&")
                    

    if args.mode == "gof":
        pass
    
    
    if args.mode == "diagnostics":
        import utilities.io_tools.combinetf_input as combinetf_input
        import matplotlib.pyplot as plt
        import numpy as np
        import ROOT
        from scipy.stats import chi2
        for pdfs in pdf_perms:
            base_pdf = pdfs[0]
            pseudo_pdfs = pdfs
            if "_agn" in args.fitType and base_pdf != "msht20":
                continue # only msht20 as central one for agn

            for pseudo_pdf in pseudo_pdfs:
                pseudo_pdf_name = pdf_names[pdf_tags.index(pseudo_pdf)]
                working_dir = glob.glob(f"{combine_dir}/*{base_pdf}")[0]
                
                rfile = ROOT.TFile.Open(f"{working_dir}/fit_{pseudo_pdf}.root")
                ttree = rfile.Get("fitresults")
                ttree.GetEntry(0)

                if hasattr(ttree,"massShiftZ100MeV"):
                    m = ttree.massShiftZ100MeV
                    merr = ttree.massShiftZ100MeV_err
                else:
                    m = 0
                    merr = 0

                val = 2*(ttree.nllvalfull - ttree.satnllvalfull)
                ndf = rfile.Get("obs;1").GetNbinsX() - ttree.ndofpartial
                p = (1-chi2.cdf(val, ndf))*100

                status = ttree.status
                errstatus = ttree.errstatus
                edmval = ttree.edmval
                
                
                
                fitres = combinetf_input.get_fitresult(f"{working_dir}/fit_{pseudo_pdf}.hdf5")
                hess = fitres["hess"][...]
                eigvals = np.linalg.eigvals(hess)
                cond_number = max(eigvals)/min(eigvals)
                print(pseudo_pdf, status, errstatus, edmval, val, ndf, p, cond_number)
                
                '''
                print(base_pdf, pseudo_pdf)
                
                cov = fitres["cov"][...]
                nuisance_impact_nois = cov = fitres["nuisance_impact_nois"][...]
                hprocs = fitres["hprocs"][...].astype(str)
                parms = fitres["parms"][...].astype(str)
                #print(parms)
                
                hess = np.stack(hess, axis=0)
                invhess = np.linalg.inv(hess)
                
                #print(np.diag(hess))
                
                diag = np.diag(np.sqrt(np.diag(invhess)))
                diag = np.linalg.inv(diag)
                corr = np.dot(diag,invhess).dot(diag)
                print(corr.shape)
                
                plt.pcolor(corr, cmap='jet', vmin=-1, vmax=1)
                plt.colorbar()
                
                plt.savefig(f"/home/submit/jaeyserm/public_html/wmass/fits/pdfMatrix/{args.fitType}{'_pdfOnly' if args.pdfOnly else ''}/{base_pdf}/{pseudo_pdf}.png")
                plt.savefig(f"/home/submit/jaeyserm/public_html/wmass/fits/pdfMatrix/{args.fitType}{'_pdfOnly' if args.pdfOnly else ''}/{base_pdf}/{pseudo_pdf}.pdf")
                
                # ['cov', 'hess', 'hnoigroups', 'hprocs', 'hreggroupidxs', 'hreggroups', 'hsignals', 'hsumgroups', 'hsystgroups', 'hsysts', 'hsystsnoconstraint', 'hsystsnoprofile', 'meta', 'mu_names', 'mu_outcov', 'mu_outvals', 'nois_names', 'nois_outcov', 'nois_outvals', 'nuisance_group_impact_nois', 'nuisance_impact_nois', 'outnames', 'parms', 'x']
                '''