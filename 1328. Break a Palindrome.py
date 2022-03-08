class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        length = len(palindrome)
        li = []
        for i in range(length):
            li.append(palindrome[i])
        i = 0
        limit = length//2
        if len(li) == 1:
            return ""
        while i < limit:
            if li[i] > "a":
                li[i] = "a"
                return "".join(li)
            if i + 1 == limit:
                li[-1] = "b"
            i+=1
        return "".join(li)
            
