from operator import eq

class ssparser:
    def __init__(self):
        self.prepareData = []
        self.categoryArray = []
        self.xData = []
        self.yData = []
        self.isDebug = False


    def setString (self, string):
        self.originString = string.lower()
        self.prepareData = self.originString.split('\n')

        if self.isDebug == True:
            print('=' * 100)
            print('prepare data : ')
            print(self.prepareData)
            print('=' * 100)

        spaceLocation = self.originString.find(' ')


        #remove dummy 
        for tempString in self.prepareData:
            if len(tempString) < 1:
                self.prepareData.remove(tempString)
        #remove dummy end


        categoryArray = []        
        for tempString in self.prepareData:
            firstSpaceLocation = tempString.find(' ')
            currentCategoryString = tempString[0:firstSpaceLocation]

            firstSpaceLocation = tempString.find(' ')
            currentCategoryString = tempString[0:firstSpaceLocation]

            # Find category / Sort
            if len(categoryArray) == 0:
                categoryArray.append(currentCategoryString)
            else:
                isExistCategory = False
                for category in categoryArray:
                    if eq(category, currentCategoryString):
                        isExistCategory = True
                
                if isExistCategory == False:
                    categoryArray.append(currentCategoryString)
            # Find Category / Sort End

    
        self.categoryArray = categoryArray

        #log
        if self.isDebug == True:
            print('=' * 100)
            print('sorted category : ') 
            print(self.categoryArray)
            print('=' * 100)

    def getXData(self):
        # Make String Array ["asdfasdf asdf asdfasdfasdf", ...]
        returnArray = []
        for tempString in self.prepareData:
            firstSpaceLocation = tempString.find(' ')
            currentString = tempString[firstSpaceLocation+1 : len(tempString)]
            returnArray.append(currentString)

        self.xData = returnArray

        if (self.isDebug == True):
            print('=' * 100)
            print('sorted category : ') 
            print(self.xData)
            print('=' * 100)

        return self.xData


    def getYData(self):
        # Make Category Index Array ex) [0, 0, 0, 1, 0, 0, 0, ...]
        returnArray = []
        for tempString in self.prepareData:
            i = 0
            currentCategoryIndexArray = []

            #get category string
            firstSpaceLocation = tempString.find(' ')
            currentCategoryString = tempString[0:firstSpaceLocation]

            currentCategoryIndex = self.categoryArray.index(currentCategoryString)
            currentString = tempString[firstSpaceLocation+1:len(tempString)]

            while i < len(self.categoryArray):
                if i == currentCategoryIndex :
                    currentCategoryIndexArray.append(1)
                else :
                    currentCategoryIndexArray.append(0)
                i += 1

            returnArray.append(currentCategoryIndexArray)
        
            if self.isDebug:
                print(currentCategoryIndexArray)

        return returnArray