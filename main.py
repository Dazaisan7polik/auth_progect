import tkinter as tk
from tkinter import messagebox
from db import get_user

def login():
    username_val = entry_username.get()
    password_val = entry_password.get()

    if not username_val or not password_val:
        messagebox.showwarning("Внимание", "Заполните логин и пароль!")
        return

    user = get_user(username_val, password_val)
    
    if user:
        show_feed(user.role)
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль!")

def show_feed(role):
    # Очищаем окно
    for widget in root.winfo_children():
        widget.destroy()
    
    role_text = "гость" if role == "гость" else role
    
    tk.Label(root, text=f"Вы вошли как {role_text}.", font=("Arial", 20)).pack(pady=30)
    tk.Label(root, text="Здесь будет лента", font=("Arial", 12)).pack(pady=10)
    tk.Button(root, text="Вернуться ко входу", command=restart).pack(pady=30)


def restart():
    for widget in root.winfo_children():
        widget.destroy()
    build_login_ui()


def build_login_ui():
    global entry_username, entry_password
    
    tk.Label(root, text="Вход", font=("Arial", 24)).pack(pady=20)
    
    tk.Label(root, text="Логин:").pack()
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)
    
    tk.Label(root, text="Пароль:").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)
    
    tk.Button(root, text="Войти", command=login, width=15).pack(pady=15)
    tk.Button(root, text="Войти как гость", command=lambda: show_feed("гость"), width=15).pack()

# Настройка окна
root = tk.Tk()
root.title("Форма входа")
root.geometry("400x400")

# Запуск
build_login_ui()
root.mainloop()