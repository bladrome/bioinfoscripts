#!/usr/bin/perl

use strict;
open (IN,"$ARGV[0]") or die "$!:\n";
open (OUT,">$ARGV[1]") or die "$!:\n";

while (<IN>){
        chomp;
        my @tmp=split /\s+/,$_;
        my ($father_GT)=(split /:/,$tmp[9])[0];
        my ($mather_GT)=(split /:/,$tmp[10])[0];
        my ($fouder_GT)=(split /:/,$tmp[11])[0];
        if ($tmp[0]=~"#CHROM"){
                print OUT "$_\n";
        }
        elsif($father_GT=~/^0\/0/ && $mather_GT=~/^0\/0/ && $fouder_GT=~/^0\/1/){
                print OUT "$_\n";
        }
        elsif($father_GT=~/^0\/0/ && $mather_GT=~/^0\/0/ && $fouder_GT=~/^1\/1/){
                print OUT "$_\n";
        }
        
        # jack add
        elsif($father_GT=~/^0\/0/ && $mather_GT=~/^0\/1/ && $fouder_GT=~/^1\/1/){
                print OUT "$_\n";
        }
        elsif($father_GT=~/^0\/1/ && $mather_GT=~/^0\/0/ && $fouder_GT=~/^1\/1/){
                print OUT "$_\n";
        }

        elsif($father_GT=~/^0\/0/ && $mather_GT=~/^1\/1/ && $fouder_GT=~/^0\/0/){
                print OUT "$_\n";
        }
        elsif($father_GT=~/^1\/1/ && $mather_GT=~/^0\/0/ && $fouder_GT=~/^0\/0/){
                print OUT "$_\n";
        }
        elsif($father_GT=~/^0\/0/ && $mather_GT=~/^1\/1/ && $fouder_GT=~/^1\/1/){
                print OUT "$_\n";
        }
        elsif($father_GT=~/^1\/1/ && $mather_GT=~/^0\/0/ && $fouder_GT=~/^1\/1/){
                print OUT "$_\n";
        }

        elsif($father_GT=~/^1\/1/ && $mather_GT=~/^1\/1/ && $fouder_GT=~/^0\/0/){
                print OUT "$_\n";
        }
        elsif($father_GT=~/^1\/1/ && $mather_GT=~/^1\/1/ && $fouder_GT=~/^0\/1/){
                print OUT "$_\n";
        }

        elsif($father_GT=~/^0\/1/ && $mather_GT=~/^1\/1/ && $fouder_GT=~/^0\/0/){
                print OUT "$_\n";
        }
        elsif($father_GT=~/^1\/1/ && $mather_GT=~/^0\/1/ && $fouder_GT=~/^0\/0/){
                print OUT "$_\n";
        }

}
        
                
