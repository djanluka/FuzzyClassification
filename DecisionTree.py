import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import sklearn.metrics as met  #modul metrics sadrzi f-je za evaluaciju modela za klasifikaciju


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

    accuracy = met.accuracy_score(true_values, predicted_values, normalize=False)
    print('Preciznost u broju instanci', accuracy)
    print('\n')

    class_report = met.classification_report(true_values, predicted_values)
    print('Izvestaj klasifikacije', class_report, sep='\n')


if __name__ == '__main__':

    df = pd.read_csv("SviNapadaciSaKlasama.csv")
    print('Prvih 5 instanci iz skupa', df.head(), sep='\n')

    x = df.drop(columns=['Name', 'Rating', 'Class'])
    y = df['Class']

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, stratify=y)

    dt = DecisionTreeClassifier()

    dt.fit(x_train, y_train)

    y_pred = dt.predict(x_train)
    calculate_metrics('Trening ', y_train, y_pred, dt.classes_)

    y_pred = dt.predict(x_test)
    calculate_metrics('Test', y_test, y_pred, dt.classes_)

    #test = df.loc[65:75, ]
    #test = cr.drop(columns=['Name', 'Rating', 'Class'])
    #y_pred = dt.predict(test)
    #print(y_pred)