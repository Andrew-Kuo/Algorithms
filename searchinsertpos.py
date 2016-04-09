class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A == []:
            return 0
        
        start = 0
        end  = len(A) - 1
        mid = 0
        
        while (start + 1 < end):
            mid = start + (end-start)/2
            
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else: 
                end = mid
                
        if A[start] >= target:
            return start
        elif A[end] >= target:
            return end
        else: 
            return end + 1