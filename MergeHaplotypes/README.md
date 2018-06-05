# MergeHaplotypes
Python parser to merge the haplotypes obtained from `phase-Extender` and `phase-Stitcher`.

**`MergeHaplotypes`** comes in two flavors

  - mergeHaplotypesPandas : is used to merge files if the 
  haplotype files are not too many and can fit into your computer memory.
  - mergeHaplotypeDask : Dask has same usage as pandas but is capable of handling many and 
  large files and due to distributive computuing and slow processing to minimize memory bloat out.
  
<br>
  
## Usage

```bash
$ python3 merge_haplotypePandas.py -h
  # or
$ python3 merge_haplotypeDask.py -h

Checking required modules 

usage: merge_haplotypePandas.py [-h] [--hapList HAPLIST] [--f1List F1LIST]
                                [--f1ParentIDs F1PARENTIDS] --output OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  --hapList HAPLIST     name of the file that contains list of path to
                        haplotype files obtained from phase-Extender.
  --f1List F1LIST       name of the file that contains list of the path to F1
                        hybrid haplotype files obtained from phase-Stitcher.
  --f1ParentIDs F1PARENTIDS
                        comma separated names of the column header that
                        indicates paternal haplotype vs. maternal haplotype in
                        F1 hybrids haplotypes. Only required if 'f1List' is
                        reported.
  --output OUTPUT       Directory name to store the merged haplotype file.
```

<br>

### Using the example file
<pre>
python3 merge_haplotypePandas.py --hapList hapList-Set.txt --f1List f1List-Set.txt --output mergedDir --f1ParentIDs Sp,My
</pre>
