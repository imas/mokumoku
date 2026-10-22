###### tags: `checkin-out` `080`

# 080 Producers list

## .ごっち

### 担当

なぎです。ひろです。さきです。

### P業以外で普段やっていること

北海道帰省したついでに鹿追にいった。大雨だった。

{%preview https://x.com/gggooottto/status/2104476794082726310?s=20 %}

### 今日やること

(discord bot関連)[DenoがCloudflareに吸収される](https://deno.com/blog/cloudflare)にあたり、denoやdeno関連のサービスの開発が終了するので、移行先を考えたい。たぶんTSとCloudflare Workerになると思う。
discord botの整備のつづき

### 今日の成果

古いDeno Deployのアクションが居座ってたので消した。GitHub Copilotに手伝ってもらった。 https://github.com/YutaGoto/imas-mokumoku-create-discord-event/pull/21
https://github.com/denoland/deployctl
亜紗里先生BOTに対して `/ping` コマンドを打てるようにした。実行した日に誕生日のアイドルがいないと500エラーになるので、次回以降修正する。。

## 導線

### 担当

- （今月誕生日だと）椎名法子

### P業以外で普段やっていること

- 最近は副業で、プログラム書くよりも文章書くほうが多いかも…

### 今日やること

- [第75回](https://hackmd.io/giDwadtfRZWw3wO-LWvnUg)の続き
  - シンデレラガールズのアイドルの「属性と年齢だけが書かれた」カードでのゲーム
  - 特殊カード（「番号を+1する」などを持ったカード）を実装したとき、それをうまく扱えるCPUを実装する

https://www.slideshare.net/slideshow/2024-8a36/272388731

### 今日の成果

- 実装してみたら、前回の実装の不備に気づいたので、次回はだいぶ実装を見直す必要がありそう
  - 具体的には、どのカードをユニットとして出すかを保存する配列に「カードの内容そのもの」を突っ込んでいたのだが、
    カードのIDも入れておかないと「（使ったので）手札から外す」って処理が書けないと気付いた
  - これデータのリレーションをちゃんと定義すべきかもしれない…
