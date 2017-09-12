from operator import eq

class slsmaker:
    def __init__(self):
        self.isDebug            = False
        self.makeLeaningData    = True
        self.leaningDataCount   = 100000
        self.category           = []
        self.sentences          = []
        self.filePath           = ''


    def writeLeaningData(self):
        # log
        if (self.isDebug == True):
            print('=' * 100)
            print ('start : make leaning data')

        # log
        if self.isDebug == True:
            print ('start : category analize')

        if len(self.filePath) < 1:
            print ('input file path does not exist')
            return

        fileDescriptor = open(self.filePath, mode='r', encoding='utf-8')
        stringArray = fileDescriptor.readlines()
        categoryArray = []
        for string in stringArray:
            firstSpaceLocation = string.find(' ')
            if firstSpaceLocation > -1:
                currentCategoryString = string[0:firstSpaceLocation]
                isNew = True
                for category in categoryArray:
                    if eq(category, currentCategoryString):
                        isNew = False
                if isNew == True:
                    categoryArray.append(currentCategoryString)

        # log
        if self.isDebug == True:
            print ('done : category analize')
            print (' find categories - ')
            print (categoryArray)

        # log
        if self.isDebug == True:
            print ('start : seperate each word array')

        # log
        if self.isDebug == True:
            print ('done : seperate each word array')

        # log
        if self.isDebug == True:
            print ('start : make each sentence')

        # log
        if self.isDebug == True:
            print ('done : make sentences')

        # log
        if self.isDebug == True:
            print ('done : make leaning data')
            print('=' * 100)