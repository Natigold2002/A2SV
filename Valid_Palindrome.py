class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=re.sub('[^a-z0-9]','',s)
        leng=len(s)
        if leng %2==0:
            if s[0:leng]==s[leng::-1]:
                return True
            else:return False
        else:
            if s[0:leng]==s[leng+1::-1]:
                return True
            else:return False

        
