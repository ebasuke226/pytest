import pytest
from app import calc
"""
# --- ケース3：アサーションと失敗メッセージ ---
def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(10, 5) == 3
# --- ケース4：fixtureでファイル操作を共通化 ---

#@pytest.fixture
#def tmpfile(tmp_path):
#    return tmp_path / "output.txt"
#
#def test_save_to_file(tmpfile):
#    calc.save_to_file(tmpfile, "hello world")
#    with open(tmpfile) as f:
#        assert f.read() == "hello world"
@pytest.fixture(params=[
    (10, 2, 5),
    (20, 4, 5),
    (-9, -3, 3),
])
def division_case(request):
    #被除数, 除数, 期待値) を返す
    return request.param

def test_divide_fixture(division_case):
    x, y, expected = division_case
    assert calc.divide(x, y) == expected


# --- ケース5：パラメタライズ ---
#@pytest.mark.parametrize(
#    ("degree", "expected"),
#    [(0, 0), (90, 1), (180, 0), (270, -1)],
#)
#def test_sin_deg(degree, expected):
#    assert round(calc.sin_deg(degree)) == expected
@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (10, 2, 5),
        (20, 4, 5),
        (9, 3, 3),
        (-8, -2, 4),
        (0, 5, 0)
    ]
)

def test_divide_parametrize(x, y, expected):
    assert calc.divide(x, y) == expected

# --- ケース6：スキップ / 期待失敗 ---
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Windowsでは実行不可")
def test_not_on_windows():
    assert True  # ここではOKとする

@pytest.mark.xfail(reason="buggy_featureはまだ修正されていない")
def test_buggy_feature():
    calc.buggy_feature()

# --- ケース7：pytest.ini で slow マーカーを利用 ---
@pytest.mark.slow
def test_slow_calc():
    import time
    time.sleep(1.1)  # 1秒超え
    assert True
"""
# --- ケース9：モック・スタブ（pytest-mock使用） ---
def test_notify_user(mocker):
    mock_sender = mocker.Mock()
    calc.notify_user("alice", send_func=mock_sender)
    mock_sender.assert_called_once_with("alice", "Hi alice, welcome!")

