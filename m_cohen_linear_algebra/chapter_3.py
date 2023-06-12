from typing import List
from functools import partial
# Coding challenge 3.12
# 1
"""
Create a linear weighted combination of three vectors. You’ll learn in later chapters that linear combinations are most effi- ciently represented as matrix-vector multiplication, but we’ll keep things simple for now. Create three 5-D vectors and a fourth vector that contains the weights for each vector. Then create the weighted sum of those vectors. Next, modify the code to compute the weighted mixture of four 5-D vectors. What is the relationship between the dimensionality of the to- be-summed vectors, the number of vectors to sum, and the dimensionality of the coefficients vector?
"""
def lin_comb(x:List[int], weight:List[int])->int:
    assert len(x) == len(weight), "vector length not matching"
    
    return (weight[i] * x[i] for i in range(0,len(weight)))
             
a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [11,22,33,44,55]

w = [1,10,12,20,42]

w_a = sum(lin_comb(a, w))
w_b = sum(lin_comb(b, w))
w_c = sum(lin_comb(c, w))
# weighted mixture of vectors
partial_lin_comb = partial(lin_comb, weight = w)
w_mix_a_c = map(partial_lin_comb, [a,b,c])
total = sum(sum(x) for x in w_mix_a_c)

# 2
"""
Develop a method to use the dot product to compute the aver- age of a set of numbers in a vector. (Hint: consider the vector of all ones, sometimes written 1.)
"""
def dot_product(a:List[int],b:List[int])->int:
    assert len(a) == len(b)
    return sum(a[i] * b[i] for i in range(0, len(a)))

def average(a:List[int])->int:
    return (dot_product([1]*len(a), a)) * (1/len(a))

one_vec = [1] * 5

print(average([1,4,10]))

# 3 
"""
What if some numbers were more important than other num- bers? 
Modify your answer to the previous question to devise a method to use the dot product to compute a weighted mean of a set of numbers.
"""

w = [3,2,1]
print(average(list(lin_comb(w, [1,4,10]))))
