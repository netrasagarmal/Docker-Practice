import pickle
import numpy as np

# Load the model
with open('SVM.pickle', 'rb') as f:
    model = pickle.load(f)

sepal_length = float(input("sepal_length: \t"))
sepal_width = float(input("sepal_width: \t"))
petal_length = float(input("petal_length: \t"))
petal_width = float(input("petal_width: \t"))

X_new = np.array([[sepal_length,sepal_width,petal_length,petal_width],[  4.9, 2.2, 3.8, 1.1 ], [  5.3, 2.5, 4.6, 1.9 ]])

print(model.predict(X_new))