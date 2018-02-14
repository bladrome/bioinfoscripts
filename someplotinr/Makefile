
OBJ=plotpdf

all:pdf


.PHONY:rnw2tex pdf view clean clean-log
rnw2tex:
	@Rscript rnw2tex.R ${OBJ}.Rnw


pdf:rnw2tex
	@xelatex ${OBJ}.tex
	@xelatex ${OBJ}.tex


view:pdf
	@evince ${OBJ}.pdf

clean:clean-log
	@-rm ${OBJ}.tex
	@-rm ${OBJ}.aux
	@-rm ${OBJ}.log
	@-rm ${OBJ}.toc
	@-rm ${OBJ}.lof
	@-rm ${OBJ}.lot
	@-rm ${OBJ}.out
	@-rm results.csv
	@-rm -r qcReport
	@-rm *.png
	@-rm ./figure/unnamed-chunk-*.pdf

clean-log:
	@rm *.log
