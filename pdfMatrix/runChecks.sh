#!/bin/bash

pf="symQuadr"


python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode check --postfix $pf
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode check --postfix $pf --inflationFactor 1.5
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode check --postfix $pf --inflationFactor 2
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode check --postfix $pf --inflationFactor 2.5
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode check --postfix $pf --inflationFactor 3
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode check --postfix $pf --inflationFactor 4
python ../scripts/pdfMatrix.py --skipCheckDir --pdfOnly --fitType mw --mode check --postfix $pf --inflationFactor 5

#python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode check --postfix $pf 
#python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode check --postfix $pf --inflationFactor 1.5
#python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode check --postfix $pf --inflationFactor 2
#python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode check --postfix $pf --inflationFactor 2.5
#python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode check --postfix $pf --inflationFactor 3
#python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode check --postfix $pf --inflationFactor 4
#python ../scripts/pdfMatrix.py --skipCheckDir --fitType mw --mode check --postfix $pf --inflationFactor 5


 