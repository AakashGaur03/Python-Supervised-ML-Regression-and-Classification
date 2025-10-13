# We rescale the data, because in larger data values it is slow to calculate gradient descent

# so For Example


# -1     <= x1 <=   1         // No need to Scale
# -3     <= x2 <=   3         // No need to Scale
# -0.3   <= x3 <=   0.3       // No need to Scale
# 0      <= x4 <=   3         // No need to Scale
# -2     <= x5 <=   0.5       // No need to Scale
# -100   <= x6 <=   100       // Too large rescale
# -0.001 <= x7 <=   0.001     // Too Small rescale
# 98     <= x8 <=   105       // Too large rescale

# when in doubt that to do feature scaling or not just do it
# As there is not any such harm to carry feature re-scaling


# There are different Techniques to do so 
# For example Divide each value by the maximim value for the feature 
# we will see in depth in Future Lab

## REVISITED