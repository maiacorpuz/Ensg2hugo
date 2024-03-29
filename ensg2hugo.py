#!/usr/bin/env python
import sys
import fileinput
import re
import json

my_file= sys.argv[1]

Lookup_geneID={}
for line in fileinput.input(my_file):
    gene_id_matches = re.findall('gene_id \"(.*?)\";',line)
    gene_name_matches = re.findall('gene_name \"(.*?)\";',line)
    text_in_columns = re.split('\t',line)
    if len(text_in_columns)>3:
      if text_in_columns[2] == "gene":
        if gene_id_matches:
          if gene_name_matches:
             Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]
print "gene_id\tgene type\tlogFC\tAveExpr"
input_file_to_change= sys.argv[2]
for line in fileinput.input(input_file_to_change):
    text_in_columns = re.split('\t',line)
    print re.sub (r'gene_id \"(.*?)\";', r'ENSG\d*.', line)
    if text_in_columns[0] in Lookup_geneID:
      if "$1" == "-f2":
        text_in_columns[0]=re.sub(r'ENSG\d*.', 'gene_name \"(.*?)\";', text_in_columns[0].rreplace(r'gene_name \"(.*?)\";'))
        print Lookup_geneID[text_in_columns[0]] + "\t" + text_in_columns[1] + "\t" + text_in_columns[2] + "\t" + text_in_columns[4]

