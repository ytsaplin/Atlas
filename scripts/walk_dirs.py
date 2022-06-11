import os

path = "datasets-aggregated-regionally/data/CORDEX"


with open(os.path.join(os.path.abspath(path), "index.txt"), 'w') as f:

    for dirpath, dirnames, filenames in os.walk(path):
        for name in filenames:
            #print(os.path.join(dirpath, name))
            f.write(os.path.join(dirpath, name)+"\n")