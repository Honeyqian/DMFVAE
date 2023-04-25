import numpy as np
import pandas as pd
pathresult = "data/8968/"
md = pd.read_excel("data/8968/association.xlsx", delimiter='\t', skiprows=0,
                             usecols=[i for i in range(0, 789)])#374行788列
A = np.transpose(md)
D_M = np.array(md)
M_D = np.array(A)
row,col = M_D.shape
print(M_D.shape)
xd_pos_set= []  # positive
xd_neg_set = []
xm_pos_set = []
xm_neg_set = []
neg_set = []  # negative
labels_0 = []
for i in range(row):  # 383
    for j in range(col):  # 495
            # label = data_MD.iloc[i][j]   # 0 or 1
        label = M_D[i][j]  # 0 or 1
        if (label == 1):  # positive
            xd_pos_set.append((i,j,1))

        else:  # negative
            xd_neg_set.append((i,j,0))
                # mc_3 = np.hstack((DE [i], NEWSD451 [i]))
                # mc_4 = np.hstack((ME [j], NEWSM451 [j]))
                # matrix_cells_01 = np.vstack((mc_1, mc_2))
                # matrix_cells_02 = np.vstack((mc_3, mc_4))
xd_pos_set = np.array(xd_pos_set)
print(xd_pos_set.shape)
xd_neg_set = np.array(xd_neg_set)
np.savez(pathresult+"XD_matrixcell_post",matrix=xd_pos_set)
np.savez(pathresult+"XD_matrixcell_neg",matrix=xd_neg_set)
for i in range(D_M.shape[0]):  # 383
    for j in range(D_M.shape[1]):  # 495
            # label = data_MD.iloc[i][j]   # 0 or 1
        label = D_M[i][j]  # 0 or 1
        if (label == 1):  # positive
            xm_pos_set.append((i,j,1))

        else:  # negative
            xm_neg_set.append((i,j,0))
xm_pos_set = np.array(xm_pos_set)
xm_neg_set = np.array(xm_neg_set)
np.savez(pathresult+"XM_matrixcell_post",matrix=xm_pos_set)
np.savez(pathresult+"XM_matrixcell_neg",matrix=xm_neg_set)