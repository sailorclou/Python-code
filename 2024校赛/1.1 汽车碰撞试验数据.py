import numpy as np
import math as m

naodu_list = [15.92, 15.84, 15.92, 16.08, 16.16, 16.00]
gangdu_list1 = []
c = 160
F = 20000
for naodu in naodu_list:
    gangdu = c * F / naodu
    gangdu_list1.append(round(gangdu, 2))
print(gangdu_list1)

# 方差
variance = np.var(gangdu_list1)

print("现场试验样本标准差：", round(m.sqrt(variance)))