import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
import sklearn.preprocessing as prep
import sklearn.metrics as met
from termcolor import colored


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


def k_neighbours():
    distances, indices = clf.best_estimator_.kneighbors(x_test)
    k = len(indices[0])
    for i in range(0, len(x_test)):

        # izdvajanje podataka o test instanci
        print(colored("test instanca: ", "blue"), colored(x_test.iloc[i], "blue"), sep="\n")

        # ako je dodeljena tacna klasa instanci, klasu u izvestaju se boji
        # zelenom bojom, a u suprotnom crvenom
        if (y_test.iloc[i] == y_pred[i]):
            color = "green"
        else:
            color = "red"

        # prikaz prave i dodeljene klase test instance
        print("prava klasa: ", colored(y_test.iloc[i], color))
        print("dodeljena klasa: ", colored(y_pred[i], color))
        print("\n")

        # izvestaj o susedima
        print(colored("susedi: ", "blue"))
        for j in range(0, k):
            print(x_train.iloc[indices[i][j]])
            print("class:", colored(y_train.iloc[indices[i][j]], "yellow"))
            print("distance: ", distances[i][j], "\n")

        print("\n")

def my_test():
    x = df.drop(columns=['Name', 'Rating', 'Class'])
    features = x.columns
    y = df['Class']

    # OBAVEZNA NORMALIZACIJA KOD KNN
    x_normalized = pd.DataFrame(prep.MinMaxScaler().fit_transform(x))
    x_normalized.columns = features

    #MI BIRAMO IGRACE KOJE CEMO UZETI U OBZIR ZA PROVERU
    arr = [10, 70, 184, 250, 600, 650]
    x_test = x_normalized.loc[arr]
    y_test = y.loc[arr]
    y_true, y_pred = y_test, clf.predict(x_test)
    k_neighbours()


if __name__ == '__main__':

    df = pd.read_csv("SviNapadaciSaKlasama.csv")
    print('Prvih 5 instanci iz skupa', df.head(), sep='\n')

    x = df.drop(columns=['Name', 'Rating', 'Class'])
    features = x.columns
    y = df['Class']

    # OBAVEZNA NORMALIZACIJA KOD KNN
    x_normalized = pd.DataFrame(prep.MinMaxScaler().fit_transform(x))
    x_normalized.columns = features

    x_train, x_test, y_train, y_test = train_test_split(x_normalized, y, train_size=0.95, stratify=y)

    parameters = {'n_neighbors': range(3, 10),
              'p': [1, 2],
              'weights': ['uniform', 'distance']}
    clf = GridSearchCV(KNeighborsClassifier(), parameters, cv=5)
    clf.fit(x_train, y_train)

    print("Best parameters", clf.best_params_, sep="\n")

    y_true, y_pred = y_train, clf.predict(x_train)
    calculate_metrics('Trening', y_true, y_pred, clf.classes_)

    y_true, y_pred = y_test, clf.predict(x_test)
    calculate_metrics('Test', y_true, y_pred, clf.classes_)
    k_neighbours()

    #my_test()


