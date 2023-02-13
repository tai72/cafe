# 【初めてのDjangoシリーズ】Django初学者向けに作成した記事のモデルサイト
![color:ff69b4](https://img.shields.io/badge/python-3.9-informational.svg?longCache=true)
![color:ff69b4](https://img.shields.io/badge/Django-v4.1.5-informational.svg?longCache=true)

---

## 概要

本プロジェクトは「初めてDjangoを用いてWebアプリケーションを作成したい」、そんな方向けに書いた紹介ブログのデモサイトです。

[デモサイト](https://cafe-project-377203.an.r.appspot.com)

記事は[こちら](https://bestrong-it-men.com/django-app-tutorial-introduction-1/)です。

## 使用技術

- Python 3.9
- Django 4.1.5
- GCP
    - GAE
    - PostgreSQL
    
## ローカル環境での始め方

### パッケージのインストール

```shell
pip install django
pip install psycopg2-binary
pip install django-allauth
pip install Pillow
pip install gunicorn
```


### settings.jsonの作成

プロジェクトのルートディレクトリに**settings.json**を作成します。Djangoプロジェクトで使用する機密情報を分離しています。

```json
{
    "SECRET_KEY":"<Djangoプロジェクトのシークレットキー>",
    "EMAIL_HOST":"<Googleアカウントのメールアドレス>",
    "EMAIL_OUTLOOK":"<Outlookのメールアドレス（あれば）>",
    "EMAIL_HOST_PASS":"<Googleのアプリパスワード>",
    "DB_USER": "<postgreSQLのユーザー名>",
    "DB_PASSWORD": "<postgreSQLのパスワード>"
}
```


### データベースの設定

ローカル環境にてデータベース（postgreSQL）の設定を行います。

[こちら](https://bestrong-it-men.com/django-app-tutorial-development-1/)を参考に行います。


### ローカルサーバーの立ち上げ

ローカルサーバーを起動します。

ターミナルにてDjangoプロジェクトのルートディレクトリに移動し、下記のコマンドを実行します。

```shell
python manage.py runserver
```

その後 http://127.0.0.1:8000 にアクセスします。

<img width="1440" alt="スクリーンショット 2023-02-13 20 06 22" src="https://user-images.githubusercontent.com/99964360/218442091-1ca0ec45-a929-4db5-a224-3c2c16e11e0c.png">
