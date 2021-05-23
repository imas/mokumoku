###### tags: `checkin-out` `020`

# 020 Producers List

## .ごっち

今日は自宅からお届けします。先月は変なホテルから参加しました。

### 担当

[限定ウサミン](https://twitter.com/gggooottto/status/1393937322496782337?s=20)引けました。めでたい。

### P業以外で普段やっていること

MinecraftのサーバをGCP上に建てました。

### 今日やること

- What3Idols開発続きをする。
  - 緯度経度からアイドルの組み合わせをだしたい。
  - [前回](https://twitter.com/gggooottto/status/1382674384104554500?s=20)作ったけど、直したい部分があるので修正してこのもくもく会中にリリースしたい。

### 今日の成果

- GoogleMap上をタップするとアイドルが表示されるやつをリリースした！
    - https://twitter.com/gggooottto/status/1395361905103966208?s=20
    - https://what3idols.vercel.app/maps
- ついでにスマホ対応した


## 導線

### 担当

メイン担当は島村卯月ですが、総選挙的には小日向美穂、VIAでは矢口美羽をメインに支援してました。今は三村かな子担当モード（デレステのイベント始まったし）

### P業以外で普段やっていること

アルゴリズム作ったりしてる某研究員

### 今日やること

デレステの楽曲情報をまとめる。特に歌唱メンバーとMV出演メンバー。

その後、それらの統計を取ったりしたい

### 今日の成果

-   過去に書いたもの（このときはMVの人数を調べるだけだった）: [「MVが3人な曲の一覧」って取得できます?（デレステ・ミリシタ・エムステ）](https://www.slideshare.net/maraigue/mv3-153914414)
-   https://imascg-slstage-wiki.gamerch.com/MV%E4%B8%80%E8%A6%A7 を見れば、MVオリジナル編成はだいたいわかる。ただデータとして打ち込むには手でのチェックは必要
-   あと、歌唱メンバーも直接引っ張ってくるのは難しいかも
-   デレステのMVオリジナルメンバーを調べるのに案外沼がある?
    -   例：YPT（イベント版とオリジナル版でメンバーが異なる。しかもイベント期間外は、デレステで機械的に調べられるのはオリジナル版だけ）
-   先の目標：例えば「【アイドル名】と一緒に曲をよく歌っているのは【アイドル名】」とかが計算できるようになりたい
    -   もともとのモチベ: https://twitter.com/dousenP/status/1223666156453548032

> 導線さんはTwitterを使っています 「用あって、デレステで以下の条件で曲を集めている ・卯月が歌っているが ・ソロは除外 ・P.C.Sも除外 ・ニュージェネが揃う曲も除外」


## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

副業先で勉強会をやるときに欄外に書くポエムを考えてる https://imastodon.net/@banjun/106266355911726675

<iframe src="https://imastodon.net/@banjun/106266355911726675/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" allowfullscreen="allowfullscreen"></iframe><script src="https://imastodon.net/embed.js" async="async"></script>

### 今日やること

im@sparqlから引いてきた色を、macOSの標準のカラーピッカーで使えるようにしたい。誰かやってそうな気もする

### 今日の成果

#### 調査

このへんが参考になる https://github.com/johnyanarella/MaterialDesignColorPicker 

が、そもそも、color list (~/Library/Colors/....cls) をつくるか、 color picker (~/Library/ColorPickers/...colorPicker) をつくるか、の2通りがありそう。

clsはこのへんか https://github.com/ramonpoca/ColorTools

#### できた！

https://github.com/banjun/colorlist-imasparql

![](https://i.imgur.com/3f2nm2n.png)


## MH35

### 担当

第10回CG総選挙は薫に、第2回VIAは舞に投票しました

### P業以外で普段やっていること

各種Webアプリケーションの開発

### 今日やること

週刊im@study編集部の復活のための、組版システム調査、および実験

### 今日の成果

Vivliostyleを従来通り続けるか、それとも、Re:VIEWに切り替えていくか、あるいは併用するかの3つがあると思う
本当に電子書籍だけ、しかもePubに統一するというなら、Sigilやcalibreあたりを使うのも手か

あと、物理媒体で出すためのコストを考えると、このご時世で紙媒体を出すには少し厳しいか？

夢百合草は永遠である

あと、今Circle CIを使っているが、GitHub Actionsを使ってビルドすることも検討したほうが良いかもしれない。サブディレクトリ絞ってビルドできるし。

https://blog.35d.jp/2020-09-29-github-actions-path

GitLabのCIなら.gitlab-ci.ymlのonly節にchangesを書いて対応

https://stackoverflow.com/questions/51661076/gitlab-ci-cd-run-jobs-only-when-files-in-a-specific-directory-have-changed/51792845
