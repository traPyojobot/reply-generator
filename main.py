import csv
import re
import neologdn
import emoji
import random


data = []

with open('conv_tweet.tsv', encoding='utf-8', newline='') as f:
    for cols in csv.reader(f, delimiter='\t'):
        if cols != ['src', 'rep']:
            data.append(cols)


# 参考 : https://ohke.hateblo.jp/entry/2019/02/09/141500

def preprocessing(text: str) -> str:
    # メンション除去
    text = re.sub(r'@[a-zA-Z0-9_]+', '', text)
    # リンク除去
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)
    # 絵文字除去
    text = ''.join(['' if c in emoji.UNICODE_EMOJI["en"] else c for c in text])
    # いい感じな正規化
    text = neologdn.normalize(text)
    return text


for d in data:
    for i in range(len(d)):
        d[i] = preprocessing(d[i])

print(data[random.randrange(len(data))][1])
