import ssparser
import slsmaker

# parser = ssparser.ssparser()
# parser.isDebug = True
# parser.setFilePath('./data_set/naver_crawler.txt')

maker = slsmaker.slsmaker()
maker.isDebug = True
maker.leaningDataCount = 100
maker.filePath = './output/data.txt'
maker.writeLeaningData()