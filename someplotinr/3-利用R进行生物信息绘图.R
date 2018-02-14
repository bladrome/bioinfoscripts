######################################
##       案例一：SV结果统计及绘图     ##
#####################################
library(ggplot2)

#读入数据及数据处理
my_sv<- read.csv("data/variants_bed.csv",stringsAsFactors=TRUE,header=TRUE)
head(my_sv)
colnames(my_sv)
summary(my_sv$chrom)

# 修改染色体顺序
my_sv$chrom <- factor(my_sv$chrom, levels=c(seq(1,22),"X","Y"))
# 修改Type顺序
my_sv$type <- factor(my_sv$type, levels=c("Insertion","Deletion","Expansion","Contraction"))


# 开始绘图
ggplot(my_sv, aes(x=chrom,fill=type)) + geom_bar()

#修改条形图的堆叠效果
ggplot(my_sv, aes(x=chrom,fill=type)) + geom_bar(position = "fill")
ggplot(my_sv, aes(x=chrom,fill=type)) + geom_bar(position = "dodge")
ggplot(my_sv, aes(x=chrom,fill=type)) + geom_bar(position = "jitter")
ggplot(my_sv, aes(x=chrom,fill=type)) + geom_bar(position = "identity")
ggplot(my_sv, aes(x=chrom,fill=type)) + geom_bar(position = "stack")

# 修改绘图元素
ggplot(my_sv, aes(x=size,fill=type)) + geom_bar(binwidth=5) + xlim(0,500)

######################################
##       案例二：修改绘图类型       ##
#####################################
my_sv<- read.csv("data/variants_bed.csv",stringsAsFactors=TRUE,header=TRUE)
# 修改绘图类型
# 1、散点图
ggplot(my_sv, aes(x=ref.dist,y=query.dist)) + geom_point()
ggplot(my_sv, aes(x=ref.dist,y=query.dist,color=type)) + geom_point()

# 2、box图
ggplot(my_sv, aes(x=type,y=size)) + geom_boxplot()
ggplot(my_sv, aes(x=type,y=size,fill=type)) + geom_boxplot()+ylim(0,1000) 
ggplot(my_sv, aes(x=type,y=size,fill=type)) + geom_boxplot() + coord_flip()

# 3、小提琴图
ggplot(my_sv, aes(x=type,y=size)) + geom_violin()
ggplot(my_sv, aes(x=type,y=size,fill=type)) + geom_violin() + ylim(0,1000) + guides(fill=FALSE)
ggplot(my_sv, aes(x=type,y=size,fill=type)) + geom_violin(adjust=0.2) + ylim(0,1000) + guides(fill=FALSE)
ggplot(my_sv, aes(x=type,y=size,fill=type)) + geom_violin() +   scale_y_log10()

# 3、密度曲线图
ggplot(my_sv, aes(x=size,fill=type)) + geom_density() + xlim(0,500)
ggplot(my_sv, aes(x=size,fill=type)) + geom_density(position="stack") + xlim(0,500)
ggplot(my_sv, aes(x=size,fill=type)) + geom_density(alpha=0.5) + xlim(0,500)

######################################
##       案例三：时间变化折线图     ##
#####################################

library(ggplot2)
time_course <- read.csv("data/time_course_data.txt",stringsAsFactors=TRUE,header=TRUE)
time_course

library(reshape2)
times <- dcast(time_course,seconds ~ sample)

#传统绘图函数
plot(times$seconds,times$A,type = "l",col="red",lwd=2,ylim=c(0,140),lty=2,
     xlab = "Second",ylab="Value")
lines(times$seconds,times$B,col="green",lwd=2)
legend("topright",legend = c("A","B"),lty = c(2,1),lwd=2,col = c("red","green"))
grid()

#利用ggplot2绘制
#library(ggplot2)
ggplot(time_course, aes(x=seconds,y=value,colour=sample)) + geom_line()

#修改为极坐标系
ggplot(time_course, aes(x=seconds,y=value,colour=sample)) + geom_line(size=2) + coord_polar()

######################################
##  案例四：变异类型统计及绘图     ##
#####################################

#读入文件
my_var <- read.csv("data/Encode.Hmm.csv",stringsAsFactors = TRUE,header=TRUE)
head(my_var)
dim(my_var)

# 进行统计分析
summary(my_var)
table(my_var$chrom)
levels(my_var$type)
table(my_var$type)
barplot(table(my_var$chrom))

