#!/bin/bash

pf="symFull"


python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode combine --postfix $pf --inflationFactor 1
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode combine --postfix $pf --inflationFactor 1.5
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode combine --postfix $pf --inflationFactor 2
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode combine --postfix $pf --inflationFactor 2.5
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode combine --postfix $pf --inflationFactor 3
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode combine --postfix $pf --inflationFactor 4
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode combine --postfix $pf --inflationFactor 5

python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode combine --postfix $pf --inflationFactor 1
python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode combine --postfix $pf --inflationFactor 1.5
python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode combine --postfix $pf --inflationFactor 2
python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode combine --postfix $pf --inflationFactor 2.5
python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode combine --postfix $pf --inflationFactor 3
python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode combine --postfix $pf --inflationFactor 4
python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode combine --postfix $pf --inflationFactor 5

