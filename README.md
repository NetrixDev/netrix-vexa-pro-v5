# 🎯 Netrix Vexta Pro v5

Netrix Vexta Pro v5 is a high-performance and beautifully designed auto-clicker application for Windows built using Python and `customtkinter`.

## ✨ Features
- 🔥 Dual click modes (Left / Right)
- 💾 Custom CPS (Clicks Per Second)
- 🎮 Hotkey support for each click type
- 🌙 Beautiful dark-themed modern GUI
- 🧠 Saves and loads settings automatically
- 💻 Built with `customtkinter`, `pyautogui`, `keyboard`

<div align="center">

<img src="https://github.com/user-attachments/assets/8351bfa9-e682-430a-87d9-8f5c8a5cea83" width="600" alt="Netrix Vexta GUI" style="border-radius: 12px; box-shadow: 0 0 10px rgba(255,255,255,0.2);" />

<br><br>

<img src="https://github.com/user-attachments/assets/7cb6bb6d-19ea-40b4-9405-a29fc6c2c0c2" width="600" alt="Netrix Vexta Features" style="border-radius: 12px; box-shadow: 0 0 10px rgba(255,255,255,0.2);" />

</div>



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
