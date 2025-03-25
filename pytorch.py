import torch

#Scalar is a single number but in tensor-speak it's a zero dimension tensor.
scalar = torch.tensor(7)
print(scalar.item())

#Vector is a one-dimensional tensor and can contain multiple numbers.
vector = torch.tensor([1, 2]) #You can tell the number of dimensions in a tesor by checking how many sqaure brackets are used to define it. (on one side)
print(vector.ndim) 
print(vector.shape) #returns the shape of the vector which is 2 (number of elements in the vector)

#Matrix is a two-dimensional tensor and can contain multiple vectors (rows).
MATRIX = torch.tensor([[7, 8],
                       [9, 10]]) 
print(MATRIX)
print(MATRIX.ndim) #matrices have an extra dimension
print(MATRIX.shape) #returns the shape of the matrix which is 2x2 (rows x columns)

#Tensor is a multi-dimensional array and can contain multiple matrices (or higher dimensions).
TENSOR = torch.tensor([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]])
print(TENSOR.ndim) #the following tensor has 3 dimensions(3 brackets on one side)
print(TENSOR.shape) #returns the shape of the tensor which is 1x3x3 (1 matrices, each with 3 rows and 3 columns)

#Creating a tensor with random values
rand_tensor = torch.rand(size=(3,4)) #creates a random tensor of size 3 and 4
print(rand_tensor, rand_tensor.dtype) #the default data type is float32

#Creating a tensor with zeros

zero_tensor = torch.zeros(size=(3, 4)) #creates a tensor of size 3 and 4 filled with zeros
print(zero_tensor, zero_tensor.dtype) #the default data type is float32

#Creating a tensor with ones
ones_tensor = torch.ones(size=(3, 4)) #creates a tensor of size 3 and 4 filled with ones
print(ones_tensor, ones_tensor.dtype) #the default data type is float32

#Creating a tensor with a specific range
range_tensor = torch.arange(start=0, end=10, step=1) #creates a tensor with values from 0 to 9 with a step of 1
print(range_tensor)

#Creating a tensor of a certain type with the same shape as an another tensor
type_tensor = torch.ones_like(input=MATRIX)
print(type_tensor)

#Tensor Data Types