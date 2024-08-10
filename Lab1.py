import tkinter as tk
from tkinter import messagebox

def show_text():
    text = entry.get()
    messagebox.showinfo("Text Output", f"You entered: {text}")

def exit_program():
    root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Simple GUI")

# Tạo khung nhập văn bản
entry_label = tk.Label(root, text="Enter your text:")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Tạo nút hiển thị văn bản
show_button = tk.Button(root, text="Show Text", command=show_text)
show_button.pack(pady=10)

# Tạo nút thoát chương trình
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=10)

# Bắt đầu vòng lặp chính của giao diện
root.mainloop()
