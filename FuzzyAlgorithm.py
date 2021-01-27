import numpy as np
import Fuzzy


class FuzzyAlgorithm:
    
    def __init__(self, bc, dr, sp, fi):
        self.ballControl = []
        self.setBallControl(bc)
        self.dribbling = []
        self.setDribbling(dr)
        self.speed = []
        self.setSpeed(sp)
        self.finishing = []
        self.setFinishing(fi)
        
        self.overall = []
        self.setOverall()
        
        self.rules = []
        self.setRules()

    def setBallControl(self, bc):
        self.ballControl.append(Fuzzy.MFInput("Low", [60, 72], [1, 0], bc))
        self.ballControl.append(Fuzzy.MFInput("Medium", [60, 72, 78, 84], [0, 1, 1, 0], bc))
        self.ballControl.append(Fuzzy.MFInput("High", [78, 84], [0, 1], bc))

    def setDribbling(self, dr):
        self.dribbling.append(Fuzzy.MFInput("Low", [62, 73], [1, 0], dr))
        self.dribbling.append(Fuzzy.MFInput("Medium", [62, 73, 79, 85], [0, 1, 1, 0], dr))
        self.dribbling.append(Fuzzy.MFInput("High", [79, 85], [0, 1], dr))

    def setSpeed(self, sp):
        self.speed.append(Fuzzy.MFInput("Low", [62, 77], [1, 0], sp))
        self.speed.append(Fuzzy.MFInput("Medium", [62, 77, 84, 90], [0, 1, 1, 0], sp))
        self.speed.append(Fuzzy.MFInput("High", [84, 90], [0, 1], sp))


    def setFinishing(self, fi):
        self.finishing.append(Fuzzy.MFInput("Low", [60, 72], [1, 0], fi))
        self.finishing.append(Fuzzy.MFInput("Medium", [60, 72, 78, 83], [0, 1, 1, 0], fi))
        self.finishing.append(Fuzzy.MFInput("High", [78, 83], [0, 1], fi))

    def setOverall(self):
        self.overall.append(Fuzzy.MFOutput("Beginner", [40, 54], [1, 0]))
        self.overall.append(Fuzzy.MFOutput("Amateur", [40, 54, 60, 66], [0, 1, 1, 0]))
        self.overall.append(Fuzzy.MFOutput("Semi-pro", [60, 66, 71, 76], [0, 1, 1, 0]))
        self.overall.append(Fuzzy.MFOutput("Professional", [71, 76, 83, 90], [0, 1, 1, 0]))
        self.overall.append(Fuzzy.MFOutput("World Class", [83, 90], [0, 1]))

    def setRules(self):
        # World class (3 high, 1 medium or 4 high)
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[2], self.speed[2], self.finishing[2], self.overall[4], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[2], self.speed[2], self.finishing[2], self.overall[4], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[1], self.speed[2], self.finishing[2], self.overall[4], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[2], self.speed[1], self.finishing[2], self.overall[4], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[2], self.speed[2], self.finishing[1], self.overall[4], Fuzzy.Logic.AND))

        # Professional (2 high, 2 medium or 1 high, 3 medium or 2 high, 1 medium, 1 low)
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[2], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[2], self.speed[1], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[2], self.speed[2], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[1], self.speed[1], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[1], self.speed[2], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[2], self.speed[1], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[1], self.speed[1], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[2], self.speed[1], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[2], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[1], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[2], self.speed[1], self.finishing[0], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[1], self.speed[2], self.finishing[0], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[1], self.speed[0], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[2], self.speed[0], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[0], self.speed[2], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[0], self.speed[1], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[2], self.speed[1], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[2], self.speed[2], self.finishing[1], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[2], self.speed[0], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[2], self.speed[2], self.finishing[0], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[1], self.speed[2], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[0], self.speed[2], self.finishing[2], self.overall[3], Fuzzy.Logic.AND))

        # Semi-pro (1 high, 1 low, 2 medium or 4 medium)
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[1], self.finishing[1], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[1], self.speed[1], self.finishing[0], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[2], self.speed[1], self.finishing[0], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[2], self.finishing[0], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[1], self.speed[0], self.finishing[1], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[2], self.speed[0], self.finishing[1], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[0], self.finishing[2], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[2], self.dribbling[0], self.speed[1], self.finishing[1], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[0], self.speed[2], self.finishing[1], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[0], self.speed[1], self.finishing[2], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[2], self.speed[1], self.finishing[1], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[1], self.speed[2], self.finishing[1], self.overall[2], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[1], self.speed[1], self.finishing[2], self.overall[2], Fuzzy.Logic.AND))

        # Amateur (3 medium, 1 low or 2 medium, 2 low)
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[1], self.finishing[0], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[0], self.finishing[1], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[0], self.speed[1], self.finishing[1], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[1], self.speed[1], self.finishing[1], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[1], self.speed[0], self.finishing[0], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[0], self.speed[1], self.finishing[0], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[0], self.speed[0], self.finishing[1], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[1], self.speed[1], self.finishing[0], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[1], self.speed[0], self.finishing[1], self.overall[1], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[0], self.speed[1], self.finishing[1], self.overall[1], Fuzzy.Logic.AND))

        # Beginner (3 low, 1 medium or 4 low)
        self.rules.append(Fuzzy.Rule(self.ballControl[1], self.dribbling[0], self.speed[0], self.finishing[0], self.overall[0], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[1], self.speed[0], self.finishing[0], self.overall[0], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[0], self.speed[1], self.finishing[0], self.overall[0], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[0], self.speed[0], self.finishing[1], self.overall[0], Fuzzy.Logic.AND))
        self.rules.append(Fuzzy.Rule(self.ballControl[0], self.dribbling[0], self.speed[0], self.finishing[0], self.overall[0], Fuzzy.Logic.AND))

    def solve(self):
        numerator = 0
        denominator = 0
        for ovr in self.overall:
            print(ovr.name, " ", ovr.mi)
            numerator += ovr.mi * ovr.value
            denominator += ovr.mi

        solution = numerator / denominator
        return solution

    def get_predicted_class(self):
        return np.argmax(self.overall) + 1

        


