m=read.table("Species.txt");
pdf("6.1.pdf");
pie(m[,3]);
pie(m[,3],
    col=rainbow(nrow(m) ),
    );

par(mar=rep(8,4) );
pie(m[,3],
    col=rainbow(nrow(m) ),
    labels=paste(m[,1],m[,2],"\n",m[,3],"%" ),
    );

dev.off();
