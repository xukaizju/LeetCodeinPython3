class Solution(object):
    def reverse(self, x):
        if x>0:
            s=0
            n=len(str(x))
            a=0
            while a<n:
                s+=(x%10)*(10**(n-a-1))
                a+=1
                x//=10
            if int(s)>2147483648:
                return 0
            else:
                return int(s)
        elif x<0:
            s=0
            y=0-x
            n=len(str(y))
            a=0
            while a<n:
                s+=(y%10)*(10**(n-a-1))
                a+=1
                y//=10
            if int(0-s)<-2147483648:
                return 0
            else:
                return int(0-s)
        elif x==0:
            return 0
