# TMG-ToDo

## 準備

### MySQL
MySQLサーバを立ち上げる
```
$ mysql.server start
```
MySQLサーバを止める
```
$ mysql.server stop
```

### Python
環境構築
```
$ pipenv install
```
仮想環境を立ち上げる
```
$ pipenv shell
```

APIサーバを立ち上げる
```
$ pipenv run tmg
```
上記で失敗した場合
```
$ pipenv run python api.py
```

## テストサンプル

### curl
POSTテスト用サンプル
```
$ curl http://127.0.0.1:5000/task -X POST -H "Content-Type: application/json" --data '{"title": "title X", "context": "context X", "limit_date": "2020-07-31 23:59:59"}'
```

UPDATEテスト用サンプル
```
curl http://127.0.0.1:5000/task/5 -X POST -H "Content-Type: application/json" --data '{"id": "1", "title": "title update", "context": "context update", "done": "1", "limit_date": "2020-07-31 23:59:59"}'
```