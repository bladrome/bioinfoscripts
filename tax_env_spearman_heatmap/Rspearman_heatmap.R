	library(ggplot2)
	library(pheatmap)
	library(stringr)
	library(purrr)
	library(gtools)


	width = 10
	height = 8

	plotheatmap <- function(filenum, outputfilename){

	pltdf <- read.csv(str_c("heatmap_corrdf_", filenum, ".csv"))
	pvaldf <- read.csv(str_c("heatmap_pvaldf_", filenum, ".csv"))
	print(dim(pltdf))
	rownames(pltdf) <- pltdf[,1]
	pltdf <- pltdf[-1]

	  ##pheatmap(as.matrix(log(pltdf + 0.0000001)),
	  pheatmap(as.matrix(pltdf),
		   filename = outputfilename,
	   #        annotation_col = annotation_coldf,
		   scale = "column",
		   border_color = "white",
		   show_rownames = T,
		   show_colnames = T,
		   cluster_rows = T,
		   cluster_cols = F,
		   width=width,
		   height=height,
		   display_numbers = as.matrix(map_dfr(pvaldf[,-1], stars.pval)),
		   color = colorRampPalette(c(
		     "#AC2024",
		     "white", "#5ebeeb"
		   ))(100))
	}

	for (filenum in 1:6) {
	    print(filenum)
	    plotheatmap(filenum, str_c("heatmap_", filenum, ".pdf"))
	}		       
