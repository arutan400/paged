1.	初期設定
・auto_setup(__file__, devices=["Android:///"])
	•	Airtest の環境をセットアップし、Android エミュレータ／実機に接続します。
	2.	汎用関数
・wait_and_touch(img_path, timeout=15, threshold=0.8)
	•	指定した画像が画面に出るまで待ち、タップします。
・skip_all(skip_imgs=("images/skip.png","images/next.png"))
	•	ムービーやポップアップを「スキップ」「次へ」で連打して読み飛ばします。
	3.	シナリオ開始
・start_ura(start_img="images/ura_start.png")
	•	URA 育成開始ボタンをタップし、続くムービーを skip_all() でスキップします。
	4.	イベント対応
・handle_event(option_img="images/event_option.png")
	•	通常イベントで常に同じ選択肢をタップします。
・handle_skill_event(skill_img="images/skill_option.png", confirm_img="images/confirm_skill.png")
	•	スキル獲得イベントで指定スキルを選び、確認までタップします。
・handle_support_event(support_img="images/support_event.png")
	•	サポートカードイベントで定型選択肢をタップします。
・handle_injury_event(injury_img="images/injury_event.png", treat_img="images/treat_injury.png")
	•	故障イベント発生時に「治療する」を選択してシナリオ継続を確保します。
	5.	体力管理
・rest_if_stamina_low(bar_img="images/stamina_blue.png", rest_img="images/rest.png")
	•	体力バーが青色（低下）を示す画像を検出したら「お休み」をタップして回復します。
	6.	練習選択
・select_speed_training(speed_img="images/train_speed.png", confirm_img="images/confirm.png")
	•	常に「スピード練習」を選択し、決定までタップします。
	7.	アイテム使用
・use_item(item_img="images/item_recovery.png", close_img="images/close_item.png")
	•	回復アイテムがあれば使用し、アイテム画面を閉じます。
	8.	レース処理
・skip_race_info(info_ok="images/info_ok.png")
	•	レース前の情報画面の「OK」をタップして読み飛ばします。
・race_sequence(race_start="images/race_start.png")
	•	レース開始ボタンをタップし、結果ムービーを skip_all()＋skip_race_info() でスキップします。
	9.	完了判定
・is_ura_finished(finish_img="images/ura_finish.png")
	•	URA シナリオ終了画面を検出したら True を返し、メインループを抜けるトリガーとします。
	10.	１ターンのまとめ処理
・process_turn()
	1.	skip_all()／skip_race_info() でムービー読み飛ばし
	2.	handle_event()／handle_skill_event()／handle_support_event()／handle_injury_event() で各種イベント対応
	3.	rest_if_stamina_low() で体力管理
	4.	select_speed_training() でスピード練習
	5.	use_item() でアイテム使用
	6.	race_sequence() でレース開始～結果スキップ
	11.	メインループ
・main()
	•	start_ura() で育成開始後、ターンをカウントしながら process_turn() を繰り返します。
	•	is_ura_finished() が True になったらループを抜けて終了処理を行います。
