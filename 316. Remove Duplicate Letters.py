class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]] = 1
        stack = []
        stack.append(s[0])
        visited = set()
        visited.add(s[0])
        for i in range(1,len(s)):
            
            if s[i] in visited:
                dic[s[i]] -= 1
                continue
            if not stack:
                stack.append(i)
                checked.add(i)
                continue
            if stack and s[i] > stack[-1]:
                if s[i] not in visited:
                    stack.append(s[i])
                    visited.add(s[i])
                    continue
            else:
                while stack and s[i] < stack[-1] and dic[stack[-1]] > 1:
                    dic[stack[-1]] -= 1
                    visited.discard(stack[-1])
                    stack.pop()
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)
