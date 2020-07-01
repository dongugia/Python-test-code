from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import  numpy as np

#we load the data with load_iris from sklearn
data = load_iris()
features = data['data']
features_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = np.array([target_names[i] for i in target])
example = np.array([target_names[i] for i in target])

for t, marker, c in zip(range(3),">ox","rgb"):
    # We plot each class on its own to get different colored markers
    plt.scatter(features[target == t,0],
                features[target == 0,1],
                marker=marker,
                c=c)

plength = features[:,2]
#use numpy operations to get setosa features
is_setosa = (labels == 'setosa')
# this is important step:
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
features = features[~is_setosa]
labels = labels[~is_setosa]
virginica = (labels == 'virginica')

print('Maximum of setosa: {0}.' .format(max_setosa))
print('Minium of others: {0}.' .format(min_non_setosa))

if features[:,2].all() < 2: print('Iris Setosa')
else: print('Iris Virginica or Iris Versicolour')

best_acc = -1.0
best_fi = 0.0
best_t = 0.0
for fi in range(features.shape[1]):
    # We ar going to gererate all posible threshold for this feature
    thresh = features[:,fi].copy()
    thresh.sort()
    # Now test all thresholds:
    for t in thresh:
        pred = (features[:,fi] > t)
        acc = (pred == virginica).mean()
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            bets_t = t
    if example[bets_fi] > t: print('Virginica')
    else: print('Versicolor')
