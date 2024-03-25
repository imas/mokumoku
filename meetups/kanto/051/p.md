###### tags: `checkin-out` `051`

# 051 Producers list

## .ごっち

### 担当

なぎです

### P業以外で普段やっていること

- [FitBoxingを始める](https://bsky.app/profile/yougoto.dev/post/3kn3yb7utrs25)
- ドメインを契約する

### 今日やること

- 次回以降のもくもく会で使用するDiscordサーバを準備する
  - https://github.com/imas/mokumoku/issues/196
  - https://github.com/imas/mokumoku/pull/200
- 時間が余ればポエム
  - https://github.com/YutaGoto/ShinyPoemsAndroidApp/pull/6

### 今日の成果

- Discordサーバを用意した
  - Slackに告知した
  - 思いつくものをザっと用意しました。GitHub連携などは必要な時にやっていきます。
- connpassのテンプレートを更新した
  - https://github.com/imas/mokumoku/pull/200
- ポエム追加した
  - https://github.com/YutaGoto/ShinyPoemsAndroidApp/pull/14
  - アプリのウィジットだけでなくWatchに表示させる仕組みを作りたい。
    - https://developer.android.com/training/wearables/watch-faces?hl=ja
- What3Idolsのdependabotがyarnに引っ張られてpnpmでのパッケージのアプデできなくなったので、一旦手動でアップデート
  - https://github.com/YutaGoto/what3idols/pull/497

## あろー

### 担当

ほたた

### P業以外で普段やっていること

普段食べてるご飯をもち麦にかえました 🍚

### 今日やること

- ShinyPoems
    - [一行ではおさまらないポエムが左によっている](https://github.com/arrow2nd/shiny-poems/issues/327) 修正したい

### 今日の成果

![image](https://hackmd.io/_uploads/rJgqhjtC6.png)
- なおした！

![image](https://hackmd.io/_uploads/r1vDdoF06.png)
- 根本的な対応ができなかったので、1行のポエムの場合はフォントサイズを下げることで対応した
    - けど、なんか右に謎の空間が生まれて消えない… (緑の下線のとこ)
- [vercel/satori](https://github.com/vercel/satori?tab=readme-ov-file#css) の CSS もどきの癖がすごい


## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

カリフォルニア行ってVision Pro買ってきました

カリフォルニア行ってStarlinkの打ち上げみてきました

ラ！ユニット甲子園みました

### 今日やること

**背景**

visionOSさまざま使い倒してはいるものの，まだまだ入口にいる。担当アイドルと同じ部屋で暮らすまでにもうちょっと先が長い。

**獲得したい要素**

任意の画像を透明ウインドウで出すやつ

透過フィルターつけられたら尚よいが...

### 今日の成果

visionOSで画像をドロップしたら，それを背景なしウインドウで開くやつつくった

https://github.com/banjun/AcrylStand/commit/443e480fb42b441ee685051742f4150d0584771f

キャプチャ

https://discord.com/channels/1220332164357427200/1220333098881781841/1220353715148685323

背景透過のPNGをドロップすると，2種類のウインドウで開く

論理サイズと物理サイズと，どっちがいいんだろと思ってるので2種実験中
