m=read.table("gene.length.txt",sep="\t",head=T);
pdf("2.1.pdf");
x=m[,1];
h=hist(x,nclass=80,
        col="pink",
        xlab="Gene Length (bp)",
        main="Histogram of Gene Length");
rug(x);
xfit<-seq(min(x),max(x),length=100);
yfit<-dnorm(xfit,mean=mean(x),sd=sd(x));
yfit <- yfit*diff(h$mids[1:2])*length(x);
lines(xfit, yfit, col="blue", lwd=2);

h=hist(x,nclass=80,
        probability=T,
        col="pink",
        xlab="Gene Length (bp)",
        main="Histogram of Gene Length");
lines(density(x),lwd=1.8,col="blue" );
rug(x);

dev.off();

