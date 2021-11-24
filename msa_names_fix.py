import os
from Bio.AlignIO import convert

list_of_files = os.listdir("msa_files")
in_file = [f"msa_files/{i}" for i in list_of_files]
out_file = [f"msa_files_corrected/{i}" for i in list_of_files]

for i in range(len(in_file)):
    file_h = open(in_file[i])
    file = file_h.readlines()
    file_h.close()

    newfile = open(out_file[i], "w")
    for i1 in file:
        if ">" in i1:
            newfile.write(i1[:5] + "\n")
        else:
            newfile.write(i1)

out_file_phylip = [f"msa_files_corrected/{i.split('.')[0]}.phy" for i in list_of_files]
for i in range(len(out_file)):
    convert(out_file[i], "fasta", out_file_phylip[i], "phylip-relaxed")
