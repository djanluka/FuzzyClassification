from FuzzyAlgorithm import FuzzyAlgorithm
import Utils
'''
import Utils
import ClassificationAlgorithms as CA

x, y = Utils.read_data()
CA.DecisionTree(x, y)
CA.DecisionTreeCV(x, y)
CA.KNN(x, y)
CA.NaiveBayes(x, y)
'''

'''
bc = int(input("Ball control: "))
dr = int(input("Dribbling: "))
sp = int(input("Speed: "))
fi = int(input("Finishing: "))
alg = FuzzyAlgorithm.FuzzyAlgorithm(bc, dr, sp, fi)
solution = alg.solve()
print(solution)
'''


x, y = Utils.read_data()
y_pred = []

for index, row in x.iterrows():
    bc = row[0]
    dr = row[1]
    sp = row[2]
    fi = row[3]
    FA = FuzzyAlgorithm(bc, dr, sp, fi)
    y_pred.append(FA.get_predicted_class())

Utils.calculate_metrics('FuzzyAlgorithm', y, y_pred)
