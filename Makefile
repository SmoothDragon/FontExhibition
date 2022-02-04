.PHONY: main clean FORCE

main: FontExhibition.pdf FontExhibition.png

FontExhibition.tex: FontExhibition.tex.py
	python FontExhibition.tex.py > FontExhibition.tex

FontExhibition.pdf: FontExhibition.tex
	latexmk -pdflatex='lualatex -halt-on-error -file-line-error -interaction=errorstopmode' -pdf FontExhibition.tex

%.png:	%.pdf
	pdftoppm -singlefile -png $< $*

clean:
	latexmk -pdf -C
