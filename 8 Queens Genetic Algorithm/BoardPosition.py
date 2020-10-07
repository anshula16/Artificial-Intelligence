class BoardPosition:
    '''
    Class for different board positions and its corresponding fitness value and survival value.
    '''
    
    def __init__(self):
        self.sequence_of_queens = None
        self.fitness = None
        self.survival = None

    def setSequenceOfQueens(self, sequence_of_queens):
        self.sequence_of_queens = sequence_of_queens

    def setFitness(self, fitness):
        self.fitness = fitness

    def setSurvival(self, survival):
        self.survival = survival

    def getAttr(self):
        return {'sequence_of_queens' : self.sequence_of_queens, 'fitness' : self.fitness, 'survival' : self.survival}
