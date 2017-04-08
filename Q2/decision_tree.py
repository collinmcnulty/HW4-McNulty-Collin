from util import entropy, information_gain, partition_classes


class DecisionTree(object):
    def __init__(self):
        self.tree = {}

    def learn(self, X, y):
        # TODO: train decision tree and store it in self.tree
        pass

    def classify(self, record):
        # TODO: return predicted label for a single record using self.tree
