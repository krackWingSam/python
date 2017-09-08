from operator import eq
import re
import os

class ssparser:
    def __init__(self):
        self.filePath = ''
        self.prepareData = []
        self.categoryArray = []
        self.xData = []
        self.yData = []
        self.dummyYData = []
        self.isDebug = False

    def loadDummyData (self):
        # TODO: 이전에 기록되어있던 yData 를 가져와 순차적으로 추가.
        currentPath = os.getcwd()

    def setFilePath (self, filePath):
        fileDescriptor = open(filePath, mode='r', encoding='utf-8')
        self.prepareData = fileDescriptor.readlines()
        self.makePrepareData()

    def makePrepareData (self):
        if self.prepareData.count == 1:
            return
        
        newArray = []
        for string in self.prepareData:
            # remove fake data
            if len(string) < 1:
                continue
            # remvoe fake data end

            # 유니코드에 포함되는 특수문자의 경우 while 을 이용하여 내부 처리하는 로직이 필요.
            string = string.lower()
            string = string.replace('\n', '')
            string = string.replace('ㆍ', '')
            string = string.replace('‘', '')
            string = string.replace('’', '')
            string = string.replace('“', '')
            string = string.replace('”', '')
            parsedString = re.sub("""[-+=.,#/?:$'"}]""", '', string)

            newArray.append(parsedString)

        self.prepareData = newArray

        # log
        if self.isDebug:
            print('=' * 100)
            print('prepare data : ')
            # print(self.prepareData)
            print('=' * 100)

        self.clasifyString()

    def clasifyString (self):
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
            print(len(self.categoryArray))
            print('=' * 100)

        self.makeYData()
        self.makeXData()

    def makeXData(self):
        # Make String Array ["asdfasdf asdf asdfasdfasdf", ...]
        returnArray = []
        for tempString in self.prepareData:
            firstSpaceLocation = tempString.find(' ')
            currentString = tempString[firstSpaceLocation+1 : len(tempString)]
            returnArray.append(currentString)

        self.xData = returnArray

        # log
        if (self.isDebug == True):
            print('=' * 100)
            print('x data count : ')
            print(len(self.xData))
            print('=' * 100)

    def makeYData(self):
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


        self.yData = returnArray

        # log
        if (self.isDebug == True):
            print('=' * 100)
            print ('y data count : ')
            print (len(self.yData))
            print('=' * 100)