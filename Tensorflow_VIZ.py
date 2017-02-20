#------------------------------------------------------------------------------
# Name:        Visualizing a Neural Network Learn
# Description: 
#
# Author:      Robert S. Spencer
#
# Created:     2/20/2017
# Python:      2.7
#------------------------------------------------------------------------------

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def layout_ANN():

	global node1_locs, node2_locs

	layer1_nodes = 196
	layer2_nodes = 10

	layer1_x = np.linspace(0.05,0.95,layer1_nodes/2)
	layer1_x = np.append(layer1_x,layer1_x)
	layer1_y_upper = np.linspace(0.05,0.05,layer1_nodes/2)
	layer1_y_lower = np.linspace(0.95,0.95,layer1_nodes/2)
	layer1_y = np.append(layer1_y_upper,layer1_y_lower)
	layer1 = np.linspace(1,1,layer1_nodes)
	node1 = np.linspace(0,layer1_nodes-1,layer1_nodes)
	node1_locs = pd.DataFrame(columns=['layer','node','x','y'], data = np.array([layer1,node1,layer1_x,layer1_y]).T)

	layer2_x = np.linspace(0.05,0.95,layer2_nodes)
	layer2_y = np.linspace(0.5,0.5,layer2_nodes)
	layer2 = np.linspace(2,2,layer2_nodes)
	node2 = np.linspace(0,layer2_nodes-1,layer2_nodes)
	node2_locs = pd.DataFrame(columns=['layer','node','x','y'], data = np.array([layer2,node2,layer2_x,layer2_y]).T)


def print_ANN_Train():

	plt.clf()
	plt.axis('off')

	plt.plot(node1_locs['x'], node1_locs['y'], 'ko')
	plt.plot(node2_locs['x'], node2_locs['y'], 'ko', ms=20)

	
	for n in range(10):
		plt.annotate(str(n), xy=(node2_locs.loc[n]['x'], node2_locs.loc[n]['y']), xytext=(node2_locs.loc[n]['x'], node2_locs.loc[n]['y']), color='w', ha='center',va='center')
	
	plt.xlim([0,1])
	plt.ylim([0,1])

	for index_2, row_2 in node2_locs.iterrows():
		for index_1, row_1 in node1_locs.iterrows():
			weight = Weights[index_1,index_2]
			c1 = plt.plot( [row_1['x'], row_2['x']], [row_1['y'], row_2['y']] , 'k-' , lw=0.5, alpha=np.abs(weight)/0.35) #, vmin=-0.4,vmax=0.4)
			#plt.colorbar(c1)
	
	

def print_ANN_Test():

	plt.clf()
	fig = plt.figure(20,30)
	fig.text(0.5,0.9,'Visualizing a Neural Network Learn',size='small',ha='center',va='center')
	fig.text(0.5,0.87,r'$\copyright Robert Sterling Spencer$',size='xx-small',ha='center',va='center')

	pl1 = fig.add_subplot(1,1,1)

	y_sample = sess.run(y, feed_dict={x: mnist.test.images[:,::4], y_: mnist.test.labels})[i]
	x_sample = mnist.test.images[:,:][i]
	accur = sess.run(accuracy, feed_dict={x: mnist.test.images[:,::4], y_: mnist.test.labels})

	fig.text(0.15, 0.2, "Accuracy: %.1f"%(accur*100)+"%", size='x-small')

	for index_2, row_2 in node2_locs.iterrows():
		for index_1, row_1 in node1_locs.iterrows():
			weight = Weights[index_1,index_2]
			if weight > 0:
				color = 'blue'
			else:
				color = 'red'
			plt.plot( [row_1['x'], row_2['x']], [row_1['y'], row_2['y']] , '-', lw=0.5, color = color, alpha=np.abs(weight)/0.35, zorder=1)
	
	plt.plot(node1_locs['x'], node1_locs['y'], 'ko', ms=2)
	plt.scatter(node2_locs['x'], node2_locs['y'], c=y_sample, cmap='Greys',s=200,zorder=2)

	for n in range(10):
		plt.annotate(str(n), xy=(node2_locs.loc[n]['x'], node2_locs.loc[n]['y']), xytext=(node2_locs.loc[n]['x'], node2_locs.loc[n]['y']), color='w', ha='center',va='center', zorder=3)
	
	plt.axis('off')
	plt.xlim([0,1])
	plt.ylim([0,1])
	
	pl2 = fig.add_subplot(5,6,19)
	pl2.imshow(x_sample.reshape([28,28]),cmap='Greys')
	
	plt.axis('off')



mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32, [None,196])

W = tf.Variable(tf.zeros([196,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])


#cross_entropy
cost_function = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))



train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cost_function)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

layout_ANN()

for i in range(300):
	batch_xs_ys = mnist.train.next_batch(100)
	batch_xs = batch_xs_ys[0][:,::4]
	batch_ys = batch_xs_ys[1]
	sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

	if i % 5 == 0:
		print (i)
		correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

		print('Run#: ',i,'   ',sess.run(accuracy, feed_dict={x: mnist.test.images[:,::4], y_: mnist.test.labels}))
		print(sess.run(cost_function, feed_dict={x: mnist.test.images[:,::4], y_: mnist.test.labels}))

		Weights = sess.run(W)
		print_ANN_Test()
		plt.savefig('ANN_VIZ/ANN'+str(i), dpi=200)
		'''
		plt.clf()
		Weights = sess.run(W)
		c = plt.imshow(Weights, aspect = 'auto', vmin=-0.4, vmax=0.4, interpolation='None',cmap='Spectral')
		plt.colorbar(c)
		'''







	


