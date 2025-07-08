# 🎯 Netrix Vexta Pro v5

Netrix Vexta Pro v5 is a high-performance and beautifully designed auto-clicker application for Windows built using Python and `customtkinter`.

## ✨ Features
- 🔥 Dual click modes (Left / Right)
- 💾 Custom CPS (Clicks Per Second)
- 🎮 Hotkey support for each click type
- 🌙 Beautiful dark-themed modern GUI
- 🧠 Saves and loads settings automatically
- 💻 Built with `customtkinter`, `pyautogui`, `keyboard`

## 🚀 Setup Instructions

1. **Clone the repository Using PowerShell**
```bash
git clone https://github.com/NetrixDev/netrix-vexta-pro-v5.git
cd netrix-vexta-pro-v5
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --icon=netrix_icon.ico Vexta.py
copy netrix_icon.ico dist\
cd dist
.\Vexta.exe
```
🛠 Output Path:
Your .exe file will be located in the dist/ folder after building.
And Copy the natrix_icon.ico file and paste it to your exe file location.
