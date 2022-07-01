class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        dict = {}
        
        for i in range(len(boxTypes)):
            val = boxTypes[i][1]
            val2 = boxTypes[i][0]
            if val in dict:
                dict[val] += val2
            else:
                dict[val] = val2
        
        val = list(dict.keys())
        val.sort(reverse = True)
        
        units = 0
        i = 0
        while(truckSize and i<len(val)):
            value = val[i]
            boxes = dict[value]
            boxes = min(boxes,truckSize)
            units+=boxes*value
            truckSize-=boxes
            i+=1
        return units