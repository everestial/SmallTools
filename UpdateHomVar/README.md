# UpdateHomVar
Update the phased index of the homozygous variants in ReadBackPhased Variants.

ReadBackPhased variants only incorporate the haplotype index for heterozygous variants. 
Sometime adding non-reference (i.e other than GT = 0/0) homozygous variants could be helpful 
if the non-ref homozygous variants is fixed in two populations, or when non-ref homozygous
variants is mostly associated with heterozygous allele in nearby genomic position.

This tool helps to update the phased genotype (PG) and phase index (PI) values in
ReadBackPhased VCF files prepared from phASER (https://github.com/secastel/phaser).
For more details on this topic see **issue number 10** under `phaser` tool.


## Usage:

   `python UpdateHomVar.py input.vcf output.vcf`
    
**Run the test data**:

   `python UpdateHomVar.py ms01e_phased.vcf ms01e_phased_updated.vcf`
