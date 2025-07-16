# paged
# -*- encoding=utf8 -*-
from airtest.core.api import auto_setup, connect_device, Template, exists, touch, wait, swipe
from poco.drivers.unity3d import UnityPoco
import time

# ── 初期設定 ──
auto_setup(__file__, devices=["Android:///"])    # エミュレータ or 実機を接続
poco = UnityPoco()                              # UnityPoco ドライバを初期化

# ── 汎用操作関数 ──
def wait_and_touch(img_path, timeout=15, threshold=0.8):
    """画像が出るまで待ってタップ"""
    wait(Template(img_path, threshold=threshold), timeout=timeout)
    touch(Template(img_path, threshold=threshold))
    time.sleep(1)

def skip_all():
    """スキップや次へボタンを連打"""
    for btn in ["images/skip.png", "images/next.png"]:
        while exists(Template(btn, threshold=0.8)):
            touch(Template(btn, threshold=0.8))
            time.sleep(0.5)

# ── 育成シナリオ操作 ──
def start_training():
    """育成開始ボタンを押す"""
    if poco(name="育成開始").exists():
        poco(name="育成開始").click()
    else:
        wait_and_touch("images/start_training.png")
    time.sleep(2)

def select_training():
    """毎ターントレーニング選択"""
    # ① スピード優先
    if poco(text="スピード").exists():
        poco(text="スピード").click()
    # ② スタミナ
    elif poco(text="スタミナ").exists():
        poco(text="スタミナ").click()
    # ③ 保健室
    elif poco(text="保健室").exists():
        poco(text="保健室").click()
    # ④ 休む（スクロール→タップ）
    else:
        swipe((300, 1600), (300, 400), duration=0.5)
        time.sleep(1)
        poco(text="休む").click()
    time.sleep(1)
    # 決定ボタン
    if poco(text="決定").exists():
        poco(text="決定").click()
    else:
        touch(Template("images/confirm.png"))
    time.sleep(1)

def race_sequence():
    """レース開始＆スキップ"""
    if poco(text="レース開始").exists():
        poco(text="レース開始").click()
        time.sleep(1)
    skip_all()

# ── メイン処理 ──
def main(turns=30):
    start_training()
    for i in range(turns):
        print(f"{i+1}ターン目")
        skip_all()
        race_sequence()
        select_training()
    print("育成完了！")

if __name__ == "__main__":
    main(30)