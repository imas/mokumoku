###### tags: `checkin-out` `028`

# 028 Producers List

## .ごっち

### 担当

なぎなぎ

### P業以外で普段やっていること

[正月からちょろっと旅行](https://twitter.com/gggooottto/status/1477125662259691520?s=20)していました

### 今日やること

- What3Idols開発続きをする。
    - [前回](https://twitter.com/gggooottto/status/1471455881284169729?s=20)色の調整をがんばった。
        - ![](https://i.imgur.com/YklARSS.png)
    - GoogleMapsの色がデフォルトなのがさみしいので、Mapの色を変更して遊んでみる。
        - https://cloud.google.com/blog/products/maps-platform/introducing-new-maps-customization-features
        - https://mapstyle.withgoogle.com/

### 今日の成果

- 色がんばった
    - https://twitter.com/gggooottto/status/1484138598400098305?s=20
    - ![](https://pbs.twimg.com/media/FJi4HEDVIAQ4kg-?format=jpg&name=large)
    - https://imas-palette.vercel.app/ im@s-paletteさまさま
    - [react-google-maps/api](https://www.npmjs.com/package/@react-google-maps/api)というパッケージを使っていたが、[GoogleMaps公式のreact-wrapper](https://www.npmjs.com/package/@googlemaps/react-wrapper)パッケージがあったので置き換え作業をする

## ひな

- https://twitter.com/ak_hina/

### 担当

- ミリオンライブ
    - 望月杏奈
    - 七尾百合子
    - 白石紬
    - 永吉昴
- シンデレラガールズ
    - 島村卯月
    - 姫川友紀
    - 大石泉
- SideM
    - 秋月涼
    - 水嶋咲
    - 卯月巻緒
    - 姫野かのん

### P業以外で普段やっていること

- SIerにて勤務
    - ポジション
        - 後進育成
    - 扱っている技術
        - RPA
        - SQL
        - Java
        - HTML5 / JavaScript / CSS
        - Ruby on Rails
        - Python
- ランニング
    - 2/11 1500m + 5000m 出走予定
    - そのうちフルマラソンしたい
- ウマ娘

### 今日やること

- ラウンジLINEのコード整理（リファクタリング）

### 今日の成果

- ラウンジLINEのコード整理（リファクタリング）
    - バグ修正
    - プラチナスターテールの後半戦無いことに対する対応（matsurihi.meでは後半戦情報持っているので無視する対応）

## あろー

### 担当

ほたほた

### P業以外で普段やっていること

ひたすら Twitter でねこをみてます。かわいい

- https://twitter.com/muddycat_atami?s=20

### 今日やること

- [シャニの専用ブラウザのやつ](https://github.com/arrow2nd/serizawa/issues/15) をやります

### 今日の成果

- バグを治したらバグができました。かなしい

## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

家事@新居

### 今日やること

副業のもくもく会でちまちまやってたこれがそろそろ出来そうなので，できたていで，応用となるはずの画像の側をつくっていく。つまり所望のフォーマットを明らかにして画像作成するおしごと 
https://github.com/banjun/WatchFaceDumper/pull/3

### 今日の成果

とりあえず既存のportraitからがっとdepthを取り出す方法の調査
https://photo.stackexchange.com/questions/105378/how-to-extract-depth-map-from-heif-image-created-with-iphone-x-using-imagemagic
https://github.com/strukturag/libheif/blob/master/examples/heif_convert.cc

純正の画像フォーマット調査

* base_....heic: ISO Media, HEIF Image HEVC Main or Main Still Picture Profile, 480x600 Display P3
* back_....heic: ISO Media, HEIF Image HEVC Main or Main Still Picture Profile, 480x600 Display P3
* mask_...png: PNG image data, 480 x 600, 8-bit grayscale, non-interlaced

→ portraitにheif-convertはdepth.pngが取れる。Preview.appでトリミングしてHEICにしたものをheif-convertするとdepth.pngは取れない。

![](https://i.imgur.com/N2WYUJ4.jpg)

というわけで分離を(既存のツールで)したのだが，portrait文字盤のbase画像は既にボケエフェクト適用後のものが使われているな・・・とわかった

↓の，上のが本物の文字盤からとってきたやつ，下のが今回フェイクして作った画像。真ん中のは背景なので画処理が必要ではあるが，動作確認用としてはこれで作れたはず

![](https://i.imgur.com/Cc7SYSG.jpg)
