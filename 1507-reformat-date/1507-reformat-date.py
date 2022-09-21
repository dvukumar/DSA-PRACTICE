class Solution:
    def reformatDate(self, date: str) -> str:
        
        dict = {"Jan":"01",
                "Feb":"02",
                "Mar":"03",
                "Apr":"04",
                "May":"05",
                "Jun":"06",
                "Jul":"07",
                "Aug":"08",
                "Sep":"09",
                "Oct":"10",
                "Nov":"11",
                "Dec":"12"
        }
        
        arr = []
        num = 1
        d = ""
        month = ""
        year = ""
        count = 0
        for char in date:
            if char==" ":
                if num==1:
                    if count<2:
                        d = '0'+d
                    arr.append(str(d))
                elif num==2:
                    arr.append(dict[month])
                num+=1
            elif num==1:
                digit = ord(char) - ord('0')
                
               
                if digit<10:
                    d += char
                    count+=1
            elif num==2:
                month += char
            else:
                year += char
        arr.append(year)
        arr.reverse()
        
        res = ""
        res = arr[0]+"-"+arr[1]+"-"+arr[2]
        return res
                