import tensorflow as tf
from tensorflow import keras
from keras.models import Model
from keras.callbacks import TensorBoard
from keras.layers import Input, Dense, Conv1D, Flatten
from keras_tuner import RandomSearch, Objective
from keras_tuner.engine.hyperparameters import HyperParameters
from sklearn.utils import class_weight
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np 
import os, time

# Load data
data = pd.read_csv('MalMem2022_isnot.csv')

# Separate features and labels
features = data.iloc[:, 1:]  # first column is the label
labels = data.iloc[:, 0]

# Encode labels using LabelEncoder
encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(labels)

# Reshape the input data to add a channel dimension (required for Conv1D layers)
features = np.expand_dims(features, axis=2)

# Split data into training and test set
x_train, x_test, y_train, y_test = train_test_split(features, encoded_labels, test_size=0.2, random_state=42)

# Define the Keras TensorBoard callback
logdir="logs/fit/" + time.strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=logdir)

# Calculate class weights
sample_weights = class_weight.compute_sample_weight('balanced', y_train)

def build_model(hp: HyperParameters):
    # Define the input layer
    input_layer = Input(shape=(x_train.shape[1], 1))

    # Define the Conv1D layers with tunable number of filters
    conv1 = Conv1D(hp.Int('conv1_filters', min_value=32, max_value=128, step=32), 3, activation='relu')(input_layer)
    conv2 = Conv1D(hp.Int('conv2_filters', min_value=32, max_value=128, step=32), 3, activation='relu')(conv1)

    # Flatten the output of the Conv1D layers
    flatten = Flatten()(conv2)

    # Define the Dense layers with tunable number of neurons
    dense = Dense(hp.Int('dense_units', min_value=8, max_value=64, step=8), activation='relu')(flatten)
    output = Dense(1, activation='sigmoid')(dense)

    # Construct the model
    model = Model(inputs=input_layer, outputs=output)

    # Compile the model with tunable learning rate
    model.compile(loss='binary_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(hp.Choice('learning_rate', [1e-2, 1e-3, 1e-4])),
                  metrics=['accuracy'])
    return model

# Define the objective
objective = Objective("val_accuracy", direction="max")

# Define the tuner
tuner = RandomSearch(
    build_model,
    objective=objective,
    max_trials=5,
    executions_per_trial=3,
    directory='random_search',
    project_name='1layersequential')

# Run the hyperparameter search
tuner.search(x_train, y_train, 
             validation_data=(x_test, y_test),
             epochs=3,
             callbacks=[tensorboard_callback])

# Get the best hyperparameters
best_hyperparameters = tuner.get_best_hyperparameters()[0]

# Build a new model using the best hyperparameters
best_model = build_model(best_hyperparameters)

# Train the best model
best_model.fit(x_train, y_train, 
               validation_data=(x_test, y_test),
               epochs=3,
               callbacks=[tensorboard_callback])

# Save the model
best_model.save('malisnot.h5')

