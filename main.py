import random
from training import Training

if __name__ == "__main__":

    # Variables to pass in the class
    categories = ["Woman", "Man"]
    datadir = "/devapps/workspaces/python/Tensor-test/datasets/personImages"
    training = []

    # Object
    training_model = Training(categories, datadir, training)

    # Proces to start the training
    training_model.create_training_data()
    # Verify Dataset Len
    print('Number of Dataset trained: ', len(training))
    # Use shuffle from dataset
    random.shuffle(training)
    # Iterate shuffle to verify the data learned
    for sample in training[:10]:
        if (sample[1] == 0):
            print ('Woman')
        else:
            print ('Man')
