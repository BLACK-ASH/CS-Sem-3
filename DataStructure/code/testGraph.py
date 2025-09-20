class Graph:
    def __init__(self,size):
        self.data = [[0]*size for _ in range(size)]
        
    def print(self):
        for row in self.data:
            for col in row:
                print(col,end=" ")
            print()
            
            
    def add(self,x,y,data=1):
        self.data[x-1][y-1] = data 
        self.data[y-1][x-1] = data 
        
        
g = Graph(5)
g.add(1,4,"a")
g.add(4,2,"b")7
g.add(2,2,"c")
g.print()