#分染色体统计
chr1 <- table(my_var[my_var$chrom=="chr1",]$type)
barplot(chr1)

# 计算突变长度
dsize = my_var$stop - my_var$start
hist(dsize)
summary(dsize)

#利用ggplot2绘图
ggplot(data=my_var,mapping = aes(x=chrom,fill=type)) + geom_bar()

#问题1 染色体名字堆在一起，顺序串了
#问题2 有些type重叠
#问题3 type名字没有按顺序排列

# 解决第一个问题，去掉chr前缀
my_var$chrom <- factor(gsub("chr", "", my_var$chrom))
ggplot(my_var,aes(x=chrom,fill=type)) + geom_bar()

# 染色体顺序
c(seq(1,22),"X","Y")

my_var$chrom <- factor(my_var$chrom, levels=c(seq(1,22),"X","Y"))
ggplot(my_var,aes(x=chrom,fill=type)) + geom_bar()


#解决第二个问题.

summary(my_var$type)

#只取部分感兴趣的的变异类型，利用包含于操作符%in% 
my_var <- my_var[my_var$type %in% c("1_Active_Promoter","4_Strong_Enhancer","8_Insulator"), ]

summary(my_var$type)
ggplot(my_var,aes(x=chrom,fill=type)) + geom_bar()

#修改图例顺序和名字
levels(my_var$type)[1]="Promoter"
levels(my_var$type)[10]="Enhancer"
levels(my_var$type)[14]="Insulator"

#利用plyr包中的revalue函数可以方便修改
#library(plyr)
#my_var$type <- revalue(my_var$type, c("1_Active_Promoter"="Promoter", "4_Strong_Enhancer"="Enhancer","8_Insulator"="Insulator"))

summary(my_var$type)
ggplot(my_var,aes(x=chrom,fill=type)) + geom_bar()
ggplot(my_var,aes(x=chrom,fill=type)) + geom_bar()+scale_fill_manual(values = c("green","blue","red"))

######################################
##       案例五：分组统计绘图     ##
#####################################

#利用分面facet
head(my_var)
colnames(my_var)

ggplot(my_var, aes(x=chrom,fill=type)) + geom_bar()+facet_grid(type ~ .)
ggplot(my_var, aes(x=chrom,fill=type)) + geom_bar()+facet_grid(chrom ~ .)



######################################
##       案例六：KEGG图              ##
#####################################
library(ggplot2)

pathway <-  read.csv("data/kegg.csv",header=T)
colnames(pathway)

pp <-  ggplot(data=pathway,mapping = aes(x=richFactor,y=Pathway))
pp + geom_point()
pp + geom_point(aes(size=AvsB))
pp + geom_point(aes(size=AvsB,color=Qvalue))
pp + geom_point(aes(size=AvsB,color=Qvalue)) + scale_colour_gradient(low="green",high="red")
pr = pp + geom_point(aes(size=AvsB,color=Qvalue)) + scale_colour_gradient(low="yellow",high="purple") +labs(color=expression(-log[10](Qvalue)),size="Gene number",x="Rich factor",y="Pathway name",title="Top20 of pathway enrichment")
pr + theme_bw()



######################################
##       案例七：GO注释条目图      ##
#####################################
library(ggplot2)

go <- read.csv("data/go.csv",header = T)
go_sort <- go[order(go$Ontology,-go$Percentage),]
m <- go_sort[go_sort$Ontology=="Molecular function",][1:10,]
c <- go_sort[go_sort$Ontology=="Cellular component",][1:10,]
b <- go_sort[go_sort$Ontology=="Biological process",][1:10,]
slimgo <- rbind(b,c,m)

#首先需要将Trem转换为因子
slimgo$Term=factor(slimgo$Term,levels=slimgo$Term)

colnames(slimgo)
pp=ggplot(data = slimgo, mapping = aes(x=Term,y=Percentage,fill=Ontology))
pp+geom_bar(stat="identity")
pbar=pp+geom_bar(stat="identity")+coord_flip()
pbar=pp+geom_bar(stat="identity")+coord_flip()+scale_x_discrete(limits=rev(levels(slimgo$Term)))
pbar
pr=pbar+scale_fill_discrete(name="Ontology",breaks=c("Biological process","Molecular function","Cellular component"))

