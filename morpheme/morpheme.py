# from data import *
# from textcnn import TextCNN
# import tensorflow as tf
# import numpy as np
from konlpy import jvm
from konlpy.tag import Twitter

# jvm.init_jvm()
pos_tagger = Twitter("/System/Library/Frameworks/JavaVM.framework/Versions/A/Commands/java")

input_text = "한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ"
normalizations = pos_tagger.phrases(input_text)
tokenizations = pos_tagger.pos(input_text)

aftertokenization = pos_tagger.pos(input_text, norm=True)

print('')
print('normalization : ')
print(normalizations)
print('')
print('tokenization : ')
print(tokenizations)
print('')
print('tokenization after normalization : ')
print(aftertokenization)
print('')
