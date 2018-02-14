#install.packages(c("vcd","gmodels","arules","ggplot2","pheatmap","gplots","devtools","qqman","VennDiagram"))
#source('http://Bioconductor.org/biocLite.R')
#biocLite()
#biocLite(c("ShortRead","airway","Rsamtools","GenomicFeatures","GenomicAlignments","DESeq2","dplyr","genefilter","AnnotationDbi","org.Hs.eg.db","PoiClaClu"))  


######################################
##       案例一：卡方检验           ##
######################################
library(vcd)
head(Arthritis)

# one way table
mytable <- with(Arthritis, table(Improved))
mytable  # frequencies
prop.table(mytable) # proportions
prop.table(mytable)*100 # percentages

# two way table
mytable <- xtabs(~ Treatment+Improved, data=Arthritis)
mytable # frequencies
margin.table(mytable,1) #row sums
margin.table(mytable, 2) # column sums
prop.table(mytable) # cell proportions
prop.table(mytable, 1) # row proportions
prop.table(mytable, 2) # column proportions
addmargins(mytable) # add row and column sums to table

# more complex tables
addmargins(prop.table(mytable))
addmargins(prop.table(mytable, 1), 2)
addmargins(prop.table(mytable, 2), 1)


# Two way table using CrossTable
library(gmodels)
CrossTable(Arthritis$Treatment, Arthritis$Improved)


# Three way table
mytable <- xtabs(~ Treatment+Sex+Improved, data=Arthritis)
mytable
ftable(mytable) 


# Chi-square test of independence
library(vcd)
mytable <- xtabs(~Treatment+Improved, data=Arthritis)
chisq.test(mytable)
mytable <- xtabs(~Improved+Sex, data=Arthritis)
chisq.test(mytable)


# Fisher's exact test
mytable <- xtabs(~Treatment+Improved, data=Arthritis)
fisher.test(mytable)



######################################
#  案例二：利用R实现vlookup提取数据 #
#####################################

#读入200个基因的列表 bigtable
genes200 <- read.csv("data/200genes.csv",header = T,stringsAsFactors = F)

#读入121个基因的list small list
genes121 <-  read.csv("data/121genes.csv",header = T,stringsAsFactors = F)
head(genes200)
head(genes121)
genes200["CLU",]

#修改gene table行名
rownames(genes200) <- genes200$gene
genes200["CLU",]
genes200[c("CLU","DCN"),]
#去除重复gene ID
gene93 <- unique(genes121$gene)
#利用数据框的访问功能，一次实现Excel Vlookup功能
dta <- genes200[gene93,]
dta
#数据中包含没有检索到的gene ID，返回值为NA，利用na.omit删除包含NA的行
dta <- na.omit(dta)
rownames(dta) <- 1:nrow(dta)

######################################
##  案例三:t检验与wilcox检验       #
#####################################
head(dta,4)
colnames(dta)
#过滤掉RPKM为0的行
rowSums(dta[2:9])<1
dta[rowSums(dta[2:9])<1,]
dta[rowSums(dta[2:9])>=1,]
#计算每组均值，差异倍数，差异倍数取log2
BaseMeanA <- rowMeans(dta[2:5])
BaseMeanB <- rowMeans(dta[6:9])
FoldChange <-  round(BaseMeanB/BaseMeanA,digits = 3)
log2FoldChange <- round(log(FoldChange,base = 2),digits = 3)
#单个基因t检验
head(dta,1)
clu <- t.test(x=c(185.677,157.8727,134.354,150.355),y=c(5490.2100,1544.78100,3195.68550,11603.02500),var.equal = T,alternative = "two.side")
clu
#取出pvalue
clu_pavlue <- clu$p.value
clu_pavlue
#计算Qvalue
p.adjust.methods
p.adjust(p =clu_pavlue,method = "fdr" )
#多个基因t检验计算
P_value <- round(apply(dta[2:9],1,FUN = function(x){t.test(x[1:4],x[5:8],paired = T)$p.value}),digits = 3)
Q_value <- p.adjust(P_value)
result <- data.frame(dta,BaseMeanA,BaseMeanB,log2FoldChange,P_value,Q_value)
result
#非参数wilcox test检验
wilcox_Pvalue <- apply(dta[2:9],1,FUN = function(x) {wilcox.test(x[1:4],x[5:8])$p.value})
wilcox_Qvalue <- p.adjust(wilcox_Pvalue,method = "fdr")
wilcox_result <- cbind(dta,BaseMeanA,BaseMeanB,log2FoldChange,wilcox_Pvalue,wilcox_Qvalue)
wilcox_result

