###### tags: `checkin-out` `041`

# 041 Producers List

## MH35

### 担当

担当？誰だったっけ…思い出せない

### P業以外で普段やっていること

Web系の開発

### 今日やること

シャニマスノウハウブック管理Webアプリケーションの実装

### 今日の成果

とりあえず作成画面まではつなぎこみ完了。編集画面作成中。それが終わったら並び替えの仕組み作って、APIのデータ投入したら、ひとまず完成か？

## .ごっち

### 担当

[久川凪](https://twitter.com/gggooottto/status/1620082740451504129?s=20)など

### P業以外で普段やっていること

[真冬にBBQ](https://twitter.com/gggooottto/status/1619187570868649985?s=20)を普段やっていない。

### 今日やること

- What3Idolsメンテ続き！
  - Nextjs 13のappDir対応をちまちまやっていく。
- 雑談ネタ: 今後のもくもく会のオンライン会場となるサービス検討

### 今日の成果

- とりあえず動いた。
  - `--turbo` は動かなかった。。
  - マージしたけどデプロイに失敗した。
    - Vercel側で設定していたNodeのバージョンが古かった。
    - 成功した！
  - React v18で[非推奨](https://github.com/reactjs/rfcs/blob/createlement-rfc/text/0000-create-element-changes.md#deprecate-defaultprops-on-function-components)となった `.defaultProps` がライブラリ側で使われているっぽいので、めっちゃwarningがでてつらい。
    - 開発も活発ではなさそうなので、もろもろ取り替えてもよさそうな感じがある。
      - https://github.com/couds/react-bulma-components
    - Bulma自体は活発なので、CSSの読み込みだけをやるようにしたほうがよさそうに見えた。

## あろー

### 担当

ほたほた

### P業以外で普段やっていること

- お引越しの準備をしています 📦
- Twitter の API に振り回されています……

### 今日やること

- シャニの衣装のやつを im@sparql に投げたいです
- idol-birthday のやつをやります
    - https://github.com/arrow2nd/idol-birthday/issues/58

### 今日の成果

- idol-birthday のやつは思ってたよりややこしそうだったので、見なかったことにしました…
- モノクロ/マテイク/ジルコン なのかな
    ![](https://i.imgur.com/j8l41y8.png)
    ![](https://i.imgur.com/5bFdcYd.png)
    絶対ちがう気がする……
- あさひ
    ![](https://i.imgur.com/HZJi7zE.png)
