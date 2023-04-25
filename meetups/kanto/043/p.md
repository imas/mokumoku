###### tags: `checkin-out` `043`

# 043 Producers List

## .ごっち

### 担当

久川凪など

### P業以外で普段やっていること

[山登り](https://twitter.com/gggooottto/status/1643955076736876544?s=20)と[pnpm](https://twitter.com/gggooottto/status/1647590541612425217?s=20)を始めた。

### 今日やること

- What3Idolsメンテ続き
  - bulmaを剥がして[Evergreen](https://evergreen.segment.com/)に乗り換える
      - https://github.com/YutaGoto/what3idols/issues/305
  - Nodejs v20にアップグレードする
      - Vercelが対応していなかったら また次回
  - 時間が余ったらCI/CDを[Cicada](https://cicada.build/)にしてみる

### 今日の成果

- DependabotのPullRequestsを片付ける。
- UIの乗り換えが大変すぎる。。
    - https://github.com/YutaGoto/what3idols/pull/325
    - ![](https://user-images.githubusercontent.com/12590762/233366686-e082f1fd-c8b6-4bf9-bcf7-67da73699cf4.png)
    - 見た目を整える調整は割とかかりそうなので、もくもく会外でやるかもしれない。

## 導線

### 担当

P.C.S, かな子, 法子, サンノス

### P業以外で普段やっていること

-   情報系の某研究員（副業）
-   旅行
-   など

### 今日やること

デレステのセレクトショップ衣装について、着られるアイドルのデータまとめ＆図表化。
データは https://gamerch.com/imascg-slstage-wiki/entry/521537 より。
参考: https://twitter.com/dousenP/status/1648635525711167495

単に表にするだけならすぐ終わるが、綺麗に見えるように表示順などを決めたい。

-   参考になるかもしれないしならないかもしれない：
    -   決定木 - Wikipedia https://ja.wikipedia.org/wiki/%E6%B1%BA%E5%AE%9A%E6%9C%A8
    -   集合被覆問題 - Wikipedia https://ja.wikipedia.org/wiki/%E9%9B%86%E5%90%88%E8%A2%AB%E8%A6%86%E5%95%8F%E9%A1%8C

### 今日の成果

-   その衣装が着られる/着られない情報をもとに、「アイドルを確実に分類できる」関係性を出力できるようにした。
    -   例えば、「“オトナのアーバンカジュアル”が着られる」「“スキあり☆スウェットワンピ”が着られる」「“ドリーミーリボンサロペット”が着られる」アイドルは、一切重複がない。
-   このような関係を一度計算し、最終的には図表まで持っていきたい

## あろー

### 担当

ほたたほた

### P業以外で普段やっていること

- みならいフロントエンジニャ🐾 になりました

### 今日やること

- 斑鳩ルカさんがアイドル名鑑に追加されていたので、im@sparql に追加します
- そろそろ ShinyPoems を App ディレクトリに移行したいです (Next.js)

### 今日の成果

- [ルカさんのプロフィールを更新しました](https://github.com/imas/imasparql/pull/535)
    - 左利きらしい。なるほど……
- Next.js の App ディレクトリ移行大変すぎる
    - なんもわからん
    - 他の方の移行ブログで `next/head` の代わりに `app/head.tsx` を使うらしいと聞いたと思ったら、なんかもう非推奨になったらしく[廃止](https://beta.nextjs.org/docs/api-reference/file-conventions/head)されてた。はやい
