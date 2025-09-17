import numpy as np

# Question 1
a1 = np.arange(5, 26)
a2 = np.random.randint(10, 51, (3, 4))

# Question 2
print(a1.shape)
print(a1.size)
print(a1.dtype)
print(a2.shape)
print(a2.size)
print(a2.dtype)

# Question 3
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)

# Question 4
b1 = np.arange(1, 10)
b2 = b1.reshape(3, 3)
print(b2 * 5)

# Question 5
c1 = np.arange(10, 26)
c2 = c1.reshape(4, 4)
print(c2[1])
print(c2[:, -1])
c2[0] = 0
print(c2)

# Question 6
d1 = np.random.randint(20, 41, 10)
mask = d1 > 30
print(d1[mask])

# Question 7
e1 = np.arange(11, 23)
e2 = e1.reshape(3, 4)
print(e2)

# Question 8
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))
print(A.T)

# Question 9
f1 = np.random.randint(10, 61, 15)
print(np.mean(f1))
print(np.median(f1))
print(np.std(f1))

# Question 10
M = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])
print(np.linalg.det(M))
print(np.linalg.inv(M))
w, v = np.linalg.eig(M)
print(w)
print(v)

# Question 11
positions = np.array([[0, 0], [2, 3], [4, 7], [7, 10], [10, 15]])
dist = np.linalg.norm(positions[-1] - positions[0])
print(dist)
step_diffs = np.diff(positions, axis=0)
step_dist = np.linalg.norm(step_diffs, axis=1)
total_dist = np.sum(step_dist)
print(total_dist)