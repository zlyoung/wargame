import pandas as pd
import numpy as np

# data1 = pd.DataFrame([[1,2,3], [4,5,6]], columns=['a','b','c'])
# data2 = pd.DataFrame([[2,3,9], [5,7,7]], columns=['b','c','d'])
# print(data1)
# print('\n')
# print(data2)
# print('\n')
# me = data1.merge(data2, how='left')
# print(me)

a = np.load('demo.npy', allow_pickle=True)
# graphTable=a.tolist()
print(a.shape)
for i in range(0,5):
    print(len(a[i]))
