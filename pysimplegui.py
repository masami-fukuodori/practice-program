import PySimpleGUI as sg
from datetime import datetime 
import os

# 画面レイアウトを指定
layout = [
  [sg.Text('MEMO')],
  [sg.Text('メモ入力', size=(15,1)), sg.InputText('ここに入力')],
  [sg.Button('Resister')],
  [sg.Button('Save')]
  ]

# ウィンドウを表示する関数
def show_window():
  d = datetime.today()
  d = d.strftime('%Y-%m-%d')
  save_file = f'MEMO_{d}'
  print(save_file)

  memo = [d]

  win = sg.Window('MEMOapp', layout)
  # イベントループ
  while True:
    event, values = win.read()
    if event == sg.WINDOW_CLOSED:
          break
    elif event == 'Resister': 
        value = print_memo(values, memo)
        memo.append(value)
        
    elif event == 'Save':
          with open(save_file, 'w') as f:
            f.write(' '.join(memo))
            print('save')

def print_memo(values, memo):
      sg.popup(values[0], ' '.join(memo))
      
      return values[0]

show_window()