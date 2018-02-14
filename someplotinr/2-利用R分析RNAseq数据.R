#利用R分析RNAseq数据

#数据质控
#source('http://Bioconductor.org/biocLite.R');
#biocLite() ;

######################################
##  案例一：数据质控               ##
#####################################
#source('http://Bioconductor.org/biocLite.R');
#biocLite("ShortRead") ;
library(ShortRead);

dirPath <- system.file(package="ShortRead", "extdata", "E-MTAB-1147")
qa <- qa(dirPath, "fastq.gz", BPPARAM=SerialParam())
#生成html格式报告，可以使用浏览器进行查看
report(qa, dest="qcReport", type="html");
showMethods("qa", where=getNamespace("ShortRead"))

######################################
##  案例二：DESeq2               ##
#####################################
#加载需要使用R包
library("DESeq2")

#通过Read Count矩阵来生成DESeqDataSeq对象----------------------
countdata <- read.csv("data/CountMatrix.csv",row.names = 1)
head(countdata, 10)
coldata <- read.csv("data/sample_table.csv",row.names = 1)
#关键步骤
dds <- DESeqDataSetFromMatrix(countData = countdata,colData = coldata,design = ~ cell + dex)

#查看DESeqDataSet对象
dim(dds)
assay(dds)
assayNames(dds)
colSums(assay(dds))
rowRanges(dds)
colData(dds)


#过滤没有reads比对上的基因，所有reads数为零
nrow(dds)
dds <- dds[rowSums(counts(dds)) > 1,]
nrow(dds)

#差异表达计算
dep <- DESeq(dds)
results(dep)

#多维数据探索
# 将数据通过rolg方法与vst方法转换，这样可以用于后面计算距离矩阵

## ----rlog方法----------------------------------------------------------------
rld <- rlog(dds, blind = FALSE)
head(assay(rld), 3)

## ----vst方法-----------------------------------------------------------------
#vsd <- vst(dds, blind = FALSE)
#head(assay(vsd), 3)


#利用转换后的结果计算样品之间距离关系
#方法1--欧氏距离--------------------------
sampleDists <- dist(t(assay(rld)))
sampleDists

library("pheatmap")
library("RColorBrewer")

## ----distheatmap, fig.width = 6.1, fig.height = 4.5----------------------
sampleDistMatrix <- as.matrix( sampleDists )
rownames(sampleDistMatrix) <- paste( rld$dex, rld$cell, sep = " - " )
colnames(sampleDistMatrix) <- NULL
pheatmap(sampleDistMatrix,clustering_distance_rows = sampleDists,
         clustering_distance_cols = sampleDists)

## 方法2，使用Poisson Distance方法------------------------------------------
library("ggplot2")
library("DESeq2")
poisd <- PoissonDistance(t(counts(dds)))
samplePoisDistMatrix <- as.matrix( poisd$dd )
rownames(samplePoisDistMatrix) <- paste( rld$dex, rld$cell, sep=" - " )
colnames(samplePoisDistMatrix) <- NULL
pheatmap(samplePoisDistMatrix,clustering_distance_rows = poisd$dd,
         clustering_distance_cols = poisd$dd)

## 方法3，PCA--------------------------------------------------------------
plotPCA(rld, intgroup = c("dex", "cell"))

## ------------------------------------------------------------------------
pcaData <- plotPCA(rld, intgroup = c( "dex", "cell"), returnData = TRUE)
pcaData
percentVar <- round(100 * attr(pcaData, "percentVar"))
ggplot(pcaData, aes(x = PC1, y = PC2, color = dex, shape = cell)) +
  geom_point(size =3) +  xlab(paste0("PC1: ", percentVar[1], "% variance")) +
  ylab(paste0("PC2: ", percentVar[2], "% variance")) +  coord_fixed()

## 方法4，MDS plot---------------------------------------------------------
library(dplyr)
mds <- as.data.frame(colData(rld))  %>%   cbind(cmdscale(sampleDistMatrix))
ggplot(mds, aes(x = `1`, y = `2`, color = dex, shape = cell)) +   geom_point(size = 3) + coord_fixed()
mdsPois <- as.data.frame(colData(dds)) %>%
  cbind(cmdscale(samplePoisDistMatrix))
