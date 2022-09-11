#TC-(N*2^N)
#SC-O(N), where NN is the length of the string ss
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        self.s = s
        self.backtrack(0,[])
        return self.result
    
    def backtrack(self,pivot,path):
        if pivot == len(self.s):
            self.result.append(path[:])
            return
        
        for i in range(pivot,len(self.s)):
            ss = self.s[pivot:i+1]
            if(self.ispalindrome(ss)):
                path.append(ss)
            
                self.backtrack(i+1,path)
                path.pop()
            
    def ispalindrome(self,ss):
        return ss == ss[::-1]