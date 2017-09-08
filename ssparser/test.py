import ssparser
import os

parser = ssparser.ssparser()
parser.isDebug = True


currentPath = os.getcwd()
stringData = open('./data_set/naver_crawler.txt', mode='r', encoding='utf-8')

parser.setFilePath('./data_set/naver_crawler.txt')

