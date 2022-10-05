import pandas as pd

words={'a':'사과','b':'키위','c':'당근'}
# print(words)

frequencys={'a':1,'b':2,'c':3}

prices={'a':10,'b':20,'c':30}

word =pd.Series(words)
# print(word)
frequency=pd.Series(frequencys)
# print(frequency)
price=pd.Series(prices)

summary =pd.DataFrame({
    'word':word,
    'frequency':frequency,
    'price':price,
})
# print(summary)
score=summary['frequency']*summary['price']
summary['score']=score
# print((score))
# print(summary)c

# 이름을 기준으로 슬라이싱
# print(summary.loc['b':'c','price':])

# 인덱스를 기준으로 슬라이싱
# print(summary.iloc[1:3,2:])

# csv로 저장
summary.to_csv("summary.csv",encoding='utf-8-sig')