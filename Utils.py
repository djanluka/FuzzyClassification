import pandas as pd
import sklearn.metrics as met
from termcolor import colored

def read_data():
    df = pd.read_csv("Attackers.csv")
    print('Prvih 5 instanci iz skupa', df.head(), sep='\n')
    print()

    x = df.drop(columns=['Name', 'Rating', 'Class'])
    y = df['Class']

    return x, y

def calculate_metrics(part, true_values, predicted_values):
    print(colored(part, "blue"))
    print('Matrica konfuzije')
    cnf_matrix = met.confusion_matrix(true_values, predicted_values)
    df_cnf_matrix = pd.DataFrame(cnf_matrix, index=get_features(), columns=get_features())
    print(df_cnf_matrix)
    print()

    accuracy = met.accuracy_score(true_values, predicted_values)
    print(colored(f'Preciznost: {accuracy}', "red"))
    print()

    class_report = met.classification_report(true_values, predicted_values)
    print('Izvestaj klasifikacije', class_report, sep='\n')

def k_neighbours(clf, x_train, y_train, x_test, y_test, y_pred):
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

def get_features():
    feature = ['Beginner', 'Amateur', 'Semi-pro', 'Professional', 'WorldClass']
    return feature
