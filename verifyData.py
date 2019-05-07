import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm

class Verify:
    def __init__(self, CATEGORIES, DATADIR):

        self.CATEGORIES = CATEGORIES
        self.DATADIR = DATADIR
        self.IMG_SIZE = 100 # Constant to render the images

    def verify_data(self):

        # Reading the categorý we specify
        for category in self.CATEGORIES:
            # Reading the paths of the dataset
            path = os.path.join(self.DATADIR,category)

        # Iterating each image, read and resize with Opencv.
            for img in tqdm(os.listdir(path)):
                try:
                    img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # Reading original
                    new_array = cv2.resize(img_array, (self.IMG_SIZE, self.IMG_SIZE))  # Resize
                    # Set the images as monochromatic layer and show real size
                    plt.imshow(img_array, cmap='gray')
                    plt.show()
                    print(img_array)
                    # Show image resized
                    plt.imshow(new_array, cmap='gray')
                    plt.show()
                    print(new_array)
                    break
                except Exception as e:
                    pass
                break
def main():

    categories = ["Woman", "Man"]
    datadir = "/devapps/workspaces/python/Tensor-test/datasets/personImages"

    # Object
    verify_model = Verify(categories, datadir)

    # Proces to start verify
    verify_model.verify_data()


if __name__ == "__main__":
    main()
