from operator import eq
import re
import os
import datetime

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
        if not os.path.exists('./output/dummy_last.txt'):
            return

        fileDescriptor = open('./output/dummy_last.txt', 'r', encoding='utf-8')
        array = fileDescriptor.readlines()
        
        newCategory = []
        for string in array:
            string = string.replace('\n', '')
            if len(string) > 1:
                newCategory.append(string)
        
        self.categoryArray = newCategory


    def writeDummyData (self):
        fileDescriptor = open('./output/dummy_last.txt', 'w', encoding='utf-8')
        writeFileString = ''
        
        for category in self.categoryArray:
            writeFileString += '\n' + category
        
        fileDescriptor.write(writeFileString)
        fileDescriptor.close()

        now = datetime.datetime.now()
        currentDate = now.strftime('%Y-%m-%d_%H:%M:%S')
        dummyFilePath = './output/dummy_' + currentDate + '.txt'
        fileDescriptor = open(dummyFilePath, 'w', encoding='utf-8')
        fileDescriptor.write(writeFileString)
        fileDescriptor.close


    def setFilePath (self, filePath):
        # log
        if self.isDebug == True:
            print("=" * 100)
            print("ssparser : set file path - " + filePath)

        fileDescriptor = open(filePath, mode='r', encoding='utf-8')

        self.prepareData = fileDescriptor.readlines()
        self.makePrepareData()

    
    def removeChar(self, originString, removalChar):
        while originString.find(removalChar) > 0:
            originString = originString.replace(removalChar, '')
        return originString

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
            string = self.removeChar(string, '\n')
            string = self.removeChar(string, 'ㆍ')
            string = self.removeChar(string, '‘')
            string = self.removeChar(string, '’')
            string = self.removeChar(string, '“')
            string = self.removeChar(string, '”')
            string = self.removeChar(string, '″')
            string = self.removeChar(string, '…')
            string = self.removeChar(string, '`')
            string = self.removeChar(string, '·')
            string = self.removeChar(string, '↑')
            string = self.removeChar(string, '→')
            string = self.removeChar(string, '↓')
            string = self.removeChar(string, '!')
            string = self.removeChar(string, '！')
            string = self.removeChar(string, '[')
            string = self.removeChar(string, ']')
            string = self.removeChar(string, '&amp;')
            string = self.removeChar(string, '&lt;')
            string = self.removeChar(string, '&gt;')
            string = self.removeChar(string, '″')
            string = self.removeChar(string, '，')
            parsedString = re.sub("""[()-+=.,#/?:$'"}]""", '', string)
            parsedString = parsedString.lstrip()

            newArray.append(parsedString)

        self.prepareData = newArray

        # log
        if self.isDebug:
            print('=' * 100)
            print('prepared data ready')
            print('=' * 100)

        self.clasifyString()


    def clasifyString (self):
        # TODO: load dummy data, 
        categoryArray = []

        self.loadDummyData()

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
        self.writeDummyData()

        #log
        if self.isDebug == True:
            print('=' * 100)
            print('sorted category : ') 
            print(len(self.categoryArray))
            print('=' * 100)

        self.makeYData()
        self.makeXData()


    def writeXData(self):
        fileDescriptor = open('./output/xData.txt', 'w', encoding='utf-8')
        writeFileString = ''
        writeFileString = '\n'.join(self.xData)
        fileDescriptor.write(writeFileString)
        fileDescriptor.close()

        # log
        if self.isDebug:
            print('=' * 100)
            print('x Data Write Done')
            print('=' * 100)


    def writeYData(self):
        fileDescriptor = open('./output/yData.txt', 'w', encoding='utf-8')
        writeFileString = ''
        for array in self.yData:
            writeFileString += '['
            seperator = ','
            writeFileString += seperator.join(str(integer) for integer in array)
            writeFileString += ']\n'
        fileDescriptor.write(writeFileString)
        fileDescriptor.close()
        
        # log
        if self.isDebug:
            print('=' * 100)
            print('y Data Write Done')
            print('=' * 100)


    def makeXData(self):
        # Make String Array ["asdfasdf asdf asdfasdfasdf", ...]
        returnArray = []
        for tempString in self.prepareData:
            firstSpaceLocation = tempString.find(' ')
            currentString = tempString[firstSpaceLocation+1 : len(tempString)]
            returnArray.append(currentString)

        self.xData = returnArray
        self.writeXData()

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
        self.writeYData()

        # log
        if (self.isDebug == True):
            print('=' * 100)
            print ('y data count : ')
            print (len(self.yData))
            print('=' * 100)