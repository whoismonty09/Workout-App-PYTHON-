import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("FitLife App developed by Monty")
root.geometry("900x700")
root.configure(bg="#1e1e2f")

title_font = ("Poppins", 24, "bold")
label_font = ("Poppins", 12)
btn_font = ("Poppins", 11, "bold")

user = {}

workouts = {
    "Biceps 💪": ["Curls", "Hammer Curl", "Concentration Curl", "Chin Ups", "Cable Curl"],
    "Triceps 🦾": ["Dips", "Kickbacks", "Overhead Extension", "Close Pushups", "Skull Crushers"],
    "Chest 🏋️": ["Pushups", "Bench Press", "Incline Press", "Chest Fly", "Dumbbell Press"],
    "Back 🏹": ["Pullups", "Deadlift", "Lat Pulldown", "Seated Row", "Back Extension"],
    "Legs 🦵": ["Squats", "Lunges", "Leg Press", "Calf Raises", "Step Ups"],
    "Shoulder 🤸": ["Shoulder Press", "Lateral Raise", "Front Raise", "Upright Row", "Shrugs"],
    "Cardio ❤️": ["Running", "Jump Rope", "Burpees", "Mountain Climbers", "Cycling"]
}

warmups = ["Jumping Jacks", "Arm Circles", "High Knees"]
stretches = ["Full Body Stretch", "Hamstring Stretch", "Breathing Stretch"]

def clear():
    for w in root.winfo_children():
        w.destroy()

def calculate_reps():
    w = float(user["weight"])
    g = user["gender"]

    if g == "Male":
        if w < 60:
            return 15, round(w*0.3)
        elif w < 80:
            return 12, round(w*0.4)
        else:
            return 10, round(w*0.5)
    else:
        if w < 60:
            return 15, round(w*0.2)
        elif w < 80:
            return 12, round(w*0.3)
        else:
            return 10, round(w*0.35)

def start_page():
    clear()
    tk.Label(root, text="💎 FitLife Workout App", font=title_font, bg="#1e1e2f", fg="white").pack(pady=20)

    frame = tk.Frame(root, bg="#2b2b44", padx=30, pady=30)
    frame.pack(pady=20)

    tk.Label(frame, text="Name", font=label_font, bg="#2b2b44", fg="white").grid(row=0, column=0)
    name_entry = tk.Entry(frame)
    name_entry.grid(row=0, column=1)

    tk.Label(frame, text="Weight (kg)", font=label_font, bg="#2b2b44", fg="white").grid(row=1, column=0)
    weight_entry = tk.Entry(frame)
    weight_entry.grid(row=1, column=1)

    tk.Label(frame, text="Height (cm)", font=label_font, bg="#2b2b44", fg="white").grid(row=2, column=0)
    height_entry = tk.Entry(frame)
    height_entry.grid(row=2, column=1)

    tk.Label(frame, text="Age", font=label_font, bg="#2b2b44", fg="white").grid(row=3, column=0)
    age_entry = tk.Entry(frame)
    age_entry.grid(row=3, column=1)

    gender = tk.StringVar(value="Male")
    tk.Label(frame, text="Gender", font=label_font, bg="#2b2b44", fg="white").grid(row=4, column=0)
    tk.OptionMenu(frame, gender, "Male", "Female").grid(row=4, column=1)

    def submit():
        user["name"] = name_entry.get()
        user["weight"] = weight_entry.get()
        user["height"] = height_entry.get()
        user["age"] = age_entry.get()
        user["gender"] = gender.get()
        workout_page()

    tk.Button(root, text="🚀 Start Workout Plan", bg="#ff6f61", fg="white", font=btn_font, width=20, command=submit).pack(pady=20)

def workout_page():
    clear()
    tk.Label(root, text="🔥 What Workout Today?", font=title_font, bg="#1e1e2f", fg="white").pack(pady=20)

    grid = tk.Frame(root, bg="#1e1e2f")
    grid.pack()

    r = c = 0
    for part in workouts:
        tk.Button(grid, text=part, width=22, height=3, bg="#6c63ff", fg="white",
                  font=btn_font, command=lambda p=part: show_plan(p)).grid(row=r, column=c, padx=15, pady=15)
        c += 1
        if c == 2:
            c = 0
            r += 1

def show_plan(part):
    clear()
    reps, weight_load = calculate_reps()

    tk.Label(root, text=f"{part} Workout Plan", font=title_font, bg="#1e1e2f", fg="white").pack(pady=10)

    box = tk.Text(root, width=75, height=22, font=("Poppins", 11), bg="#f4f4ff")
    box.pack(pady=10)

    box.insert(tk.END, "🟡 Warm Up\n")
    for w in warmups:
        box.insert(tk.END, f"{w} → {reps} reps\n")

    box.insert(tk.END, "\n🔵 Main Workout\n")
    for m in workouts[part]:
        box.insert(tk.END, f"{m} → {reps} reps with {weight_load} kg\n")

    box.insert(tk.END, "\n🟢 Stretching\n")
    for s in stretches:
        box.insert(tk.END, f"{s} → 30 sec\n")

    tk.Button(root, text="⬅ Back", bg="#00c896", fg="white", font=btn_font, command=workout_page).pack(pady=10)

start_page()
root.mainloop()
