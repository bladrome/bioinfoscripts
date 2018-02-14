m=read.table("cog.class.annot.txt",head=T,sep="\t");
pdf("3.1.pdf",width=12,height=7);
layout(matrix(c(1,2),nr=1),widths=c(20,13));
par( mar=c(3,4,4,1)+0.1 );

class <- c(
        "J","A","K","L","B",
        "D","Y","V","T","M","N","Z","W","U","O",
        "C","G","E","F","H","I","P","Q",
        "R","S");
t = factor( as.character(m[,1]),levels=class );
m <- m[order(t),]
x <- m[,3];

barplot(x,
        space=F,col=rainbow(25),
        ylab="Number of genes",
       );
mtext( m[,1],side=1,at=1:25-0.5 );

l <- c(0,5,15,23,25);
id<- c("INFORMATION STORAGE\nAND PROCESSING",
       "CELLULAR PROCESSES\nAND SIGNALING",
       "METABOLISM",
       "POORLY\nCHARACTERIZED"
      );
abline( v = l[c(-1,-5)] );
for( i in 2:length(l) ){
    text( (l[i-1]+l[i])/2,max(m[,3])*1.1,
            id[i-1],
            cex=0.8,xpd=T,
        );
}

par(mar=c(2,0,2,1)+0.1 );
plot(0,0,type="n",
        xlim=c(0,1),ylim=c(0,26),
        bty="n",axes=F,xlab="",ylab="",
    );

for( i in 1:length(class) ){
    text(0,26-i+0.5,paste(m[i,1],m[i,2]),
            pos=4,cex=1,pty=T,
        );
}
title("COG function classification");

dev.off();



