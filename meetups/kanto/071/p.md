###### tags: `checkin-out` `071`

# 071 Producers list

## みかみん

### 担当

箱崎星梨花ほか

### P業以外で普段やっていること

データエンジニア（分析、モデル開発、基盤構築）など

### 今日やること

langchain/langgraphからim@sparql呼び出すコードを書いてみるの続き

### 今日の成果

#### toolの汎用性を高める

前回のものより汎用性を高めるため、LLMにSPARQLを書かせるtoolに変更。

````python
def execute_imasparql(query):
    endpoint_url = "https://sparql.crssnky.xyz/spql/imas/query"
    return_format='json'
    headers = {'Accept': f'application/sparql-results+{return_format}'}
    response = requests.get(
        endpoint_url,
        headers=headers,
        params={'query': query},
    )
    if response.status_code == 200:
        return response.json()
    return None

def get_attribute_list():
    resp = execute_imasparql("""
    PREFIX imas: <https://sparql.crssnky.xyz/imasrdf/URIs/imas-schema.ttl#>
    PREFIX schema: <http://schema.org/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT distinct ?p
    WHERE {
     ?s ?p ?o;
     schema:name ?name;
     rdf:type imas:Idol;
    }
    LIMIT 200
    """)
    results = resp["results"]["bindings"]
    attrs = [e["p"]["value"] for e in results]
    return "\n".join(attrs)

attribute_list = get_attribute_list()

prompt_get_attribute = """
以下の条件で、$ATTRを取得するSPARQLクエリを書いてください。
結果にはSPARQLクエリ本文以外の情報を一切含めないで下さい
schema:name: $NAME

取得する属性は、次の一覧から利用して下さい
```
$ATTR_LIST
```

schema:nameの絞り込みは、次の例のようにFILTER,containsを用いる必要があります
```
PREFIX schema: <http://schema.org/>

SELECT ?attr
WHERE {
  ?person schema:name ?name;
  <取得したい属性> ?attr .
  FILTER(contains(str(?name), '対象の名前'))
}
```
"""

@tool
def get_attribute(a: str, b: str) -> str:
    """人名から属性情報を求める

    Args:
        a: 人名
        b: 属性情報
    """
    prompt = prompt_get_attribute
    prompt = prompt.replace('$ATTR_LIST', attribute_list)
    prompt = prompt.replace('$NAME', a)
    prompt = prompt.replace('$ATTR', b)
    rtn = llm.invoke(prompt)
    query = rtn.content
    results_01 = execute_imasparql(rtn.content)
    return results_01
````

実行例

コード
```python
# Invoke
content = """
星梨花はどんなことが好き？
"""
from langchain.messages import HumanMessage
messages = [HumanMessage(content=content)]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()
```

結果
```
================================ Human Message =================================


星梨花はどんなことが好き？

================================== Ai Message ==================================
Tool Calls:
  get_attribute (SWEQW7B6LHiTfU4EEjRDDrixbivUVQsw)
 Call ID: SWEQW7B6LHiTfU4EEjRDDrixbivUVQsw
  Args:
    a: 星梨花
    b: 好きなこと
================================= Tool Message =================================

{'head': {'vars': ['hobby']}, 'results': {'bindings': [{'hobby': {'type': 'literal', 'xml:lang': 'ja', 'value': 'バイオリン'}}]}}
================================== Ai Message ==================================

星梨花はバイオリンを弾くことが好きです。
```

この時発行したSPARQLクエリと応答
```
---- SPARQL Query
PREFIX schema: <http://schema.org/>
PREFIX imas: <https://sparql.crssnky.xyz/imasrdf/URIs/imas-schema.ttl#>

SELECT ?hobby
WHERE {
  ?person schema:name ?name ;
          imas:Hobby ?hobby .
  FILTER(contains(str(?name), '星梨花'))
}
---- SPARQL Response
{'head': {'vars': ['hobby']}, 'results': {'bindings': [{'hobby': {'type': 'literal', 'xml:lang': 'ja', 'value': 'バイオリン'}}]}}
```

これでim@sparqlにデータがある、アイドルの属性を自然言語で問い合わせることは出来る。
曖昧な聞き方をすると変なSPARQLを生成してしまうので、その辺りチェックする仕組みが必要になる。

## 導線

### 担当

（来週のデレxR出演者の中では）島村卯月、本田未央、神谷奈緒

### P業以外で普段やっていること

最近は副業でサーバ管理的な諸々をすることが多い…

### 今日やること

シンデレラガールズの配役情報RDF https://api.hhiro.net/rdf/?r=imascast.rdf で、RubyのSPARQLライブラリ https://github.com/ruby-rdf/sparql/ のバージョンを最新にしたら、一部のクエリがエラーで処理できなくなる件

- ライブラリのここを修正すればおそらく大丈夫、というのはわかったが、他のところに影響が出るかもしれない
- でテストコードを走らせてみたら、そもそも通らないテストが大量に存在した（テストコードのメンテがされてない？）
- ということでそこは断念し、問題点を文章で説明したissueとして出すところまでやりたい

### 今日の成果

- Issueがほとんどまとまった。あと10分後くらいにはGitHubに出てるはず https://github.com/ruby-rdf/sparql/issues
  - どんなバグだったのか（先週には判明してた） https://x.com/h_hiro_/status/1987049762714271930

## .ごっち

### 担当

なぎです。ひろです。

### P業以外で普段やっていること

古代のハイラルを救う未来の姫
{%preview https://x.com/gggooottto/status/1990053680402640992?s=20 %}

### 今日やること

前回 im@sparql-mcpをそれなりに作って、時間外に一通り動くところまでやりプルリクエストを作るところまでやった。

![](https://pbs.twimg.com/media/G3grtTGXkAAVCwg?format=jpg&name=large)

{%preview https://github.com/YutaGoto/imasparql-mcp-server/pull/1 %}

{%preview https://x.com/gggooottto/status/1979380112027193798?s=20 %}

copilot reviewで指摘されている部分を見直しつつ、エンティティを増やしてもよさそうな。

### 今日の成果

マージした。

```
> 星梨花の誕生日は？

╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✓  search_entities (imasparql MCP Server) {"q":"星梨花"}                                                            │
│                                                                                                                     │
│ [                                                                                                                   │
│   {                                                                                                                 │
│     "id": "https://sparql.crssnky.xyz/imasrdf/RDFs/detail/Hakozaki_Serika",                                         │
│     "title": "箱崎星梨花",                                                                                          │
│     "snippet": "箱崎星梨花 / 箱崎星梨花 / はこざきせりか / MillionLive / 身長:146.0 / 体重:37.0 / 誕生日:--02-20"   │
│   },                                                                                                                │
│   {                                                                                                                 │
│     "id": "https://sparql.crssnky.xyz/imasrdf/RDFs/detail/Hakozaki_Serika",                                         │
│     "title": "箱崎星梨花",                                                                                          │
│     "snippet": "箱崎星梨花 / Serika Hakozaki / はこざきせりか / MillionLive / 身長:146.0 / 体重:37.0 /              │
│ 誕生日:--02-20"                                                                                                     │
│   }                                                                                                                 │
│ ]                                                                                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ 星梨花の誕生日は2月20日です。
```

copilot instructionsのドキュメントを準備した。

{%preview https://github.com/YutaGoto/imasparql-mcp-server/pull/2 %}
