import sys
sys.path.insert(0, '/home/shreyas/anaconda3/lib/python3.7/site-packages')


import numpy as np
from sklearn.ensemble import RandomForestClassifier
#import joblib

labels = []
file = open('Training Dataset.arff').read()
data_list = file.split('\n')
data = np.array(data_list)
data1 = [i.split(',') for i in data]
data1 = data1[0:-1]
for i in data1:
    labels.append(i[30])

print("kool")
data1 = np.array(data1)
features = data1[:,:-1]
# Choose only the relevant features from the data set.
features=features[:,[0,5,6,8,12,13,14,15,23,24,27]]
features = np.array(features).astype(np.float)

features_train = features
labels_train = labels
# features_test=features[10000:]
# labels_test=labels[10000:]


print("\n\n ""Random Forest Algorithm Results"" ")
clf4 = RandomForestClassifier(min_samples_split=7, verbose=True)
clf4.fit(features_train, labels_train)
    
features_test = [[1, 1, 1, 1, -1, -1, -1, 0, 1, 1, 1],]#features_extraction.main(url)
# Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
features_test = np.array(features_test).reshape((1, -1))

#clf = joblib.load('classifier/random_forest.pkl')

pred = clf4.predict(features_test)
if int(pred[0]) == 1:
    print("SAFE")
elif int(pred[0]) == -1:
    print("PHISHING")


