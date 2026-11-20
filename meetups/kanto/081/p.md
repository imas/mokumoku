###### tags: `checkin-out` `081`

# 081 Producers list

## 導線

### 担当

（直近で誕生日だった担当は）小松伊吹（11/17）

### P業以外で普段やっていること

最近は鯖缶業務に忙しい

つい先日、北陸Ruby会議02@福井に行きました https://x.com/search?q=%23hokurikurk02%20from%3Ah_hiro_&src=typed_query&f=top

### 今日やること

- [第80回](https://hackmd.io/pUK0051YSyO0b_hZlcW66w)の続き
  - シンデレラガールズのアイドルの「属性と年齢だけが書かれた」カードでのゲーム
  - 特殊カード（「番号を+1する」などを持ったカード）を実装したとき、それをうまく扱えるCPUを実装する
  - https://www.slideshare.net/slideshow/2024-8a36/272388731
- 前回：今のデータ構造のままじゃCPU作るの難しくね？って思ってデータ構造を見直した（カードにID振っておけというのがあった）
- 今回：なのでCPUを作り進める

### 今日の成果

- 「カードにID振っておけ」は完成した
- カードを出せる条件（番号の間隔が一定、かつ同属性もしくは3属性）を満たせるカードの組み合わせがあれば出すことは、特殊カードなしのものは出せるようになった（下図）
  - ただ、特殊カードを含む場合は全く別の実装が必要で、書き始めている（結構できてはいる）

```
TURN 0 PLAYER 0 CASTED Cu13日高愛,Co13成宮由,Cu13大沼く
TURN 0 PLAYER 0 CASTED Cu18丹羽仁,Co18上条春,Cu18藤本里
TURN 5 PLAYER 0 CASTED Co26和久井,Pa20斉藤洋,Cu14輿水幸
TURN 9 PLAYER 0 CASTED Co18桐生つ,Pa17難波笑,Cu16安斎都
TURN 12 PLAYER 0 CASTED Cu17道明寺,Cu17白雪千,Cu17井村雪
TURN 15 PLAYER 0 CASTED Cu20原田美,Pa18相葉夕,Cu16佐久間
TURN 18 PLAYER 0 CASTED Pa19イヴ・,Pa16及川雫,Pa13双海真
TURN 21 PLAYER 0 CASTED Co28川島瑞,Pa22並木芽,Co16藤原肇
TURN 22 PLAYER 0 CASTED Co25木場真,Co23相川千,Co21伊集院
TURN 25 PLAYER 0 CASTED Co25服部瞳,Co20黒川千,Cu15大原み
TURN 29 PLAYER 0 CASTED Cu17小日向,Cu15楊菲菲,Pa13小関麗
TURN 32 PLAYER 0 CASTED Cu20大西由,Co18八神マ,Pa16堀裕子
TURN 39 PLAYER 0 CASTED Pa15キャシ,Co14最上静,Pa13双海亜
TURN 40 PLAYER 0 CASTED Co13氏家む,Cu13乙倉悠,Pa13村上巴
TURN 44 PLAYER 0 CASTED Co19鷺沢文,Co16如月千,Co13白坂小
TURN 45 PLAYER 0 CASTED Pa15浜口あ,Co15松尾千,Pa15イム・
TURN 48 PLAYER 0 CASTED Cu20日下部,Cu19宮本フ,Cu18月宮雅
```

## .ごっち

### 担当

なぎです。ひろです。さきです。

### P業以外で普段やっていること

山に登った
{%preview https://x.com/gggooottto/status/2119040732640223439?a=s3uAec1s7j_bmkjjRgQ&s=20 %}

### 今日やること

香名江さんが入学してびっくり（ストーリーをまだ見てない）したので、imasparqlに登録する。
{%preview https://github.com/imas/imasparql/issues/589 %}

discordイベントが自動で作られる時に imasparqlが落ちてたらerrorと表示されるのでそれの対応。ついでにスラッシュコマンドも対応。
![image](https://hackmd.io/_uploads/Sygbbw2Cfg.png)

### 今日の成果

- rdf追加: https://github.com/imas/imasparql/pull/591
  - コピペのままのやつを見つけたのでこの後すぐ対応する
- botの対応: https://github.com/YutaGoto/imas-mokumoku-create-discord-event/pull/22
