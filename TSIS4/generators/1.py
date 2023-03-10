class squares:
    def __init__(self,x):
        self.x=x
        self.n=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>self.x:
            raise StopIteration
        answer=self.n**2
        self.n+=1
        return answer
for i in squares(5):
    print(i)