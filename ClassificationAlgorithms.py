import Utils
import pandas as pd
import sklearn.preprocessing as prep
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

def DecisionTree(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, stratify=y)

    dt = DecisionTreeClassifier()

    dt.fit(x_train, y_train)

    y_pred = dt.predict(x_train)
    Utils.calculate_metrics('Training Decision Tree ', y_train, y_pred, dt.classes_)

    y_pred = dt.predict(x_test)
    Utils.calculate_metrics('Test  Decision Tree ', y_test, y_pred, dt.classes_)

    # test = df.loc[65:75, ]
    # test = cr.drop(columns=['Name', 'Rating', 'Class'])
    # y_pred = dt.predict(test)
    # print(y_pred)

def DecisionTreeCV(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, stratify=y)

    parameters = [{'criterion': ['gini', 'entropy'],
                   'max_depth': [3, 5, 7, 9, 11]
                   }]

    scores = ['precision', 'f1']

    for score in scores:
        print("Mera ", score)
        print()

        clf = GridSearchCV(DecisionTreeClassifier(), parameters, cv=5, scoring=f'{score}_macro')

        clf.fit(x_train, y_train)

        print("Najbolji parametri:")
        print(clf.best_params_)
        print()

        y_true, y_pred = y_train, clf.predict(x_train)
        Utils.calculate_metrics('Training Decision Tree CV', y_true, y_pred, clf.classes_)

        y_true, y_pred = y_test, clf.predict(x_test)
        Utils.calculate_metrics('Test  Decision Tree CV', y_true, y_pred, clf.classes_)

        # test = df.loc[250:260, ]
        # test = test.drop(columns=['Name', 'Rating', 'Class'])
        # y_pred = clf.predict(test)
        # print(y_pred)


def KNN(x, y):
    features = x.columns
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.95, stratify=y)

    scaler = prep.MinMaxScaler().fit(x_train)
    x_normalized_train = pd.DataFrame(scaler.transform(x_train), columns=features)
    x_normalized_test = pd.DataFrame(scaler.transform(x_test), columns=features)

    parameters = {'n_neighbors': range(3, 10),
                  'p': [1, 2],
                  'weights': ['uniform', 'distance']}

    clf = GridSearchCV(KNeighborsClassifier(), parameters, cv=5)
    clf.fit(x_normalized_train, y_train)

    print("Best parameters", clf.best_params_, sep="\n")

    y_true, y_pred = y_train, clf.predict(x_normalized_train)
    Utils.calculate_metrics('Training KNN', y_true, y_pred, clf.classes_)

    y_true, y_pred = y_test, clf.predict(x_normalized_test)
    Utils.calculate_metrics('Test KNN', y_true, y_pred, clf.classes_)
    Utils.k_neighbours(clf, x_train, y_train, x_test, y_test, y_pred)

def NaiveBayes(x, y):
    features = x.columns
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.70, stratify=y)

    scaler = prep.MinMaxScaler().fit(x_train)
    x_normalized_train = pd.DataFrame(scaler.transform(x_train), columns=features)
    x_normalized_test = pd.DataFrame(scaler.transform(x_test), columns=features)

    clf_gnb = GaussianNB()
    clf_gnb.fit(x_normalized_train, y_train)

    print('MODEL')
    print('class_count: ', clf_gnb.class_count_)
    print('class_prior: ', clf_gnb.class_prior_)
    print('classes: ', clf_gnb.classes_)
    print()

    y_true, y_pred = y_train, clf_gnb.predict(x_normalized_train)
    Utils.calculate_metrics('Training Naive Bayes', y_true, y_pred, clf_gnb.classes_)

    y_true, y_pred = y_test, clf_gnb.predict(x_normalized_test)
    Utils.calculate_metrics('Test Naive Bayes', y_true, y_pred, clf_gnb.classes_)

    # test = df.loc[60:70, ]
    # test = test.drop(columns=['Name', 'Rating', 'Class'])
    # y_pred = clf_gnb.predict(test)
    # print(y_pred)'