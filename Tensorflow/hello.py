import tensorflow as tf

# Simple TensorFlow computation
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])
c = tf.matmul(a, b)  # Matrix multiplication
print("Result of a @ b:\n", c)
