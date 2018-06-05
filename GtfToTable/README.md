# gtf to table

## Introduction
**This is a python parser that can be used to mine the features and attributes value from a gtf/gff file** 

for more details on gtf/gff file see: http://www.ensembl.org/info/website/upload/gff.html , http://mblab.wustl.edu/GTF22.html




# Prerequisites:
Python packages and modules
- sys (https://docs.python.org/3/library/sys.html)
- Python3 (https://www.python.org/)
- pandas (http://pandas.pydata.org/)
- io/StringIO (https://docs.python.org/3/library/io.html)
- subprocess (https://docs.python.org/3/library/subprocess.html)
- argparse (https://docs.python.org/3/library/argparse.html)






# Running gtf_to_table.py

**For the given input file: ** `test_input.gtf`

## Usage (**using the following code**): 

    python GtfToTable.py --gtf test_input.gtf --feature gene,CDS,exon --attributes gene_name,gene_id --output test --remove_columns score,strand

**will generate the output as**

    contig	source	feature	start	end	frame	gene_name	gene_id
    2	jgi	CDS	3213	3464	0	NA	scaffold_200002.1
    2	jgi	exon	3213	3488	.	NA	scaffold_200002.1
    2	jgi	exon	5262	5496	.	CP5	scaffold_200003.1
    2	jgi	gene	5262	6915	.	CP5	scaffold_200003.1
    2	jgi	CDS	5282	5496	0	CP5	scaffold_200003.1
    2	jgi	CDS	5579	5750	1	CP5	scaffold_200003.1
    2	jgi	exon	5579	5750	.	CP5	scaffold_200003.1
