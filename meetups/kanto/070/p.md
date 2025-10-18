###### tags: `checkin-out` `070`

# 070 Producers list

## .ごっち

### 担当

なぎです。ひろです。

### P業以外で普段やっていること

- kaigi on rails 参戦
- ぱいそん農家

{%preview https://x.com/gggooottto/status/1977648349156401381 %}

### 今日やること

前回 chatGPTと一緒にimagparql-mcpサーバ作成をし始めたのでそのつづき。

{%preview https://x.com/gggooottto/status/1968656760853426490 %}

### 今日の成果

アイドルのユニット取得までできた。

![image](https://hackmd.io/_uploads/rySWmvAaee.png)

ユニットのメンバー検索まではできなかった（ChatGPTのフリープランの上限がきた）

CursorのMCPに登録させて現状のものでもできないかなーとやったらできた。

![image](https://hackmd.io/_uploads/HycItwCpll.png)


## 導線

### 担当

（今月誕生日の中では）椎名法子

### P業以外で普段やっていること

副業で情報系の研究職やってます

### 今日やること

シンデレラガールズ声優さんの配役情報をRDF化してSPARQLで検索できるシステム https://api.hhiro.net/rdf/?r=imascast.rdf が、RubyのSPARQLライブラリをアップデートすると（検索クエリによっては）エラーを吐くようになったので、その対処をする

- 公開用のバージョンは、ライブラリを旧バージョンにして動かしているが、新バージョンでもちゃんと動くようにしたい
  - あるいはもしかしたら自分のSPARQLのクエリの書き方が悪いのかもしれないが、旧バージョンで動いていた以上はちゃんと原因究明したい
- これまでの取り組み
  - Ruby東海のもくもく会で、「ライブラリのバージョンの切り替えをbundlerで行えるようにする」ことをしてました（今までbundlerをまともに使ったことがなかった）
  - RubyのSPARQL gemがバージョン3.3.2（現在の最新版）以降だと動かないクエリが多発したことを確認していたのだが、ソースコードを読んだ感じ、クエリを中間表現に変換する処理が追加されたようで、それが悪さをしているように見える

### 今日の成果

クエリの書き方を直せば動いてくれる例はあった。例えば、ライブラリ更新前には動いていたけど更新後にエラーを吐くようになったクエリとして

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>
PREFIX imas: <https://sparql.crssnky.xyz/imasrdf/URIs/imas-schema.ttl#>
PREFIX imascast: <https://api.hhiro.net/rdf/imascast.rdf#>
SELECT * WHERE {
  ?a rdf:type imascast:VoiceActor;
     schema:name ?声優フルネーム;
     imas:givenNameKana ?声優名前;
     filter(regex(str(?声優名前),"^あやか$") || regex(str(?声優名前),"^はるか$")).
  ?c rdf:type imascast:Casting;
     imascast:ActedBy ?a;
     imascast:CharacterName ?アイドル名.
}
```

というものがあったのだが、filterを外に出して

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>
PREFIX imas: <https://sparql.crssnky.xyz/imasrdf/URIs/imas-schema.ttl#>
PREFIX imascast: <https://api.hhiro.net/rdf/imascast.rdf#>
SELECT * WHERE {
  ?a rdf:type imascast:VoiceActor;
     schema:name ?声優フルネーム;
     imas:givenNameKana ?声優名前.
  ?c rdf:type imascast:Casting;
     imascast:ActedBy ?a;
     imascast:CharacterName ?アイドル名.
  filter(regex(str(?声優名前),"^あやか$") || regex(str(?声優名前),"^はるか$")).
}
```

とすれば更新後のライブラリでも動いてくれた。ただその対処をしてもなお動かないクエリもあったりしてよくわからない。

あと、旧ライブラリでは適度な時間で処理が完了したのに、新ライブラリだといつまで経っても処理が終わらないケースが生じている。ただ「そのことを検証できる小さいコード」が作れなくて困っている（それが作れればバグ報告ができるのだが…）

## ばんじゅん🍓

### 担当

橘ありす
ほか

### P業以外で普段やっていること

Vision Proを人にかぶせている
ARIAのコンサートがよかった

### 今日やること

AVPのアクスタのやつをvisionOS 26, Xcode 26前提に上げて整理する
betaじゃなくなったので

### 今日の成果

https://github.com/banjun/AcrylStand/pull/4

床のスナップと、部屋への(ライフサイクルの)固定があるので(Lock-in-Place)、それとなじむように、下端揃えにした(アクスタの足が面につく)

ビルドするたびにLock-in-Placeが動かなかったりしたが、同じビルドでもAVPを再起動すると直るのでなんか変なの踏んでるだけかもしれない → 再現&workaround確認とれた

絵は変わってないが:

![IMG_2803](https://hackmd.io/_uploads/r1-usvRple.jpg)



## みかみん

### 担当

箱崎星梨花ほか

### P業以外で普段やっていること

データエンジニア（分析、モデル開発、基盤構築）など

### 今日やること

langchain/langgraphからim@sparql呼び出すコードを書いてみる

### 今日の成果

LangGraphで、テンプレートに変数を埋める形のim@sparqlクエリを呼ぶ部分は試すことができた。
SPARQL自体の生成もプロンプトを工夫すればLLMで出来そう。

#### LangGraphとimasparqlの呼び出し

LangGraphでのtool callingは、以下のquickstartの通りでよい。
https://docs.langchain.com/oss/python/langgraph/quickstart

LLMにgpt-ossを使いたい場合。
・次のようにインストールと起動。
```
$ brew install llama.cpp
$ llama-server -hf ggml-org/gpt-oss-20b-GGUF --port 1337 --jinja
```
・init_chat_modelを次のように置き換える。
```
llm = init_chat_model(
    "openai:gpt-oss-20b",
    temperature=0
)
```

sparqlの呼び出しは、SPARQLWrapperを使えばOK。

SPARQLクエリのテンプレートに変数を埋める形のtoolでよければ、以上で作成できる。
例: <箱崎星梨花>の<身長>を教えて ※<>部分が変数

```python
@tool
def get_attribute(a: str, b: str) -> str:
    """人名から属性情報を求める

    Args:
        a: 人名
        b: 属性情報
    """
    attr = None
    if b in ("height", "身長"):
        attr = "height"
    elif b in ("birthday", "誕生日"):
        attr = "birthDate"
    elif b in ("birthPlace", "生まれた場所", "生誕地"):
        attr = "birthPlace"

    if attr is None:
        return "unknown"

    endpoint_url = "https://sparql.crssnky.xyz/spql/imas/query"
    return_format='json'
    query = """
PREFIX afn: <http://jena.apache.org/ARQ/function#>
PREFIX schema: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX imas: <https://sparql.crssnky.xyz/imasrdf/URIs/imas-schema.ttl#>
SELECT (?nm as ?NAME) (str(?at) as ?ATTR)
WHERE {
 ?s rdf:type imas:Idol;
 schema:name ?nm;
 schema:$ATTR ?at.
 FILTER(lang(?nm) = 'ja')
 FILTER(str(?nm) = '$NAME')
}
ORDER BY ?NAME
LIMIT 1
    """
    query = query.replace('$NAME', a)
    query = query.replace('$ATTR', attr)
    headers = {'Accept': f'application/sparql-results+{return_format}'}
    response = requests.get(
        endpoint_url,
        headers=headers,
        params={'query': query},
    )
    results_01 = response.json()

    return results_01["results"]["bindings"][0]["ATTR"]["value"]

```

#### LLMによるSPARQLの生成

SPARQL自体の生成もプロンプトを工夫すればLLMで出来そう。
クエリ:
```
以下の条件で、誕生日を取得するSPARQLクエリを書いてください。
schema:name: 箱崎星梨花

取得する属性は、schema.orgのスキーマ情報を利用してください
schema:nameの絞り込みは、次の例のようにFILTERを用いる必要があります
SELECT ?attr
WHERE {
  ?person schema:name ?name;
  <取得したい属性> ?attr .
  FILTER(str(?name) = '対象の名前')
}
```
回答:
```
PREFIX schema: <http://schema.org/>

SELECT ?birthDate
WHERE {
  ?person  schema:name     ?name ;
           schema:birthDate ?birthDate .
  FILTER (str(?name) = "箱崎星梨花")
}
```
