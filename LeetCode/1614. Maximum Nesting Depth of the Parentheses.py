

#code:


class Solution:
    def maxDepth(self, s: str) -> int:
        
        
        open=0 
        depth=0
        for i in s:
            if i== "(":
                open+=1
                if depth < open:
                    depth= open
                
            if i==")":
                open-=1
          
            
            
        
        return depth
