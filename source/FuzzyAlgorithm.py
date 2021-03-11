import numpy as np
from Fuzzy import MFInput, MFOutput, Rule, Logic


class FuzzyAlgorithm:

    def __init__(self, bc, dr, sp, fi):
        self.ball_control = []
        self.set_ball_control(bc)
        self.dribbling = []
        self.set_dribbling(dr)
        self.speed = []
        self.set_speed(sp)
        self.finishing = []
        self.set_finishing(fi)

        self.overall = []
        self.set_overall()

        self.rules = []
        self.set_rules()

    def set_ball_control(self, bc):
        self.ball_control.append(MFInput("Low", [56, 68], [1, 0], bc))
        self.ball_control.append(MFInput("Medium", [56, 68, 74, 80], [0, 1, 1, 0], bc))
        self.ball_control.append(MFInput("High", [74, 80], [0, 1], bc))

    def set_dribbling(self, dr):
        self.dribbling.append(MFInput("Low", [62, 73], [1, 0], dr))
        self.dribbling.append(MFInput("Medium", [62, 73, 79, 85], [0, 1, 1, 0], dr))
        self.dribbling.append(MFInput("High", [79, 85], [0, 1], dr))

    def set_speed(self, sp):
        self.speed.append(MFInput("Low", [56, 71], [1, 0], sp))
        self.speed.append(MFInput("Medium", [56, 71, 78, 84], [0, 1, 1, 0], sp))
        self.speed.append(MFInput("High", [78, 84], [0, 1], sp))

    def set_finishing(self, fi):
        # self.finishing.append(MFInput("Low", [60, 72], [1, 0], fi))
        # self.finishing.append(MFInput("Medium", [60, 72, 78, 83], [0, 1, 1, 0], fi))
        # self.finishing.append(MFInput("High", [78, 83], [0, 1], fi))
        self.finishing.append(MFInput("Very bad", [50, 52], [1, 0], fi))
        self.finishing.append(MFInput("Bad", [52, 57, 62, 67], [0, 1, 1, 0], fi))
        self.finishing.append(MFInput("OK", [62, 67, 72, 77], [0, 1, 1, 0], fi))
        self.finishing.append(MFInput("Good", [72, 77, 82, 87], [0, 1, 1, 0], fi))
        self.finishing.append(MFInput("Very good", [82, 87], [0, 1], fi))

    def set_overall(self):
        self.overall.append(MFOutput("Beginner", [40, 51], [1, 0]))
        self.overall.append(MFOutput("Amateur", [39, 54, 60, 66], [0, 1, 1, 0]))
        self.overall.append(MFOutput("Semi-pro", [60, 66, 71, 76], [0, 1, 1, 0]))
        self.overall.append(MFOutput("Professional", [71, 76, 83, 87], [0, 1, 1, 0]))
        self.overall.append(MFOutput("World Class", [83, 87], [0, 1]))
    '''
    def set_rules(self):
        logic = Logic.AND

        # World class
        # 4 high
        # 3 high, 1 medium
        # 2 high, 2 medium
        goal = self.overall[4]
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[1], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[2], self.finishing[1], goal, logic))

        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[1], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[2], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[1], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[2], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[1], self.finishing[1], goal, logic))

        # Professional
        # 1 low, 3 high
        # 1 high, 3 medium
        # 2 high, 1 medium, 1 low
        goal = self.overall[3]
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[2], self.finishing[0], goal, logic))

        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[1], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[1], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[2], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[1], self.finishing[2], goal, logic))

        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[2], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[1], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[1], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[2], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[2], self.finishing[2], goal, logic))

        # Semi-pro
        # 4 medium
        # 2 low, 2 high
        # 1 high, 1 low, 2 medium
        goal = self.overall[2]

        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[1], self.finishing[1], goal, logic))

        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[0], self.finishing[0], goal, logic))

        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[1], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[2], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[1], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[1], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[2], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[1], self.finishing[2], goal, logic))

        # Amateur
        # 3 medium, 1 low
        # 2 medium, 2 low
        # 3 low, 1 high
        # 2 low, 1 medium, 1 high
        goal = self.overall[1]
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[1], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[1], self.finishing[1], goal, logic))

        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[0], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[1], self.finishing[1], goal, logic))

        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[0], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[0], self.finishing[0], goal, logic))

        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[1], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[2], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[0], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[0], self.finishing[0], goal, logic))

        # Beginner
        # 4 low
        # 3 low, 1 medium
        goal = self.overall[0]
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[0], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[0], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[0], self.finishing[0], goal, logic))
        '''

    def set_rules(self):
        logic = Logic.AND

        # World class
        goal = self.overall[4]
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[2], self.finishing[4], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[1], self.finishing[4], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[2], self.finishing[3], goal, logic))

        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[2], self.finishing[4], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[2], self.speed[1], self.finishing[4], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[1], self.finishing[4], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[2], self.finishing[3], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[1], self.finishing[3], goal, logic))

        # Professional
        goal = self.overall[3]
        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[2], self.finishing[2], goal, logic))

        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[1], self.finishing[3], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[2], self.finishing[3], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[1], self.finishing[4], goal, logic))

        self.rules.append(Rule(self.ball_control[2], self.dribbling[2], self.speed[1], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[2], self.finishing[3], goal, logic))

        # Semi-pro
        goal = self.overall[2]

        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[1], self.finishing[2], goal, logic))

        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[2], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[0], self.finishing[2], goal, logic))

        self.rules.append(Rule(self.ball_control[2], self.dribbling[1], self.speed[1], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[2], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[0], self.finishing[3], goal, logic))
        self.rules.append(Rule(self.ball_control[2], self.dribbling[0], self.speed[1], self.finishing[3], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[1], self.finishing[3], goal, logic))

        # Amateur
        goal = self.overall[1]
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[1], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[0], self.finishing[2], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[1], self.finishing[2], goal, logic))

        self.rules.append(Rule(self.ball_control[1], self.dribbling[1], self.speed[0], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[1], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[0], self.finishing[2], goal, logic))

        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[1], self.speed[2], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[2], self.finishing[1], goal, logic))

        # Beginner
        goal = self.overall[0]
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[0], self.finishing[0], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[1], self.finishing[0], goal, logic))

        self.rules.append(Rule(self.ball_control[1], self.dribbling[0], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[1], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[0], self.finishing[1], goal, logic))
        self.rules.append(Rule(self.ball_control[0], self.dribbling[0], self.speed[0], self.finishing[1], goal, logic))

    def solve(self):
        numerator = 0
        denominator = 0
        for ovr in self.overall:
            numerator += ovr.mi * ovr.value
            denominator += ovr.mi

        solution = numerator / denominator
        return solution

    def get_predicted_class(self):
        return np.argmax(self.overall) + 1
