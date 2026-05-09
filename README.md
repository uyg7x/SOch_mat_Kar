
# 🌙 Health Reminder

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![Dependencies](https://img.shields.io/badge/Dependencies-None-orange.svg)

A lightweight, background-running desktop app that gently reminds you to drink water, rest your eyes, stretch, or walk every hour. Built with **pure Python & Tkinter** (zero external runtime dependencies).

## ✨ Features
- ✅ **Custom Reminders** – Pick what you want: Water, Sleep, Eyes, Stand/Walk, Stretch
- 🎞️ **Smooth Animations** – Borderless, center-screen popups with fade-in/out effects
- 💾 **Ultra Lightweight** – ~10–12 MB RAM, `0.0%` CPU when idle
- 🛑 **Background Mode** – Minimized to taskbar after activation, stays out of your way
- 📦 **One-Click Build** – Compiles to a single `.exe` with a custom icon using PyInstaller
- 🔒 **No External Libraries** – Uses only Python's built-in `tkinter`

## 📸 Preview
*(Replace this with a GIF or screenshot of your app in action)*
![App Preview]<img width="44" height="40" alt="Screenshot 2026-05-09 223143" src="https://github.com/user-attachments/assets/4739e886-d4c6-472b-9cb7-9ab90e12ac51" /><img width="164" height="161" alt="Screenshot 2026-05-09 223248" src="https://github.com/user-attachments/assets/06e45c73-2234-4636-bb65-9617f3e1d86d" />


## 🚀 Quick Start
### Prerequisites
- Python 3.8 or higher installed on your system

### Run from Source
1. Clone this repository:
   ```bash
   git clone https://github.com/uyg7x/HealthReminder.git
   cd HealthReminder
   ```
2. Run the app:
   ```bash
   python src/health_reminder.py
   ```

## 🛠️ Build to `.exe` (Windows)
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --icon=assets/icon.ico --name HealthReminder src/health_reminder.py
   ```
3. Your `HealthReminder.exe` will be inside the `dist/` folder. Double-click to run!

*(Optional: Run `build.bat` for a one-click build experience.)*

## 📖 Usage
1. Launch the app → Select your preferred reminders
2. Click **`✅ Activate & Run in Background`**
3. The window minimizes to your taskbar. Reminders will popup every hour.
4. Click the minimized window anytime → Press **`⏹ Stop Reminder`** to exit.

## 🛑 How to Force Stop
If the app gets stuck or you want to kill it instantly:
```cmd
taskkill /f /im HealthReminder.exe
```

## 📁 Project Structure
```
HealthReminder/
├── src/
│   └── health_reminder.py      # Main application logic
├── assets/
│   ├── icon.ico                # Custom .exe icon
│   └── screenshot.png          # Preview image for README
├── build.bat                   # One-click Windows build script
├── requirements.txt            # PyInstaller for building
├── README.md                   # This file
├── LICENSE                     # MIT License
└── .gitignore                  # Clean repo structure
```

## ⚙️ Tech Stack
- **Python 3.8+**
- **Tkinter** (Built-in GUI framework)
- **PyInstaller** (Executable packaging)

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
💡 *Made with ❤️ to encourage healthy screen habits. Star ⭐ this repo if it helped you!*
