# -*- coding: utf-8 -*-
"""01_neural_network_regression_with_tensorflow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OmBr9g2JS1tg4XFxcWjZGGp0tvZyuEir
"""

l

"""# Introduction to Regression with Neural Networks in TensorFlow

There are many definitions for a regression problem, but in our case we are going to simplify it: predicting a numerical variable based on some other combination of variables, even shorter... predicting a number
"""

# Import TensorFlow
import tensorflow as tf

print(tf.__version__)

"""# Creating Data to view and fit"""

import numpy as np
import matplotlib.pyplot as plt

# Create the features
x = np.array([-7.0, -4.0, -1.0, 2.0, 5.0, 8.0, 11.0, 14.0])

# Create labels
y = np.array([3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])

#Visualize it
plt.scatter(x, y);

y == x + 10

"""## Input and Output shapes"""

# Create a demo tensor for our housing price prediction problem
house_info = tf.constant(["bedroom", "bathroom", "garage"])
house_price = tf.constant([937000])

house_info, house_price

input_shape = x[0].shape
output_shape = y[0].shape

input_shape, output_shape

# Turn our numpy arrays into tensors with dtype float32
X = tf.cast(tf.constant(x), dtype=tf.float32)
Y = tf.cast(tf.constant(y), dtype=tf.float32)

input_shape = X[0].shape
output_shape = Y[0].shape
input_shape, output_shape

"""## Steps in modeling with tensorflow

1. **Creating a model**- define the input and output layers, as well as the hidden layers of a deep learning model.
2. **Compile a model** - define the loss function (in other words, the function which tells our function how wrong it is) and the optimizer (tells our model how to improve the patterns its learning) and evaluation metrics (what we can use to interpret the performance of our model)
3. **Fitting a model**- letting the model try to find patterns between X & y (features and labels)



"""

# Set random seed
tf.random.set_seed(42)

# 1. Create a model using the sequential API

model = tf.keras.Sequential([
  tf.keras.layers.Dense(1)
])

# 2. Compile the model
model.compile(loss=tf.keras.losses.mae, #mae is short for mean absolute error
              optimizer=tf.keras.optimizers.SGD(), # stochastic gradient descent
              metrics = ["mae"]
)

#. Fit the model
model.fit(tf.expand_dims(X, axis = -1), Y, epochs = 5)

# Check out X and y
X, Y

# Try and make a prediction with out model
y_pred = model.predict([17.0])

y_pred

y_pred + 11

"""## Improving our model

We can improve our model by altering the steps we took to create a model

1. **Creating a model** - here we might add more layers, increase the number of hidden units (also called neurons) within ecah of the hidden layers, change the activation functions of each layer.
2. **Compiling a model** - here we might change the optimization function or perhaps the **learning rate** of the optimization function
3. **Fitting a model** - here we might fit a model for more **epochs** (leave it training for logner) or on more data (give the model more examples to learn from).


"""

# Let's rebuild our model

#1. Create the model

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1)
])

# 2. Compile the model

model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.SGD(),
              metrics = ["mae"])
# 3. Fit the model
model.fit(tf.expand_dims(X, axis = -1), Y, epochs = 100)

# Remind ourselves of the data

X, Y

# Let's see if our model's prediction has improved

model.predict([17.0])

# Rebuild model again

model = tf.keras.Sequential([
    tf.keras.layers.Dense(100, activation = "relu"),
    tf.keras.layers.Dense(100, activation = "relu"),
    tf.keras.layers.Dense(100, activation = "relu"),
    tf.keras.layers.Dense(1)
])

model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.Adam(lr=.0001),
              metrics = ["mae"])

model.fit(tf.expand_dims(X, axis = -1), Y, epochs = 100)

# Let's see if we can make another to improve our model

model = tf.keras.Sequential([
    tf.keras.layers.Dense(50, activation = None),
    tf.keras.layers.Dense(1)
])

model.compile(loss = tf.keras.losses.mae,
              optimizer = tf.keras.optimizers.Adam(lr = .01),
              metrics = ["mae"])
model.fit(tf.expand_dims(X, axis = -1), Y, epochs = 100)

# Let's remind ourselves of the data
  X, Y

  model.predict([17.0])

  #Learning Rate is most important hyperparaemter of many different neural networks

"""## Evaluating a model

In practice, a typical workflow you'll go through when building neural networks is:

'''
Build a model -> fit it -> evaluate it -> tweak a model -> fit it -> evaluate it -> tweak a model -> fit it -> evaluate it -> ...
'''

When it comes to evaluation... there are 3 words you should memorize:

> "Visualize, Visualize, Visualize"

It's a good idea to visualize:

* The data - what data are we working with? What does it look like
* The model itself - what does our model look like?
* The training of a model - how does a model perform while it learns?
* The predictions of a model - how do the predictions of a model line up against the ground truth (the original labels)?
"""

