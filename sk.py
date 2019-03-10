import sys

sys.path.insert(0,'/home/shreyas/anaconda3/lib/python3.7/site-packages')

#import sklearn

from sklearn.externals import joblib
def main():
    new_features_test=[[1, 1, 1, 1, -1, -1, -1, 0, 1, 1, 1],]
    infile = open('rf123.pkl','rb')

    '''clf = joblib.load(infile)
    pred=clf.predict(new_features_test)
    prob=clf.predict_proba(new_features_test)

    if int(pred[0])==1:
        print ("SAFE")
    elif int(pred[0])==-1:
        print("PHISHING")
'''
if __name__=="__main__":
    main()