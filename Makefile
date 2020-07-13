target = proposal

$(target).pdf: *.tex refs.bib
	pdflatex $(target)
	bibtex $(target)
	pdflatex $(target)
	pdflatex $(target)
	pdflatex $(target)

clean:
	rm *.aux *.bbl *.blg *.idx *.log *.out *.pdf *.toc
