import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# --- НАСТРОЙКИ СЕРВЕРА STANT RUSSIA ---
SERVER_IP = "IP_твоего_сервера"  # ЗАМЕНИ на реальный IP
SERVER_PORT = "7777"              # ЗАМЕНИ на реальный порт

class StantRussiaLauncher:
    def __init__(self, master):
        self.master = master
        master.title("Stant Russia Launcher")
        master.geometry("400x250")

        self.label = tk.Label(master, text="Добро пожаловать в Stant Russia!", font=("Arial", 12))
        self.label.pack(pady=10)

        self.path_frame = tk.Frame(master)
        self.path_frame.pack(pady=5)
        self.path_label = tk.Label(self.path_frame, text="Путь к samp.exe:")
        self.path_label.pack(side=tk.LEFT)
        self.path_entry = tk.Entry(self.path_frame, width=30)
        self.path_entry.pack(side=tk.LEFT, padx=5)
        self.browse_button = tk.Button(self.path_frame, text="Обзор", command=self.browse_file)
        self.browse_button.pack(side=tk.LEFT)

        self.nick_frame = tk.Frame(master)
        self.nick_frame.pack(pady=5)
        self.nick_label = tk.Label(self.nick_frame, text="Ваш никнейм:")
        self.nick_label.pack(side=tk.LEFT)
        self.nick_entry = tk.Entry(self.nick_frame)
        self.nick_entry.pack(side=tk.LEFT, padx=5)

        self.launch_button = tk.Button(master, text="ЗАПУСТИТЬ ИГРУ", command=self.launch_game, bg="green", fg="white", font=("Arial", 10, "bold"))
        self.launch_button.pack(pady=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Выберите samp.exe", filetypes=[("Executable files", "*.exe")])
        if file_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, file_path)

    def launch_game(self):
        game_path = self.path_entry.get()
        nickname = self.nick_entry.get()

        if not game_path or not nickname:
            messagebox.showerror("Ошибка", "Укажите путь к игре и никнейм!")
            return

        command = f'"{game_path}" -c -n "{nickname}" -h {SERVER_IP} -p {SERVER_PORT} -loadsamp'

        try:
            subprocess.Popen(command, shell=True)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось запустить игру: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    launcher = StantRussiaLauncher(root)
    root.mainloop()
