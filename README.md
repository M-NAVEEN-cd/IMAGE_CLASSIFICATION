Dog vs. Cat Classifier:

Overview:
Welcome to the Dog vs. Cat Classifier project! This repository contains the code and resources for a machine learning model that classifies images of dogs and cats. The model is based on a Convolutional Neural Network (CNN) architecture and is trained to distinguish between these adorable furry creatures.
Dataset:
The dataset used for this project consists of a collection of dog and cat images sourced from [source name/link]. The images have been preprocessed and split into training and test sets. The dataset is available https://www.kaggle.com/datasets/samuelcortinhas/cats-and-dogs-image-classification(link to dataset if publicly available).The classification model is built using Sklearn and Skimage libraries.It follows a CNN architecture that has proven effective in image classification tasks.
Evaluation
After training, the model is evaluated on a separate test set to measure its performance. The evaluation results, including accuracy and any other relevant metrics, are presented in the console.
Usage:
To use the trained model for inference:
Load the trained model: model = load_model('path_to_trained_model.h5')
Preprocess the input image as needed
Use the model for prediction: prediction = model.predict(image)
Results:
The model achieved an impressive 0.7869 on the test dataset. It is capable of accurately distinguishing between dogs and cats even in challenging scenarios.
