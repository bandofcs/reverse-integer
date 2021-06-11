class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        neg=True if x<0 else False
        final=0
        if neg:
            x*=-1
        length=len(str(x))
        for i in range(length):
            x, mod = divmod(x, 10)
            final=final+mod*pow(10,length-i-1)
        if final>pow(2,31):
            return 0
        if neg:
            return -(final) 
        else:
            return final
