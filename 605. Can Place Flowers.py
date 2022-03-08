class Solution(object):
    def canPlaceFlowers(self, li, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        
        if len(li) == 1 and li[0] == 0:
            if n == 1:
                return True
            
            else:
                return False
        if len(li) == 2:
            if li[0] == 0 and li[1] == 0:
                if n == 1:
                    return True
                return False
            
            else:
                return False        
            
        i = 0
        j = 1
        k = 2
        counta = 0
        while k < len(li):
            if li[i] == 0 and li[j] == 0 and li[k] == 0:
                if i == 0 and k == len(li) - 1:
                    counta+=1
                    counta+=1
                    li[i] = 1
                    li[k] = 1
                    i+=1
                    j+=1
                    k+=1
                    continue
                elif i == 0:
                    counta+=1
                    li[i] = 1
                    i+=1
                    j+=1
                    k+=1
                    continue
                    
                    
                else:
                    counta+=1
                    li[j] = 1
                    i+=1
                    j+=1
                    k+=1
                    
            elif li[i] == 0 and li[j] == 0 and li[k] == 1:
                if i == 0:
                    li[i] = 1
                    counta+=1
                    i+=1
                    j+=1
                    k+=1
                    continue
                else:
                    i+=1
                    j+=1
                    k+=1
                    continue
                    
            elif li[i] == 1 and li[j] == 0 and li[k] == 0:
                if k == len(li) - 1 :
                    li[k] = 1
                    counta+=1
                    i+=1
                    j+=1
                    k+=1
                    continue
                   
                else:
                    i+=1
                    j+=1
                    k+=1
                    continue
                
                
            else:
                i+=1
                j+=1
                k+=1
                
                
        # print(counta)
        if counta >= n:
            return True
        else:
            return False
                
  
        
            
