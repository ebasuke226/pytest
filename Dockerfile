FROM python:3.11-slim

# システム依存のビルドパッケージ（pytest-mock が依存することあり）
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを指定
WORKDIR /code

# 依存ライブラリを先にコピー
COPY requirements.txt .

# Python ライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをすべてコピー
COPY . .

# app モジュールを見つけやすくするために PYTHONPATH を明示
ENV PYTHONPATH=/code
