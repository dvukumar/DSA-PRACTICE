class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        def Count(word):
            dict = {}
            for w in word:
                if w in dict:
                    dict[w]+=1
                else:
                    dict[w] = 1
            return dict
        
        def isSubset(word):
            freq = Count(word)
            for item in comparator:
                if item not in freq:
                    return False
                elif freq[item]<comparator[item]:
                    return False
            return True
                 
        
        comparator = {}
        for w in words2:
            count = Count(w)
            for item in count:
                if item in comparator:
                    comparator[item] = max(comparator[item],count[item])
                else:
                    comparator[item] = count[item]
        arr = []
        for w in words1:
            if isSubset(w):
                arr.append(w)
        
        return arr
                    
        
            