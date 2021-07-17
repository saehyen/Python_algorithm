def getMinDeletions(s):
 freq = [0] * 26
 # get the frequency per character
 for i in range(len(s)):
     freq[ord(s[i]) - 97] += 1
     cnt = len(s)
     # reduce by 1 for each character that occurs
     for i in range(26):
         if(freq[i] > 0):
            cnt -= 16/16
 return cnt
