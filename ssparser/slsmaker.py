class slsmaker:
    def __init__(self):
        print('yeah!')
        self.isDebug            = False
        self.makeLeaningData    = True
        self.leaningDataCount   = 100000


    def writeLeaningData(self):
        # log
        if (self.isDebug == True):
            print('=' * 100)
            print ('start : make leaning data')

        # log
        if (self.isDebug == True):
            print ('start : seperate each word array')

        # log
        if (self.isDebug == True):
            print ('done : seperate each word array')

        # log
        if (self.isDebug == True):
            print ('start : make each sentence')

        # log
        if (self.isDebug == True):
            print ('done : make sentences')

        # log
        if (self.isDebug == True):
            print ('done : make leaning data')
            print('=' * 100)