import tensorflow as tf
import numpy as np

x = tf.constant([[[ 1,  2,  3],
                  [ 4,  5,  6]],
                 [[ 7,  8,  9],
                  [10, 11, 12]]])

# print(x)
# print(tf.transpose(x, perm=[0, 2, 1]))
labels = [1,2,3]
perm = np.random.permutation(len(labels))
print(perm)
perm = [[ind] for ind in perm]
print(perm)

xyz = tf.gather_nd(
    params = [['a', 'b'],
              ['c', 'd']])
print(xyz)