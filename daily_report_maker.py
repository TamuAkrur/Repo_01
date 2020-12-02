# 日報 Maker
import datetime

# 作成者
writer = 'グルン'
writer_fullname = 'グルンアクル－ル'
# 社員番号
emp_id = '「000755」'
# 現在の時間
today = datetime.date.today()
# 日付カストマイズ
custom_dateformat = str(today.year) + '/' + str('%02d' %today.month) + '/' + str('%02d' % today.day)
# メ－ル＿タイトル
mail_title = '【業務日報】' + writer_fullname + ' ' + custom_dateformat
print(mail_title)
# メ－ル内容
mail_template = '各位\n\nお疲れ様です。' + writer + emp_id + 'です。\n\
本日：' + custom_dateformat + ' の業務報告を致します。\n\
\n\
１.実績\n\
　⇒今日の業務実績を記載願います。\n\
\n\
２.予定\n\
　⇒明日の業務予定や今後の休暇予定等を記載願います。\n\
\n\
３.問題課題\n\
　⇒問題や課題を記載願います。\n\
\n\
４.その他\n\
　⇒何か質問、意見、確認などがあれば記載願います。'

print(mail_template)
