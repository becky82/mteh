#!/bin/bash

# Set your version manually
VERSION="0.1.1"

python3 ./generate_latex_code.py


# (this only needs to be done once to generate square0.pdf through square12.pdf)
#
# for i in {0..12}; do
#     xelatex -interaction=nonstopmode "square${i}.tex"
# done


# Include the version as a macro when calling xelatex
# Example for mteh.tex
xelatex -interaction=nonstopmode "\def\version{$VERSION}\input{mteh.tex}"

# HSK5 with answers
xelatex -interaction=nonstopmode -jobname=mteh_HSK5_answers "\def\datafile{mteh_input_HSK5.txt}\def\answerson{1}\def\version{$VERSION}\def\hsklevel{HSK5}\input{mteh_bulk.tex}"

# HSK5 without answers
xelatex -interaction=nonstopmode -jobname=mteh_HSK5_noanswers "\def\datafile{mteh_input_HSK5.txt}\def\version{$VERSION}\def\hsklevel{HSK5}\input{mteh_bulk.tex}"

# HSK6 with answers
xelatex -interaction=nonstopmode -jobname=mteh_HSK6_answers "\def\datafile{mteh_input_HSK6.txt}\def\answerson{1}\def\version{$VERSION}\def\hsklevel{HSK6}\input{mteh_bulk.tex}"

# HSK6 without answers
xelatex -interaction=nonstopmode -jobname=mteh_HSK6_noanswers "\def\datafile{mteh_input_HSK6.txt}\def\version{$VERSION}\def\hsklevel{HSK6}\input{mteh_bulk.tex}"

# HSK7-9 with answers
xelatex -interaction=nonstopmode -jobname=mteh_HSK7-9_answers "\def\datafile{mteh_input_HSK7-9.txt}\def\answerson{1}\def\version{$VERSION}\def\hsklevel{HSK7-9}\input{mteh_bulk.tex}"

# HSK7-9 without answers
xelatex -interaction=nonstopmode -jobname=mteh_HSK7-9_noanswers "\def\datafile{mteh_input_HSK7-9.txt}\def\version{$VERSION}\def\hsklevel{HSK7-9}\input{mteh_bulk.tex}"

# All with answers
xelatex -interaction=nonstopmode -jobname=mteh_all_answers "\def\datafile{mteh_input.txt}\def\answerson{1}\def\version{$VERSION}\def\hsklevel{all}\input{mteh_bulk.tex}"

# All without answers
xelatex -interaction=nonstopmode -jobname=mteh_all_noanswers "\def\datafile{mteh_input.txt}\def\version{$VERSION}\def\hsklevel{all}\input{mteh_bulk.tex}"

