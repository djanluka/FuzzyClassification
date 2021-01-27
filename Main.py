import FuzzyAlgorithm
'''
import Utils
import ClassificationAlgorithms as CA

x, y = Utils.read_data()
CA.DecisionTree(x, y)
CA.DecisionTreeCV(x, y)
CA.KNN(x, y)
CA.NaiveBayes(x, y)
'''

bc = int(input("Ball control: "))
dr = int(input("Dribbling: "))
sp = int(input("Speed: "))
fi = int(input("Finishing: "))
alg = FuzzyAlgorithm.FuzzyAlgorithm(bc, dr, sp, fi)
solution = alg.solve()
print(solution)
