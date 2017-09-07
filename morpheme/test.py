#-*-coding: utf-8
import numpy as np

data = open('./data_set/naver_crawler.txt', mode='r', encoding='utf-8')
# data = np.genfromtxt('./data_set/naver_crawler.txt', 'r')

string = data.readline()

print(string)