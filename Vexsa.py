import customtkinter as ctk
import threading
import pyautogui
import keyboard
import json
import os
import time
import sys
from PIL import Image, ImageTk
import tkinter as tk

SETTINGS_FILE = "netrix_settings.json"
ICON_FILE = "netrix_icon.ico"

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoadingScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Netrix VEXA Pro v5")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a1a')
        self.root.overrideredirect(True)
        self.center_window()
        
        try:
            if os.path.exists(ICON_FILE):
                self.root.iconbitmap(ICON_FILE)
        except:
            pass
        
        self.create_loading_ui()
        self.progress = 0
        self.loading_complete = False
        
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_loading_ui(self):
        main_frame = tk.Frame(self.root, bg='#1a1a1a', bd=2, relief='raised')
        main_frame.pack(fill='both', expand=True, padx=2, pady=2)
        
        title_label = tk.Label(main_frame, text="🎯 NETRIX VEXA PRO", 
                             font=("Arial Black", 20), 
                             fg='#00aaff', bg='#1a1a1a')
        title_label.pack(pady=30)
        
        version_label = tk.Label(main_frame, text="v5.0 - Premium Edition", 
                               font=("Arial", 12), 
                               fg='#888888', bg='#1a1a1a')
        version_label.pack(pady=5)
        
        self.loading_frame = tk.Frame(main_frame, bg='#1a1a1a')
        self.loading_frame.pack(pady=30)
        
        self.loading_text = tk.Label(self.loading_frame, text="🔄 Loading...", 
                                   font=("Arial", 14), 
                                   fg='#00aaff', bg='#1a1a1a')
        self.loading_text.pack()
        
        progress_bg = tk.Frame(main_frame, bg='#333333', height=6)
        progress_bg.pack(pady=10, padx=50, fill='x')
        
        self.progress_bar = tk.Frame(progress_bg, bg='#00aaff', height=6)
        self.progress_bar.pack(side='left', fill='y')
        
        self.status_text = tk.Label(main_frame, text="Initializing components...", 
                                  font=("Arial", 10), 
                                  fg='#aaaaaa', bg='#1a1a1a')
        self.status_text.pack(pady=10)
        
        copyright_label = tk.Label(main_frame, text="© 2024 Hexsa Technologies", 
                                 font=("Arial", 8), 
                                 fg='#666666', bg='#1a1a1a')
        copyright_label.pack(side='bottom', pady=10)
        
    def update_progress(self, value, status="Loading..."):
        self.progress = value
        total_width = 300
        bar_width = int((value / 100) * total_width)
        self.progress_bar.config(width=bar_width)
        self.status_text.config(text=status)
        dots = "." * (int(time.time() * 2) % 4)
        self.loading_text.config(text=f"🔄 Loading{dots}")
        self.root.update()
        
    def start_loading(self):
        loading_steps = [
            (20, "Loading libraries..."),
            (40, "Initializing GUI components..."),
            (60, "Setting up hotkey system..."),
            (80, "Loading user settings..."),
            (100, "Ready to launch!")
        ]
        
        for progress, status in loading_steps:
            self.update_progress(progress, status)
            time.sleep(0.8)
            
        self.loading_complete = True
        time.sleep(0.5)
        self.root.destroy()

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Netrix VEXA Pro v5")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#121212')
        
        self.set_window_icon()
        
        self.left_clicking = False
        self.right_clicking = False
        self.left_key = None
        self.right_key = None
        self.left_cps = 20
        self.right_cps = 20
        self.running = True
        self.is_setting_key = False
        
        self.left_click_thread = None
        self.right_click_thread = None
        self.hotkey_thread = None
        

        self.load_settings()
        self.build_ui()
        self.start_hotkey_listener()
        
    def set_window_icon(self):
        try:
            if os.path.exists(ICON_FILE):
                self.root.iconbitmap(ICON_FILE)
        except Exception as e:
            print(f"Icon loading failed: {e}")

    def build_ui(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Header
        header_frame = ctk.CTkFrame(self.root, corner_radius=20, fg_color="#1f1f1f", border_width=2, border_color="#00aaff")
        header_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        header_frame.grid_columnconfigure(0, weight=1)
        
        title_label = ctk.CTkLabel(header_frame, text="💎 NETRIX VEXA PRO 💎", 
                                  font=("Arial Black", 32, "bold"), 
                                  text_color="#00aaff")
        title_label.grid(row=0, column=0, pady=(15, 5))
        
        subtitle_label = ctk.CTkLabel(header_frame, text="Precision Auto-Clicker Suite", 
                                    font=("Arial", 14, "italic"), 
                                    text_color="#bbbbbb")
        subtitle_label.grid(row=1, column=0, pady=(0, 15))

        # Main Content Frame
        main_content_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        main_content_frame.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")
        main_content_frame.grid_columnconfigure((0, 1), weight=1)
        main_content_frame.grid_rowconfigure(0, weight=1)

        # Left Click Frame
        left_frame = ctk.CTkFrame(main_content_frame, corner_radius=15, fg_color="#1f1f1f", border_width=2, border_color="#00aaff")
        left_frame.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="nsew")
        left_frame.grid_columnconfigure(0, weight=1)
        left_frame.grid_rowconfigure(4, weight=1)

        # Right Click Frame
        right_frame = ctk.CTkFrame(main_content_frame, corner_radius=15, fg_color="#1f1f1f", border_width=2, border_color="#ff8800")
        right_frame.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="nsew")
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_rowconfigure(4, weight=1)

        # Left Click Config
        left_title = ctk.CTkLabel(left_frame, text="🖱️ LEFT CLICK", font=("Arial Black", 20), text_color="#00aaff")
        left_title.grid(row=0, column=0, pady=(15, 10))
        
        self.left_key_label = ctk.CTkLabel(left_frame, text=f"Hotkey: {self.format_key(self.left_key)}", font=("Arial", 14, "bold"))
        self.left_key_label.grid(row=1, column=0, pady=10)
        
        left_key_btn = ctk.CTkButton(left_frame, text="🎮 SET HOTKEY", command=lambda: self.set_key('left'), fg_color="#0088cc", hover_color="#00aaff", font=("Arial", 12, "bold"))
        left_key_btn.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        left_cps_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        left_cps_frame.grid(row=3, column=0, pady=(10, 5), padx=20, sticky="ew")
        left_cps_frame.grid_columnconfigure(0, weight=3)
        left_cps_frame.grid_columnconfigure(1, weight=1)
        
        self.left_cps_entry = ctk.CTkEntry(left_cps_frame, placeholder_text="Enter CPS (1-1000)", font=("Arial", 12), justify="center")
        self.left_cps_entry.grid(row=0, column=0, sticky="ew")
        self.left_cps_entry.bind("<Return>", lambda event: self.update_cps_from_entry('left'))

        left_cps_save_btn = ctk.CTkButton(left_cps_frame, text="💾 SAVE", command=lambda: self.update_cps_from_entry('left'), fg_color="#0088cc", hover_color="#00aaff", font=("Arial", 12, "bold"), width=70)
        left_cps_save_btn.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        
        self.left_cps_label = ctk.CTkLabel(left_frame, text=f"{self.left_cps} CPS", font=("Arial", 14, "bold"), text_color="#00ddff")
        self.left_cps_label.grid(row=4, column=0, pady=(5, 10))

        # Right Click Config
        right_title = ctk.CTkLabel(right_frame, text="🖱️ RIGHT CLICK", font=("Arial Black", 20), text_color="#ff8800")
        right_title.grid(row=0, column=0, pady=(15, 10))
        
        self.right_key_label = ctk.CTkLabel(right_frame, text=f"Hotkey: {self.format_key(self.right_key)}", font=("Arial", 14, "bold"))
        self.right_key_label.grid(row=1, column=0, pady=10)
        
        right_key_btn = ctk.CTkButton(right_frame, text="🎮 SET HOTKEY", command=lambda: self.set_key('right'), fg_color="#dd7700", hover_color="#ff8800", font=("Arial", 12, "bold"))
        right_key_btn.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        right_cps_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
        right_cps_frame.grid(row=3, column=0, pady=(10, 5), padx=20, sticky="ew")
        right_cps_frame.grid_columnconfigure(0, weight=3)
        right_cps_frame.grid_columnconfigure(1, weight=1)

        self.right_cps_entry = ctk.CTkEntry(right_cps_frame, placeholder_text="Enter CPS (1-1000)", font=("Arial", 12), justify="center")
        self.right_cps_entry.grid(row=0, column=0, sticky="ew")
        self.right_cps_entry.bind("<Return>", lambda event: self.update_cps_from_entry('right'))
        
        right_cps_save_btn = ctk.CTkButton(right_cps_frame, text="💾 SAVE", command=lambda: self.update_cps_from_entry('right'), fg_color="#dd7700", hover_color="#ff8800", font=("Arial", 12, "bold"), width=70)
        right_cps_save_btn.grid(row=0, column=1, padx=(10, 0), sticky="ew")

        self.right_cps_label = ctk.CTkLabel(right_frame, text=f"{self.right_cps} CPS", font=("Arial", 14, "bold"), text_color="#ffaa00")
        self.right_cps_label.grid(row=4, column=0, pady=(5, 10))

        # Status and Controls
        status_controls_frame = ctk.CTkFrame(self.root, corner_radius=15, fg_color="#1f1f1f", border_width=2, border_color="#555555")
        status_controls_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        status_controls_frame.grid_columnconfigure(0, weight=1)

        self.status_label = ctk.CTkLabel(status_controls_frame, text="Status: 💤 Idle", font=("Arial", 18, "bold"), text_color="gray")
        self.status_label.grid(row=0, column=0, pady=(15, 10))

        button_frame = ctk.CTkFrame(status_controls_frame, fg_color="transparent")
        button_frame.grid(row=1, column=0, pady=15)
        
        stop_btn = ctk.CTkButton(button_frame, text="⏹️ STOP ALL", fg_color="#cc0000", hover_color="#ff0000", command=self.stop_all_clicking, width=160, height=45, font=("Arial", 14, "bold"), corner_radius=10)
        stop_btn.pack(side="left", padx=15)
        
        reset_btn = ctk.CTkButton(button_frame, text="🔄 RESET", fg_color="#cc6600", hover_color="#ff8800", command=self.reset_settings, width=160, height=45, font=("Arial", 14, "bold"), corner_radius=10)
        reset_btn.pack(side="left", padx=15)

        # Footer
        footer_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        footer_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        footer_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(footer_frame, text="© 2025 Netrix Technologies - Premium Edition", font=("Arial", 10, "italic"), text_color="#666666").pack()

    def format_key(self, key):
        return "❌ NOT SET" if not key else f"🎯 {key.upper()}"

    def update_cps_from_entry(self, click_type):
        if click_type == 'left':
            entry = self.left_cps_entry
            label = self.left_cps_label
        else:
            entry = self.right_cps_entry
            label = self.right_cps_label
        
        try:
            cps_val = int(entry.get())
            if 1 <= cps_val <= 1000:
                if click_type == 'left':
                    self.left_cps = cps_val
                else:
                    self.right_cps = cps_val
                label.configure(text=f"{cps_val} CPS")
                self.save_settings()
                entry.delete(0, 'end')
                self.root.focus()
            else:
                entry.delete(0, 'end')
                entry.insert(0, "1-1000 only")
        except ValueError:
            entry.delete(0, 'end')
            entry.insert(0, "Invalid number")

    def set_key(self, click_type):
        if self.is_setting_key:
            return
        self.is_setting_key = True
        
        label = self.left_key_label if click_type == 'left' else self.right_key_label
        label.configure(text="🔴 Press any key...", text_color="red")
        self.root.update()
        threading.Thread(target=self._capture_key, args=(click_type,), daemon=True).start()

    def _capture_key(self, click_type):
        key_name = keyboard.read_key()

        # Using root.after to ensure GUI updates are thread-safe
        if click_type == 'left':
            self.left_key = key_name
            self.root.after(0, lambda: self.left_key_label.configure(text=f"Hotkey: {self.format_key(self.left_key)}", text_color="lime"))
            self.root.after(1500, lambda: self.left_key_label.configure(text_color="white"))
        else:
            self.right_key = key_name
            self.root.after(0, lambda: self.right_key_label.configure(text=f"Hotkey: {self.format_key(self.right_key)}", text_color="lime"))
            self.root.after(1500, lambda: self.right_key_label.configure(text_color="white"))
        
        self.save_settings()
        self.restart_hotkey_listener()

        # Wait for the key to be released before allowing hotkey checks again
        while True:
            try:
                if not keyboard.is_pressed(key_name):
                    break
                time.sleep(0.01)
            except:
                break # Stop if key check fails for any reason
        
        self.is_setting_key = False

    def hotkey_listener_loop(self):
        left_key_was_pressed = False
        right_key_was_pressed = False

        while self.running:
            if self.is_setting_key:
                time.sleep(0.02)
                continue
            
            try:
                # Left key handling
                if self.left_key and keyboard.is_pressed(self.left_key):
                    if not left_key_was_pressed:
                        self.root.after(0, self.toggle_left_click)
                    left_key_was_pressed = True
                else:
                    left_key_was_pressed = False
                
                # Right key handling
                if self.right_key and keyboard.is_pressed(self.right_key):
                    if not right_key_was_pressed:
                        self.root.after(0, self.toggle_right_click)
                    right_key_was_pressed = True
                else:
                    right_key_was_pressed = False
            except Exception:
                # This can happen if a key is not recognized by the library, e.g. during a key change.
                # It's safer to just continue the loop.
                pass
            
            time.sleep(0.02) # Check every 20ms

    def start_hotkey_listener(self):
        if self.hotkey_thread is None or not self.hotkey_thread.is_alive():
            self.hotkey_thread = threading.Thread(target=self.hotkey_listener_loop, daemon=True)
            self.hotkey_thread.start()

    def restart_hotkey_listener(self):
        # The listener loop is always running and will pick up the new key values.
        pass

    def toggle_left_click(self):
        self.left_clicking = not self.left_clicking
        if self.left_clicking:
            self.left_click_thread = threading.Thread(target=self.auto_click, args=('left',), daemon=True)
            self.left_click_thread.start()
        self.update_status()

    def toggle_right_click(self):
        self.right_clicking = not self.right_clicking
        if self.right_clicking:
            self.right_click_thread = threading.Thread(target=self.auto_click, args=('right',), daemon=True)
            self.right_click_thread.start()
        self.update_status()

    def auto_click(self, click_type):
        clicking_flag = 'left_clicking' if click_type == 'left' else 'right_clicking'
        cps = self.left_cps if click_type == 'left' else self.right_cps

        if cps <= 0:
            while getattr(self, clicking_flag) and self.running:
                time.sleep(0.1)
            return

        interval = 1.0 / cps
        next_click_time = time.time()

        while getattr(self, clicking_flag) and self.running:
            pyautogui.click(button=click_type)
            next_click_time += interval
            sleep_time = next_click_time - time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)

    def stop_all_clicking(self):
        self.left_clicking = False
        self.right_clicking = False
        self.update_status()

    def update_status(self):
        if self.left_clicking and self.right_clicking:
            self.status_label.configure(text="Status: 🔄 DUAL CLICKING", text_color="#00ff88")
        elif self.left_clicking:
            self.status_label.configure(text=f"Status: 🔁 LEFT ({self.left_cps} CPS)", text_color="#00aaff")
        elif self.right_clicking:
            self.status_label.configure(text=f"Status: 🔁 RIGHT ({self.right_cps} CPS)", text_color="#ffaa00")
        else:
            self.status_label.configure(text="Status: 💤 IDLE", text_color="gray")

    def save_settings(self):
        settings = {
            "left_key": self.left_key,
            "right_key": self.right_key,
            "left_cps": self.left_cps,
            "right_cps": self.right_cps
        }
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f, indent=4)

    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r") as f:
                    data = json.load(f)
                    self.left_key = data.get("left_key")
                    self.right_key = data.get("right_key")
                    self.left_cps = data.get("left_cps", 20)
                    self.right_cps = data.get("right_cps", 20)
            except (json.JSONDecodeError, KeyError):
                self.reset_to_defaults()
        else:
            self.reset_to_defaults()

    def reset_to_defaults(self):
        self.left_key = None
        self.right_key = None
        self.left_cps = 20
        self.right_cps = 20

    def reset_settings(self):
        self.stop_all_clicking()
        self.reset_to_defaults()
        self.save_settings()
        
        self.left_key_label.configure(text=f"Hotkey: {self.format_key(self.left_key)}")
        self.right_key_label.configure(text=f"Hotkey: {self.format_key(self.right_key)}")
        self.left_cps_label.configure(text=f"{self.left_cps} CPS")
        self.right_cps_label.configure(text=f"{self.right_cps} CPS")
        self.left_cps_entry.delete(0, 'end')
        self.right_cps_entry.delete(0, 'end')
        
        self.restart_hotkey_listener()
        self.update_status()

    def cleanup(self):
        self.running = False
        self.stop_all_clicking()
        self.root.quit()

def main():
    loading = LoadingScreen()
    loading.start_loading()
    
    if loading.loading_complete:
        root = ctk.CTk()
        app = AutoClickerApp(root)
        root.protocol("WM_DELETE_WINDOW", app.cleanup)
        root.mainloop()

if __name__ == "__main__":
    main()
