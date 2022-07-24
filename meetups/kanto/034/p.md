###### tags: `checkin-out` `034`

# 034 Producers List

## .ごっち

### 担当

久川姉妹はいいぞ
デレステのイベントもよろしくおねがいします。

### P業以外で普段やっていること

connpassのイベント用画像を更新しました！
Twitterのスペース名 なんかいいの思いつきませんでした。

### 今日やること

- [What3Idols](https://what3idols.vercel.app)開発続きをします。
    - [前回](https://twitter.com/gggooottto/status/1537413467233087489?s=20&t=dan6lWJFDsSQE6Fk4CLhdA)、アイドルのCSVデータを作った。
    - もくもく会外でBigQueryにデータを入れるところまでやった。
        - ![](https://i.imgur.com/HtO695t.png)
    - アイドル名 <-> 緯度経度の処理を実際に書いていきます。
- react-hook-formへの置き換え作業を始める
    - https://react-hook-form.com

### 今日の成果

- できた :world_map:
    - https://twitter.com/gggooottto/status/1550081716487786496?s=20&t=dan6lWJFDsSQE6Fk4CLhdA
    - https://github.com/YutaGoto/what3idols/pull/214
    - deployしました https://what3idols.vercel.app/

## あろー

### 担当

ほたほた

### P業以外で普段やっていること

[TUIなTwitterクライアント](https://github.com/arrow2nd/nekome)をつくったりしてました 🐈

### 今日やること

- Deno の Web フレームワーク [fresh](https://fresh.deno.dev/) を使って、im@sparql のデータダッシュボード的なものをつくります

### 今日の成果

- たぶんうごいてます https://imasparql-data-dashboard.deno.dev/
    - ほんとはブランド毎の内訳みたいなのも出したかったけど、SPARQLのクエリが書けなかったのと、Node.jsじゃないのでライブラリを探すのが面倒でやめました...
- ついでに[シャニの新衣装を追加するPR](https://github.com/imas/imasparql/pull/511)もだしました

## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

チームトポロジーを読みはじめました。ガラにもなく。
ピアノの練習をつづけています。さいきん渋谷がおおい。

### 今日やること

先月のこれ https://github.com/banjun/IdolCharts
もうちょい試していきたい

### 今日の成果

Swift Chartsのbeta1でX軸のラベル回転機能が動いてなくて未実装かな?って1文字ずつ改行で疑似縦書きしてたけど、beta3では回転機能の度指定ができなくなって、90度ごとになってた。動いたけど、そんなんアリ?

```diff
-                        AxisValueLabel(text.reduce(into: "") {$0 += "\n" + String($1)}, collisionResolution: .greedy, orientation: .angle(.degrees(45)))
+                        AxisValueLabel(text, orientation: .vertical)
```

NDAによりスクショは貼れないのでコードだけだが、5ブランドのアイドルの背の順をSwift Chartで出せた

https://github.com/banjun/IdolCharts/commit/11e5a57875d6b9e1f938ba47a840df251157706d
