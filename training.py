import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random

class Training:

    def __init__(self, CATEGORIES, DATADIR, TRAINING):

        self.CATEGORIES = CATEGORIES
        self.DATADIR = DATADIR
        self.TRAINING = TRAINING
        self.IMG_SIZE = 100 # Constant to render the images

    def create_training_data(self):

        # Reading the categorý we specify
        for category in self.CATEGORIES:
            # Reading the paths of the dataset
            path = os.path.join(self.DATADIR,category)
            #The clasification of each one is depending the categories we add 0=woman 1=man
            class_num = self.CATEGORIES.index(category)

            # Iterating each image, read and resize with Opencv.
            for img in tqdm(os.listdir(path)):
                try:
                    img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # Reading
                    new_array = cv2.resize(img_array, (self.IMG_SIZE, self.IMG_SIZE))  # Resize
                    # Adding data to the TRAINING variable
                    self.TRAINING.append([new_array, class_num])
                # Exeptions
                except Exception as e:
                    pass
                except OSError as e:
                   print("OSErrroBad img: ", e, os.path.join(path,img))
                except Exception as e:
                   print("general exception: ", e, os.path.join(path,img))
        return self.TRAINING
