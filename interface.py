import tkinter as tk
from tkinter import messagebox
from main import parse_group

def start_parsing():
    username = entry_username.get()
    password = entry_password.get()
    group_url = entry_group_url.get()
    limit = int(entry_limit.get())
    hours = int(entry_hours.get())

    try:
        parse_group(username, password, group_url, limit, hours)
        messagebox.showinfo("Info", "Парсинг завершен.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Создание пользовательского интерфейса
root = tk.Tk()
root.title("Facebook Parser")

tk.Label(root, text="Email:").grid(row=0)
tk.Label(root, text="Password:").grid(row=1)
tk.Label(root, text="Group URL:").grid(row=2)
tk.Label(root, text="Limit (N):").grid(row=3)
tk.Label(root, text="Hours (H):").grid(row=4)

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
entry_group_url = tk.Entry(root)
entry_limit = tk.Entry(root)
entry_hours = tk.Entry(root)

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
entry_group_url.grid(row=2, column=1)
entry_limit.grid(row=3, column=1)
entry_hours.grid(row=4, column=1)

tk.Button(root, text="Start", command=start_parsing).grid(row=5, column=1, pady=4)

root.mainloop()
