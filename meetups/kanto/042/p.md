###### tags: `checkin-out` `042`

# 042 Producers List

## .ごっち

### 担当

[久川凪](https://twitter.com/gggooottto/status/1620082740451504129?s=20)など

### P業以外で普段やっていること

[線路を敷く](https://twitter.com/gggooottto/status/1629095729099841537?s=20)

### 今日やること

- What3Idolsメンテ続き
  - react bulma componentを剥がして、bulmaを取り込む
    - https://github.com/YutaGoto/what3idols/issues/277

### 今日の成果

- 進捗なにもない
- Bulmaのコンポーネントをちまちま作ってたけど、[本家](https://github.com/couds/react-bulma-components)にPRを送ったほうが早い説。
  - 大変だけど。
  - リポジトリが動いているか怪しいけど。
  - イメージ: https://github.com/chakra-ui/chakra-ui/pull/7068
- 乗り換え先としてant-designも考えたけど、Nextjsでlessを扱うのかなり面倒だった記憶があるので躊躇してしまう。
- https://evergreen.segment.com/, https://arco.design/en-US 気になる。
- おとなしくtailwindで自作してくださいという話になるかもしれない。

## MH35

### 担当

最近はアルストロメリアとストレイライト

### P業以外で普段やっていること

Web開発

### 今日やること

例のノウハウマネージャをもう少しまともに使えるようにしたい(例えば特定のノウハウが入ったブックを検索するとか)

### 今日の成果

検索画面がある程度めどが立った。動線も考えないと

## あろー

### 担当

ほたほた

### P業以外で普段やっていること

引っ越しの 📦 をまとめています……

### 今日やること

- yarn を使ってるプロジェクトを pnpm に移行します
- パッケージの自動更新を depfu から Renovate に切り替えたい……

### 今日の成果

- [pnpm に移行した！](https://github.com/arrow2nd/imas-palette/pull/154)
    - ディスクがちょっと空いて install も速くなったので嬉しい 🐱
    - pnpm だと動かないパッケージもあるとの噂を聞いたので様子を見ていきたい (Storybook とか動かないらしい)
- [Renovate も導入した](https://github.com/arrow2nd/imas-palette/pull/155)
    - ![](https://i.imgur.com/4BVlW7n.png)
    - 依存パッケージ以外に Actions の更新もしてくれるのとても嬉しい
