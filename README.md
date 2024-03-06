# 画像のサイズをMB以上/以下にする
このプロジェクトは、アップロードした画像を指定されたファイルサイズにリサイズするアプリケーションです。Flaskフレームワークを使用しており、簡単にローカルで実行できます。

## 特徴
- 画像を指定のサイズ（MB単位）にリサイズします。
- 画質を段階的に下げることでファイルサイズを減らします。

## 前提条件
このアプリケーションを実行する前に、以下のツールがインストールされている必要があります。
- Python3
- Flask
- Pillow

## インストール方法
リポジトリをクローンして、必要な依存関係をインストールします。

```bash
git clone https://github.com/your-username/resize-image-app.git
cd resize-image-app
pip install -r requirements.txt
```
## 使用方法
アプリケーションを起動するには、以下のコマンドを実行してください。

```bash
python app.py
```
次に、ブラウザで http://127.0.0.1:5000/ を開いて、画像ファイルとファイルサイズをフォームに入力してボタンを押すと変換されるはずです。
