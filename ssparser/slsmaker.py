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
        print('=' * 100)
        print ('start : make leaning data')

        if len(self.filePath) < 1:
            print ('input file path does not exist')
            return

        # log
        if self.isDebug == True:
            print ('start : category analize')

        fileDescriptor = open(self.filePath, mode='r', encoding='utf-8')
        stringArray = fileDescriptor.readlines()
        categoryArray = []
        titleArray = []
        for string in stringArray:
            firstSpaceLocation = string.find(' ')
            currentCategoryIndex = 0
            if firstSpaceLocation > -1:
                currentCategoryString = string[0:firstSpaceLocation]
                isNew = True
                replaceString = currentCategoryString + ' '
                for category in categoryArray:
                    if eq(category, currentCategoryString):
                        isNew = False
                if isNew == True:
                    categoryArray.append(currentCategoryString)
                    titleArray.append([])
                # category 분류 완료

                # 카테고리를 삭제한 제목만을 갖는 스트링 생성 - 쓸모없는 문자 삭제
                parsedString = string.replace(replaceString, '')
                parsedString = parsedString.replace('\n', '')

                # 삽입된 카테고리의 인덱스애 맞추어 titleArray 배열에 밀어넣기
                index = categoryArray.index(currentCategoryString)
                titleArray[index].append(parsedString)
        # 카테고리 분류 완료
        # 카테고리별 제목 배열 생성 완료

        # log
        if self.isDebug == True:
            print ('done : category analize')
            print (' find categories - ')
            print (categoryArray)

        # log
        if self.isDebug == True:
            print ('start : separate each word array')

        # word array 생성
        wordArray = []
        for array in titleArray:
            index = titleArray.index(array)
            # log
            if self.isDebug == True:
                print('\tstart stack words : ', index)
            wordArray.append([])
            for title in array:
                tempWordArray = title.split(' ')
                for word in tempWordArray:
                    isNew = True
                    if word in wordArray[index]:
                        isNew = False
                    if isNew == True:
                        wordArray[index].append(word)
            # log
            if self.isDebug == True:
                print('\tend stack words : ', index)
        # word Array 생성 완료

        # log
        if self.isDebug == True:
            print ('done : separate each word array')

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