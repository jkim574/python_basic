import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import activations


def get_dataset(training = True):
    mnist = keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    if training:
#        print('train_images: ' + str(train_images.shape))
#        print('train_labels: ' + str(train_labels.shape))
#        print(type(train_images))
#        print(type(train_labels))
#        print(type(train_labels[0]))
        return (train_images, train_labels)
    if not training:
#        print('test_images:  '  + str(test_images.shape))
#        print('test_labels:  '  + str(test_labels.shape))
        return (test_images, test_labels)


def print_stats(train_images, train_labels):
    (train_images, train_labels) = get_dataset()
    (test_images, test_labels) = get_dataset(False)
    print(train_images.shape[0])
    print(str(train_images.shape[1]) + "x" + str(train_images.shape[2]))    
    class_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

    unique, counts = np.unique(train_labels, return_counts=True)
#     print("Train labels: ", counts)

    for label in range(10):
        print(str(label) + ". " + str(class_names[label]) + " - " + str(counts[label]))

   
#    print(test_images.shape[0])
#    print(str(test_images.shape[1]) + "x" + str(test_images.shape[2]))
#    class_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    
#    counts = np.unique(test_labels, return_counts = True)
#    for label in range(10):
#        print(str(label) + ". " + str(class_names[label]) + " - " + str(counts[label]))    



def build_model():
    model = keras.Sequential()
    model.add(layers.Flatten(input_shape = (28, 28)))
    model.add(layers.Dense(128, activation=activations.relu))
    model.add(layers.Dense(64, activation=activations.relu))
    model.add(layers.Dense(10))
    opt = keras.optimizers.SGD(learning_rate = 0.001)
    loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits = True)
    accuracy = keras.metrics.CategoricalAccuracy()

    model.compile(loss = loss_fn, optimizer = opt, metrics = ['accuracy']) 

    return model

def train_model(model, train_images, train_labels, T):
    model.fit(train_images, train_labels, epochs = T)

def evaluate_model(model, test_images, test_labels, show_loss = True):
    test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose = 0)
    if show_loss:
      #  print("Loss:", test_loss)
        print("Accuracy: %.2f%%" % (100.0 * test_accuracy))

    if not show_loss:
        print("Loss: {:.4f}".format(test_loss))
        print("Accuracy: %.2f%%" % (100.0 * test_accuracy))


def predict_label(model, test_images, index):
    predictions = model.predict(test_images)
    print(predictions[index])

def main():
    (train_images, train_labels) = get_dataset()
    (test_images, test_labels) = get_dataset(False)
    print_stats(train_images, train_labels)    
    model = build_model()
    train_model(model, train_images, train_labels, 5)
    evaluate_model(model, test_images, test_labels, show_loss=False)
    predict_label(model, test_images, 1)

if __name__ == "__main__":
    main()
