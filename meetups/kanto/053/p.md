###### tags: `checkin-out` `053`

# 053 Producers list

## .ごっち

学園アイドルマスターはもくもく会のあとに入学します（定時制プロデューサー科）

### 担当

なぎです

### P業以外で普段やっていること

[佐賀・長崎に行ってきた](https://bsky.app/profile/yougoto.dev/post/3ks2uidwotj2p)

### 今日やること

- mokumoku会用の自動でプルリクエストを作るステップの説明文がmocriのままになっているので直す
  - https://github.com/imas/mokumoku/blob/6ff6650a949a79a72ae7b70ab67b789b146bf466/.github/workflows/mokumoku.yml#L44
- Wear OSにポエムのつづき
  - 前回
  - <img width="200" src="https://hackmd.io/_uploads/SkwbP5RlA.jpg" />

### 今日の成果

- mokumoku会用のプルリクエストつくった
  - https://github.com/imas/mokumoku/pull/207
  - ついでにActionで使用するUbuntuのバージョンも上げた
- wear OS ポエム
  - wear用のモジュールを作ったらkotlinのバージョンが古いと怒られたのでアップグレードした
  - Tile上で表示できるようになった。
    - https://x.com/gggooottto/status/1791085939189792868
    - Truncateされているのは次回以降に直す（Layout処理部分なにもわからない。。）
    - https://github.com/YutaGoto/ShinyPoemsAndroidApp/pull/15

## ぼでー

### 担当

櫻井桃華と春霞ユニット推し

### P業以外で普段やっていること

いやらしいことを呟いている

### 今日やること

- アイマスハッカソン2024(仮)のテーマややること、内容を決める

### 今日の成果

- 考えていることをブログにデプロイした
  - https://bode-mmk.hatenablog.com/entry/2024/05/16/213647

## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

Vision Proをかぶって踊ってみたしたりしてます P業か... https://www.youtube.com/shorts/sWzYBCe-tzs

Vision Proをかぶって座談会をやったりしてみてます https://www.youtube.com/watch?v=FLcmOzI2LfM

### 今日やること

Vision Proのなかにアクリルクロックを置くやつ、そろそろ文字盤の部分つくりたい

### 今日の成果

まずは秒針を置きたい

![image](https://hackmd.io/_uploads/rkwqltXmR.png)

Reality Composer Proではほぼモデルは作れないので、頂点をずらしてそれっぽい形にしたいのでグラフ描いた。こうすれば針っぽくね? `y=s|_cdot_0.1({cos({5({x-t})})exp({({-5({x-t})})})}), t = -0.7,s=|_list_{-1,+1}`![image](https://hackmd.io/_uploads/HJb1zYmX0.png)


![image](https://hackmd.io/_uploads/SJzReYX7A.png)

だがしかし、こいつが全然MaterialXのノードで実装できない。座標系なのか値なのかズレてるのだろうが、なんもわからん...マテリアルのプレビューと適用した結果と違うし...

![image](https://hackmd.io/_uploads/BJbxZF7QA.png)
