#!/bin/bash

mode="wlike"
pf="symNone"



python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode check --postfix $pf --inflationFactor 1.0
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode check --postfix $pf --inflationFactor 1.5
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode check --postfix $pf --inflationFactor 2
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode check --postfix $pf --inflationFactor 2.5
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode check --postfix $pf --inflationFactor 3
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode check --postfix $pf --inflationFactor 4
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode check --postfix $pf --inflationFactor 5

python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode check --postfix $pf --inflationFactor 1.0
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode check --postfix $pf --inflationFactor 1.5
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode check --postfix $pf --inflationFactor 2
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode check --postfix $pf --inflationFactor 2.5
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode check --postfix $pf --inflationFactor 3
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode check --postfix $pf --inflationFactor 4
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode check --postfix $pf --inflationFactor 5