ggplot(mdsPois, aes(x = `1`, y = `2`, color = dex, shape = cell)) +
  geom_point(size = 3) + coord_fixed()


# 差异表达计算
dep <- DESeq(dds)
res <- results(dep)
res
write.csv(x = res,file = "des.csv")

#调整对照组与处理组顺序
res1 <- results(dep, contrast=c("dex","trt","untrt"))
mcols(res, use.names = TRUE)
summary(res)

#筛选出p值小于0.05的基因
res.05 <- results(dep, alpha = 0.05)
table(res.05$padj < 0.05)

#重新设置比对条件——单独比对
results(dep, contrast = c("cell", "N061011", "N61311"))

#统计p值小于0.05差异表达基因数目
sum(res$pvalue < 0.05, na.rm=TRUE)
sum(!is.na(res$pvalue))
sum(res$padj < 0.1, na.rm=TRUE)

#筛选出差异表达明显的基因Significant，设定标准为p值小于0.01，至于使用0.05还是0.01，具体问题具体分析
resSig <- subset(res, padj < 0.1)
#按log2差异倍数排序，先升序，设置decreasing = TRUE降序
head(resSig[ order(resSig$log2FoldChange), ])
head(resSig[ order(resSig$log2FoldChange, decreasing = TRUE), ])



#火山图
dta <- read.csv("data/des.csv",header = T)
head(dta)
dta <- na.omit(dta)
volcano <- ggplot(dta,aes(log2FoldChange,-1*log10(padj)))
volcano+geom_point()
volcano+geom_point()+xlim(-10,10) + ylim(0,100)
dta$significant[dta$log2FoldChange<=-1] ="down"
dta$significant[dta$log2FoldChange>=1] ="up"
dta$significant[dta$log2FoldChange>-1 & dta$log2FoldChange <1] ="no"
volcano+geom_point(aes(color=dta$significant))+xlim(-10,10) + ylim(0,100)

#MA图
plotMA(res, ylim = c(-5,5))


#====================END====================================


######################################
##  案例：差异表达基因功能注释     ##
#####################################
library("AnnotationDbi")
library("org.Hs.eg.db")
columns(org.Hs.eg.db)
#"ACCNUM"       "ALIAS"        "ENSEMBL"      "ENSEMBLPROT"  "ENSEMBLTRANS" "ENTREZID"     "ENZYME"       "EVIDENCE"     "EVIDENCEALL" 
#"GENENAME"     "GO"           "GOALL"        "IPI"          "MAP"          "OMIM"         "ONTOLOGY"     "ONTOLOGYALL"  "PATH"        
#"PFAM"         "PMID"         "PROSITE"      "REFSEQ"       "SYMBOL"       "UCSCKG"       "UNIGENE"      "UNIPROT

dta <- read.csv("data/des.csv",header = T,stringsAsFactors = F)
dta <- na.omit(dta)
head(dta)
dta <- dta[dta$padj<0.01,]
nrow(dta)

genelist <- dta$X

dta$symbol <- mapIds(org.Hs.eg.db,keys=genelist,column="SYMBOL",keytype="ENSEMBL",multiVals="first")
dta$entrez <- mapIds(org.Hs.eg.db,keys=genelist,column="ENTREZID",keytype="ENSEMBL", multiVals="first")
dta$go <- mapIds(org.Hs.eg.db,keys=genelist,column="GO",keytype="ENSEMBL",multiVals="first")
dta$ontology <- mapIds(org.Hs.eg.db,keys=genelist,column="ONTOLOGYALL",keytype="ENSEMBL",multiVals="first")
dta$path <- mapIds(org.Hs.eg.db,keys=genelist,column="PATH",keytype="ENSEMBL",multiVals="first")

dtaDF <- as.data.frame(dta)[1:100, ]
write.csv(dtaDF, file = "results.csv")

#获取R工具信息
devtools::session_info()

#====================END====================================

