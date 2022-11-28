class Service:
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    def getName(self):
        return self.__name

    def getCost(self):
        return self.__cost
