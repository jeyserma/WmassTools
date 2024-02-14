
import lz4.frame
import pickle
import hist
from utilities import boostHistHelpers as hh,logging
import numpy as np
import os
import json
import hdf5plugin
import h5py
from narf import ioutils
import ROOT
import uproot
import re
import sys



h5file = h5py.File(sys.argv[1], "r")
meta = h5file.get("results", h5file.get("meta", None))
results = ioutils.pickle_load_h5py(meta) if meta else None


print(results.keys())

print(results['Wmunu']['output']['nominal_pdfMSHT20'].get()) # categorical pdf
#print(results['Wmunu']['output']['nominal_scetlib_dyturboMSHT20VarsCorr'].get())


'''

Hist(
  Variable([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 20, 23, 27, 32, 40, 54, 100], underflow=False, name='ptll'),
  Regular(20, -2.5, 2.5, name='yll'),
  StrCategory(['pdf0MSHT20', 'pdf1MSHT20Down', 'pdf1MSHT20Up', 'pdf2MSHT20Down', 'pdf2MSHT20Up', 'pdf3MSHT20Down', 'pdf3MSHT20Up', 'pdf4MSHT20Down', 'pdf4MSHT20Up', 'pdf5MSHT20Down', 'pdf5MSHT20Up', 'pdf6MSHT20Down', 'pdf6MSHT20Up', 'pdf7MSHT20Down', 'pdf7MSHT20Up', 'pdf8MSHT20Down', 'pdf8MSHT20Up', 'pdf9MSHT20Down', 'pdf9MSHT20Up', 'pdf10MSHT20Down', 'pdf10MSHT20Up', 'pdf11MSHT20Down', 'pdf11MSHT20Up', 'pdf12MSHT20Down', 'pdf12MSHT20Up', 'pdf13MSHT20Down', 'pdf13MSHT20Up', 'pdf14MSHT20Down', 'pdf14MSHT20Up', 'pdf15MSHT20Down', 'pdf15MSHT20Up', 'pdf16MSHT20Down', 'pdf16MSHT20Up', 'pdf17MSHT20Down', 'pdf17MSHT20Up', 'pdf18MSHT20Down', 'pdf18MSHT20Up', 'pdf19MSHT20Down', 'pdf19MSHT20Up', 'pdf20MSHT20Down', 'pdf20MSHT20Up', 'pdf21MSHT20Down', 'pdf21MSHT20Up', 'pdf22MSHT20Down', 'pdf22MSHT20Up', 'pdf23MSHT20Down', 'pdf23MSHT20Up', 'pdf24MSHT20Down', 'pdf24MSHT20Up', 'pdf25MSHT20Down', 'pdf25MSHT20Up', 'pdf26MSHT20Down', 'pdf26MSHT20Up', 'pdf27MSHT20Down', 'pdf27MSHT20Up', 'pdf28MSHT20Down', 'pdf28MSHT20Up', 'pdf29MSHT20Down', 'pdf29MSHT20Up', 'pdf30MSHT20Down', 'pdf30MSHT20Up', 'pdf31MSHT20Down', 'pdf31MSHT20Up', 'pdf32MSHT20Down', 'pdf32MSHT20Up'], name='pdfVar'),
  storage=Double()) # Sum: 12554.730994667549
  
Hist(
  Variable([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 20, 23, 27, 32, 40, 54, 100], underflow=False, name='ptll'),
  Regular(20, -2.5, 2.5, name='yll'),
  Variable(array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12.,
       13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25.,
       26., 27., 28., 29., 30., 31., 32., 33., 34., 35., 36., 37., 38.,
       39., 40., 41., 42., 43., 44., 45., 46., 47., 48., 49., 50., 51.,
       52., 53., 54., 55., 56., 57., 58., 59., 60., 61., 62., 63., 64.,
       65.]), underflow=False, name='vars'),
  storage=Double()) # Sum: 12741.495358371689


'''