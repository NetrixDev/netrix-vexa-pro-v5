# 🎯 Netrix Vexta Pro v5

Netrix Vexta Pro v5 is a high-performance and beautifully designed auto-clicker application for Windows built using Python and `customtkinter`.

## ✨ Features
- 🔥 Dual click modes (Left / Right)
- 💾 Custom CPS (Clicks Per Second)
- 🎮 Hotkey support for each click type
- 🌙 Beautiful dark-themed modern GUI
- 🧠 Saves and loads settings automatically
- 💻 Built with `customtkinter`, `pyautogui`, `keyboard`

<div align="center" style="margin-top: 40px;">

<h2 style="font-size:28px; font-weight:800; margin-bottom: 10px;">🚀 Launch Animation</h2>

<img src="https://github.com/user-attachments/assets/881e0d68-4aac-41f4-8e70-58ce64678b11" width="720" alt="Netrix Vexta Loading" style="border-radius: 18px; box-shadow: 0 0 30px rgba(0, 176, 255, 0.45); border: 1px solid rgba(0, 255, 255, 0.2); margin-bottom: 50px;" />

<h2 style="font-size:28px; font-weight:800; margin-bottom: 10px;">🖥️ Main GUI Interface</h2>

<img src="https://github.com/user-attachments/assets/f91e7774-5b09-4c01-9bc9-c0a521652518" width="720" alt="Netrix Vexta GUI" style="border-radius: 18px; box-shadow: 0 0 30px rgba(0, 255, 153, 0.45); border: 1px solid rgba(0, 255, 136, 0.2);" />

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
