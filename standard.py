import numpy as np
import pandas as pd

'''
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = x == y
k = np.array_equal(x, y)
print(k)
'''

#a = np.array([[1, 1],
#              [0, 0]])
'''
print(a)
a = a.T
print(a)
'''
'''
a = a.reshape((4, 1))
print(a)
a = a.reshape((1, 4))
print(a)
'''
'''
x = np.array([1, 3, 2])
print(x.sum())

print(x.min())

print(x.max())

print(x.mean())

print(x.std())
'''
'''
a = np.array([[1, 1],
              [2, 2]])
print(a.sum(axis=0))
print(a.sum(axis=1))
'''

'''

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])

print(np.dot(x, y))
print(np.cross(x, y))

a = np.array([[1, 1],
              [2, 2]])
b = np.array([[1, 3],
              [2, 4]])
print(np.matmul(a, b))
'''

'''
s = pd.Series([1, 2, 5, np.nan, 6, 8])
print(s)
print("####")
'''
df = pd.DataFrame(np.random.randn(6, 4), columns=['A','B','C','D'])
'''
print(df)
print("####")
print(df.head(0))
print("####")
print(df.tail(2))
print("####")
print(df.columns)
print("####")
print(df['B'])
'''
'''
s1 = pd.Series([1, 2, 3, 4, 5, 6])
print(s1)
df['F'] = s1
print(df)
'''
'''
df.at[0, 'A'] = 0
print(df)
df.iat[0, 1] = np.nan
print(df)
'''
'''
df1 = pd.DataFrame(np.random.randn(3, 5), columns=['A', 'B', 'C', 'D', 'F'])
print(df)
df = pd.concat((df, df1), axis=0)
print(df)
df = df.reset_index(drop=True)
print(df)
'''

c1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9], name='Z')
print(c1)
c = pd.concat([df, c1], axis=1)
print(c)