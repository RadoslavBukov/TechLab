'''
Да се направи графично приложение на Tkinter за изчисляване на BMI. Потребителят въвежда височината си в метри и
теглото си в килограми и индексът на телесна маса се изчислява като теглото се раздели на повдигнатата на квадрат
височина в метри. Тълкуването на стойнистите може да се намери в Интернет.
'''
import tkinter as tk
from tkinter import messagebox


def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        interpretation = "Underweight"
    elif 18.5 <= bmi < 25:
        interpretation = "Normal weight"
    elif 25 <= bmi < 30:
        interpretation = "Overweight"
    else:
        interpretation = "Obesity"

    return bmi, interpretation


def on_calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        if not (1.40 <= height <= 2.20):
            raise ValueError("Height out of range")
        if not (40 <= weight <= 150):
            raise ValueError("Weight out of range")

        bmi, interpretation = calculate_bmi(height, weight)
        result_text.set(f"BMI: {bmi}\nInterpretation: {interpretation}")
    except ValueError as e:
        if str(e) == "Height out of range":
            messagebox.showerror("Invalid input", "Height must be between 1.40 m and 2.20 m")
        elif str(e) == "Weight out of range":
            messagebox.showerror("Invalid input", "Weight must be between 40 kg and 150 kg")
        else:
            messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight")


# Main window
root = tk.Tk()
root.title("BMI Calculator")

# Height input
tk.Label(root, text="Height (cm):").grid(row=0, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=0, column=1, padx=10, pady=10)

# Weight input
tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=10)

# Calculating button
btn_calculate = tk.Button(root, text="Calculate BMI", command=on_calculate_bmi)
btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

# Results
result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text, font=("Helvetica", 12))
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Main cycle
root.mainloop()
