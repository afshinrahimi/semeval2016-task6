'''
Created on 1 Nov 2015

@author: af
'''
import data_loader as dl
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
import numpy as np
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report

def baseline_1(training_data, eval_data):
    
    #clf = SGDClassifier(loss='hinge', penalty='l1', n_iter=20, shuffle=True, verbose=True, n_jobs=2, average=False)
    train_d = [tweet for tweet in training_data['Tweet'] + ' ' + training_data['Target']]
    eval_d = [tweet for tweet in eval_data['Tweet'] + ' ' + eval_data['Target']]
    
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_df=1.0, min_df=1, binary=True, norm='l2', use_idf=True, smooth_idf=False, sublinear_tf=True, encoding='latin1')
    
    X_train = vectorizer.fit_transform(train_d)
    X_eval = vectorizer.transform(eval_d)
    Y_train = np.asarray([stance for stance in training_data['Stance']])
    Y_eval = np.asarray([stance for stance in eval_data['Stance']])
    
    tuned_parameters = {'alpha': [10 ** a for a in range(-12, 0)]}
    clf = GridSearchCV(SGDClassifier(loss='hinge', penalty='elasticnet',l1_ratio=0.75, n_iter=10, shuffle=True, verbose=False, n_jobs=4, average=False)
                      , tuned_parameters, cv=10, scoring='f1_weighted')
    clf.fit(X_train, Y_train)
    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    for params, mean_score, scores in clf.grid_scores_:
        print("%0.3f (+/-%0.03f) for %r"
              % (mean_score, scores.std() * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = Y_eval, clf.predict(X_eval)
    print(classification_report(y_true, y_pred))
    print()
    
if __name__ == '__main__':
    dl.init()
    baseline_1(dl.training_data, dl.dev_data)