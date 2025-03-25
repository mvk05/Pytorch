import torch

#Scalar is a single number but in tensor-speak it's a zero dimension tensor.
scalar = torch.tensor(7)
print(scalar.item())

#Vector is a one-dimensional tensor and can contain multiple numbers.
vector = torch.tensor([1, 2])
print(vector.ndim)