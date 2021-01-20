# File function: Run program
# Person write this file: Tianhe Wu
# Date: 2020.10.15

from Interface_Pre_SVM.Run_Fuc import Run

f_run = Run()
f_run.run()
miRNA_name = []
miRNA_ = f_run.get_sorted_m()


idx = 0
for key in miRNA_:
    print(miRNA_[key])
    if idx <= 10:
        miRNA_name.append(miRNA_[key])
    idx += 1

print(miRNA_name)

