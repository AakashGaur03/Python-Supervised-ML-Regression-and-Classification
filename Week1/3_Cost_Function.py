# # cost function ; Squared error Cost Function

# Calculated using for each i
# (Y hat (estimated value) - Y (original value))^2
# the result can came out too big so we calculate avg of them 
# ((Y hat (estimated value) - Y (original value))^2)/m
# we also divide it by two that helps us in some future calculation
# ((Y hat (estimated value) - Y (original value))^2)/2*m
# This is used to find out the more accurate value of w and b so we can get minimum cost function

# Gradient Descent Algorithm is used to find out the best w and b to find out minimum cost function as with higher data values it is difficult to find out values of w and b manually