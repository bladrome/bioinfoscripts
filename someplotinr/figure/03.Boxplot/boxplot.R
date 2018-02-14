pdf("4.1.pdf");
m <- read.table("test.txt");
x <- m[,1];
y <- m[,2];
z <- m[,3];

boxplot(z~x,outline=F);
boxplot(z~y,outline=F,
        main="test boxplot",
        xlab="Group",ylab="Value");
boxplot(z~x*y,outline=F,
        main="test boxplot",
        xlab="Group",ylab="Value",
        col=(c("gold","lightblue")),
        );

library(vioplot);
m=read.table("test.matrix",head=T);
vioplot(m[,1],m[,2],m[,3],
        names=colnames(m)[1:3],col="blue");

dev.off();



