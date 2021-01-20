# File function: Send the parameter into SVM and train
# Person write this file: Tianhe Wu
# Date: 2020.10.16

from SVM_REF.Classifier.SVM_Classifier import SVM_CF
from Interface_Pre_SVM.Label_Data import Label
import numpy as np
import copy


class Run:

    # No parameter need to send
    def __init__(self) -> None:
        self.save_f_w = []
        self.f_w = []
        self.f_b = []
        self.sorted_w = []
        # miRNA name -> index, str -> int
        self.name_w = {}
        # miRNA index -> name, int -> str
        self.f_mw = {}
        # Final miRNA name to w
        self.sorted_mw = {}

    # Run the program
    def run(self) -> None:
        self.label = Label()
        f_matrix = self.label.get_label_matrix()
        f_dimension = self.label.l_dimension
        f_svm = SVM_CF(f_dimension, f_matrix)
        f_svm.train()

        # Transform to list
        l_w_ = []
        for i in f_svm.w:
            for j in i:
                l_w_.append(j)

        self.f_w = l_w_
        self.f_b = f_svm.b[0]
        # Save the unsorted f_w
        self.save()

    # Save the f_w
    def save(self) -> None:
        self.save_f_w = copy.deepcopy(self.f_w)

    # Return w length
    def get_w_len(self) -> int:
        return np.shape(self.f_w)[1]

    # Get sorted w
    def get_sorted_w(self) -> list:
        self.f_w = sorted(self.f_w, key=abs)
        self.f_w.reverse()
        self.sorted_w = copy.deepcopy(self.f_w)
        self.f_w = copy.deepcopy(self.save_f_w)
        return self.sorted_w

    # Set miRNA dict
    def set_m(self) -> None:
        self.name_w = self.label.get_miRNA()

    # Get miRNA dict
    def get_m(self) -> dict:
        return self.name_w

    # Set miRNA name to w
    def set_mw(self) -> None:
        r_mi = self.label.get_r_miRNA()
        for i in range(len(self.f_w)):
            if i not in self.f_mw:
                self.f_mw[self.f_w[i]] = r_mi[i]

    # Get miRNA -> w
    def get_mw(self) -> list:
        return self.f_mw

    # Sort the w and return w -> miRNA name
    def get_sorted_m(self) -> dict:
        self.set_mw()
        for i in self.get_sorted_w():
            if i not in self.sorted_mw:
                self.sorted_mw[i] = self.f_mw[i]
        return self.sorted_mw









