# sparse and one-hot labels
import numpy as np

softmax_outputs = np.array([[0.7, 0.1, 0.2],
                            [0.1, 0.5, 0.4],
                            [0.02, 0.9, 0.08]])

# here, we have one-hot encoded labels; each row corresponds to a row of the outputs
# one means that index is the target, 0 means that index isn't
class_targets = np.array([[1, 0, 0],
                          [0, 1, 0],
                          [0, 1, 0]])

# we can also have sparse labels; each index corresponds to the correct class for that row
# class_targets[0] = 0; this means the 0th index of the first row of outputs is the target
# class_targets[1] = 1; this means the 1st index of the second row of outputs is the target, and so on...
class_targets = [0, 1, 1]

# see ch5-2.py for sparse labels; this example will use one-hot encoded
class_targets = np.array([[1, 0, 0],
                          [0, 1, 0],
                          [0, 1, 0]])

# if class_targets' shape is 1 (1D, list; sparse)...
if len(class_targets.shape) == 1:
    # the confidences are ones at the specified indexes for each row
    correct_confidences = softmax_outputs[range(len(softmax_outputs)), class_targets]
# if class_targets' shape is 2 (2D, array; one-hot encoded)
elif len(class_targets.shape) == 2:
    # the confidences are the sum of each row, where each item is multiplied by the corresponding value in class_targets (most will be *0)
    correct_confidences = np.sum(softmax_outputs*class_targets, axis=1)
    
neg_log = -np.log(correct_confidences)
average_loss = np.mean(neg_log)

print(average_loss)
