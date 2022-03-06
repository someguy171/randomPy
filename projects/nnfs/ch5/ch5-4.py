# classes for loss

import numpy as np

class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_CatergoricalCrossEntropy(Loss):
    # where y_pred is the softmax ouput (prediction of what is right), and y_true is the targets (actual, correct class)
    # other than these two variable renames, this is the same as ch5-3.py
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
        
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[
                range(samples),
                y_true
            ]
            
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(
                y_pred_clipped*y_true,
                axis=1
            )
            
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods