#!/bin/bash

#python3 scripts/histmakers/mw_with_mu_eta_pt.py  --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p msht20
#python3 scripts/histmakers/mw_with_mu_eta_pt.py  --pdf nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p nnpdf40
#python3 scripts/histmakers/mw_with_mu_eta_pt.py  --pdf ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p ct18
#python3 scripts/histmakers/mw_with_mu_eta_pt.py  --pdf nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 ct18 -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p nnpdf31
#python3 scripts/histmakers/mw_with_mu_eta_pt.py  --pdf pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 ct18 nnpdf31 -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p pdf4lhc21
#python3 scripts/histmakers/mw_with_mu_eta_pt.py  --pdf herapdf20 msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p herapdf20
#python3 scripts/histmakers/mw_with_mu_eta_pt.py  --pdf msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p msht20an3lo


python3 scripts/histmakers/mw_with_mu_eta_pt.py --pdf ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p ct18z_symHess
python3 scripts/histmakers/mw_with_mu_eta_pt.py --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p msht20_symHess
python3 scripts/histmakers/mw_with_mu_eta_pt.py --pdf nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p nnpdf40_symHess
python3 scripts/histmakers/mw_with_mu_eta_pt.py --pdf ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p ct18_symHess
python3 scripts/histmakers/mw_with_mu_eta_pt.py --pdf nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p nnpdf31_symHess
python3 scripts/histmakers/mw_with_mu_eta_pt.py --pdf pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p pdf4lhc21_symHess
python3 scripts/histmakers/mw_with_mu_eta_pt.py --pdf herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p herapdf20_symHess
python3 scripts/histmakers/mw_with_mu_eta_pt.py --pdf msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p msht20an3lo_symHess


#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p ct18z
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p msht20
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p nnpdf40
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p ct18
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p nnpdf31
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p pdf4lhc21
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p herapdf20
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p msht20an3lo

#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py  --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo -o /scratch/submit/cms/jaeyserm/Analysis/ -p msht20
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py  --pdf nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 -o /scratch/submit/cms/jaeyserm/Analysis/ -p nnpdf40
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py  --pdf ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 -o /scratch/submit/cms/jaeyserm/Analysis/ -p ct18
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py  --pdf nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 ct18 -o /scratch/submit/cms/jaeyserm/Analysis/ -p nnpdf31
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py  --pdf pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 ct18 nnpdf31 -o /scratch/submit/cms/jaeyserm/Analysis/ -p pdf4lhc21
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py  --pdf herapdf20 msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 -o /scratch/submit/cms/jaeyserm/Analysis/ -p herapdf20
#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py  --pdf msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 -o /scratch/submit/cms/jaeyserm/Analysis/ -p msht20an3lo

#python3 scripts/histmakers/mz_dilepton.py --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/ -p msht20
#python3 scripts/histmakers/mz_dilepton.py --pdf nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/ -p nnpdf40
#python3 scripts/histmakers/mz_dilepton.py --pdf ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/ -p ct18 
#python3 scripts/histmakers/mz_dilepton.py --pdf nnpdf31 pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 ct18 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/ -p nnpdf31
#python3 scripts/histmakers/mz_dilepton.py --pdf pdf4lhc21 herapdf20 msht20an3lo msht20 nnpdf40 ct18 nnpdf31 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/ -p pdf4lhc21
#python3 scripts/histmakers/mz_dilepton.py --pdf herapdf20 msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/ -p herapdf20
#python3 scripts/histmakers/mz_dilepton.py --pdf msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/ -p msht20an3lo


#python3 scripts/histmakers/mz_dilepton.py --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p msht20
#python3 scripts/histmakers/mz_dilepton.py --pdf nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p nnpdf40
#python3 scripts/histmakers/mz_dilepton.py --pdf ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p ct18
#python3 scripts/histmakers/mz_dilepton.py --pdf nnpdf31 pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p nnpdf31
#python3 scripts/histmakers/mz_dilepton.py --pdf pdf4lhc21 herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p pdf4lhc21
#python3 scripts/histmakers/mz_dilepton.py --pdf herapdf20 msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p herapdf20
#python3 scripts/histmakers/mz_dilepton.py --pdf msht20an3lo ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p msht20an3lo
#python3 scripts/histmakers/mz_dilepton.py --pdf ct18z msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo --axes ptll yll -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p ct18z


#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo atlasWZj20 ct18z -o /scratch/submit/cms/jaeyserm/Analysis/new/ -p msht20




#python3 scripts/histmakers/mw_with_mu_eta_pt.py --theoryCorr scetlib_dyturbo scetlib_dyturboMSHT20Vars scetlib_dyturboMSHT20_pdfas horacenloew --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p msht20_pdfTh

#python3 scripts/histmakers/mw_with_mu_eta_pt.py --theoryCorr scetlib_dyturboMSHT20an3lo scetlib_dyturboMSHT20an3loVars scetlib_dyturboMSHT20an3lo_pdfas horacenloew --pdf msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20  -o /scratch/submit/cms/jaeyserm/Analysis/ --theoryAgnostic --poiAsNoi -p msht20an3lo_pdfTh


#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --theoryCorr scetlib_dyturbo scetlib_dyturboMSHT20Vars scetlib_dyturboMSHT20_pdfas horacenloew --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo -o /scratch/submit/cms/jaeyserm/Analysis/ -p msht20_pdfTh

#python3 scripts/histmakers/mz_wlike_with_mu_eta_pt.py --theoryCorr scetlib_dyturboMSHT20an3lo scetlib_dyturboMSHT20an3loVars scetlib_dyturboMSHT20an3lo_pdfas horacenloew --pdf msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20  -o /scratch/submit/cms/jaeyserm/Analysis/  -p msht20an3lo_pdfTh





#python3 scripts/histmakers/mz_dilepton.py --axes ptll yll --theoryCorr scetlib_dyturbo scetlib_dyturboMSHT20Vars scetlib_dyturboMSHT20_pdfas horacenloew --pdf msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20 msht20an3lo -o /scratch/submit/cms/jaeyserm/Analysis/  -p msht20_pdfTh

#python3 scripts/histmakers/mz_dilepton.py --axes ptll yll --theoryCorr scetlib_dyturboMSHT20an3lo scetlib_dyturboMSHT20an3loVars scetlib_dyturboMSHT20an3lo_pdfas horacenloew --pdf msht20an3lo msht20 nnpdf40 ct18 nnpdf31 pdf4lhc21 herapdf20  -o /scratch/submit/cms/jaeyserm/Analysis/  -p msht20an3lo_pdfTh

