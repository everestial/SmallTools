# FilterHaplotypes
A python parser to filter the haplotypes obtained from 
[phase-Extender](https://github.com/everestial/phase-Extender).
The filtering is based on the number of variants present in the haplotype blocks.

**This tool takes 5 positional arugment as different arugment input and all the arguments are mandatory.**

## Usage:
```
python3  FilterHaplotypes.py  arg01  arg02  arg03  arg04  arg05

# where,
   arg01 -> is name of the input haplotype file that is to be filtered.
   arg02 -> is the haplotype stats of the same file obtained from phaseExtender.
   arg03 -> variant cutoff size (integer).
            Any haplotype block that has number of variant below this cutt off is removed.
   arg04 -> sample name in the haplotype file.
   arg05 -> name of the output file.
```

<br>
<br>


## Example (from the example folder):

```
$ cat final_haplotype_stats_Sp21-small.txt

CHROM	Sp21:PI	num_Vars_by_PI	range_of_PI	total_haplotypes	total_Vars
1	13424,13034,5102,13184,17222,10737,12510,10050,10053,10054,17751	20,7,193,2,137,16,168,56,2,172,871	1677,468,8245,101,8920,8425,3961,1646,31,11150,39580	11	1644
```

We can see that there are few haplotypes that have few number of variants per blocks.
Block with PI **13184** and **10053** have only 2 variants per block. So, those two blocks are
preventing futher phase extension because `phase-Extender` works by reading two consecutive 
blocks at a time. It would therefore be wise to remove these blocks.

**Use the command:**

    python3 FilterHaplotypes.py extended_haplotype_Sp21-small.txt final_haplotype_stats_Sp21-small.txt 5 Sp21 filtered_Sp21haplotpe.txt

The output file won't have the lines from those blocks any more.