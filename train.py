import os
import sys

sys.path.insert(0,'/home/shreyas/anaconda3/lib/python3.7/site-packages')

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn import metrics
from sklearn.externals import joblib
import pickle

def main():
	labels=[]
	features=[]
	file=open('Training Dataset.arff').read()
	list=file.split('\n')
	data=np.array(list)
	data1=[i.split(',') for i in data]
	data1=data1[0:-1]
	for i in data1:
		labels.append(i[30])

	print(data1)
	data1=np.array(data1)
	features=data1[:,:-1]
	features=features[:,[0,5,6,8,12,13,14,15,23,24,27]]
	features=np.array(features).astype(np.float)

	features_train=features
	labels_train=labels

	classifier = RandomForestClassifier(min_samples_split=7, verbose=True)
	classifier.fit(features_train, labels_train)

	filename='rf_sav.sav'
	outfile = open(filename,'wb')

	#joblib.dump(classifier,outfile)
	pickle.dump(classifier,outfile)

if __name__=="__main__":
    main()