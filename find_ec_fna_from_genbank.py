#!/usr/bin/python
#This script generate nucloetide sequence from genbank in fasta form that matches EC number
#gzip(gz) support
#Usage: python genbank_to_fna.py genbankfile.gbk.gz ec_number > output.fna
#example: python genbank_to_fna.py genbankfile.gbk.gz 3.2.1.4> output.fna

import sys
import gzip
from Bio import SeqIO

def main():
    if sys.argv[1][-2:] == 'gz':
        gb_file = gzip.open(sys.argv[1],'rb')
    else:
        gb_file = open(sys.argv[1],'r')
    ec = sys.argv[2]
    for gb_record in SeqIO.parse(gb_file,"genbank") :
        genome_name = gb_record.name
        for feat in gb_record.features:
            if feat.type == "CDS":
                name = "unkown"
                if("EC_number" in feat.qualifiers):
                    if feat.qualifiers['EC_number'][0] == ec :
                        if("locus_tag" in feat.qualifiers):
                            name = feat.qualifiers['locus_tag'][0]
                        elif("gene" in feat.qualifiers):
                            name = feat.qualifiers['gene'][0]
                        print ">%s from %s\n%s" %(name,genome_name,feat.extract(gb_record.seq))

if __name__ == '__main__':
    main()
