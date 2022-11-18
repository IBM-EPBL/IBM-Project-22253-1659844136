from tensorflow.keras.models import load_model
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2

def getModel():
    model =load_model('/home/digital/Desktop/IBM/models/mnist/mnistCNN.h5')
    return model

