import random
class BetterRandom:
    '''
        A random int generator
    '''
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def random_int(self):
        '''
            returns a random number
        '''
        return random.randint(self._start, self._end)
