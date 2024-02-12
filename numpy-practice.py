import numpy as np

arr = np.array([21, 4, 52, 7, 8, 4353, 7, 9, 3, 32, 3, 6, 67, 988, 3, 245, 9, 0, 6, 5])

print(
    f"""Array is: {arr}
Number of dimensions is: {arr.ndim}
Number of elements is  : {arr.size}\n"""
)

arr_2d = arr.reshape(4, 5)
print(
    f"""2D array is:\n{arr_2d}
Number of dimensions is: {arr_2d.ndim}
Number of elements is  : {arr_2d.size}
Element at the index [2,2] is: {arr_2d[2,2]}
Element at the index [2,:] is: {arr_2d[2,:]}\n"""
)

arr_3d = arr.reshape(2, 5, 2)
print(
    f"""3D array is:\n{arr_3d}
Number of dimensions is: {arr_3d.ndim}
Number of elements is  : {arr_3d.size}
Element at the index [2,2,1] is: {arr_3d[1,0,1]}
Element at the index [2,:] is: {arr_3d[0,:,1]}\n"""
)

array_1d = np.random.randint(50, size=10, dtype="int8")
array_2d = np.random.randint(100, size=(3, 5), dtype="int8")
array_3d = np.random.randint(10, size=(3, 3, 4), dtype="int8")
print(
    f"""1D array is: {array_1d}
Indexing at index 6 for 1D array: {array_1d[6]}
Slicing at index 3:8 for 1D array: {array_1d[3:8]}"""
)
print(
    f"""2D array is:\n{array_2d}
Indexing at index 2, 0 for 2D array: {array_2d[2,0]}
Slicing at index 1:3, 4 for 2D array: {array_2d[1:3, 4]}"""
)
print(
    f"""3D array is:\n{array_3d}
Indexing at index 2,0,3 for 3D array: {array_3d[2,0,3]}
Slicing at index 0:2, 1,2:4 for 3D array:\n{array_3d[0:2, 1, 2:4]}"""
)

arr_zeros = np.zeros((4, 5))
arr_ones = np.ones((4, 5))
print(
    f"(4,5) array of all zeros is:\n{arr_zeros}\n(4,5) array of all ones is:\n{arr_ones}"
)
new_array = np.concatenate([arr_ones, arr_zeros], axis=0)
print(f"Concatenated array at axis 0 is:\n{new_array}")
new_array = np.concatenate([arr_ones, arr_zeros], axis=1)
print(f"Concatenated array at axis 1 is:\n{new_array}")
