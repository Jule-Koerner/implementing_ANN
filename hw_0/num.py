import numpy as np

#
a = np.random.normal(0, 1, size = (5,5))
print(a)
a[np.square(a) > 0.09] = 42
print(a[:,3])
#print(test)
#print(test[np.square(test) > 0.09])


#if np.square(test) > 0.09:


#print(np.square(test))


#test = np.where(np.square(test) > 0.09, 42, test)
#print(test)
#print(array)


#array = np.array([[1,2,3,4,5],[6,7,8,9,1],["a","b",3,4,5],[1,2,"c",4,5],[1,2,3,4,5]])
#print(array[:,1])


#a = np.array([[1,2,3],[1,2,3],[1,2,3]])
#a[np.square(a) > 4] = 10
#a[:,1] = 5
#print(a)

a = np.array([[5,5,3],[1,2,3],[1,2,3]])
print(a[0,(0:1)])
print(np.ndim(a))

#b = np.arange(1,8,2)
#print(b)
#c = np.ones((5,4))
#print(c)

#print(c+b)
