# 040 Producers List

###### tags: `checkin-out` `040`

## .ごっち

### 担当

久川凪など

### P業以外で普段やっていること

[ポゴの時間だ](https://twitter.com/gggooottto/status/1613881669223874566?s=20&t=_pbbAiQbqYbmRjDYi4S3kg)！

### 今日やること

- connpassやKPTのテンプレを編集します。
- 時間が余れば What3Idolsメンテします。

### 今日の成果

- テンプレ更新のプルリクエストを作った
    - https://github.com/imas/mokumoku/pull/170
    - 今月の第3木曜日の日付を取得する計算が地味にややこしい。Python便利 :snake:
- What3IdolsにきてたDependabotのプルリクエストを片づけた（マージした）。
- Nextjs v13のappディレクトリにするやつ対応を始める。
    - 起動してページ表示まではうまくいったけども、GoogleMapsが表示されず次回以降に持ち越し
        - クライアントコンポーネントでごりごりやっているので、サーバコンポーネントに向かないというのは。。そう。。
        - めっちゃリファクタリングがいるかな。。 https://beta.nextjs.org/docs/getting-started
        - https://github.com/YutaGoto/what3idols/pull/257

## ak_hina

### 担当

- 望月杏奈 etc...

### P業以外で普段やっていること
- SE
- コスプレ
    - 付随タスク
        - ダイエット
        - スキンケア
- スポーツ応援

### 今日やること
- not コーラスパークル but アイマスパークル
    - SPARQL50本ノックを読みながら勉強します
        - https://blab.booth.pm/items/1172740
        - 少しづつノックを進めている
    - ミリオン関連のライブのrdfが書かれてないみたいだから書いたほうがいいのかな？
        - issuesみたら一応書かれては居るみたいだから手出しはやめておくか、反映されてないけど。よくよく見ると、Merging is blockedされてるんだけどなんでなの？
            - とりあえずslackに投げたのでクロミサさんあたりに対応してもらおうｗ
    - 可能なことなら、ラウンジLINEのbotに765+ミリの誕生日通知を盛り込みたいんだけど、GASにライブラリあんだろうか
        - GETかPOST投げてResponse帰ってくるんならありがたいけど、下記みたくできるんだろうか
            - https://data.e-stat.go.jp/lodw/sparqlendpoint/api
        - 要件
            - 明日が誕生日なら前日夕方の定時通知に記載
            - 当日が誕生日なら当日朝・昼・夕方の定時通知に記載

### 今日の成果

## あろー

### 担当

ほたほた

### P業以外で普段やっていること

- 物件の契約をしました 🏠

### 今日やること

 - 更新が入ったっぽいので im@sparql にシャニの衣装を投げたい
 - [idol-birthday](https://idol-birthday.vercel.app/) の改善もやりたい

### 今日の成果

- シャニの更新、明日でした…
- とりあえず今ある分を投げた!
    - https://github.com/imas/imasparql/pull/524
- URLをコピーするボタンが無かったので増やした
    - ![](https://i.imgur.com/6tzH9q9.png)
