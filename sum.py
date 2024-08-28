

# Write and test a function to meet this specification.

# sumList(nums). nums is a list of numbers. Returns the sum of the numbers in the list. 

# nums could be [0, 0, 0, 1, 3, 5] 
#            or [0]
#            or [1, 1, 1, 1]


def sumList(nums):
    total = 0
    for each in nums:
        total = total + each
    print(total)
    
l = [1,2,3]

sumList(l)