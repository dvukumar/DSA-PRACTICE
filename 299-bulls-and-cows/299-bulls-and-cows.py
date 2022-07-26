class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b,c = 0,0
        dict = {}
        for i in range(len(secret)):
            s = secret[i]
            if s in dict:
                dict[s]+=1
            else:
                dict[s] = 1
                
        for i in range(len(secret)):
            s = secret[i]
            g = guess[i]
            if s==g:
                b+=1
                dict[s]-=1
        
        for i in range(len(secret)):
            s = secret[i]
            g = guess[i]
            if s!=g:
                if g in dict:
                    if dict[g]>0:
                        c+=1
                        dict[g]-=1
        
        return str(b)+"A"+str(c)+"B"