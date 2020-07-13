#!/bin/sh

pdflatex $1
pdfcrop $1
mv $1-crop.pdf $1.pdf
