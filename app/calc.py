import math
"""
def divide(x, y):
    return x / y

def save_to_file(path, content):
    with open(path, "w") as f:
        f.write(content)

def sin_deg(degree):
    #角度をラジアンに変換してsin計算
    return math.sin(math.radians(degree))

def buggy_feature():
    #既知のバグがある仮の機能
    return 1 / 0
"""
def notify_user(user, send_func):
    #ユーザーに通知を送る（外部依存あり）
    body = f"Hi {user}, welcome!"
    send_func(user, body)
