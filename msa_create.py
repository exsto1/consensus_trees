import os
from Bio.AlignIO import convert

list_of_files = os.listdir("genolevures_uniquefamilies")
in_file = [f"genolevures_uniquefamilies/{i}" for i in list_of_files]
out_file = [f"msa_files/{i}" for i in list_of_files]
for i in range(len(in_file)):
    os.system(f"mafft --auto --reorder {in_file[i]} > {out_file[i]}")

# convert(out_file, "fasta", "../temp/msa_new.phylip", "phylip-relaxed")
# convert(out_file, "fasta", "../temp/msa_new.nexus", "nexus", "protein")