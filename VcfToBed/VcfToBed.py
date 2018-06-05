#!/home/bin/python

# Builtin modules
import sys

print('\n Checking required modules \n')

inFile = sys.argv[1]
outFile = sys.argv[2]


with open(outFile, "w") as f:
#with open("vcf_to_Bed_File.bed", "w") as f:
    vcf_file = open(inFile, "r+")
    #vcf_file = open("DNA_Samples.Passed_Variants.vcf", "r+")

    for lines in vcf_file:
        if lines.startswith('#'):
            continue

        lines = lines.strip("\n").split("\t")

        chrom = lines[0]
        pos = int(lines[1])
        alleles = lines[3] + ',' + lines[4]

        alleles_len = [len(i) for i in alleles.split(',')]

        max_allele_len = max(alleles_len)

        f.write("\t".join([chrom, str(pos -1), str(pos + max_allele_len)]) + '\n')






    
