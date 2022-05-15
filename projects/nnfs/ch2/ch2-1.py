# calculating output from input, weight and bias

inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# create a list for the outputs of each neuron on the layer
layer_outputs = []

# for each neuron's incoming weights and its bias...
for neuron_weights, neuron_bias in zip(weights, biases):
    
    # set the output to a default of 0
    neuron_output = 0
    
    # for each input value and its corresponding weight...
    for n_input, weight in zip(inputs, neuron_weights):
        
        # multiply them together, and add the result to the neuron's output
        neuron_output += n_input*weight
        
    # add the bias to the neuron's output
    neuron_output += neuron_bias
    
    # append the final ouput for the neuron to the list
    layer_outputs.append(neuron_output)

print(layer_outputs)