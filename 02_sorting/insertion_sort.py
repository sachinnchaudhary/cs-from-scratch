#Examples...........................

"""array =  np.array([4,2,5,6,3])

n = len(array) 

for j in range(1, n):  
    
    key = array[j]
    i = j - 1  
     
    while i >= 0 and array[i] > key:  
        array[i +1] = array[i]
     
        i = i - 1

    array[i+1] = key 

print(array)
"""


"""arr = [4,7,3,5,2]

n = len(arr)


for j in range(1, n):  

     key = arr[j]
     
     i = j - 1

     while i >= 0  and arr[i] > key:  

          arr[i+1] = arr[i]

          i = i -1  
          print(arr)
     arr[i+1] = key
     print(arr) 

print(arr)"""


"""arr = [5,2,1,6,8]

n = len(arr)

for j in range(1,n):  
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > key:   
        arr[i +1] = arr[i]  
        i = i- 1
    arr[i + 1] = key  


print(arr)
"""

#exercise 2.1  : Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the array A [31;41;59;26;41;58]

arr = [31,41,59,26,41,58]

n = len(arr)

for j in range(1,n):  

     key = arr[j]
     i = j - 1
 
     while i >= 0 and arr[i] > key:  
          
        arr[i+1] = arr[i]
        i = i - 1

     arr[i+1] = key  

"""print(arr)"""

#Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of non decreasing order.

     
arr = [31,41,59,26,41,58]

n = len(arr)

for j in range(1,n):  

     key = arr[j]
     i = j - 1
 
     while i >= 0 and arr[i] < key:  
          
        arr[i+1] = arr[i]
        i = i - 1

     arr[i+1] = key  

"""print(arr)"""


"""2.1-3:  
Consider the searching problem:
Input: A sequence of n numbers A D ha1;a2;:::;ani and a value .
Output: An index i such that D AŒi or the special value NIL if does not
appear in A.
Write pseudocode for linear search, which scans through the sequence, looking
for . Using a loop invariant, prove that your algorithm is correct. Make sure that
your loop invariant fulfills the three necessary properties."""


A = [4,1,6,7,2] 

n = len(A)

for j in range(1,n):  
    
    key = A[j]
    i = j - 1  
     
    while i>=0 and A[i] >= j:   
        A[i+1] = A[i]
        i = i -1  
    A[i+1] = key  
print(A)
value = 2  
for i in range(n):  

     if A[i] == value:  
         print(i)
         
   
         