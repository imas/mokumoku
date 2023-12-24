###### tags: `checkin-out` `048`

# 048 Producers list

## 導線

### 担当

（多いので12月誕生日のアイドルのみ抜粋）本田未央、小日向美穂、萩原雪歩、大崎姉妹

### P業以外で普段やっていること

X(Twitter)のボット作成ツール [https://maraigue.hhiro.net/twbot/](https://maraigue.hhiro.net/twbot/) を、新APIに対応させてる途中

### 今日やること

-   [シンデレラガールズの声優キャスティング情報RDF](https://api.hhiro.net/rdf/?r=imascast.rdf)に、イヴさんはおろか大石泉も反映できていないので更新する
-   それに合わせて、RDFで書かれた情報を見やすくする&編集しやすくするツールの導入もしたい

### 今日の成果

-   [RDFの更新はしました](https://twitter.com/dousen_kikaku/status/1737799583147917771)
-   RDFのエディタとしては、個人的には「表計算ソフトのようなGUI」で編集できるものを探していたのだが、「RDF Editor GUI」とかで検索しても「テキストエディタのRDF向けのもの」とかが出てきてしまう
    -   表のファイルをRDFに変換する、というツールを使うほうがよいのかもしれない

## .ごっち

### 担当

なぎです

### P業以外で普段やっていること

- [椅子を買いました](https://x.com/gggooottto/status/1729335423024197676?s=20)。
- 気軽に飲める温かい飲み物を模索している

### 今日やること

- [フィヨルドブートキャンプの配信](https://www.youtube.com/live/SBVMuEUT5B4?si=_UMO-uejIVwYCLaP)をみながらもくもくします。
- [mocriに集中用BGMを流せる機能](https://x.com/mocri_jp/status/1734466331905548449?s=20)がついたので流してみる。
- [ひとりアドベントカレンダー](https://adventar.org/calendars/9122)用に今年のimas_mokumokuの振り返りと成果のまとめ記事を書く。
  - [去年も書いた](https://yutagoto.github.io/blog/posts/20221216-imas-mokumoku/)
- 時間があれば[シャイニーポエムAndroidWidget](https://github.com/YutaGoto/ShinyPoemsAndroidApp)のポエム追加をしたい
  - imasparqlが503を吐いているのでpoem？取得をどうしようかな。。
  - cromisaさんが対応してくださった！うれしい！

### 今日の成果

- 今年のもくもくまとめの下書きを書いた
  - https://github.com/YutaGoto/blog/pull/1108
  - <img width="320" src="https://hackmd.io/_uploads/rklCssWwa.png" />
- シャイニーポエムウィジェットに八宮めぐるのポエムを追加した。
  - https://github.com/YutaGoto/ShinyPoemsAndroidApp/pull/3
  - <img width="320" src="https://hackmd.io/_uploads/rkDJZ3Zvp.jpg" />
- imasparqlのポエムにtypoがあったので修正プルリクを作った
  - https://github.com/imas/imasparql/pull/548

## ばんじゅん🍓

### 担当
橘ありす
ほか

### P業以外で普段やっていること
ラ!の曲をきいてる

### 今日やること
なにしようかな
ラ!のLinked Open Dataほしさはあるが...

前回のPhotoSudioPlayerのやつちゃんとするか


### 今日の成果

SwiftHotReloadをPhotoStudioPlayerに組込む。Debug/Releaseビルドちゃんとする。(DebugではHotReloadできるようにセキュリティを弱めるが、Releaseはちゃんとするし、余計な影響を与えない)

PRにまとめた
https://github.com/banjun/PhotoStudioPlayer/pull/29
