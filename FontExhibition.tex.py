#!/usr/bin/env python3

import os
import re


TEX_HEADER = r'''
% latexmk -pdflatex='lualatex' -pdf FontExhibition.tex
\documentclass{article}
\usepackage{fontspec}

\begin{document}
'''

TEX_FOOTER = r'''
\end{document}
'''

fonts = os.popen('fc-list').read()
fontfiles = re.findall(r'[^/]*?\.[o|t]tf', fonts)
fontfiles = sorted(fontfiles)

body = []
for font in fontfiles:
    fontname, fonttype = font.split('.')
    if 'VariableFont' in fontname:
        continue  # Skip font folders
    if ' ' in fontname:
        continue  # Spaces in font names cause problems
    body.append(r'\setmainfont[Extension=.'+fonttype+']{'+fontname+'}')
    body.append(r'\noindent \verb!'+font+'!')
    # body.append('\nTHE QUICK BROWN FOX jumped over the lazy dog.\n')
    body.append('\nTHE QUICK BROWN FOX jumped over the lazy dog.♔♕♖♗♘♙♚♛♜♝♞♟\n')


print(TEX_HEADER)
print('\n'.join(body))
print(TEX_FOOTER)

