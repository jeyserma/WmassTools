#!/bin/bash

mode="wlike"
pf="symFull"

#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode matrixh --postfix $pf --inflationFactor 1.0
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode matrixh --postfix $pf --inflationFactor 1.5
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode matrixh --postfix $pf --inflationFactor 2.0
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode matrixh --postfix $pf --inflationFactor 2.5
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode matrixh --postfix $pf --inflationFactor 3.0
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode matrixh --postfix $pf --inflationFactor 4.0
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode matrixh --postfix $pf --inflationFactor 5.0

#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode matrixh --postfix $pf --inflationFactor 1.0
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode matrixh --postfix $pf --inflationFactor 1.5
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode matrixh --postfix $pf --inflationFactor 2.0
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode matrixh --postfix $pf --inflationFactor 2.5
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode matrixh --postfix $pf --inflationFactor 3.0
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode matrixh --postfix $pf --inflationFactor 4.0
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode matrixh --postfix $pf --inflationFactor 5.0

python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode summary --postfix $pf
python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode summary --postfix $pf