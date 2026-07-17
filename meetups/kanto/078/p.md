###### tags: `checkin-out` `078`

# 078 Producers list

## .ごっち

### 担当

なぎです。ひろです。さきです。

### P業以外で普段やっていること

TSKaigiに参加した。

{%preview https://x.com/tskaigi/status/2058062865303773209?s=20 %}

11月1日（日曜）に仙台でやります。

### 今日やること

前にHATSUBOSHI GAKUENのロゴをCanvas(Rust + WASM)で描いてみたをやりましたが、

{%preview https://hatsuboshi-logo.pages.dev/ %}

![GkO7sL0aoAA94f6](https://github.com/user-attachments/assets/01ee50f3-dfe8-4f6b-b27a-b64218cc986b)

Hatsuboshi Idol Festivalのロゴも再現できそう（むしろこっちのほうが簡単そう）なので、やってみる。

![image](https://hackmd.io/_uploads/ByOVSXLNGe.png)

### 今日の成果

大体できた。

![image](https://hackmd.io/_uploads/ry75JIL4fx.png)

本物と比べると内側のダイヤ:sparkles:の円弧が4分の1円ではなさそうだったので、次回以降微調整。
https://github.com/YutaGoto/Hatsuboshi-Logo-wasm/pull/365
↓雑にくりぬいて重ねてみたもの。白が本物で黒が今回作ったもの。

![image](https://hackmd.io/_uploads/SJIzg88Nze.png)


Discordのメンバー権限を整理したらbotが動かなくなってそうなので、これも次回。


## ばんじゅん🍓

### 担当
橘ありす
ほか

### P業以外で普段やっていること

WWDC26現地行ってきた
その近くのVision Proイベントでブース出してきた
これはそのブースで無限再生しておく用の動画
https://www.youtube.com/watch?v=2cSAGViaCZI
最近Final Cut ProとMotionをやりはじめたので動画が触れるようになった

### 今日やること

https://www.youtube.com/watch?v=soEs22k4Z9Y

1年越し、今年はRealityKitのインスタンシングでマテリアルID触れるようになったらしいから、アイドルのカラー表示をそれにしたい (去年はインスタンシングはできるようになったけど、マテリアル触れなかったので諦めた回があった)


### 今日の成果

確認した
* Reality Composer Pro 3のShader Graphで、Instance IDのノードがある
  * ![image](https://hackmd.io/_uploads/HyjvQLLNfe.png)

* とはいえインスタンス設定は前と変わらなそう。コードから入れられるのはtransformのみ。ということは、インスタンス番号からカラーを引いてくるためのバッファをなんらか渡さないといけなさそうだが、どうやって...?
    * 極論、テクスチャにアイドルカラーを書き込んで、そこから引いてくればとれそうではあるが

確認できそうでできてない
* RCP3で互換がなくなったので、RCP3で書いたシェーダーグラフをSwiftからロードする方法が分からなくなった
  * 参りました ![image](https://hackmd.io/_uploads/ByZAGU8EMl.png)



困る
* RCP3、ネイティブアプリなのかあやしくて、popupがwindowの外にはみ出て、かつwindowでclipされるので、選択もできなくてこまった
  * ![image](https://hackmd.io/_uploads/H1-8yII4fg.png)



## Sapphire(林)

### 担当
千早
ロコ

### P業以外で普段やっていること
TskaigiなどのコミュニティのStaffやOSS活動（まだ、１回）しています。

### 今日やること
日本語難しいので、Hermes AgentのCronを使って日本語能力試験の準備ができるようなアプリ（PWA）を作ってみようと考えています。
今日は匿名の処理とGoogleのログインを入れようと考えています。

問題を解いた日にはデレステログインボーナススタンプを使いたいんですが、使ってもいいか悩みます。。。。

### 今日の成果

最初は匿名で処理し、後でデータを保存したい場合はその時にGoogleにログインします。
初回のGoogleログインに限り、ローカルに保存された記録を活用してデータを保存します。

学習可視化カレンダーに完了時にデレステスタンプを入れたいのですが、悩んでいます。

![image](https://hackmd.io/_uploads/S1kc8LUEMg.png)

![i13224543116](https://hackmd.io/_uploads/BJWR88IVMx.jpg)
![i13246192160](https://hackmd.io/_uploads/S1exDIUNGe.jpg)
![Screenshot_20200113-000202](https://hackmd.io/_uploads/rJjePILEGe.jpg)
