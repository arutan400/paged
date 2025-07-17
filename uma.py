# -*- encoding=utf8 -*-
from airtest.core.api import (
    auto_setup, connect_device,
    Template, exists, touch,
    wait, sleep
)
import time

# ── 初期設定 ──
auto_setup(__file__, devices=["Android:///"])  # Androidデバイス（エミュレータ／実機）に接続

# ── 汎用操作関数 ──
def wait_and_touch(img_path, timeout=15, threshold=0.8):
    """指定画像が表示されるまで待ってタップ"""
    wait(Template(img_path, threshold=threshold), timeout=timeout)
    touch(Template(img_path, threshold=threshold))
    sleep(0.5)

def skip_all(skip_imgs=("images/skip.png", "images/next.png")):
    """スキップ／次へボタンを連打"""
    for img in skip_imgs:
        while exists(Template(img, threshold=0.8)):
            touch(Template(img, threshold=0.8))
            sleep(0.3)

# ── URAシナリオ開始 ──
def start_ura():
    """URAシナリオの開始ボタンをタップ"""
    wait_and_touch("images/ura_start.png")  # URA育成開始画面
    skip_all()

# ── イベント対応 ──
def handle_event(option_img="images/event_option.png"):
    """割り込みイベントで常に同じ選択肢をタップ"""
    if exists(Template(option_img, threshold=0.8)):
        touch(Template(option_img, threshold=0.8))
        sleep(0.5)

# ── 体力管理 ──
def rest_if_stamina_low(bar_img="images/stamina_blue.png", rest_btn="images/rest.png"):
    """体力バーが青いときお休みをタップ"""
    if exists(Template(bar_img, threshold=0.8)):
        if exists(Template(rest_btn, threshold=0.8)):
            touch(Template(rest_btn, threshold=0.8))
        else:
            # ボタン位置が固定なら座標タップでも可 (例)
            touch((540, 1700))
        sleep(0.5)

# ── スピード練習選択 ──
def select_speed_training(train_img="images/train_speed.png", confirm_img="images/confirm.png"):
    """常にスピード練習を選択して決定"""
    if exists(Template(train_img, threshold=0.8)):
        touch(Template(train_img, threshold=0.8))
        sleep(0.3)
        if exists(Template(confirm_img, threshold=0.8)):
            touch(Template(confirm_img, threshold=0.8))
            sleep(0.5)

# ── レーススキップ ──
def race_sequence(race_btn="images/race_start.png"):
    """レース開始＆結果スキップ"""
    if exists(Template(race_btn, threshold=0.8)):
        touch(Template(race_btn, threshold=0.8))
        sleep(1)
    skip_all()

# ── URA完了判定 ──
def is_ura_finished(finish_img="images/ura_finish.png"):
    """URAシナリオ完了画面を検出"""
    return exists(Template(finish_img, threshold=0.8))

# ── メインループ ──
def main():
    start_ura()
    turn = 0
    while True:
        turn += 1
        print(f"{turn}ターン目実行中…")
        skip_all()
        if is_ura_finished():
            print("🎉 URAシナリオ完遂！")
            break
        handle_event()
        rest_if_stamina_low()
        select_speed_training()
        race_sequence()
    print("スクリプト終了")

if __name__ == "__main__":
    main()