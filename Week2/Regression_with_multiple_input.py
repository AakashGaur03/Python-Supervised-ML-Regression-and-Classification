# Multiple linear regression

# fw,b(X) = W1X1 + W2X2 + .... +WnXn + b
# b is like base price 


# Vectorization

# without it
# f= w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + b

# or with for loop
# f = 0
# for j in range(0,n):
#     f = f + w[j] * x[j]
# f = f + b

# Using Vectorization
# numpy dot function
# much faster than both approach above because nunpy uses parallel hardware in your computer
# f = np.dot(w,x) + b