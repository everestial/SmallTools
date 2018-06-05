#!/home/bin/python3

print('\nChecking and Importing required modules \n')

# Call the required modules
import sys
import os


''' Call input and output argument variable names'''
inFile = sys.argv[1]
outFile = sys.argv[2]


with open(outFile, 'w') as f:
#with open("ms01e_phased_updated.vcf", 'w') as f:
    print("reading input file: ", os.path.basename(sys.argv[1]))

    ''' Create an empty string variable to store the PI value
    from the phased heterozygote genotype block '''
    carryover_PI_value = ''
    carryover_CONTIG_value = ''

    vcf_data = open(inFile, 'r')
    #vcf_data = open('ms01e_phased.vcf', 'r').read().strip('\n').split('\n')

    chr_on_process = ''
    for lines in vcf_data:
        lines = lines.rstrip('\n')
        if lines.startswith('#'):
            ''' write the header part '''
            f.write(lines + '\n')

        else:
            lines = lines.split('\t')

            ''' write the values from CHR upto FORMAT field, wait for the SAMPLE field '''
            f.write('\t'.join(lines[0:9]))

            ''' now start mining the values and then update the field as necessary '''
            contig = lines[0]
            if chr_on_process != contig:  # to check with chromosome is being processed
                print('contig %s is being processed' % str(contig))
                print()
                chr_on_process = contig

            FORMAT_field = lines[8].split(':')
            SAMPLE_field = lines[9].split(':')
            #print(FORMAT_field)
            #print(SAMPLE_field)


            ''' Purpose: pick the index level for PI and PG tag from the INFO field. The tag position
             are not fixed in each line, so we had to employ this method'''
            PI_field_idx = FORMAT_field.index('PI')
            PG_field_idx = FORMAT_field.index('PG')


            ''' Purpose: now, pick the value for that index level from SAMPLE field '''
            PI_field_value = SAMPLE_field[PI_field_idx]
            PG_field_value = SAMPLE_field[PG_field_idx]

            #print(PI_field_idx, PI_field_value, PG_field_idx, PG_field_value, 'mark 01')


            if '|' in PG_field_value:
                """ Purpose:
                Now, start mining the data if the genotype is phased (PG with '|') in this line/site, like:

                GT:AD:DP:GQ:PL:PG:PB:PI:PW:PC:PM 0/1:48,91:139:99:.:.:2626,0,1270:1|0:2-15881553-C-A,
                2-15881764-T-C,2-15881944-C-T,2-15881974-C-A,2-15882091-A-T,2-15882328-T-A,2-15882364-T-G,
                2-15882451-T-C,2-15882454-T-C,2-15882493-T-C,2-15882505-T-A,2-15882592-G-A,2-15882607-C-T,
                2-15882615-A-G,2-15882618-G-C,2-15882822-G-A,2-15883059-C-G,2-15883070-G-C,2-15883071-T-C,
                2-15883431-A-T:4:|:0.5:0 """

                ''' update the carryover PI and contig value '''
                carryover_PI_value = PI_field_value
                carryover_CONTIG_value = contig

                ''' and write the line as is. No update required for this line. '''
                f.write('\t' + lines[9] + '\n')



                ''' Now, move to the next line if the condition isn't met.'''

            elif '/' in PG_field_value:
                ''' Now, the proceeding line may have a non-phased homozygous genotype, something like:
                GT:AD:DP:GQ:PL:PG:PB:PI:PW:PC:PM  1/1:134,0:134:99:.:.:0,120,1800:1/1:.:.:1/1:.:.

                In this case we burrow the 'carryover PI value' from previous line to update the PI index
                for this line.
                '''

                ''' first split the PG value '''
                PG_split = PG_field_value.split('/')
                #print(PG_split[0], PG_split[1], PG_split[0]==PG_split[1])


                if PG_split[0] == PG_split[1] and \
                        PG_split[0] != '.' and \
                        contig == carryover_CONTIG_value:

                    ''' Only update the PG and PI: if PG != ./.,
                     PG is Homozygous (0/0, 1/1, 2/2, etc),
                     if contig from previous line matches current contig
                     '''
                    new_PI_value = carryover_PI_value
                    new_PG = PG_field_value.replace('/', '|')
                    #print(carryover_PI_value, new_PI_value, '\n')

                    ''' update the values inside SAMPLE field for this line '''
                    SAMPLE_field[PI_field_idx] = new_PI_value
                    SAMPLE_field[PG_field_idx] = new_PG

                    ''' append the updated value to this line '''
                    f.write('\t' + ':'.join(SAMPLE_field) + '\n')

                else:
                    ''' for the lines that have PG as ./. '''
                    f.write('\t' + ':'.join(SAMPLE_field) + '\n')

            else:
                ''' for all other lines where PG might be '.' or something else '''
                f.write('\t' + ':'.join(SAMPLE_field) + '\n')

    print("updated phased state of Homozygous variants for the output file :", os.path.basename(sys.argv[2]))
    print()



