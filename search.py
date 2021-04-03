import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word,csv_name,csv_name_add):
    # 検索対象取得
    df=pd.read_csv(f"./{csv_name}")
    source=list(df["name"])
    # 検索
    if csv_name == '':
        eel.view_log_js("CSVファイル名を入力してください")
        return False
    elif word == '':
        eel.view_log_js("検索ワードを入力してください")
        return False
    elif word in source:
        print(f"『{word}』はあります")
        eel.view_log_js(f"『{word}』はあります")
    elif csv_name_add=='':
        print(f"『{word}』はありません")
        eel.view_log_js(f"『{word}』はありません")
        eel.view_log_js(f"『{word}』を追加する場合は1を入力して再度検索ボタンを押してください")
    elif int(csv_name_add) == 1:
        eel.view_log_js(f"『{word}』を追加しました")
        source.append(word)
    else:
        eel.view_log_js(f"『{csv_name_add}』は無効です")
        
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv(f"./{csv_name}", encoding="utf_8-sig")
    print(source)
