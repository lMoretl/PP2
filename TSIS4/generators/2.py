class Evens:
    def __init__(self,n):
        self.n=n
        self.x=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<self.x:
            raise StopIteration
        if self.x%2==0:
            answer=self.x
            self.x+=1
            return answer
        elif self.x%2==1:
            self.x+=1
            return ','
for  i in Evens(6):
    print(i,end='')