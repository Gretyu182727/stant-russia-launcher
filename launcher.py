import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import webbrowser
import os

# --- ССЫЛКИ ПРОЕКТА STANT RUSSIA ---
TELEGRAM_URL = "https://t.me/stantrusiaonline"
VK_CHAT_URL = "https://vk.me/join/2qA4rNyv1g4pI6awCtfyO34Kcy0J6VdYRS8="
GAME_DOWNLOAD_URL = "https://disk.yandex.ru/d/pTV9wW6AnsihJA"

# --- НАСТРОЙКИ СЕРВЕРА (пока заглушка) ---
SERVER_IP = "IP_твоего_сервера"
SERVER_PORT = "7777"

class StantRussiaLauncher:
    def __init__(self, master):
        self.master = master
        master.title("Stant Russia Launcher")
        master.geometry("450x400")
        master.configure(bg="#1a1a2e")

        self.title_label = tk.Label(
            master, 
            text="🔥 STANT RUSSIA 🔥", 
            font=("Arial", 16, "bold"), 
            fg="#ff6b00", 
            bg="#1a1a2e"
        )
        self.title_label.pack(pady=15)

        self.social_frame = tk.Frame(master, bg="#1a1a2e")
        self.social_frame.pack(pady=10)

        self.tg_button = tk.Button(
            self.social_frame, 
            text="📱 Telegram", 
            command=lambda: webbrowser.open(TELEGRAM_URL),
            bg="#0088cc", fg="white", width=15
        )
        self.tg_button.pack(side=tk.LEFT, padx=5)

        self.vk_button = tk.Button(
            self.social_frame, 
            text="💬 Беседа ВК", 
            command=lambda: webbrowser.open(VK_CHAT_URL),
            bg="#4a76a8", fg="white", width=15
        )
        self.vk_button.pack(side=tk.LEFT, padx=5)

        self.download_button = tk.Button(
            master, 
            text="⬇️ Скачать игру", 
            command=lambda: webbrowser.open(GAME_DOWNLOAD_URL),
            bg="#ff6b00", fg="white", font=("Arial", 11, "bold"), width=30
        )
        self.download_button.pack(pady=10)

        self.sep = tk.Label(master, text="─" * 40, fg="#444", bg="#1a1a2e")
        self.sep.pack(pady=5)

        self.path_frame = tk.Frame(master, bg="#1a1a2e")
        self.path_frame.pack(pady=5)
        self.path_label = tk.Label(self.path_frame, text="Путь к samp.exe:", fg="white", bg="#1a1a2e")
        self.path_label.pack(side=tk.LEFT)
        self.path_entry = tk.Entry(self.path_frame, width=25)
        self.path_entry.pack(side=tk.LEFT, padx=5)
        self.browse_button = tk.Button(self.path_frame, text="Обзор", command=self.browse_file)
        self.browse_button.pack(side=tk.LEFT)

        self.nick_frame = tk.Frame(master, bg="#1a1a2e")
        self.nick_frame.pack(pady=5)
        self.nick_label = tk.Label(self.nick_frame, text="Ваш никнейм:", fg="white", bg="#1a1a2e")
        self.nick_label.pack(side=tk.LEFT)
        self.nick_entry = tk.Entry(self.nick_frame)
        self.nick_entry.pack(side=tk.LEFT, padx=5)

        self.launch_button = tk.Button(
            master, 
            text="▶️ ЗАПУСТИТЬ ИГРУ", 
            command=self.launch_game, 
            bg="#00aa00", fg="white", font=("Arial", 12, "bold"), width=25
        )
        self.launch_button.pack(pady=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Выберите samp.exe", 
            filetypes=[("Executable files", "*.exe")]
        )
        if file_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, file_path)

    def launch_game(self):
        game_path = self.path_entry.get()
        nickname = self.nick_entry.get()

        if not game_path or not nickname:
            messagebox.showerror("Ошибка", "Укажите путь к игре и никнейм!")
            return

        if not os.path.exists(game_path):
            messagebox.showerror("Ошибка", "Файл samp.exe не найден по указанному пути!")
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
