# Python 3.11 slim + pytest, ここだけで完結
FROM python:3.11-slim

# システムツール（任意） & Poetry などを使わない最小構成
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# 依存ライブラリを一括インストール
RUN pip install --no-cache-dir \
      pytest \
      pytest-cov \
      pytest-mock

# 作業ディレクトリ
WORKDIR /code
COPY . /code
