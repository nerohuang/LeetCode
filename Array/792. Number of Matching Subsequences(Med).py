class Solution:
   def numMatchingSubseq(self, S: str, words: List[str]) -> int:
       ans = 0;
       charIdx = {};
       for i in range(len(S)):
           if S[i] not in charIdx:
               charIdx[S[i]] = [i];
           else:
               charIdx[S[i]].append(i);
       
       for word in words:
           lastCharPos = -1;
           wordCount = 0;
           for i in range(len(word)):
               if word[i] not in charIdx:
                   continue;
               else:
                   count = 0;
                   for idx in charIdx[word[i]]:
                       if idx > lastCharPos:
                           lastCharPos = idx;
                           break;
                       count += 1;
                   if count == len(charIdx[word[i]]):
                       break;
               wordCount += 1;
           if wordCount == len(word):
               ans += 1;
       return ans;


#S = "abcde"
#words = ["a", "bb", "acd", "ace"]
#
#import collections
##class Solution:
##    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
#words_unique=collections.Counter(words)
#res=0
#for i in words_unique:
#    start=0
#    flag=1
#    for j in i:
#        start=S.find(j,start)+1
#        if not start:
#            flag=0
#            break
#    if flag==1:
#        res+=words_unique[i]
#    
#print(res)