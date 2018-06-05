
## An interactive python tool to extract the desired features and attribute values from a gtf file

# Builtin modules
import sys

print('\n Checking required modules \n')

try: from io import StringIO
except: sys.exit('StrinIO module not found.\nPlease install it.')

try: import pandas as pd
except: sys.exit('pandas module not found.\nPlease install it.')

try: import subprocess
except: sys.exit('subprocess module not found.\nPlease install it.')

try: import argparse
except: sys.exit('argparse module not found.\nPlease install it.')


# Starting a function to prepare interactive session

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gtf",
                        help="gtf file to extract the information from", required=True)
    parser.add_argument("--feature",
                        help="features to extract", default='gene', required=True)
    parser.add_argument("--attributes",
                        help="attributes to extract", default= 'gene_id', required=True)
    parser.add_argument("--output",
                        help="prefix for the output file name", required=True)

    ## optional argument
    parser.add_argument("--chr", help="Restrict to a specific chromosome.",
                        required=False)
    parser.add_argument("--remove_columns",
                        help="optional columns to remove", default= 'gene_id', required=False)


    global args;
    args = parser.parse_args()


    # got to this function
    read_gtf()


def read_gtf():
    global args;

    ## Step 01:
    # prepare an argument to select the lines except headers (which start with #)
    call_gtf = ["grep", r'^#', '-v', args.gtf]

    # subprocess the argument and pipe the stdout
    gtf = subprocess.Popen(call_gtf, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    gtf_main_data = gtf.communicate()[0]
    # Note: the output from subprocess Popen is [stdout, stderror]
    # so, selecting the first index at 0

    ## Step 02: sort the data
    sort_gtf = ['sort', '-k1,1', '-k2,2n']
    # gtf is a bed file, so sorting at contig and start position

    gtf_sort = subprocess.Popen(sort_gtf, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    gtf_main_data_sorted = gtf_sort.communicate(gtf_main_data)[0].decode('utf-8')

    # clear memory
    del call_gtf, gtf_main_data, gtf, sort_gtf, gtf_sort

    # return this data to another function
    return mine_gtf(gtf_main_data_sorted)

def mine_gtf(gtf_main_data_sorted):
    global args;

    # Step 03-A: Read the data into pandas dataframe
    gtf_df = pd.read_csv(StringIO(gtf_main_data_sorted), sep='\t',
                         names=['contig', 'source', 'feature', 'start', 'end',
                                'score', 'strand', 'frame', 'attribute'])

    del gtf_main_data_sorted


    ## Step 03-B: expand attributes and handle the user input requirements

    # expand the attribute values as each column
    gtf_df['attribute'] = gtf_df['attribute'].apply(lambda x: x.rstrip(';')\
                                                    .replace('"', '').split('; '))
    attri_values_X = [dict(tuple(b.split())[:2] for b in a) for a in gtf_df['attribute']]


    # indetify the features to select
    features = str(args.feature).split(',')

    # identify the attributes to select
    attributes = str(args.attributes).split(',')

    # identify the chrmosome/contig to select
    chrom = str(args.chr).split(',')

    #### Note: if interger method is desired, do
    # chrom = map(int, chrom) # but since some of contig might be like scaffold_216 (as string type data)
    # so, str(x).split and then pandas.DF.astype(str).isin(chrom) is implied to take contig value as string

    # identify the columns to remove
    remove = str(args.remove_columns).split(',')


    ## Step 03-C: Select the user output requirements

    ## update pandas dataframe using user selected attributes
    df = pd.DataFrame(attri_values_X, columns=attributes)

    ## update the gtf_df using the user selected feature values
    gtf_df = gtf_df.loc[gtf_df['feature'].isin(features)]

    ## update the gtf_df using the user selected chrom/contig values
    gtf_df = gtf_df.loc[gtf_df['contig'].astype(str).isin(chrom)]

    ## Join the dataframes (features and attributes) and fill the na values with 'NA'
    # the join happens along the default pandas index ...
    # ... so the original feature-attribute connection is preserved
    gtf_df = gtf_df.join(df).fillna(value='NA')

    ## update pandas dataframe by removing optional columns
    gtf_df.drop(remove, axis=1, inplace=True)

    # sort the dataframe
    gtf_df.sort_values(by=['contig', 'start'], inplace=True, ascending=True)

    del gtf_df['attribute'], df, features, attributes, attri_values_X

    # write dataframe to table
    pd.DataFrame.to_csv(gtf_df, args.output + '_gtf_to_table.txt', sep='\t', index=False)

    print('\n gtf to table complete ! \n')

# we are creating a new function called "fun_flush_print" ..
# .. which is/will-be used for working with several other functions within the program
def fun_flush_print(text):
    print(text);
    sys.stdout.flush();


def fatal_error(text):
    fun_flush_print("     FATAL ERROR: " + text);
    quit();


if __name__ == "__main__":
    main();