# Make a bigger dataset

X = tf.range(-100, 100, 4)
X

# Make labels for the dataset
y = X + 10
y

# Visualize the data
import matplotlib.pyplot as plt
plt.scatter(X, y)

"""### The 3 sets...

* **Training set** - the model learns from this data, which is typically 70-80% of the total data you have available
* **Validation set** - the model gets tuned on this data, which is 10-15% of the data available
* **Test set**- the model gets evaluated on this data to test what it has learned, this set is typically 10-15% of the total data available
"""

# Check the length of how many samples we have

len(X)

# split the data into train and test sets
X_train = X[:40] # first 40 training samples (80% of data)
y_train = y[:40]

X_test = X[40:] # last 10 are testing samples (20% of data)
y_test = y[40:]

len(X_train), len(X_test), len(y_train), len(y_test)

"""### Visualizing the data
Now we've got our data in training and test sets... let's visualize it again!
"""

plt.figure(figsize=(10,7))

#plot training data in blue
plt.scatter(X_train, y_train, c = "b", label = "Training data")
#plot test data in green
plt.scatter(X_test, y_test, c = "g", label = "Test data")
plt.legend();

# Let's have a look at how to build a neural network for our data

#1. Create a model

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1)
])
#2. Compile a model
model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.SGD(),
              metrics = ["mae"])
#3. Fit the model
#model.fit(tf.expand_dims(X_train, axis = -1), y_train, epochs = 100)

"""### Visualizing the model"""

model.summary

# Let's create a model which builds automatically by defining the input_shape argument in the first layer

tf.random.set_seed(42)

# 1. Create a model (same as above)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape = [1], name = "input_layer"),
    tf.keras.layers.Dense(1, name = "output_layer")
], name = "model_1")
#2. compile a model
model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.SGD(),
              metrics = ["mae"])

model.summary()

"""* Total params - total number of parameters in the model.
* Trainable parameters - these are the parameters (patterns) the model can update as it trains.
* Non-trainable params - these parameters aren't updated during training (this is typical when you bring in already learned patterns or paramaters from other models during **transfer learning**)
"""

# Let's fit our model to the training data
model.fit(X_train, y_train, epochs = 100, verbose = 0)

from tensorflow.keras.utils import plot_model

plot_model(model=model, show_shapes = True)

"""### Visualizing our model's predictions

To visualize predictions, it's a good idea to plot them against the ground truth labels.

Often you'll see this in the form of 'y_test' or 'y_true' vs. 'y_pred' (ground truth versus your model's prediction).
"""

# Make some predictions
y_pred = model.predict([X_test])
y_pred

y_test

"""**Note:** If you feel like you're going to reuse some kind of functionality,  in the future it is a good idea to turn it into a function"""

# Let's create a plotting function
def plot_predictions(train_data=X_train,
                     train_labels=y_train,
                     test_data=X_test,
                     test_labels=y_test,
                     predictions=y_pred):
  """
  Plots training data, test data and compares predictions to ground truth
  """

  plt.figure(figsize=(10,7))
  # Plot training data in blue
  plt.scatter(train_data, train_labels, c="b", label="Training Data")
  #Plot testing data in green
  plt.scatter(test_data, test_labels, c="g", label = "Test Data")
  # Plot model's predictions in red
  plt.scatter(test_data, predictions, c = "r", label = "Predicted Data")
  #Show the legend
  plt.legend();

plot_predictions(train_data=X_train,
                 train_labels = y_train,
                 test_data = X_test,
                 test_labels = y_test,
                 predictions=y_pred)

"""### Evaluating our model's prediction with regression evaluation metrics

Depending on the problem you're working on, there will be different evaluation metrics to evaluate your model's performance.

Since we're working on a regression problem, two of the main metrics:
* MAE - mean absolute error, "on average, how wrong is each of my model's predictions"
* MSE - mean square error, "square the average errors"
"""

# Evaluate the model on the test set
model.evaluate(X_test, y_test)

# Calculate the mean absolute error
mae = tf.metrics.mean_absolute_error(y_true =y_test,
                                     y_pred = tf.constant(y_pred))
mae

tf.constant(y_pred)

y_test

#Calculate mae
mae = tf.metrics.mean_absolute_error(y_true = y_test,
                                     y_pred = tf.squeeze(y_pred))
mae

# Calcualte the mean square error
mse = tf.metrics.mean_squared_error(y_true = y_test,
                                   y_pred = tf.squeeze(y_pred))
mse

# Make some functions to reuse MAE and MSE

def mae(y_true, y_pred):
  return tf.metrics.mean_absolute_error(y_true=y_true,
                                        y_pred= tf.squeeze(y_pred))
