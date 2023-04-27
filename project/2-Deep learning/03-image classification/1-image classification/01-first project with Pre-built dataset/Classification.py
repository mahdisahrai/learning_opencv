import numpy as np
from tensorflow import keras
from keras.constraints import maxnorm
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPool2D, Dense, Dropout, Flatten
from keras.layers import BatchNormalization
from keras.callbacks import EarlyStopping
from sklearn.metrics import confusion_matrix
from keras.utils import np_utils
from keras.datasets import cifar10
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()


#x is image , y = is label
(X_train, y_train), (X_test, y_test) = cifar10.load_data()


# Normalize the inputs from 0-255 to between 0 and 1 by dividing by 255
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0


# One-hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)


num_class = y_test.shape[1] #10



model = Sequential()
model.add(Conv2D(32, (3,3), padding='same', input_shape=X_train.shape[1:], activation='relu'))
model.add(Dropout(0.2)) # Dropout is used for turning off Neurons To prevent other neurons from becoming lazy
model.add(BatchNormalization()) # BatchNormalization does normal result for each layer
model.add(Conv2D(64, (3,3), padding='same', activation='relu'))
model.add(MaxPool2D(2))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Conv2D(64, (3,3), padding='same', activation='relu'))
model.add(MaxPool2D(2))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Conv2D(128, (3,3), padding='same', activation='relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Dense(num_class, activation = 'softmax')) #softmax shows that which is the best result between outputs 0-1 


model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy']) # categorical_crossentropy: for revising loss

model.summary()


# batch_size: for example = 50000/64 = 782
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=30, batch_size=64)


for key,val in history.history.items():
  print(key)

pd.DataFrame(history.history).plot()


labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

model.save('fisrtmodel.h5')
loader = load_model('fisrtmodel.h5')

loader.predict(X_test[0:10])[0]

y_test[0]

labels[3]


# y_test = y_test.astype(int)
# predictions = predictions.astype(int)

# fig, axes = plt.subplots(ncols=7, nrows=3, sharex=False, sharey=True, figsize=(17, 8))
# index = 0
# for i in range(3):
#     for j in range(7):
#         axes[i,j].set_title('actual:' + labels[y_test[index][0]] + '\n' 
#                             + 'predicted:' + labels[predictions[index][0]])
#         axes[i,j].imshow(X_test[index], cmap='gray')
#         axes[i,j].get_xaxis().set_visible(False)
#         axes[i,j].get_yaxis().set_visible(False)
#         index += 1

# plt.show()
