m=read.table("prok_representative.txt",sep="\t");
pdf("1.1.pdf");
x=m[,2];
y=m[,4];
plot(x,y,pch=16,
        xlab="Genome Size",ylab="Genes");
fit <- lm(y~x);
abline( fit,col="blue",lwd=1.8 );
rr <- round( summary(fit)$adj.r.squared,2);
intercept <- round( summary(fit)$coefficients[1],2);
slope <- round( summary(fit)$coefficients[2],2);
eq <- bquote( atop( "y = " * .(slope) * " x + " * .(intercept), R^2 == .(rr) ) );
text(12,6e3,eq);
#legend("topleft",legend=eq,bty="n");

dev.off();


