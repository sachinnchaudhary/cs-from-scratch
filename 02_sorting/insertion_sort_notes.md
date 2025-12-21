# Algorithm: Insertion Sorting

## 1. Problem Statement 
: in Array A where [a^1,a^2..a^n] we are sorting in a way where [a^1<=a^2<=..a^n]
- Input:Array = [a^1,a^2..a^n]
- Output: Array = [a^1<=a^2<=..a^n]
- Constraints / assumptions: there is local search here. the key j only looks for its left side rather and searching in entire array.



---

## 2. Core Idea (one paragraph)
Idea is simple you basically take one element lets say its J from array and look in its left side if that left element is greater then J then we move it right, and then we move left subsequentl with repeating this process. and then put J in the zeroth position. The reason this algorithm works because putting J in most left element, thats where we basically repair the invariant which we broke.  



---

## 3. Representation
How is the problem represented *computationally*?
there are two variables one is key which is J element of array which move from 1 to length n. second one is the I which is j-1 for looking most left element and third one is i = i - 1 and array[i+1] = key where array is in form of data structure.  


---

## 4. Invariant / Structural Property
in Array A where there is elements A= [a^1,a^2..a^n] the A[1...j-1] is always sorted and A[j] is key we are sorting with A[j+1...n] will be unsorted. This invariant remain true in intialization, maintainance, and even in termination. where in initialization the A[1] will always be assumed to sort. and in maintainance where before the loop A[1...j-1] is sorted but after the one iteration A[1...j] is going to be sorted and in termination where A[1...n] will be sorted.



