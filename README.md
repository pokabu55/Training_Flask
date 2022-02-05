# Training_Flask
flaskのトレーニング用

## 環境構築
* 多分、gitignore のせいで、そのままだと動かせない？
### 手順
1. Python の インストール
2. このリポジトリのディレクトリに移動
3. 仮想環境の構築 `$ python3 -m venv venv`
4. 仮想環境のアクティベート `. venv/bin/activate` 次章に記載してるね
5. flask のインストール `(venv) $ pip install flask`

## venv の起動
* VSCode の起動で自動で切り替わらない場合は、端末で
* `. venv/bin/activate` と打つ または `source venv/bin/activate`
* 手動で venv を無効にする場合は
* `(venv) $ deactivate` と打つ

## サーバーの起動
* `python ***.py` で実行すると起動
* 設定しなければ `http://127.0.0.1:5000` でWebアプリが起動
* サーバーを止める場合、VSCODEのターミナルで `ctrl + c`

## 参考
* [ここ](https://tech-diary.net/flask-introduction/)を参考にしてます
* 