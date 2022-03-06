from matplotlib.pyplot import axis
import numpy as np

softmax_outputs = np.array([[0.7, 0.2, 0.1],
                            [0.5, 0.1, 0.4],
                            [0.02, 0.9, 0.08]])

class_targets = np.array([0, 1, 1])

# get the highest value of each row (i.e. the class which the network has most confidence in)
predictions = np.argmax(softmax_outputs, axis=1)

# if targets are one-hot encoded, convert them to sparse
if len(class_targets.shape) == 2:
    class_targets = np.argmax(class_targets, axis=1)

# find whether the prediction (for each row) matches the target
# if it does, return 1; if it doesn't return 0
# find the mean of this list of 1s and 0s; this is the accuracy
accuracy = np.mean(predictions == class_targets)

print("acc:", accuracy)