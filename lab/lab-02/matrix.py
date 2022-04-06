
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

print ("Addition of two matrices: ")
print (numpy.add(x,y))

print ("Subtraction of two matrices : ")
print (numpy.subtract(x,y))

print ("Matrix Division : ")
print (numpy.divide(x,y))
print ("Multiplication of two matrices: ")
print (numpy.multiply(x,y))
print ("The product of two matrices : ")
print (numpy.dot(x,y))
print ("square root is : ")
print (numpy.sqrt(x))
print ("The summation of elements : ")
print (numpy.sum(y))
print ("The column wise summation  : ")
print (numpy.sum(y,axis=0))
print ("The row wise summation: ")
print (numpy.sum(y,axis=1))

print ("Matrix transposition : ")
print (x.T)
#  