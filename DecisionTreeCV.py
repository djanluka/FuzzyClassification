import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
import sklearn.metrics as met
from sklearn.tree import DecisionTreeClassifier

def calculate_metrics(part, true_values, predicted_values, class_names):

    print('Skup ', part)
    print('Matrica konfuzije')
    cnf_matrix = met.confusion_matrix(true_values, predicted_values)
    df_cnf_matrix = pd.DataFrame(cnf_matrix, index=class_names, columns=class_names)
    print(df_cnf_matrix)
    print('\n')

    accuracy = met.accuracy_score(true_values, predicted_values)
    print('Preciznost', accuracy)
    print('\n')

    class_report = met.classification_report(true_values, predicted_values)
    print('Izvestaj klasifikacije', class_report, sep='\n')


if __name__ == '__main__':

    df = pd.read_csv("SviNapadaciSaKlasama.csv")
    print('Prvih 5 instanci iz skupa', df.head(), sep='\n')

    x = df.drop(columns=['Name', 'Rating', 'Class'])
    y = df['Class']

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
        calculate_metrics('Trening', y_true, y_pred, clf.classes_)

        y_true, y_pred = y_test, clf.predict(x_test)
        calculate_metrics('Test', y_true, y_pred, clf.classes_)

        #test = df.loc[250:260, ]
        #test = test.drop(columns=['Name', 'Rating', 'Class'])
        #y_pred = clf.predict(test)
        #print(y_pred)
