from konlpy import jvm
from konlpy.tag import Twitter
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Komoran

jvm.init_jvm()

########    use Twitter    ########
twitter = Twitter()

input_text = "한국어를 처리하는 예시입니다"
normalizations = twitter.phrases(input_text)
tokenizations = twitter.pos(input_text)

aftertokenization = twitter.pos(input_text, norm=True)

print('')
print('########    Twitter    ########')
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


########    use Kkma    ########
kkma = Kkma()

normalizations = kkma.morphs(input_text)
tokenizations = kkma.pos(input_text)

print('')
print('########    Kkma    ########')
print('')
print('normalization : ')
print(normalizations)
print('')
print('tokenization : ')
print(tokenizations)
print('')


########    use Hannanum    ########
hannanum = Hannanum()

normalizations = hannanum.morphs(input_text)
tokenizations = hannanum.pos(input_text)

print('')
print('########    Hannanum    ########')
print('')
print('normalization : ')
print(normalizations)
print('')
print('tokenization : ')
print(tokenizations)
print('')


########    use Komoran    ########
komoran = Komoran()

normalizations = komoran.morphs(input_text)
tokenizations = komoran.pos(input_text)

print('')
print('########    Komoran    ########')
print('')
print('normalization : ')
print(normalizations)
print('')
print('tokenization : ')
print(tokenizations)
print('')