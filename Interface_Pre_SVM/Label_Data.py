# File function: Label matrix and create the matrix can send into SVM
# Person write this file: Tianhe Wu
# Date: 2020.10.15

from Preprocessing.Build_Data_Graph import Data


class Label:

    # No parameter need to send
    def __init__(self) -> None:

        self.data_c = Data()
        # Middle process matrix
        self.mp_matrix = self.data_c.get_graph()
        # Final label matrix
        self.l_matrix = []
        # Label dimension
        self.l_dimension = self.data_c.get_len()

    # Label middle matrix
    def label(self) -> None:
        for i in range(1, len(self.mp_matrix)):
            if self.mp_matrix[i][0][13] == '0':
                # 01 is sick
                self.mp_matrix[i].append(1)
            elif self.mp_matrix[i][0][13] == '1':
                # 11 is health
                self.mp_matrix[i].append(-1)

    # Get the final matrix with label
    def get_label_matrix(self) -> [list]:
        # Label the middle matrix
        self.label()
        # Filter the first element which is the title of the sample
        for i in range(1, len(self.mp_matrix)):
            cur_ = []
            for j in range(1, len(self.mp_matrix[i])):
                cur_.append(self.mp_matrix[i][j])
            self.l_matrix.append(cur_)

        return self.l_matrix

    # Get miRNA index
    def get_miRNA(self) -> dict:
        return self.data_c.miRNA

    # Get index -> miRNA
    def get_r_miRNA(self) -> dict:
        return self.data_c.r_miRNA
