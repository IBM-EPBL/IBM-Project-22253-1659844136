

# Importing Necessary 
#------------------------------------------------Sprint 1

import numpy #used for numerical analysis
import tensorflow as tf#open source used for both ML and DL for computation
from tensorflow.keras.datasets import mnist #mnist dataser
from tensorflow.keras.models import Sequential #it is a plain stack of Layers
from tensorflow.keras import layers #A Layer consists of a tensor-in tensor-out computation function
from tensorflow.keras.layers import Dense, Flatten #Dense-Dense Layer is the regular deeply connected n
#Faltten-used fot flattening the input or change the dimension
from tensorflow.keras.layers import Conv2D #Convolutional Layer
from keras.optimizers import Adam #optimizer
from keras.utils import np_utils #used for one-hot encoding
import matplotlib.pyplot as plt
import numpy as np

mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()

#gettting shape of data
print("Shape of training and testing dataset ")
print(x_train.shape)
print(x_test.shape)
#------------------------------------------------------Sprint 2
print("Analyzing the data")
print("Printing the first data and its label")
print(x_train[0])
print(y_train[0])
print("Visualising the data ")
plt.imshow(x_train[0])
plt.show()

x_train=x_train.reshape(60000,28,28,1).astype('float32')
x_test=x_test.reshape(10000,28,28,1).astype('float32')
print(x_train.shape)
print(x_test.shape)

print("Applying One Hot Encoding && Normalization")
no_of_classes=10
y_train=np_utils.to_categorical(y_train,no_of_classes)
y_test=np_utils.to_categorical(y_test,no_of_classes)
x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)
print(y_train[0])
print("A")

#creating the model cnnlayers
model =Sequential()
model.add(Conv2D(64,(3*3),input_shape =(28,28,1),activation='relu' ))
model.add(Conv2D(32,(3*3),activation='relu' ))
model.add(Flatten())
model.add(Dense(no_of_classes,activation='softmax'))

#compiling the model
model.compile(loss="categorical_crossentropy",optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=5,validation_split=0.3,batch_size=5)

#--------------------------------------------------Sprint 3
#Evaluation
test_loss,test_acc=model.evaluate(x_test,y_test)
print("Test accuracy: ",test_acc)
print("Test validation  loss: ",test_loss)

#Testing 
predictions=model.predict([x_test])
print(predictions[6])
print(np.argmax(predictions[8]))
plt.show()

print("Saving the model")
model.save('models/mnistCNN.h5')
