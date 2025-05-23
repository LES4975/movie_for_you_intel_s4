import pandas as pd
import re
from konlpy.tag import Okt

df = pd.read_csv('./cleaned_data/movie_reviews.csv')
df.info()
print(df.head())

#한글 데이터만 남겨서 문장 정리하기
okt = Okt()
cleaned_sentences = []
for review in df.reviews:
    review = re.sub('[^가-힣]', ' ', review)
    tokened_review = okt.pos(review, stem=True) # pos는 형태소와 형태소의 품사까지 구분하여 저장할 수 있게 해 준다.
    # print(tokened_review)
    df_token = pd.DataFrame(tokened_review, columns=['word', 'class'])
    df_token = df_token[(df_token['class'] == 'Noun') |
                        (df_token['class'] == 'Adjective') |
                        (df_token['class'] == 'Verb')] # 필요한 품사만 인덱싱
    # print(df_token)
    words = []
    for word in df_token.word:
        if 1 < len(word): # 2글자 이상의 형태소만 words에 추가한다
            words.append(word)
    cleaned_sentence = ' '.join(words)
    print(cleaned_sentence)
    cleaned_sentences.append(cleaned_sentence)


df['reviews'] = cleaned_sentences
df.dropna(inplace=True) # 결측치 제거
df.info()
df.head()

df.to_csv('./cleaned_data/cleaned_reviews.csv', index=False) # csv 파일로 저장