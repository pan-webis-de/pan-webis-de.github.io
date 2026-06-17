TEX = pan-notebook-template
LATEX = pdflatex
BIBTEX = bibtex

.PHONY: $(TEX).pdf

all: $(TEX).pdf

$(TEX).pdf: $(TEX).tex
	$(LATEX) $(TEX)
	$(BIBTEX) $(TEX)
	$(LATEX) $(TEX)
	$(LATEX) $(TEX)

clean:
	rm -f $(TEX).aux $(TEX).bbl $(TEX).blg $(TEX).log $(TEX).out $(TEX).toc $(TEX).abs $(TEX).xmpdata pdfa.xmpi

distclean: clean
	rm -f $(TEX).pdf

.PHONY: all clean distclean
