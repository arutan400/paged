# -*- encoding=utf8 -*-
from airtest.core.api import *
auto_setup(__file__, devices=["Android:///"])

import time

# ----------------------------------------
# 🔧 汎用タップ関数
# ----------------------------------------
def tap_if_exists(image_path, threshold=0.8, wait=0.5):
    if exists(Template(image_path, threshold=threshold)):
        touch(Template(image_path, threshold=threshold))
        time.sleep(wait)

# ----------------------------------------
# 🎭 イベント処理（選択肢やスキル、故障対応）
# ----------------------------------------
def handle_event():
    tap_if_exists("images/event_option.png")
    tap_if_exists("images/skill_option.png")
    tap_if_exists("images/confirm_skill.png")
    tap_if_exists("images/support_event.png")
    tap_if_exists("images/injury_event.png")
    tap_if_exists("images/treat_injury.png")

# ----------------------------------------
# 💪 トレーニング or お休みの選択
# ----------------------------------------
def handle_training():
    if exists(Template("images/stamina_blue.png", threshold=0.8)):
        tap_if_exists("images/rest.png")
    elif exists(Template("images/train_speed.png", threshold=0.8)):
        touch(Template("images/train_speed.png"))
        time.sleep(0.3)
        tap_if_exists("images/confirm.png")

# ----------------------------------------
# 🏇 レース処理
# ----------------------------------------
def handle_race():
    tap_if_exists("images/race_start.png")
    tap_if_exists("images/info_ok.png")

# ----------------------------------------
# ⏩ スキップ処理
# ----------------------------------------
def handle_skip():
    tap_if_exists("images/skip.png", wait=0.2)
    tap_if_exists("images/next.png", wait=0.2)

# ----------------------------------------
# 🔁 メイン育成ループ
# ----------------------------------------
for i in range(35):
    print(f"📘 {i+1}ターン目")
    handle_event()
    handle_training()
    handle_race()
    handle_skip()

print("✅ 育成終了（途中終了でもOK）")