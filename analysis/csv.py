#! /usr/bin/env python
# coding: utf-8

import os

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)
    with open(path_to_file,"r") as f:
        preview = f.readline()
        print("Yeah! We managed to read the file. Here is a preview:")
        print(preview)

def main():
    launch_analysis('current_mps.csv')
    
if __name__ == "__main__":
    main()
else:
    print("import {}".format(__name__))