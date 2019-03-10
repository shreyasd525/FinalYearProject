import os
import sys

sys.path.insert(0,'/home/shreyas/anaconda3/lib/python3.7/site-packages')
import features_extraction
from sklearn.externals import joblib
import pickle



def main():
    #features_test = sys.argv[1]#.split(',')
    #url = 'http://myau-user.com/'
    url = 'https://www.google.com'
    features_test=features_extraction.main(url)
    #print(features_test)

    features_test=[features_test,]
    #print(features_test)

    #new_features_test=[[1, 1, 1, 1, -1, -1, -1, 0, 1, 1, 1],]
    #print(new_features_test)


    infile = 'rf_sav.sav'
    #clf = joblib.load('rf12345','r')
    '''

    clf = pickle.load(open(infile,'rb'))
    
    #print("kool reached upto joblib")

    pred=clf.predict(features_test)
    #print(pred)
    prob=clf.predict_proba(features_test)
    #print('Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred)
    #print ("The probability of this site being a phishing website is ", features_test[0], "%")
    #print(pred)
    


    if int(pred[0])==1:
        # print "The website is safe to browse"
        print ("SAFE")
    elif int(pred[0])==-1:
        # print "The website has phishing features. DO NOT VISIT!"
        print("PHISHING")

    #print('Error -', features_test)
    #print("good")
    '''


if __name__=="__main__":
    main()

