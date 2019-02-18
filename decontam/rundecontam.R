library(decontam)

datadf = read.csv("OTU表2019-02-17.csv")
otumatrix = datadf[,11:length(colnames(datadf)) - 1]
otunames = datadf$OTU
samplenames = colnames(otumatrix)

totumatrix = t(otumatrix)
colnames(totumatrix) = otunames
rownames(totumatrix) = samplenames
decontaminput = totumatrix
neglogical = c(rep(T, 3), rep(F, 65)) 
#ret = isContaminant(decontaminput, neg=neglogical)
#contamret = subset(ret, contaminant == TRUE)

for (p in seq(0, 1, 0.05)){
	ret = isContaminant(decontaminput, neg=neglogical, threshold = p)
	contamret = subset(ret, contaminant == TRUE)
	filename = paste("OTUcontaminant_p", format(p, nsmall=2), ".tsv", sep="")
	write.table(contamret, filename) 
}
