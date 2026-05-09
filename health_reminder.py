import tkinter as tk

REMINDERS = {
    "💧 Drink Water": "Time to hydrate! Take a pause and drink a glass of water. 💧",
    "😴 Sleep/Rest": "Your body needs rest. Take a 5-minute break or prepare for sleep. 😴",
    "👁️ Blink & Eye Rest": "Protect your eyes! Blink slowly, look away, and rest for 20 seconds. 👁️",
    "🚶 Stand & Walk": "Sit too long? Stand up, stretch, and walk around for 2 mins. 🚶",
    "🧘 Stretch & Breathe": "Take 3 deep breaths and do a quick neck/shoulder stretch. 🧘"
}

class ReminderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Health Reminder Setup")
        self.root.geometry("320x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a1a")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        tk.Label(self.root, text="Select Reminders:", fg="#ffffff", bg="#1a1a1a", font=("Segoe UI", 14, "bold")).pack(pady=10)

        self.vars = {}
        for name in REMINDERS:
            var = tk.BooleanVar()
            self.vars[name] = var
            tk.Checkbutton(self.root, text=name, variable=var, bg="#1a1a1a", fg="#e0e0e0",
                           font=("Segoe UI", 11), selectcolor="#333333", activebackground="#1a1a1a").pack(anchor="w", padx=20)

        self.start_btn = tk.Button(self.root, text="✅ Activate & Run in Background", command=self.start,
                                   bg="#4CAF50", fg="white", font=("Segoe UI", 12, "bold"), relief="flat", bd=0, padx=10, pady=6)
        self.start_btn.pack(pady=15)

        self.status = tk.Label(self.root, text="", fg="#888888", bg="#1a1a1a", font=("Segoe UI", 10))
        self.status.pack()

        self.selected = []
        self.idx = 0
        self.is_running = False

        # Quick exit shortcut: Ctrl + Shift + Q
        self.root.bind("<Control-Shift-Q>", lambda e: self.on_close())

    def start(self):
        self.selected = [name for name, var in self.vars.items() if var.get()]
        if not self.selected:
            self.status.config(text="⚠️ Select at least one reminder!", fg="#ff5555")
            return

        self.is_running = True
        self.root.withdraw()  # ✅ Hides window completely, runs silently
        self.schedule_next()

    def show_popup(self):
        if not self.is_running: return
        msg = REMINDERS[self.selected[self.idx % len(self.selected)]]

        win = tk.Toplevel(self.root)
        win.overrideredirect(True)
        win.configure(bg="#252525")
        win.attributes("-topmost", True)

        tk.Label(win, text=msg, bg="#252525", fg="#ffffff", font=("Segoe UI", 13, "bold"), justify="center").pack(padx=25, pady=25)

        win.update_idletasks()
        x = (win.winfo_screenwidth() - win.winfo_width()) // 2
        y = (win.winfo_screenheight() - win.winfo_height()) // 2
        win.geometry(f"+{x}+{y}")

        alpha = 0.0
        win.attributes("-alpha", alpha)

        def fade_in():
            nonlocal alpha
            alpha = min(alpha + 0.1, 1.0)
            win.attributes("-alpha", alpha)
            if alpha < 1.0:
                win.after(25, fade_in)
            else:
                win.after(10000, fade_out)

        def fade_out():
            nonlocal alpha
            alpha = max(alpha - 0.1, 0.0)
            win.attributes("-alpha", alpha)
            if alpha > 0.0:
                win.after(25, fade_out)
            else:
                win.destroy()
                self.schedule_next()

        fade_in()

    def schedule_next(self):
        self.idx += 1
        self.root.after(3600000, self.show_popup)  # 1 hour

    def on_close(self):
        self.is_running = False
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ReminderApp()
    app.run()