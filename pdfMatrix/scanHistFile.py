
import hist
from utilities import boostHistHelpers as hh,logging
import hdf5plugin
import h5py
from narf import ioutils
import ROOT
import uproot
import sys



def main(fIn):
    h5file = h5py.File(fIn, "r")
    meta = h5file.get("results", h5file.get("meta", None))
    results = ioutils.pickle_load_h5py(meta) if meta else None


    print(results.keys())

    #print(results['ZmumuPostVFP']['output'].keys())
    print(results['ZmumuPostVFP']['output']['nominal_yll_pdfNNPDF40'].get()) # categorical pdf
    print(results['ZmumuPostVFP']['output']['nominal_yll_pdfNNPDF40alphaS002'].get()) # categorical pdf
    
    #print(results['Wmunu']['output']['nominal_scetlib_dyturboMSHT20VarsCorr'].get())

if __name__ == "__main__":
    main(sys.argv[1])
