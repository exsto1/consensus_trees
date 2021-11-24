import os
from Bio.Phylo import Consensus, NewickIO, draw

# trees = []
# for i in os.listdir("trees"):
#     if "tree" in i:
#         file_h = open(f"trees/{i}")
#         x = NewickIO.Parser(file_h).parse()
#         for tree in x:
#             trees.append(tree)
#         file_h.close()
#
# majority = 0.3
# result = Consensus.majority_consensus(trees, majority)
# draw(result, show_confidence=False)


with open("main_trees/original_phylo.txt") as orig:
    orig_tree = NewickIO.Parser(orig).parse()
    for tree in orig_tree:
        n_t = tree.get_nonterminals()
        t = tree.get_terminals()
        print(len(n_t), len(t))
        draw(tree)