pr=pbar+scale_fill_discrete(name="Ontology",breaks=c("Biological process","Molecular function","Cellular component"))+guides(fill=FALSE)
pr+theme_bw()


######################################
##       案例八：Manhattan图         ##
#####################################
#install.packages("qqman")
library(qqman)
library(RColorBrewer)
str(gwasResults)
head(gwasResults)

# Plot !
manhattan(gwasResults)
manhattan(gwasResults, main = "Manhattan Plot", ylim = c(0, 10), cex = 0.6,cex.axis = 0.9, col = c("blue4", "orange3"), 
          suggestiveline = F, genomewideline = F,chrlabs = c(1:20, "P", "Q"))


#换个好看的颜色
number <- length(unique(gwasResults$CHR))
set.seed(888)
yanse <- sample(colors(),number,replace = F)
manhattan(gwasResults,col = yanse,main = "Manhattan Plot")

#高亮显示部分SNP结果
snpsOfInterest
manhattan(gwasResults, highlight = snpsOfInterest)

#注释SNP结果

manhattan(gwasResults, annotatePval = 0.01)
manhattan(gwasResults, annotatePval = 0.005, annotateTop = FALSE)    

#help("manhattan")
#vignette("qqman")


######################################
##       案例九：维恩图              #
#####################################
# Gene lists for Venn Diagram
listA <- read.csv("data/genes_list_A.txt",header=FALSE)
A <- listA$V1
listB <- read.csv("data/genes_list_B.txt",header=FALSE)
B <- listB$V1
listC <- read.csv("data/genes_list_C.txt",header=FALSE)
C <- listC$V1
listD <- read.csv("data/genes_list_D.txt",header=FALSE)
D <- listD$V1

length(A);length(B);length(C);length(D)
intersect(A,B)
setdiff(A,B)
setdiff(B,A)
union(C,D)

#利用gplots包绘制韦恩图
library(gplots)
E <- sample(unique(union(C,D)),500,replace = F)
vennlist <- list(A,B,C,D,E)
venn(vennlist[1:3])
venn(vennlist[1:4])
venn(vennlist)

#利用VennDiagram绘制韦恩图
# install package VennDiagram
library(VennDiagram)

# This function only works by saving directly to a file
venn.diagram(list("list C"=C, "list D"=D), fill = c("yellow","cyan"), cex = 1.5,filename = "venn2.png")
venn.diagram(list(A = A, C = C, D = D), fill = c("yellow","red","cyan"), cex = 1.5,filename="venn3.png")
venn.diagram(list(A = A, B = B, C = C, D = D), fill = c("yellow","red","cyan","forestgreen"), cex = 1.5,filename="venn4.png")
venn.diagram(list(A = A, B = B, C = C, D = D , E = E ), fill = c("yellow","red","cyan","forestgreen","lightblue"), cex = 1.5,filename="venn5.png")


######################################
##       案例十：Heatmap              #
#####################################
dta <- read.csv("data/heatmap.csv",header = T,row.names = 1)
heatmap(as.matrix(dta))

heatmap(as.matrix(dta),col=colorRampPalette(c("green","black","red"))(20),ColSideColors=colorRampPalette(c("green","black","red"))(20),
        Colv=NA,cexRow=0.8,cexCol=1.2)

#利用gplots包绘制
#install.packages(gplots)
library(gplots)
dta <- read.csv("data/heatmap.csv",header = T,row.names = 1)
heatmap.2(as.matrix(dta))
group=colorRampPalette(c("green","red"))(ncol(dta))
heatmap.2(as.matrix(dta),col=redgreen,ColSideColors=group,key=TRUE,symkey=FALSE,density.info="none",trace="none")
heatmap.2(as.matrix(dta),col=redgreen,ColSideColors=group,key=TRUE,symkey=FALSE,density.info="none",trace="none",scale = "row")

#利用pheatmap包中的pheatmap函数绘制热图
library(pheatmap)   
dta=read.table("data/heatmap.csv",header=TRUE,row.names=1,sep=",")
pheatmap(dta)
mat=cor(dta)   
pheatmap(mat,cluster_rows=F,cluster_cols=F,display_numbers=TRUE) 
dta=t(dta)  
matrix=cor(dta)  
pheatmap(matrix,cluster_rows=T,cluster_cols=T,display_numbers=TRUE,fontsize_number=4,number_format = "%.2f") 

