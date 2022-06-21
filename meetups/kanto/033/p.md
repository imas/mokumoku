###### tags: `checkin-out` `033`

# 033 Producers List

## .ごっち

### 担当

久川姉妹はいいぞ :tada:

### P業以外で普段やっていること

きゅうりの収穫作業 https://twitter.com/gggooottto/status/1534881408896102400?s=20&t=PyCIzPu5Bamyo0AhpO_ZaQ

### 今日やること

- [What3Idols](https://what3idols.vercel.app)開発続きをします。
    - [前回](https://github.com/imas/mokumoku/blob/main/meetups/kanto/032/p.md#%E4%BB%8A%E6%97%A5%E3%81%AE%E6%88%90%E6%9E%9C)、データを再生成するために計算をしていた。
        - [アイドル名から緯度経度を検索できるようにしたい]([)](https://github.com/YutaGoto/what3idols/issues/62)
    - スクリプトを書いて40353264(4035万)行のCSVデータを作る（かもしれない）
        - GoogleBigQuery用のデータ
        - 直接データをいれることができればいいかもしれないが、、

### 今日の成果

- 3GBのCSVデータができあがった。。
    - スクリプトミスがあったので何回か実行した。
    - ![](https://i.imgur.com/xBtmhmx.png)
    - 次回までにBigQueryに反映させたいところ。
- im@sparqlのデータを眺めていたら施設データに346プロの建物データがなかったのでissueたてた
    - https://github.com/imas/imasparql/issues/508
- `stat` コマンドを知った

## ak_hina

### 担当
- ML
    - 望月杏奈
    - 七尾百合子
    - 永吉昴
    - 白石紬
- CG
    - 島村卯月
    - 姫川友紀
    - 乙倉悠貴
    - 大石泉
- SideM
    - 秋月涼
    - 水嶋咲
    - ピエール
    - 卯月巻緒
    - 神楽麗

### P業以外で普段やっていること
- プログラマ寄りのSE
    - 最近は Ruby やら VBA やら
- スポーツ観戦
    - 野球やらバスケやららサッカーやらいろいろ(ただし、贔屓の選手が出ていないので代表戦とかは見ない）
- コスプレ
    - https://twitter.com/i/events/1530879200210845696
    - KPT毎回ぶん回してるけどやるたびにメンタルが死んでるｗ
        - 何か感想ください

### 今日やること
- ラウンジサーバー向けのDiscord情報連携システムの整備
    - 現状:matsurihi.meからボーダー情報とアップデート情報を定期配信
        - https://api.matsurihi.me/docs/

### 今日の成果
- ラウンジサーバー向けのDiscord情報連携システムの整備
    - 配信情報の追加: 後半戦の日時情報の配信

## MH35

### 担当

最近はアルストロメリアとピコプラ

### P業以外で普段やっていること

Web系の開発

### 今日やること

im@sparqlに何か加える

### 今日の成果

- https://github.com/imas/imasparql/pull/507

## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

ピアノの練習にいきました
https://www.youtube.com/channel/UCVXYOHRKNis46SBM1sE30Yw
:チャンネル登録::高評価: :+1:
    登録と高評価しました :+1: / ak_hina

### 今日やること

betaではあるがXcode 14からSwift Chartsが使えるので、SwiftSparqlでim@sparqlにリクエストして返ってきたやつを、Swift Chartsに繋ぎこむ練習をしたい

### 今日の成果

betaなのでNDAからスクショは出せない。がコードは出していいはず。

https://github.com/banjun/IdolCharts つくった

![](https://i.imgur.com/BkWLFDa.png)


ついでに、そこから使うのに欲しかったのでSwiftSparqlをasync/awaitに対応した。(やりかけのを片付けた)

https://github.com/banjun/SwiftSparql/pull/38

こうつかえる

![](https://i.imgur.com/JICc9OL.png)
