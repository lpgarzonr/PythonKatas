class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs == None or len(strs) == 0:
            return ""
        shortestStr = self.getShortestStr(strs)
        prefix = self.getLongestPrefix(shortestStr, strs, 0)
        return prefix
            
    def getShortestStr(self, strs):
        minLengt = len(strs[0])
        minStr = strs[0]
        for string in strs[1:]:
            if len(string) < minLengt:
                minLengt = len(string)
                minStr = string
        return minStr
    
    def getLongestPrefix(self, prefix, strs, fromIdx):
        if self.allHavePrefix(prefix, strs, fromIdx):
            return prefix
        
        midIdx = len(prefix)//2
        leftPrefix = self.getLongestPrefix(prefix[:midIdx], strs, fromIdx)
        
        if len(leftPrefix):
            rightPrefix = self.getLongestPrefix(prefix[midIdx:], strs, fromIdx + midIdx)
            return leftPrefix + rightPrefix
        
        return leftPrefix;
            
    def allHavePrefix(self, prefix, strs, fromIdx):
        for string in strs:
            if string.startswith(prefix, fromIdx) == False:
                return False
        return True

lop = Solution()
print(lop.longestCommonPrefix(["flower","florwe","flowflow"]))