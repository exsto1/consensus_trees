import os
from Bio.AlignIO import convert

in_file = "../temp/msa.fasta"
out_file = "../temp/msa_new.fasta"
os.system(f"mafft --auto --reorder {in_file} > {out_file}")

convert(out_file, "fasta", "../temp/msa_new.phylip", "phylip-relaxed")
convert(out_file, "fasta", "../temp/msa_new.nexus", "nexus", "protein")