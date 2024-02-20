#!/bin/bash

mode="mw"
pf="symNone"


python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode combine --postfix $pf --inflationFactor 1
python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode combine --postfix $pf --inflationFactor 1.5
python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode combine --postfix $pf --inflationFactor 2
python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode combine --postfix $pf --inflationFactor 2.5
python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode combine --postfix $pf --inflationFactor 3
python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode combine --postfix $pf --inflationFactor 4
python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode combine --postfix $pf --inflationFactor 5

#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode combine --postfix $pf --inflationFactor 1
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode combine --postfix $pf --inflationFactor 1.5
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode combine --postfix $pf --inflationFactor 2
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode combine --postfix $pf --inflationFactor 2.5
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode combine --postfix $pf --inflationFactor 3
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode combine --postfix $pf --inflationFactor 4
#python ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode combine --postfix $pf --inflationFactor 5

