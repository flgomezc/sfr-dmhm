LATEX = pdflatex
MAIN  = ms

$(MAIN).pdf: 	$(MAIN).tex
	$(LATEX) $(MAIN).tex 
#	bibtex $(MAIN)
#	$(LATEX) $(MAIN).tex 
	$(LATEX) $(MAIN).tex 


diff:
	latexdiff $(MAIN)_old.tex $(MAIN).tex > $(MAIN)_diff.tex
	$(LATEX) $(MAIN)_diff.tex 

clean:
	rm -f *.aux
	rm -f *.bbl
	rm -f *.ps
	rm -f *.blg
	rm -f *.log
	rm -f *.dvi
	rm -f $(MAIN).pdf $(MAIN)_diff.pdf
	rm -f *~
view: 
	open $(MAIN).pdf &

