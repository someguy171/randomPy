# implementing cross-entropy loss with batches of outputs
import numpy as np

softmax_outputs = [[0.7, 0.1, 0.2],
                   [0.1, 0.5, 0.4],
                   [0.02, 0.9, 0.08]]

class_targets = [0, 1, 1]

# pair each row of the outputs to the respective target class
# e.g. [0.7, 0.1, 0.2] pairs with 0
# e.g. [0.1, 0.5, 0.4] pairs with 1
# print the probability at the class index
for target_idx, distribution in zip(class_targets, softmax_outputs):
    print(distribution[target_idx])

# the same thing can be done using numpy
softmax_outputs = np.array([[0.7, 0.1, 0.2],
                            [0.1, 0.5, 0.4],
                            [0.02, 0.9, 0.08]])

# [0, 1, 2] refers to the rows
# class_targets gets the value at the indexes specified in that list
# you can see this as [y (rows), x (columns)]
print(softmax_outputs[[0, 1, 2], class_targets])

# equally, [0, 1, 2] can be replaced with a range()
print(softmax_outputs[range(len(softmax_outputs)), class_targets])

# then, apply the negative log to these values to find the loss...
loss_array = -np.log(softmax_outputs[range(len(softmax_outputs)), class_targets])

# ... and calculate a mean of those losses; now we have one value to quantify the loss for the whole batch!
average_loss = np.mean(loss_array)
print(average_loss)