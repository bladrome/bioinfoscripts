argv <- commandArgs(TRUE)
library(knitr);
knit(as.character(argv[1]));
