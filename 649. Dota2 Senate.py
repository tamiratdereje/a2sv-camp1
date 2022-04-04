class Solution:
    def predictPartyVictory(self, li: str) -> str:
        countD = 0
        countR = 0        
        banR = 0
        banD = 0
        arr = []
        for i in range(len(li)):
            arr.append(li[i])
            if li[i] == "R":
                countR+=1
            else:
                countD+=1   
        i = 0
        while i < len(arr):
            if arr[i] == "R":
                if banR == 0:
                    banD +=1
                    i+=1
                else:
                    banR -= 1
                    arr[i] = "B"
                    countR-=1
                    i+=1
            elif arr[i] == "B":
                i+=1

            elif arr[i] =="D":
                if banD == 0:
                    banR +=1
                    i+=1
                else:
                    banD -= 1
                    arr[i] = "B"
                    countD-=1
                    i+=1
            if i == len(arr):
                i = 0
            if countD == 0:
                return "Radiant"
            if countR == 0:
                return "Dire"