######################################
##      案例四:利用R进行数据挖掘   ##
#####################################
#4.1 计算相关性矩阵
opar <- par(no.readonly = T)
head(state.x77)
cor(x=state.x77,use = "everything",method = "pearson")
cor(x=state.x77,use = "everything",method = "spearman")
cor(x=state.x77,use = "everything",method = "kendall")

#单独计算
x <- state.x77[,c("Population", "Income", "Illiteracy", "HS Grad")]
y <- state.x77[,c("Life Exp", "Murder")]
cor(x,y)
#相关性检验
cor.test(state.x77[,3], state.x77[,5])

#4.2 数据挖掘
states <- as.data.frame(state.x77[,c("Murder", "Population","Illiteracy", "Income", "Frost")])
fit <- lm(Murder ~ Population + Illiteracy + Income + Frost,data=states)
summary(fit)
#fitted(fit)
#residuals(fit)
par(mfrow=c(2,2))
plot(fit)

fit2 <- lm(Murder ~ Population + Illiteracy, data=states)
anova(fit2, fit)
par(opar)

######################################
##  案例五：乳腺癌预测             ##
#####################################
breast <- read.csv("data/breast.csv", header=TRUE, na.strings="?")
df <- breast[-1]
head(df)

#进行抽样，df分成df.train与dr.validate
df$class <- factor(df$class, levels=c(2,4),labels=c("benign", "malignant"))

set.seed(1234)
train <- sample(nrow(df), 0.7*nrow(df))
df.train <- df[train,]
df.validate <- df[-train,]
table(df.train$class)
table(df.validate$class)

# 逻辑回归- Logistic regression with glm()
fit.logit <- glm(class~., data=df.train, family=binomial())
summary(fit.logit)
prob <- predict(fit.logit, df.validate, type="response")
logit.pred <- factor(prob > .5, levels=c(FALSE, TRUE), labels=c("benign", "malignant"))
logit.perf <- table(df.validate$class, logit.pred,dnn=c("Actual", "Predicted"))
logit.perf

#模拟数据
a <- c(sample(1:9,9,replace = T))
b <- c(sample(1:9,9,replace = T))
c <- c(sample(1:9,9,replace = T))
d <- c(sample(1:9,9,replace = T))
e <- c(sample(1:9,9,replace = T))
newdata <- data.frame(1:5,rbind(a,b,c,d,e))
colnames(newdata) <- colnames(df)[-11]
#predict(object = fit.logit,newdata = newdata,type = "response")
newdata$bareNuclei <- as.factor(newdata$bareNuclei)
predict(object = fit.logit,newdata = newdata,type = "response")



######################################
##  案例六：实验设计与方差分析      ##
#####################################
attach(ToothGrowth)
table(supp,dose)
aggregate(len, by=list(supp,dose), FUN=mean)
aggregate(len, by=list(supp,dose), FUN=sd)
dose <- factor(dose)
fit <- aov(len ~ supp*dose)
summary(fit)

#绘图
interaction.plot(dose, supp, len, type="b", col=c("red","blue"), pch=c(16, 18),
                 main = "Interaction between Dose and Supplement Type")


######################################
##  案例七：聚类分析               ##
#####################################
#计算距离
dta <- read.csv("data/tcga_genesets.csv",header = T,stringsAsFactors = F,row.names = 1)
dta[,colSums(dta)==0]
dta <- dta[,colSums(dta)>0]
d <- dist(dta, method = "euclidean", diag = FALSE, upper = FALSE)
#"euclidean", "maximum", "manhattan", "canberra", "binary" or "minkowski"
#进行聚类
fit.average <- hclust(d, method="average")  
fit.average
plot(fit.average, hang=-1, cex=.8, main="Average Linkage Clustering")

#换种聚类算法
dta <- read.csv("data/tcga_genesets.csv",header = T,stringsAsFactors = F,row.names = 1)
labs <- read.csv("data/labels.csv",header = T,stringsAsFactors = F,row.names=1)
names <- labs[rownames(dta),]
rownames(dta) <- paste0(names,"-",0:49)
d <- dist(dta, method = "maximum", diag = FALSE, upper = FALSE)
fit.average <- hclust(d, method="complete")                          
plot(fit.average, hang=-1, cex=.8, main="complete Linkage Clustering")

######################################
##  案例八：购物篮分析               ##
#####################################
#购物篮分析
#install.packages("arules")
library(arules)
data(Groceries)
Groceries

#inspect(Groceries)
fit <- apriori(Groceries,parameter = list(support=0.01,confidence=0.5))
summary(fit)
inspect(fit)

