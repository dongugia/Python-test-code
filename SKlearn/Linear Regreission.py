import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

data = pd.read_csv("Data\student-mat.csv", sep=";")

data= data[["G1","G2","G3","studytime","failures","absences"]]
print(data.head())

predict = "G3"
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# TRAIN MODEL MULTIPLE TIMES FOR BEST SCORE
best = 0
for _ in range(20):
    x_train,  x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accurary: " + str(acc))

    if acc > best:
        best = acc
        with open("studentgrades.pickle","wb") as f:
            pickle.dump(linear, f)

# LOAD MODEL
pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)

print("_______________________________________")
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print("_______________________________________")

predicted = linear.predict(x_test)
for x in range(len(predicted)):
    print(predicted[x], x_test[x], y_test[x])

# Drawing and plotting model

plot = "failures"
plt.scatter(data[plot], data["G3"])
plt.legend(loc=4)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()


# #Xác định mô hình sử dụng
# linear = linear_model.LinearRegression()
#
# #Đào tạo và chấm điểm
# linear.fit(x_train, y_train)
# acc = linear.score(x_test, y_test)
# print(acc)
#
# # Xem các hằng đã dùng để tạo hàm
# print('Coefficient: \n', linear.coef_) # Giá trị độ dốc
# print('Intercept: \n', linear.intercept_) # giới hạn
#
# predictions = linear.predict(x_test) # Danh sách phỏng đoán
# for x in range(len(predictions)):
#     print(predictions[x], x_test[x],y_test[x])