def mse(y_true, y_pred):
  return tf.metrics.mean_squared_error(y_true = y_true,
                                       y_pred = tf.squeeze(y_pred))

"""### Running experiments to improve our model

```
Build a model -> fit it -> evaluate it -> tweak it -> fit it -> evaluate it -> tweak it -> fit it - evaluate it -> ...
```

1. Get more data - get more examples for model to train on (more opportunities to learn patterns or relationships between features and labels).
2. Make your model larger (use a more complex model) - this might come in the form of more layers or more hidden units in each layer.
3. Train for longer - give your model more of a chance to find patterns in the data

Let's do 3 modelling experiments:

1. `model_1` - same as the original model, 1 layer, trained for 100 epochs.
2. `model_2` - 2 layers, trained for 100 epochs.
3. `model_3` - 2 layers, trained for 500 epochs.
4. `model_4` - 2 layers, with adams for 100 epochs
5.  `model_5` - 2 layers, with adams for 500 epochs

**Build`model_1`**
"""

# Set random seed
tf.random.set_seed(42)

#1. Create the model
model_1 = tf.keras.Sequential([
    tf.keras.layers.Dense(1)
])
#2. Compile the model
model_1.compile(loss=tf.keras.losses.mae,
                optimizer=tf.keras.optimizers.SGD(),
                metrics = ["mae"])
#3. Fit the model
model_1.fit(tf.expand_dims(X_train, axis = -1), y_train, epochs = 100)

# Make and plot predictions for model_1
y_preds_1 = model_1.predict(X_test)
plot_predictions(predictions=y_preds_1)

# Calculate model_1 evaluation metrics

mae_1 = mae(y_test, y_preds_1)
mse_1 = mse(y_test, y_preds_1)

mae_1, mse_1

"""** Build `model_2`

* 2 dense layers, trained for 100 epochs
"""

tf.random.set_seed(42)

model_2 = tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
model_2.compile(loss=tf.keras.losses.mae,
                optimizer=tf.keras.optimizers.SGD(),
                metrics=["mse"])

model_2.fit(tf.expand_dims(X_test, axis = -1), y_test, epochs = 200)

y_preds_2 = model_2.predict(X_test)
plot_predictions(predictions=y_preds_2)

mae_2 = mae(y_test, y_preds_2)
mse_2 = mse(y_test, y_preds_2)
mae_2, mse_2

"""**Build `model_3`**
*2 layers, trained for 500 epochs
"""

model_3 = tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
model_3.compile(loss=tf.keras.losses.mae,
                optimizer=tf.keras.optimizers.SGD(),
                metrics = ["mae"])
model_3.fit(tf.expand_dims(X_test, axis = -1), y_test, epochs = 500)

y_preds_3 = model_3.predict(X_test)
plot_predictions(predictions=y_preds_3)

mae_3 = mae(y_test, y_preds_3)
mse_3 = mse(y_test, y_preds_3)
mae_3, mse_3

"""### Comparing the results of our experiments
We've run a few experiments, let's compare the results
"""

# Let's compare our model's results using a pandas DataFrame
import pandas as pd

model_results = [["model_1", mae_1.numpy(), mse_1.numpy()],
                 ["model_2", mae_2.numpy(), mse_2.numpy()],
                 ["model_3", mae_3.numpy(), mse_3.numpy()]]

all_results = pd.DataFrame(model_results, columns= ["model", "mae", "mse"])
all_results

model_2.summary()

"""## Tracking your experiments

One really good habit in machine learning modeling is to track the results of your experiments.

And when doing so, it can be tedious if you're runing lots of experiments.

Luckily, there are tools to help us!

Resource: As you build more models, you'll want to look into using:

* Tensorboard - a component of the tensorflow library to help track modelling experiments (we'll see this one later).
* Weights & Biases - a tool for tracking all kinds of machine learning experiments (plugs straight into tensorboard).

## Saving our models

Saving our models allows us to use them outside of Google Collab (or wherever they were trained) such as in a web application or a mobile app

There are 2 main formats we can save our model's too:

1. The SavedModel format
2. the HDF5 format
"""

# Save a model using the SavedModel format
model_2.save("best_model_SavedModel_format")

# Save a model using the HDF5 format

model_2.save("best_model_HDF5_format.h5")

"""## Loading in a saved model"""

# Load in the SavedModel format
loaded_SavedModel_format = tf.keras.models.load_model("/content/best_model_SavedModel_format")
loaded_SavedModel_format.summary()

model_2_preds = model_2.predict(X_test)
loaded_SavedModel_format_preds = loaded_SavedModel_format.predict(X_test)

model_2_preds == loaded_SavedModel_format_preds

# Load in a model using the .h5 format

