import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import numpy as np

# ウェブカメラの初期化
cap = cv2.VideoCapture(0)

# ウィンドウの作成
root = tk.Tk()
root.title('Dot Detection')

# キャンバスの作成（ウェブカメラ画像用）
canvas = tk.Canvas(root, width=640, height=480)
canvas.grid(row=0, column=0)

# 情報表示用テキストボックス
text_info = tk.Text(root, height=10, width=50)
text_info.grid(row=1, column=0)

# 色を変更する関数
def change_color(color):
    root.configure(bg=color)
    root.update()
    ret, frame = cap.read()
    analyze_frame(frame, color)

# フレームを解析する関数
def analyze_frame(frame, color):
    # ここに解析コードを書く
    # 現在はキャプチャしたフレームを表示するだけ
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    image_tk = ImageTk.PhotoImage(image=image)
    canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
    text_info.delete(1.0, tk.END)
    text_info.insert(tk.END, f"Changed to {color}")

# ボタン作成
button1 = ttk.Button(root, text='White', command=lambda: change_color('white'))
button1.grid(row=0, column=1)
button2 = ttk.Button(root, text='Black', command=lambda: change_color('black'))
button2.grid(row=1, column=1)
button3 = ttk.Button(root, text='Red', command=lambda: change_color('red'))
button3.grid(row=2, column=1)
button4 = ttk.Button(root, text='Green', command=lambda: change_color('green'))
button4.grid(row=3, column=1)

root.mainloop()

# ウェブカメラの解放
cap.release()
cv2.destroyAllWindows()
