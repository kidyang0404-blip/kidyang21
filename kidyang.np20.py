import numpy as np 
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x): 
    return x * (1 - x)

X = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], 
              [0.8], [0.9], [1.0]]) 
y = np.array([[0.00], [0.36], [0.64], [0.84], 
              [0.96], [1.00], [0.96], [0.84], 
              [0.64], [0.36], [0.00]]) 
input_size = 1
hidden_size = 4 
output_size = 1

np.random.seed(42)
weights_input_hidden = np.random.uniform(-1, 1, (input_size, output_size)) 
weights_hidden_output =np.random.uniform(-1, 1 (hidden_size, output_size)) 
learning_rate = 0.7
iterations = 500000

hidden_input = np.dot(X, weights_input_hidden)
hidden_output = sigmoid(final_input) 

error = y -find_output

d_output = error * sigmoid_derivative(final_output)
error_hidden = d_output.dot(weights_hidden_output.T) 
d_hidden = error_hidden*sigmoid_derivative(hidden_output)
weights_hidden_output += hidden_output.T.dot(d_hidden) * learning_rate

if i % 100000 == 0:
    loss = np.mean(np.square(error))
    print(f"Iteration {i},Loss: {loss}")

plt.piot(X, y, 'ro', label='Actual Data')
plt.plot(X, fianl_output, 'b-', label='Predicted')
plt.xlabel('Input (x)')
plt.ylabel('Output (f(x))')
plt.legend()
plt.title('Neural Network Approximation of' 'f(x) = 4x(1 - x)')
plt.show()