loaded_h5_model = tf.keras.models.load_model("/content/best_model_HDF5_format.h5")
loaded_h5_model.summary()

# check if h5 is same as model 2

loaded_h5_model_preds = loaded_h5_model.predict(X_test)
model_2_preds = model_2.predict(X_test)

model_2_preds == loaded_h5_model_preds

"""### Download a model (or any other file) from Google Colab

If you want to download your files from Google Colab:

1. You can go to the "files" tab and right click on the file you're after and click "download".
2. Use code (see the cell below)  
3. Save it to google drive by connecting Google Drive and copying it there (see 2nd code cell below)
"""

# Download a file from google colab
from google.colab import files
files.download("/content/best_model_HDF5_format.h5")

# Save a file from Google Colab to Google Drive (requires mounting Google Drive)
!cp /content/best_model_HDF5_format.h5 /content/drive/MyDrive/TensorflowCourse

!ls /content/drive/MyDrive/TensorflowCourse

"""### A Larger Example"""

# Import required libraries
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

# Read in the insurance dataset
insurance = pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")

insurance

insurance_one_hot = pd.get_dummies(insurance)
insurance_one_hot.head()

# Create X and y values (labels and features)
X = insurance_one_hot.drop("charges", axis = 1)
y = insurance_one_hot["charges"]

# View x
X.head()

# View y
y.head()

# Create training and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
len(X_train), len(y_train)

# Build a neural network (sort of like model_2 above)
tf.random.set_seed(42)

insurance_model = tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
insurance_model.compile(loss = tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.SGD(),
              metrics=["mae"])
insurance_model.fit(tf.expand_dims(X_train, axis = -1), y_train, epochs = 100)

# Check the results of the insurance model on the test data
insurance_model.evaluate(X_test, y_test)

"""Right now it looks like our model isn't performing too well... let's try and improve it!

To (try) improve our model, we'll run 2 experiments:

1. Add an extra layer with more hidden units
2. Train for longer
"""

# Trial 1
tf.random.set_seed(42)
insurance_model_1 = tf.keras.Sequential([
    tf.keras.layers.Dense(100),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
insurance_model_1.compile(loss=tf.keras.losses.mae,
                          optimizer=tf.keras.optimizers.Adam(),
                          metrics=["mae"])
insurance_model_1.fit(tf.expand_dims(X_train, axis = -1), y_train, epochs = 100, verbose = 1)

insurance_model_1.evaluate(X_test, y_test)

# Trial 2
tf.random.set_seed(42)
insurance_model_2 = tf.keras.Sequential([
    tf.keras.layers.Dense(100),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
insurance_model_2.compile(loss=tf.keras.losses.mae,
                          optimizer=tf.keras.optimizers.Adam(),
                          metrics = ["mae"])
history = insurance_model_2.fit(tf.expand_dims(X_train, axis = -1), y_train, epochs = 200)

insurance_model_2.evaluate(X_test, y_test)

# Plot history (also known as a loss curve or a training curve)
pd.DataFrame(history.history).plot()
plt.ylabel("loss")
plt.xlabel("epochs")

"""### Preprocessing data (normalization and standardization)

In terms of scaling values, neural networks tend to prefer normalization.

If you're not sure on which to use, you could try both and see which performs better.


"""

import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

# Read in the insurance dataframe
insurance = pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")
insurance

"""To prepare out data, we can borrom a few classes from Scikit-Learn."""

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
# Create a column transformer
ct = make_column_transformer(
    (MinMaxScaler(), ["age", "bmi", "children"]), # turn all values in these columns between 0 and 1
    (OneHotEncoder(handle_unknown="ignore"), ["sex", "smoker", "region",])
)

# Create X and y
X = insurance.drop("charges", axis = 1)
y = insurance["charges"]

# Build our train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

# Fit the column transformer to our training data
ct.fit(X_train)

# Transform training and test data with normalization (MinMaxScaler) and OneHotEncoder

X_train_normal = ct.transform(X_train)
X_test_normal = ct.transform(X_test)

# What does our data look like now?
X_train.loc[0]

y_train.shape, X_train_normal.shape

"""Data has been normalized and one hot encoded. Now let's build a neural network on it and see how it goes."""

# Build a neural network model to fit on our normalized data
tf.random.set_seed(42)
insurance_model_3 = tf.keras.Sequential([
    tf.keras.layers.Dense(100),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
insurance_model_3.compile(loss=tf.keras.losses.mae,
                          optimizer=tf.keras.optimizers.Adam(),
                          metrics = ["mae"])
insurance_model_3.fit(tf.expand_dims(X_train_normal, axis = -1), y_train, epochs = 100)

# Evaluate our model

insurance_model_3.evaluate(X_test_normal, y_test)

X["bmi"].plot(kind="hist")

X["children"].plot(kind="hist")