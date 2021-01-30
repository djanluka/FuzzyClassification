from enum import Enum, unique


class MFInput:

    def __init__(self, name, x, y, x0):
        self.name = name
        self.points = [(x[i], y[i]) for i in range(len(x))]
        self.mi = self.get_mi(x0)

    def __lt__(self, other):
        return self.mi < other.mi

    @staticmethod
    def get_y(x1, y1, x2, y2, x0):
        if y1 == y2:
            return y1
        if y1 < y2:
            return (x0 - x1) / (x2 - x1)
        else:
            return (x2 - x0) / (x2 - x1)

    def get_mi(self, x0):
        if x0 <= self.points[0][0]:
            return self.points[0][1]
        if x0 >= self.points[-1][0]:
            return self.points[-1][1]
        for i in range(1, len(self.points)):
            x1 = self.points[i - 1][0]
            x2 = self.points[i][0]
            if x1 <= x0 < x2:
                y1 = self.points[i - 1][1]
                y2 = self.points[i][1]
                return self.get_y(x1, y1, x2, y2, x0)


class MFOutput:

    def __init__(self, name, x, y):
        self.name = name
        sum_x = 0
        nb1 = 0
        self.points = []
        for i in range(len(x)):
            self.points.append((x[i], y[i]))
            if y[i] == 1:
                sum_x += x[i]
                nb1 += 1
        self.mi = 0
        self.value = sum_x / nb1

    def __lt__(self, other):
        return self.mi < other.mi


@unique
class Logic(Enum):
    OR = 0
    AND = 1


class Rule:
    def __init__(self, input1, input2, input3, input4, output, logic):

        self.inputArray = []
        self.inputArray.append(input1)
        self.inputArray.append(input2)
        self.inputArray.append(input3)
        self.inputArray.append(input4)
        self.output = output

        if logic == Logic.OR:
            max_i = input1.mi
            for i in range(1, 4):
                max_i = max(max_i, self.inputArray[i].mi)
            self.output.mi = max(self.output.mi, max_i)
        else:
            min_i = input1.mi
            for i in range(1, 4):
                min_i = min(min_i, self.inputArray[i].mi)
            self.output.mi = max(self.output.mi, min_i)
