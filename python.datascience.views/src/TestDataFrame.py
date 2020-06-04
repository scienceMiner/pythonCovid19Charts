'''
Created on 19 May 2020

@author: ethancollopy
'''
import pandas as pd

df = pd.DataFrame({
                    'A':[1, 2, 3], 
                    'B':[4, 5,6],
                    'C':[7, 8, 9],})

print( df )
 #  A  B  C
#0  1  4  7
#1  2  5  8
#2  3  6  9

print( df.loc[[0,1],:].applymap(lambda x: 2*x) )

#    A   B   C
#0   2   8   14
#1   4   10  16

print( df.loc[[1,2],:].applymap(lambda x: 3*x) )

print( df.applymap(lambda y: y.rolling(window=3).mean())  )
#casesData3.iloc[:,[0]].rolling(window=3).mean()

#    A   B   C
#1   6   15  24
#2   9   18  27