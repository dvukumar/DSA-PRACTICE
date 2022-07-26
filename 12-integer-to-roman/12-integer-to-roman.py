class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        if num>=1000:
            count = num//1000
            result+=count*'M'
            num-=count*1000
        if num>=900:
            count = num//900
            result+=count*'CM'
            num-=count*900
        if num>=500:
            count = num//500
            result+=count*'D'
            num-=count*500
        if num>=400:
            count = num//400
            result+=count*'CD'
            num-=count*400
        if num>=100:
            count = num//100
            result+=count*'C'
            num-=count*100
        if num>=90:
            count = num//90
            result+=count*'XC'
            num-=count*90
        if num>=50:
            count = num//50
            result+=count*'L'
            num-=count*50
        if num>=40:
            count = num//40
            result+=count*'XL'
            num-=count*40
        if num>=10:
            count = num//10
            result+=count*'X'
            num-=count*10
        if num>=9:
            count = num//9
            result+=count*'IX'
            num-=count*9
        if num>=5:
            count = num//5
            result+=count*'V'
            num-=count*5
        if num>=4:
            count = num//4
            result+=count*'IV'
            num-=count*4
        if num>=1:
            count = num//1
            result+=count*'I'
            num-=count*1
        
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        