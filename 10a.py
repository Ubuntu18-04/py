class Matrix:
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.matrix=[[0 for j in range(col)]for i in range(row)]
    def populate(self,name):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j]=int(input("enter element:"))
                print()
                
        
    def read(self,name):
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j],"\t")
            
    def add(self,name,MatrixB):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j]+=MatrixB.matrix[i][j]
        self.read(name)
MatrixA=Matrix(2,2)
MatrixA.populate('matA')
MatrixB=Matrix(2,2)
MatrixB.populate('matB')
MatrixA.add('matA',MatrixB)
