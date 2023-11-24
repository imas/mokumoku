###### tags: `checkin-out` `047`

# 047 Producers List

## .ごっち

### 担当

なぎです
シャニソン始めました。超ライトにがんばります。

### P業以外で普段やっていること

- [Kaigi on Rails](https://kaigionrails.org/2023/)に[参加した](https://x.com/gggooottto/status/1718058305795629215?s=20)が、[おなかを壊した](https://x.com/gggooottto/status/1718033332599222621?s=20)ので実質参加していない。
- メインで使っている端末のyarnをぶっ壊してしまったので、個人開発のものをすべてpnpmに移行した。

### 今日やること

- 他の勉強会に参加してから参加します！
- 上で書いたとおり、パッケージマネージャをyarnで管理していたwhat3idolsもpnpmに移行している途中です。
  - https://github.com/YutaGoto/what3idols/pull/456
  - CircleCIを直したら多分うごく
- 前回の[Try](https://github.com/imas/mokumoku/blob/main/meetups/kanto/046/kpt.md#try)で書いた Androidのウィジットにポエムを載せるやつのひな型まで作ったので本実装する。
  - https://github.com/YutaGoto/ShinyPoemsAndroidApp
  - ポエムデータ(?)をhttpリクエストで取得するのは大変そうなので定数で持たせる。

### 今日の成果

- とりあえずアプリ本体にポエムを載せられた。
  - <img width="220px" src="https://hackmd.io/_uploads/BkHDp4zET.jpg" />
- 雑だけどもWidgetもできた。
  - https://github.com/YutaGoto/ShinyPoemsAndroidApp/pull/1
  - [ShinyPoems](https://shiny-poems.vercel.app/)にポエムコピー機能があるのよい～。
  - AndroidのWidgetの仕様で最低でも30分待たないと更新できないので、気がついたらポエムが変わっている感じ。
    - Widgetを2‐3並べたら、それぞれ別のポエムが表示されているのが確認できる。
  - Widgetのサイズの調整が難しい気がする
    - <img width="220px" src="https://hackmd.io/_uploads/Bk6voVGNT.jpg" />
- What3Idolsのpnpm対応したかった
  - CircleCIのnode-orbsがpnpm対応していないっぽい
    - https://github.com/CircleCI-Public/node-orb/issues/167
    - pnpmドキュメントをみたら気合のあるyamlだった。https://pnpm.io/ja/continuous-integration#circleci
  - GitHubActionsで書き直そうかな。


## 導線

### 担当

（たくさんいるけど、今回は担当のうち12月誕生日のアイドルのみ集めました）

本田未央, 小日向美穂, 萩原雪歩, 大崎姉妹

### P業以外で普段やっていること

最近はPythonばっかり書いてます（機械学習・データ処理で）

### 今日やること

美穂誕関連のデータ集めとWebサイトデザイン

### 今日の成果

https://kohhi.net/

デザインするのでいっぱいいっぱいだった。データ集めは後日します…

-   自由に使えるWebサイトデザインのテンプレートを持ってこようかとも考えたが、いい具合のものを見つけられず…（おしゃれすぎて自分には取り回せないものが多い…）
-   初めてCSSの `box-shadow` （枠に影を付けられる）を使ってみた。これ結構手軽に見栄えを良くできますね

## ひな

### 担当

たくさんいるので直近の動向だけ上げておきます。
昨日リリースされたシャニソンで郁田はるきさんが担当に加わりました。

### P業以外で普段やっていること

PythonやDB設計、GASが最近は主戦場です

### 今日やること

Notionのアイマス関連のDBの整理だったり、
ラウンジLINEのbotの書き直しだったりいろいろやります

### 今日の成果

- Notion
    - 765やデレマス、シャニマス用のデータを放り込む準備
        - やることが多すぎる
            - 全アイドル・声優の入力
            - 全CDの入力
            - 全楽曲の入力
            - 全セットリストの入力
- GAS
    - 作業端末(Chromebook)へのclaspの導入
    - 資材のclone
    - 各ソースへのコメントの記入
    - ロジックの追加実装
    - 資材のpush2

## あろー

### 担当

ほたた

### P業以外で普段やっていること

Angularとバトルしています

### 今日やること

- [ShinyPoems](https://shiny-poems.vercel.app/) のつづき
- シャニソンにも衣装ポエムらしきものがあったので気になる

### 今日の成果

- 新しくなってた React のドキュメントとにらめっこしていたら終わった
- <img width="512" src="https://hackmd.io/_uploads/r1Kqi4GVT.png">
- 衣装ポエムある…うれしい

## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

P業だけど、U149のフラスタ出した

https://www.instagram.com/p/Czn6bNYPchZ/c/18243447538230277/


### 今日やること

最近Swiftでホットリロードするライブラリを作ってる

https://github.com/banjun/SwiftHotReload

ので、これを使って、PhotoStudioPlayerのフィルタ書くとか、im@sparqlにアクセスするとか、やりたい

### 今日の成果

デモらないと伝わらないだろなと思いつつ

色の数値とかはなんかこう、試せる設定UI作ればいいじゃん感あるのだが、そもそもCoreImageのAPIどう使うんだっけな? colorSpaceの設定有無でなんか変わるの? みたいないろいろのアレコレは、コード書きながら試せるとうれしい。って思いました。

![名称未設定 (2)](https://hackmd.io/_uploads/HJdg1HGVa.jpg)

![名称未設定2](https://hackmd.io/_uploads/SkOxyBfE6.jpg)


## みかみん

### 担当

星梨花 ほか

### P業以外で普段やっていること

データエンジニア・データサイエンス

### 今日やること

LangChainのQAGenerationChainをさわってみる
Reference: https://api.python.langchain.com/en/latest/chains/langchain.chains.qa_generation.base.QAGenerationChain.html
参考ブログ: https://note.com/npaka/n/ncf1dbb190caf

### 今日の成果

ちょっとpromptをチューニングしないと、よさげな問題が作られない。
（ソースはピクシブ百科事典）

箱崎星梨花に関する問題
1. 登場人物の名前と年齢は？
2. 文中に描かれている人物にはどのような特徴がありますか?
3. この人物はどのような性格ですか？
4. アイドルを目指したきっかけは何ですか？
5. 文中で言及されている映画の名前は何ですか?

高槻やよいに関する問題
1. アイドルマスターがピザハットのCMに出演した広告プロジェクトの名前は何ですか?
2. やよいが示す最低限の運動能力とは？
3. 体力や運動神経が良さそうなキャラクターは？

橘ありすに関する問題
1. 文中に登場する人物の身長と体重はどれくらいですか?
2. カードに関連付けられている特殊なスキルまたは効果の名前は何ですか? (小さな妖精)
3. 文中に記載されているCDデビューのタイトルは何ですか？
4. アイドルマスターシンデレラガールズにオープンした新しいエリアの名前は何ですか? (初登場時)
5. キャラクターの強いコンプレックスの主な理由は何ですか？

あなたは高校教師が読解に関する問題を考えるのを助けるように設計された賢いアシスタントです。
与えられたテキストに対して、生徒の読解能力をテストするために使用できる質問と回答のペアを考え出す必要があります。
この質問と回答のペアを思いついたときは、次の形式で応答する必要があります。
```
{{
    "question": "$YOUR_QUESTION_HERE",
    "answer": "$THE_ANSWER_HERE"
}}
```
次のテキストについて、指定された JSON 形式で質問と回答のペアを作成してください。
{text}
