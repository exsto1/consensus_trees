import os
from subprocess import run
from tqdm import tqdm

import os

list_of_files = os.listdir("msa_files_corrected")
list_of_files = [i for i in list_of_files if "_" not in i]
list_of_files = [i for i in list_of_files if ".phy" in i]
in_file = [f"msa_files_corrected/{i}" for i in list_of_files]
out_file = [f"trees/{i.split('.')[0]}" for i in list_of_files]

for i in tqdm(range(len(in_file))):
    run(f"/home/exsto/PHYML/PhyML-3.1/PhyML-3.1_linux64 -i {in_file[i]} -d aa -b 0 > {out_file[i]}", shell=True)