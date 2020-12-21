import pandas as pd
from sklearn.naive_bayes import GaussianNB #koristi se kada su atributi neprekidni
from sklearn.model_selection import train_test_split
import sklearn.preprocessing as prep
import sklearn.metrics as met


if __name__ == "__main__":
    df = pd.read_csv("SviNapadaciSaKlasama.csv")
    print('Prvih 5 instanci iz skupa', df.head(), sep='\n')

    x = df.drop(columns=['Name', 'Rating', 'Class'])
    features = x.columns
    y = df['Class']

    x_normalized = pd.DataFrame(prep.MinMaxScaler().fit_transform(x))
    x_normalized.columns = features

    x_train, x_test, y_train, y_test = train_test_split(x_normalized, y, train_size=0.70, stratify=y)

    clf_gnb = GaussianNB()
    clf_gnb.fit(x_train, y_train)

    y_pred = clf_gnb.predict(x_test)
    print('MODEL')
    print('class_count: ', clf_gnb.class_count_)
    print('class_prior: ', clf_gnb.class_prior_)
    print('classes: ', clf_gnb.classes_)
    print()


    cnf_matrix = met.confusion_matrix(y_test, y_pred)
    print("Matrica konfuzije", cnf_matrix, sep="\n")
    print("\n")

    accuracy = met.accuracy_score(y_test, y_pred)
    print("Preciznost", accuracy)
    print("\n")

    class_report = met.classification_report(y_test, y_pred)
    print("Izvestaj klasifikacije", class_report, sep="\n")

    #test = df.loc[60:70, ]
    #test = test.drop(columns=['Name', 'Rating', 'Class'])
    #y_pred = clf_gnb.predict(test)
    #print(y_pred)'