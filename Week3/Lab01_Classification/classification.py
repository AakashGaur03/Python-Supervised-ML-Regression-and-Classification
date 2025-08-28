# Classification have small amount of values that can be an answer unlike regression that can have any vast amount of number
# Linear Regression is not a good algo for classification problems

# We will study logistic regrerssion for it

# Ex of classification
# Email is spam or not    Yes or No
# Transaction fraud or not  Yes or No
# Tumor is serious or not   Yes or No

# When only two options then know as Bunary classification



# explaination of Linear Regression failing in Classification

# What the image shows:

# X-axis: Tumor size (in cm).

# Y-axis: Whether the tumor is malignant (1 = Yes, malignant; 0 = No, benign).

# Blue circles: Benign tumors (label = 0).

# Red crosses: Malignant tumors (label = 1).

# We want to predict whether a tumor is malignant or not.

# What linear regression does here:

# Linear regression tries to fit a straight line (f(x) = wx + b) through the data.

# But classification is not about predicting a continuous number — it’s about predicting discrete labels (0 or 1).

# So people try to “force” linear regression into classification by saying:

# If the output f(x) is ≥ 0.5, predict malignant (ŷ=1).

# If the output f(x) is < 0.5, predict benign (ŷ=0).

# This is what the purple threshold line at 0.5 represents.

# The problems shown in the image:

# Predictions go outside 0 and 1:
# Linear regression can predict values like -0.2 or 1.4, which don’t make sense as probabilities.

# Bad separation of classes:
# Notice how some red crosses (malignant) are below the 0.5 threshold line — they get wrongly classified as benign.

# Sensitive to slope of the line:
# Depending on how the line is fit (blue line vs green line), the predictions change a lot. There is no guarantee it will properly separate 0’s and 1’s.