#!/bin/bash

mode="wlike"
pf="symNone"


python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode fit --postfix $pf --inflationFactor 1.0 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode fit --postfix $pf --inflationFactor 1.5 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode fit --postfix $pf --inflationFactor 2.0 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode fit --postfix $pf --inflationFactor 2.5 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode fit --postfix $pf --inflationFactor 3.0 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode fit --postfix $pf --inflationFactor 4.0 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --pdfOnly --fitType $mode --mode fit --postfix $pf --inflationFactor 5.0 --nohup --nThreads 1

python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode fit --postfix $pf --inflationFactor 1.0 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode fit --postfix $pf --inflationFactor 1.5 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode fit --postfix $pf --inflationFactor 2.0 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode fit --postfix $pf --inflationFactor 2.5 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode fit --postfix $pf --inflationFactor 3.0 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode fit --postfix $pf --inflationFactor 4.0 --nohup --nThreads 1
python3 ../WmassTools/pdfMatrix/pdfMatrix.py --skipCheckDir --fitType $mode --mode fit --postfix $pf --inflationFactor 5.0 --nohup --nThreads 1

