class powernum(object):
    def __init__(self,n,m):
        self.n=n
        self.m=m
    
    def __iter__(self):
        self.c=0
        return self
    def __next__(self):
        r=n**c
        if self.c<=self.m:
            self.c=c+1
            return r
        else:
            raise StopIteration("you have used all power")
        
    
def main():
    p=power(int(input("name:")),int(input("max:")))
    p=iter(p)
    while input("do want poer press someting"):
        try:
            n=next(p)
            print(n)
        except StopIteration as e:
            prit("error",e)
            print("do you eant another number's power2",end='\t')
            
            
