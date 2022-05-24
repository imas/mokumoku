###### tags: `checkin-out` `032`

# 032 Producers List

## .ごっち

### 担当

なぎなぎ

### P業以外で普段やっていること

- コードを書いて戦わたりしています。
    - https://twitter.com/gggooottto/status/1513138526140846082?s=20&t=Bn7IA-JyacaXMtqZsYo_zQ
    - https://twitter.com/gggooottto/status/1522625363091677184?s=20&t=kwc2q4Fxlf0YrceUSh8Y3A
    - https://store.steampowered.com/app/1137320/Screeps_Arena/

### 今日やること

- [What3Idols](https://what3idols.vercel.app)開発続きをします。
    - [前回](https://twitter.com/gggooottto/status/1514567992612335616?s=20&t=kkII39qsLvZLsFH4rVmViw)は突貫で404ページを作りました。
        - https://what3idols.vercel.app/404
    - 現状 雑にIDを割り当てた値から緯度経度を特定させているので、アイドル名（文字列）から緯度経度を割り出せるようにしたい。
        - https://github.com/YutaGoto/what3idols/issues/62
        - データを作り直すところから始まる予定。

### 今日の成果

- データ挿入用CSVファイルを作るための準備をしていた。
    - 南北、東西にそれぞれ何分割すればよいか。。。。。
- 順列にすると4035万行(344 P 3)になるので、それでよさそう。。？？
- `40353264` をいい感じに2数に分解できないか解いてた。
    - `x * y == 40353264 が成立して、 x + y が最小となるx,yは？`してた
        - パッと解き方が思いつかなかったのが悲しい。。
    - 6321 * 6384
- 南北に6321分割、東西に6384分割すればよい。

## あろー

### 担当

ほたほた

### P業以外で普段やっていること

[denoくんを伸ばしたりしていました](https://github.com/arrow2nd/longdeno)

### 今日やること

- [idol-rdf-maker](https://github.com/arrow2nd/idol-rdf-maker) に CD のデータを作成するコマンドを追加します
    - データの形は [このPR](https://github.com/imas/imasparql/pull/502/files) を参考にしたい
    - まだ提案段階とのことなので、なんかそれっぽいのが出力されるようにする（？）

### 今日の成果

![](https://i.imgur.com/iJ3FeeF.png)
- トラック情報を除くデータの雛形が出力できるようになった 💿
- アイマスのCD、意外と色んなパターンがあるので「思ってたより複雑なのでは...？」になった
- RDFなにもわからないので、見たことない語彙をぽちぽち調べるなどしました
