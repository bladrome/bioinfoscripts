pdf("5.1.pdf");
m=read.table("GC-depth.txt");
nf <- layout(matrix(c(0,2,0,0,1,3),2,3,byrow=T),c(0.5,3,1),c(1,3,0.5),TRUE);
par(mar=c(5,5,0.5,0.5));
x=m[,1];
y=m[,2];
plot(x,y,
        xlab='GC Content(%)',ylab='Depth',
        pch=46,col="#FF000077",
        xlim=c(0,100),ylim=c(0,max(y) ),
    );

xbreaks <- 100;
ybreaks <- floor( max(y) - 0 );
xhist <- hist(x,breaks=xbreaks,plot=FALSE);
yhist <- hist(y,breaks=ybreaks,plot=FALSE);

par(mar=c(0,5,1,1));
barplot(xhist$counts,space=0,xlim=c(0,100) );

par(mar=c(5,0,1,1));
barplot(yhist$counts,space=0,horiz=TRUE,ylim=c(0,max(y) ) );

dev.off();


