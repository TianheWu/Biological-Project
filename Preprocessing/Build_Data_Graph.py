# File function: Define the Data class and create the graph
# Person write this file: Tianhe Wu
# Date: 2020.10.15

import pandas as pd


class Data:

    # No parameter need to send
    def __init__(self) -> None:

        file = "D:\wutianhe_document\Project_Filter_Biomarkers\data.csv"
        self.datafile = pd.read_csv(file)
        # The data matrix
        self.data_graph = [[] for _ in range(565)]
        # miRNA string -> idx, str -> int
        self.miRNA = {}
        # idx -> miRNA, int -> str
        self.r_miRNA = {}

    # Create the matrix
    def build_table(self) -> None:

        # Fill the first line into data_graph[0]
        idx_ = 0
        for i in self.datafile:
            if i not in self.miRNA and i != 'id':
                # Give each miRNA an index
                self.miRNA[i] = idx_
                self.r_miRNA[idx_] = i
                idx_ += 1
            self.data_graph[0].append(i)

        # Fill other lines with data
        for i in self.datafile:
            idx_ = 1
            for j in self.datafile[i]:
                self.data_graph[idx_].append(j)
                idx_ += 1

    # For the dimension of SVM
    def get_len(self) -> int:
        return len(self.data_graph[1]) - 1

    # Get the graph of data
    def get_graph(self) -> [list]:
        self.build_table()
        return self.data_graph
