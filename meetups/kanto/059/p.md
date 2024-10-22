###### tags: `checkin-out` `059`

# 059 Producers list

## 導線

### 担当

（最近誕生日を迎えた担当だと）椎名法子

### P業以外で普段やっていること

- 副業: Pythonばかり書いてる
- 趣味: P業以外の趣味が滞りまくってる…

### 今日やること

- ハッカソンで発表した、[シンデレラガールズの「シンプルな」カードゲーム](https://www.slideshare.net/slideshow/2024-8a36/272388731)の制作の続き
  - ゲームバランスを考える（どのカードをどう集めればデビューさせられるか）

### 今日の成果

- まずは「サポートカード」を実装する方針にかじを切った
  - 例えば基本ルールでは「番号が等間隔でなければならない」というのがあるが、それを1つずれでもOKにするとか
- その定義をプログラムとして行えるようにしている途中

## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

visionOSアプリつくる技術の研究開発とか、織物とか

### 今日やること

マストドンクライアントiMastがvisionOSで動くわけだけど、ちょっと気になってるとこちゃんとしてみようかな
https://github.com/cinderella-project/iMast


### 今日の成果

visionOS 2 SDKでビルドしたらだいたいいい感じになった(タブとかオーナメントとか)。
投稿ウインドウがたまに奥にいってしまうことがあるので、なんとかしたい。
修正には至らず。調査:

windowはここで出てる
https://github.com/cinderella-project/iMast/blob/3eaf868131b7bcf12c299290d14917356a3665e4/Sources/iOS/App/NewPostSceneDelegate.swift#L54

sceneはprominentで出てる。実装はよさそうだが、visionOSの挙動がよくない。
https://github.com/cinderella-project/iMast/blob/3eaf868131b7bcf12c299290d14917356a3665e4/Sources/iOS/App/Extensions/UIViewController%2BshowAsWindow.swift#L39

placementをいい感じにする方法や、activeのexternal eventsをハンドルする方法がUIKitでは不明...

そこじゃなく、キーボードとの相性かもしれない
https://forums.developer.apple.com/forums/thread/731700

## .ごっち

### 担当

なぎです。りーぴゃんです。

### P業以外で普段やっていること

[タブレット他](https://x.com/gggooottto/status/1843462834006700447)を買いました
イヤホンに慣れない

### 今日やること

ハッカソンで作った初星学園のロゴのつづき。右上の `HATSUBOSHI GAKUEN` の部分をtextを使わずに線を引く。

これ（本物

<img src="https://gakuen.idolmaster-official.jp/assets/img/common/logo_text.svg" />

### 今日の成果

`HATSUBOSHI GAKUEN` の `HA` の途中

https://x.com/gggooottto/status/1846896510015098957

![image](https://hackmd.io/_uploads/SJW98KRJyx.png)

`H` の文字を描くのに二次元の座標計算をさせられた。 `A` が難しすぎる。
そもそも真横方向に描かれた文字を並べて `rotate()` させたほうがすんなりいけそう

https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/rotate
