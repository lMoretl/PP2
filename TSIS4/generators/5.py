class Backslay:
    def __init__(self,n):
        self.n=n+1
        self.x=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n==self.x:
            raise StopIteration
        self.n-=1
        return self.n
for i in Backslay(5):
    print(i)