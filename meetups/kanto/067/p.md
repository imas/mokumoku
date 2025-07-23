###### tags: `checkin-out` `067`

# 067 Producers list

## .ごっち

### 担当

なぎです。ひろです。

### P業以外で普段やっていること

よいモニターを買った。

{%preview https://bsky.app/profile/yougoto.dev/post/3lse3w4wc7224 %}

### 今日やること

im@sparqlを自分でも動かしてみたい。Rust製のもので試してみる。
{%preview https://github.com/oxigraph/oxigraph/tree/main/cli#using-a-docker-image %}

Discordイベント作成時に誕生日のアイドルの取得に失敗したら `error` ではなく、それなりのテキストとしたい。
![image](https://hackmd.io/_uploads/SymsCL8Lgl.png)

### 今日の成果

サーバの起動はしたものの、データの読み込みができていなかった。（Gemini と格闘していた。）

![image](https://hackmd.io/_uploads/HkzE1uIIll.png)

おとなしくim@sparqlのREADMEに書かれている jena-fuseki でたてようと思ったところで時間切れ。

## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

怒涛のライブのあいまをぬって転職(?)とかしてました。多忙すぎ

### 今日やること

visionOS 26で、パフォーマンス上がるかもしれないAPIを、アイドルのカラー可視化のやつでやってみる
im@sparqlが動いてたら


### 今日の成果

im@sparql動いてなかったので、テストのためにRDFから名前とカラーを抜き出してハードコードした

https://github.com/banjun/IdolHue/commit/29375d6ef16ecb4c25c72b857852c0461feaf1f6#diff-c8fc9afa37e26a2e76f5e8520abe12e293f4b896c0ecfa590db4df6ff815167bR16

アイドルの数だけたくさん球を置くので、Meshの位置違いだから、インスタンスにすれば速くなるかもと思ったが...
https://developer.apple.com/documentation/realitykit/meshinstancescomponent

Entityを1個に束ねる仕組みらしく、マテリアルを変えられないから色を変えられなくて、不採用になった

しかたないので、普通にパフォーマンスのマシなマテリアルに変えるだけにした(Unlit)

hover effectをshaderでつけた

![image](https://hackmd.io/_uploads/HJhLfdLUll.png)

## あろー

### 担当
ほたたたた

### P業以外で普段やっていること
個人開発のサービスをつくったりつくらなかったりしてる

>https://x.com/_arrow2nd/status/1944264608208105653

### 今日やること
なんかめちゃめちゃ溜まってる renovate のPRを潰す

### 今日の成果

renovate のPR、そんなに溜まってなかった

- [:arrow_up: Update jest monorepo to v30 (major) by renovate\[bot\] · Pull Request #826 · arrow2nd/imas-palette](https://github.com/arrow2nd/imas-palette/pull/826)
    - toBeCalled が toHaveBeenCalled になってた
- [chore(deps): update dependency vite to v7 by renovate\[bot\] · Pull Request #379 · arrow2nd/imas-artwork-search](https://github.com/arrow2nd/imas-artwork-search/pull/379#issuecomment-3083833919)
    - vite-plugin-solid が vite 7 に未対応だったのでそっと閉じた

[display: 283;](https://display283.arrow2nd.com/) を Cloudflare Pages -> Workers に移行してみた
- Pagesのプロジェクト、デプロイが沢山あるとコンソールから消せなくてつらい 🥺
    - {%preview https://x.com/_arrow2nd/status/1945824892555022627 %}
