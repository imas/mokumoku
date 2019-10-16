# カズキック2

## 担当

入門者です！何卒お教えくださいませ...

## P業以外で普段やっていること

新規事業開発でエンジニアをしています。昨日スムージー屋になりました。

## 今日やること

- プリメイド AI のマスタースレーブを準備してから何かしようと思っていたのですが、準備が間に合わず。。申し訳ない。。
- 過去のハッカソンネタを参考にしながら im@sparql の使い方を理解して何かします。

## 今日の成果

im@sparql を利用したパスワード生成スクリプトの設計だけ！

```
#!/bin/bash

# JPCERT/CC 曰く、「つよいパスワードとは」
# □ パスワードの文字列は、長めにする（12文字以上を推奨）
# □ インターネットサービスで利用できる様々な文字種（大小英字、数字、記号）を組み合わせると、より強固になる
# □ 推測されやすい単語、生年月日、数字、キーボードの配列順などの単純な文字の並びやログインIDは避ける
# □ 他のサービスで使用しているパスワードは使用しない

# im@sparql を利用してこれを実現しようという企み

# ランダムでローマ字表記の名前を取得
SPURL="https://sparql.crssnky.xyz/spql/imas/query?output=json&force-accept=text%2Fplain&query=PREFIX%20schema%3A%20%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX%20imas%3A%20%3Chttps%3A%2F%2Fsparql.crssnky.xyz%2Fimasrdf%2FURIs%2Fimas-schema.ttl%23%3E%0ASELECT%20%3Fo%20%3Fh%0AWHERE%20%7B%0A%20%20%3Fs%20schema%3Aname%7Cschema%3AalternateName%20%3Fo%3B%0A%20%20%20%20%20schema%3Aheight%20%3Fh.%0A%7Dorder%20by%20rand()"
curl -s $SPURL | jq ".results.bindings[]"

# ランダムで生年月日を取得
# ランダムで身長情報を取得
# 連結する
# option -v で母音を抜く
# https://password.kaspersky.com/jp/ の強度を図る
```
