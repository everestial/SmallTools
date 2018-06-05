#!/home/bin/python3

print('\nChecking and Importing required modules \n')

# Call the required modules
import sys
import os


''' Call input and output argument variable names'''
# update to descriptive argument in the future :)
inHaplotype = sys.argv[1]
inStats = sys.argv[2]
inCutoff = sys.argv[3]
inSample = sys.argv[4]
outFile = sys.argv[5]


## Function: The phase-Extender recursively joins the short RBphased haplotypes.
  # After certain point it is difficult to futher extend the haplotype due to small haplotype
  # .. chunks present between two large haplotypes. In such situation it is helpful to remove ..
  # .. those haplotypes that have small number of variants.

#inStats="/home/priyanka/Downloads/FromHenry2/final_haplotype_stats_Sp21-Set02.txt"
#inHaplotype="/home/priyanka/Downloads/FromHenry2/extended_haplotype_Sp21.txt"
#outFile="/home/priyanka/Downloads/FromHenry2/extended_haplotype_Sp21-filtered.txt"

with open(inHaplotype, 'r') as inhap, \
    open(inStats, 'r') as hapstats, \
        open(outFile, 'w') as newhap:

    # Part A: Create the a list of haplotypes indexes (PI) that needs filtering
    # based on the user input cutoff size of the haplotype block
    # this removes all the haplotype blocks that have variants ..
    # .. this size or smaller
    variant_cutoff_size = int(inCutoff) #5
    my_samples = inSample

    pi_to_remove_dict = {}
    for line in hapstats:
        if line.startswith('CHROM'):
            # CHROM	Sp21:PI	num_Vars_by_PI	range_of_PI	total_haplotypes	total_Vars

            sample_pi_idx = my_samples + ':PI'
            pi_idx = line.rstrip('\n').split('\t').index(sample_pi_idx)

            # index position of the column that contains number of variants for each PI
            num_vars_idx = line.rstrip('\n').split('\t').index('num_Vars_by_PI')

            #except IndexError:
                #sys.exit()

            continue

        # Now, find the indexes of the PI that has number of variants below cutoff_size
        # .. then find the acutal PI based on that cutoff
        new_line = line.rstrip('\n').split('\t')
        chrom = new_line[0]

        pi_list = new_line[pi_idx].split(',')
        vars_list = new_line[num_vars_idx].split(',')

        idx_of_vars_below_cutoff = [i for i, e in enumerate(vars_list)
                                    if int(e) < variant_cutoff_size]

        vars_below_cutoff = [vars_list[x] for x in idx_of_vars_below_cutoff]

        pi_below_cutoff = [int(pi_list[x]) for x in idx_of_vars_below_cutoff]
        pi_to_remove = {chrom: pi_below_cutoff}

        # Store the PI values to filter in a dictionary using chrom as keyes
        for ks, vs in pi_to_remove.items():
            if ks in pi_to_remove_dict.keys():
                pi_to_remove_dict[ks] += vs
            else:pi_to_remove_dict[ks] = vs


    # Part B: Now, take the list of "PI" that have number of variants below cutoff ..
    # .. and filter those lines out
    for linex in inhap:
        if linex.startswith('CHROM'):
            sample_pi_idx = my_samples + ':PI'
            sample_pgal_idx = my_samples + ':PG_al'

            pi_idx = linex.rstrip('\n').split('\t').index(sample_pi_idx)
            pg_idx = linex.rstrip('\n').split('\t').index(sample_pgal_idx)

            newhap.write(linex)
            continue


        linex = linex.rstrip('\n').split('\t')
        #if int(linex[1]) > 15000:
            #break

        chrom = linex[0]
        pi_in_linex = linex[pi_idx]

        new_linex = linex.copy()
        if chrom in pi_to_remove_dict.keys():
            if pi_in_linex == '.':
                new_linex = new_linex
                newhap.write('\t'.join(new_linex) + '\n')

            elif int(pi_in_linex) in pi_to_remove_dict[chrom]:
                # do not write the line
                continue
                # ** for future: if we need to write the line but remove the GT and PI values
                #del new_linex[pi_idx:pg_idx +1]
                #new_linex.insert(pi_idx, '.')
                #new_linex.insert(pg_idx, '.')
        else: new_linex = new_linex

        newhap.write('\t'.join(new_linex) + '\n')

    print('Complete :) ')

















