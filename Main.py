import Fuzzy
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

ballControl = []
ballControl.append(Fuzzy.MFInput("Low", [60, 72], [1, 0], bc))
ballControl.append(Fuzzy.MFInput("Medium", [70, 72, 78, 84], [0, 1, 1, 0], bc))
ballControl.append(Fuzzy.MFInput("High", [80, 84], [0, 1], bc))

dribbling = []
dribbling.append(Fuzzy.MFInput("Low", [62, 73], [1, 0], dr))
dribbling.append(Fuzzy.MFInput("Medium", [70, 73, 79, 85], [0, 1, 1, 0], dr))
dribbling.append(Fuzzy.MFInput("High", [81, 85], [0, 1], dr))

speed = []
speed.append(Fuzzy.MFInput("Low", [62, 77], [1, 0], sp))
speed.append(Fuzzy.MFInput("Medium", [72, 77, 84, 90], [0, 1, 1, 0], sp))
speed.append(Fuzzy.MFInput("High", [86, 90], [0, 1], sp))

finishing = []
finishing.append(Fuzzy.MFInput("Low", [60, 72], [1, 0], fi))
finishing.append(Fuzzy.MFInput("Medium", [67, 72, 78, 83], [0, 1, 1, 0], fi))
finishing.append(Fuzzy.MFInput("High", [80, 83], [0, 1], fi))

overall = []
overall.append(Fuzzy.MFOutput("Beginner", [40, 54], [1, 0]))
overall.append(Fuzzy.MFOutput("Amateur", [47, 54, 60, 66], [0, 1, 1, 0]))
overall.append(Fuzzy.MFOutput("Semi-pro", [61, 66, 71, 76], [0, 1, 1, 0]))
overall.append(Fuzzy.MFOutput("Professional", [71, 76, 83, 90], [0, 1, 1, 0]))
overall.append(Fuzzy.MFOutput("World Class", [85, 90], [0, 1]))

rules = []

# World class (3 high, 1 medium or 4 high)
rules.append(Fuzzy.Rule(ballControl[2], dribbling[2], speed[2], finishing[2], overall[4],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[2], speed[2], finishing[2], overall[4],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[1], speed[2], finishing[2], overall[4],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[2], speed[1], finishing[2], overall[4],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[2], dribbling[2], speed[2], finishing[1], overall[4],  Fuzzy.Logic.AND))

# Proffesional (2 high, 2 medium or 1 high, 3 medium or 2 high, 1 medium, 1 low)
rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[2], finishing[2], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[2], speed[1], finishing[2], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[2], speed[2], finishing[1], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[1], speed[1], finishing[2], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[1], speed[2], finishing[1], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[2], speed[1], finishing[1], overall[3],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[2], dribbling[1], speed[1], finishing[1], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[2], speed[1], finishing[1], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[2], finishing[1], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[1], finishing[2], overall[3],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[2], dribbling[2], speed[1], finishing[0], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[1], speed[2], finishing[0], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[1], speed[0], finishing[2], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[2], speed[0], finishing[1], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[0], speed[2], finishing[1], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[2], dribbling[0], speed[1], finishing[2], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[2], speed[1], finishing[2], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[2], speed[2], finishing[1], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[2], speed[0], finishing[2], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[2], speed[2], finishing[0], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[1], speed[2], finishing[2], overall[3],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[0], speed[2], finishing[2], overall[3],  Fuzzy.Logic.AND))


# Semi-pro (1 high, 1 low, 2 medium or 4 medium)
rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[1], finishing[1], overall[2],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[2], dribbling[1], speed[1], finishing[0], overall[2],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[2], speed[1], finishing[0], overall[2],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[2], finishing[0], overall[2],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[2], dribbling[1], speed[0], finishing[1], overall[2],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[2], speed[0], finishing[1], overall[2],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[0], finishing[2], overall[2],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[2], dribbling[0], speed[1], finishing[1], overall[2],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[0], speed[2], finishing[1], overall[2],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[0], speed[1], finishing[2], overall[2],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[0], dribbling[2], speed[1], finishing[1], overall[2],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[1], speed[2], finishing[1], overall[2],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[1], speed[1], finishing[2], overall[2],  Fuzzy.Logic.AND))

# Amateur (3 medium, 1 low or 2 medium, 2 low)
rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[1], finishing[0], overall[1],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[0], finishing[1], overall[1],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[0], speed[1], finishing[1], overall[1],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[1], speed[1], finishing[1], overall[1],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[1], dribbling[1], speed[0], finishing[0], overall[1],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[0], speed[1], finishing[0], overall[1],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[0], speed[0], finishing[1], overall[1],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[1], speed[1], finishing[0], overall[1],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[1], speed[0], finishing[1], overall[1],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[1], dribbling[0], speed[1], finishing[1], overall[1],  Fuzzy.Logic.AND))

# Beginner (3 low, 1 medium or 4 low)
rules.append(Fuzzy.Rule(ballControl[1], dribbling[0], speed[0], finishing[0], overall[0],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[1], speed[0], finishing[0], overall[0],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[0], speed[1], finishing[0], overall[0],  Fuzzy.Logic.AND))
rules.append(Fuzzy.Rule(ballControl[0], dribbling[0], speed[0], finishing[1], overall[0],  Fuzzy.Logic.AND))

rules.append(Fuzzy.Rule(ballControl[0], dribbling[0], speed[0], finishing[0], overall[0],  Fuzzy.Logic.AND))


numerator = 0
denominator = 0
for ovr in overall:
    numerator += ovr.mi * ovr.value
    denominator += ovr.mi

solution = numerator / denominator

print(solution)
