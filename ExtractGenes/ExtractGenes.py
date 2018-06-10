#!/home/bin/python3

import collections
import shutil
import os
import sys

genefile=sys.argv[1]
goinames=sys.argv[2]
output=sys.argv[3]


print()
''' Function: We have transcripts sequence extracted from overall genome. We can now 
extract sequences for specific genes and/or transcripts. '''

with open(genefile) as infile, \
        open(goinames) as goifile:

    #goi = ['AL1G10010']  # naming genes of interest
    # goi -> means "genes of interest"
    goi_ids = goifile.read().rstrip('\n').split('\n')


    # store goi as keys-values (geneid:genename)pair
    goiKeyNval = collections.OrderedDict()
    for items in goi_ids:
        if items.startswith('#'):
            continue
        items = items.split('\t')

        # update the keys-values pair
        goiKeyNval[items[0]] = items[2]

    #print('GenesIDs vs. GeneNames')
    #print(goiKeyNval)
    #print()


    '''Now, we start reading the transcript file. 
       And, extract the sequences for the "goi". '''

    # write the sequences of each sample in separate directory
    # create one file for each gene
    if os.path.exists(output + '_sequences'):
        shutil.rmtree(output + '_sequences', ignore_errors=False, onerror=None)
    os.makedirs(output + '_sequences', exist_ok=True)

    for genename in goiKeyNval.values():
        open(output + '_sequences' + '/' + genename + '.fa', 'w+')

    writeseq = ''
    for lines in infile:
        if lines.startswith('>'):

            # Find the geneId or any other identifier
            # **this may change depending upon how the gene identifier has been set
            geneid = lines.lstrip('>').rstrip('\n').split('|')[1].split(':')[0].split('_')[0]

            # if gene of interest matches the current sequence write the sequence data
            if geneid in goiKeyNval.keys():
                # write a new line for the output gene,transcript sequence
                # this new line will have a geneName
                writeline = open(output + '_sequences' + '/' + goiKeyNval[geneid] + '.fa', 'a')
                writeseq = True

                ## Optional** - but doesn't work when there are multiple transcripts, with same geneId
                # remove that key from the dictionary
                # this reduces loop burden
                #goiKeyNval[geneid]
            else:
                writeseq = False

        if writeseq == True:
            #writeline = open(output + '_sequences' + '/' + genename + '.fa', 'a')
            writeline.write(lines)

    print()
    print('The End :)')



