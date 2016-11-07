
import tensorflow as tf

x = tf.Variable(0.)
y = (x - 1000) ** 2 + 4

train_step = tf.train.GradientDescentOptimizer(0.3).minimize(y)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(20):
  sess.run(train_step)
  print('x:',sess.run(x))
  print('y:',sess.run(y))
