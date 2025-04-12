class Matrix:
    def __init__(self,a,b,c,d):
        self.matrix = [(a, b), (c, d)]

    def __add__(self, other):
        return Matrix(self.matrix[0][0]+other.matrix[0][0],
                      self.matrix[0][1]+other.matrix[0][1],
                      self.matrix[1][0]+other.matrix[1][0],
                      self.matrix[1][1]+other.matrix[1][1])

    def __mul__(self, other):
        return Matrix(self.matrix[0][0]*other.matrix[0][0] + self.matrix[0][1]*other.matrix[1][0],
                      self.matrix[0][0]*other.matrix[0][1] + self.matrix[0][1]*other.matrix[1][1],
                      self.matrix[1][0]*other.matrix[0][0] + self.matrix[1][1]*other.matrix[1][0],
                      self.matrix[1][0]*other.matrix[0][1] + self.matrix[1][1]*other.matrix[1][1])

    def __str__(self):
        return f"[{self.matrix[0][0]}, {self.matrix[0][1]}; \n;{self.matrix[1][0]}, {self.matrix[1][1]}]"

    def __repr__(self):
        return f"Matrix({self.matrix[0][0]}, {self.matrix[0][1]}, {self.matrix[1][0]}, {self.matrix[1][1]})"

m1 = Matrix(5, 6, 7, 8)
m2 = Matrix(2, 0, 1, 2)
m3 = m1 + m2
print(m3)
m4 = m1 * m2
print(m4)
print(repr(m4))