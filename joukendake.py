# -*- encoding=utf8 -*-
from airtest.core.api import *
auto_setup(__file__, devices=["Android:///"])

import time

# スクリプト開始直後の画面でタップ（必要に応じて）
if exists(Template("images/ura_start.png")):
    touch(Template("images/ura_start.png"))
    time.sleep(1)

# 30ターン前後の仮ループ（途中終了してもOK）
for i in range(35):
    print(f"{i+1}ターン目")

    # イベント選択肢が出たら押す
    if exists(Template("images/event_option.png", threshold=0.8)):
        touch(Template("images/event_option.png", threshold=0.8))
        time.sleep(0.5)

    # スキルイベントが出たら選択 → 決定
    if exists(Template("images/skill_option.png", threshold=0.8)):
        touch(Template("images/skill_option.png", threshold=0.8))
        time.sleep(0.5)
    if exists(Template("images/confirm_skill.png", threshold=0.8)):
        touch(Template("images/confirm_skill.png", threshold=0.8))
        time.sleep(0.5)

    # 故障イベントが出たら治療する
    if exists(Template("images/injury_event.png", threshold=0.8)):
        touch(Template("images/treat_injury.png", threshold=0.8))
        time.sleep(0.5)

    # サポートイベントが出たら選択肢をタップ
    if exists(Template("images/support_event.png", threshold=0.8)):
        touch(Template("images/support_event.png", threshold=0.8))
        time.sleep(0.5)

    # 青体力バーが出ていたら休む
    if exists(Template("images/stamina_blue.png", threshold=0.8)):
        if exists(Template("images/rest.png", threshold=0.8)):
            touch(Template("images/rest.png", threshold=0.8))
            time.sleep(1)

    # スピード練習が可能なら選んで決定
    if exists(Template("images/train_speed.png", threshold=0.8)):
        touch(Template("images/train_speed.png", threshold=0.8))
        time.sleep(0.5)
        if exists(Template("images/confirm.png", threshold=0.8)):
            touch(Template("images/confirm.png", threshold=0.8))
            time.sleep(1)

    # レース開始が出ていたら出走してスキップ
    if exists(Template("images/race_start.png", threshold=0.8)):
        touch(Template("images/race_start.png", threshold=0.8))
        time.sleep(1)

    # レース情報OKボタン
    if exists(Template("images/info_ok.png", threshold=0.8)):
        touch(Template("images/info_ok.png", threshold=0.8))
        time.sleep(0.5)

    # スキップ／次へ 連打
    if exists(Template("images/skip.png", threshold=0.8)):
        touch(Template("images/skip.png", threshold=0.8))
        time.sleep(0.3)
    if exists(Template("images/next.png", threshold=0.8)):
        touch(Template("images/next.png", threshold=0.8))
        time.sleep(0.3)

print("自動育成終了（途中でも終了OK）")