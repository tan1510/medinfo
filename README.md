# medinfo

## 機能(やりたいこと)
* db構築
* ペプチド配列のあいまい検索
* 配列の質量からフラグメントで近い質量をもつものを検索する
+ 先にこちらをつかってある程度検索して絞りこむことができないか
+ 今の所トリプシンの’Kおよび'R'の部分で切断されている場合のみを考慮している

### ペプチドの配列分解
test_searchディレクトリのaimai.pyとsearch_mass.pyでそれぞれあいまい検索と

## データベースの構成
1. Entryを主キーとし、それに対応するアミノ酸配列とその長さのテーブル
2. そのEntryと何番目の部分配列かという組み合わせで複合機キーをなし部分配列とその重さ
## resources
### uniprot_fragment_csv
swiss-protの人かつレビュー済みのデータ
### sequence.txt
自作の検索スクリプトのテストにuniprot_fragment.csvのSEQUENCEタグの部分だけ１０００個が入ったテキストデータ

## connecter
基本的にmysql操作してデータベースの作成が目的
### 前準備
config.pyを以下のようにして  connectorディレクトリに作成
```config.py
config = { 'host' : 'localhost',
           'user' : 'user',
           'password' : 'pass',
           'database' : 'use db',
           }

host='locahost'
user='uset'
password='pass'
db='db name'  
```

userなどの変数を環境に合わせて設定

## todo
* データベースの構築する場合コンソールでMysql立ち上げてテーブル作ってread_sequence.pyのmainを逐次必要なメソッドを呼び出すように切り替えるがあるので普通にread_sequence.pyを引数与えて実行するだけでやれるようにしたい
* データベースの部分配列を格納するテーブルのカラムs-pos,g-posの要素が全て0 になってる　　　修正したけど実行結果確認してない
* 部分配列格納するほうのDBの作成でかなり時間を食っている
** pythonで文字列の置き換え、分割してる部分の改善とそもそも実行環境が思い可能性
* 
### 現状
read_sequence.pyはテーブルにデータを設定する処理は書けてはいるがテーブルの追加自体は普通にコンソールでやってしまっていたので
