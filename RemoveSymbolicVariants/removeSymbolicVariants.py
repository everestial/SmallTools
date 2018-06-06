#!/home/bin/python3

print('\nChecking and Importing required modules \n')

# Call the required modules
import sys
import os


''' Call input and output argument variable names'''
# update to descriptive argument in the future :)
inHaplotype = sys.argv[1]
outHaplotype = sys.argv[2]


'''Function: The Vcf produced from GATK had symbolic variants represented by "*". 
    These variants aren't acceptable by G2Gtools. So, removing them. '''

with open(inHaplotype) as inhap, \
        open(outHaplotype, 'w') as outhap:
    for lines in inhap:
        if lines.startswith('CHORM'):
            outhap.write(lines)
            continue

        split_line = lines.rstrip('\n').split('\t')
        ref = split_line[2]  # read reference allele in that line

        # do not replace the "*" in all-alleles columns but only in sample:PG_al column
        updated_line = []
        for cols in split_line[4:]:
            if '*' in cols:
                cols.replace('*', ref)
            updated_line.append(cols)

        outhap.write('\t'.join(split_line[0:4] + updated_line) + '\n')

    print('VCF update complete')





