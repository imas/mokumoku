###### tags: `checkin-out` `074`

# 074 Producers list

## 導線

### 担当

（876プロでは）日高愛、灯里愛夏

### P業以外で普段やっていること

副業では最近Pythonばかり書いてる。あるいは数式か

### 今日やること

以前から構想してコードもちょっとだけ書いていた、シンデレラガールズのカードゲーム https://www.slideshare.net/slideshow/2024-8a36/272388731 の実装を進める

- CPUを簡易的でも作成したい

### 今日の成果

簡易CPUを実装した。出せるカードの組み合わせがあれば出す（複数あれば最も高いものを出す）だけ。
- 初期手札は10枚
- 出せるカード：「3枚組で」「数の間隔が一定で」「タイプは一致かバラバラ」
- 点数：
  - タイプがバラバラの場合、数が同なら3点、1つ違いなら2点、2つ違いなら1点、3つ以上の違いなら0点。
  - タイプが一致する場合、上記の点数＋１。
  - ただしカードを出し切らないと（全員をデビューさせないと）アガリにならないので、0点でも出す意義はある。
- 出せるカードがなくなったら山札から1枚引く

```
TURN 0 PLAYER 0 CASTED Cu16浅野風,Pa15星井美,Co14神崎蘭
       HAND[7] Cu14関裕美,Cu16長富蓮,Co17神谷奈,Cu19涼宮星,Co20黒川千,Co25高垣楓,Pa28片桐早
TURN 0 PLAYER 0 ONEDRAW
       HAND[8] Cu14関裕美,Cu16長富蓮,Co17神谷奈,Cu19涼宮星,Co20黒川千,Co25高垣楓,Pa28片桐早,Pa15喜多日
TURN 1 PLAYER 0 CASTED Co17神谷奈,Cu16長富蓮,Pa15喜多日
       HAND[5] Cu14関裕美,Cu19涼宮星,Co20黒川千,Co25高垣楓,Pa28片桐早
TURN 1 PLAYER 0 ONEDRAW
       HAND[6] Cu14関裕美,Cu19涼宮星,Co20黒川千,Co25高垣楓,Pa28片桐早,Pa15秋月涼
TURN 2 PLAYER 0 ONEDRAW
       HAND[7] Cu14関裕美,Pa15秋月涼,Cu19涼宮星,Co20黒川千,Co25高垣楓,Pa28片桐早,Cu17三村か
:
:
:
TURN 47 PLAYER 0 ONEDRAW
       HAND[7] Pa13首藤葵,Cu13椎名法,Co18上条春,Cu20原田美,Pa25相馬夏,Co28川島瑞,Cu19有浦柑
TURN 48 PLAYER 0 ONEDRAW
       HAND[8] Pa13首藤葵,Cu13椎名法,Co18上条春,Cu19有浦柑,Cu20原田美,Pa25相馬夏,Co28川島瑞,Pa19夢見り
TURN 49 PLAYER 0 CASTED Cu20原田美,Pa19夢見り,Co18上条春
       HAND[5] Pa13首藤葵,Cu13椎名法,Cu19有浦柑,Pa25相馬夏,Co28川島瑞
TURN 49 PLAYER 0 ONEDRAW
       HAND[6] Pa13首藤葵,Cu13椎名法,Cu19有浦柑,Pa25相馬夏,Co28川島瑞,Cu12古賀小
```

このようなシミュレーションを多数回行い、残りやすい（出しにくい）カードに高い点数を与えるという方針を検討

## .ごっち

### 担当

なぎです。ひろです。

### P業以外で普段やっていること

冬を見てきた {%preview https://x.com/gggooottto/status/2020012566383387001?s=20 %}

### 今日やること

Discordのイベント自動作成で、ロケーションに誕生日アイドルが入るとつらいことになるので、説明欄に移動させる。
時間があればmcpつづき（ネタ探しをしたい）

### 今日の成果

作った。 [:adhesive_bandage: move idol name to description by YutaGoto · Pull Request #16 · YutaGoto/imas-mokumoku-create-discord-event](https://github.com/YutaGoto/imas-mokumoku-create-discord-event/pull/16)

誕生日アイドルを質問して返す機能を作ってなかったので追加した。

[feat add birthdate search on SearchEntity by YutaGoto · Pull Request #4 · YutaGoto/imasparql-mcp-server](https://github.com/YutaGoto/imasparql-mcp-server/pull/4)

![image](https://hackmd.io/_uploads/rklyytNO-g.png)

```md
### User Input

来週が誕生日のアイドルはいますか？

*Running MCP tool*

*Running MCP tool*

*Running MCP tool*

*Running MCP tool*

*Running MCP tool*

*Running MCP tool*

*Running MCP tool*

### Planner Response

来週（2026年2月23日〜3月1日）が誕生日のアイドルは以下の通りです。

### 2月23日
*   **天道 輝**（SideM）

### 2月24日
*   **園田 智代子**（シャイニーカラーズ）
*   **桐生 つかさ**（シンデレラガールズ）

### 2月25日
*   **如月 千早**（765AS）
*   **月岡 恋鐘**（シャイニーカラーズ）
*   **三船 美優**（シンデレラガールズ）

### 2月26日
*   **黒川 千秋**（シンデレラガールズ）

### 3月1日
*   **ロコ**（ミリオンライブ！）

来週は多くの人気アイドルの誕生日が重なっており、特にお祝いが賑やかになりそうですね！
```

期間指定の検索もいけなくもなさそうだけどどうなんだろうか。。

{%preview https://space.pikopikopla.net/query/22008d5a18 %}

## ばんじゅん🍓

### 担当
橘ありす
ほか

### P業以外で普段やっていること
レンダラーを自作している
https://x.com/banjun/status/2020402926561497208/photo/1
いや、P業かもしれない

### 今日やること
あみあみGiftの花海咲季ぬいが来たのでスキャンした
https://www.youtube.com/watch?v=cx9YWOzWa_4

前のありすのスキャンは、てきとうに関節pointを打って、頂点との雑距離計算でRigをつくってパペット的に動かせるようにしたが、そろそろまともな方法でやりたい。あるいはスキャンに後処理して、破綻を消したり色をよくしたりしたい。


### 今日の成果
![image](https://hackmd.io/_uploads/SkOPPuV_Ze.png)
![image](https://hackmd.io/_uploads/HJwQuOVdWg.png)
![image](https://hackmd.io/_uploads/r1dH_ONOZl.png)

Sculpt ModeでFlattenとかSmoothだと、ちまちました作業になりすぎ
Edit Modeでツノの頂点消してからFで閉じるとテクスチャが失なわれるが、それを再度つくるの大変そう
Sculpt ModeでGrabでてきとうにツノの頂点を押しさげてから、FlattenとSmoothでならすといいかも?
![image](https://hackmd.io/_uploads/r1U7RuNOZl.png)
![image](https://hackmd.io/_uploads/BysiAOVO-g.png)
![image](https://hackmd.io/_uploads/Sk0OktE_Wg.png)

書き出すと、触ってないデータ消えるけど...
disp0はもともと画像はあるけど使ってないデータらしい...Object Captureの仕組みがそうなのか...
aoは使われてたっぽいが、Blenderでは付けられないらしい...? Reality Composer Proで再度つけなおすのか...
![image](https://hackmd.io/_uploads/HyJXNY4dZg.png)

RCPでaoつけなおし→usdz書き出し
![image](https://hackmd.io/_uploads/ryh6LK4_Wl.png)

TODO: 結果をみてみて良さそうなら完成
