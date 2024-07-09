import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(value):
    if value == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid Input")
    elif value == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg='purple')

# Entry widget to display input and output
entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '00','%', 'x'
]

# Function to create circular buttons with adjusted label positions
def create_circle_button(canvas, x, y, text):
    button_radius = 30
    canvas.create_oval(x - button_radius, y - button_radius, x + button_radius, y + button_radius, fill='white')
    # Adjust the text position to move it to the left
    canvas.create_text(x, y, text=text, font=('Arial', 14, 'bold'))

# Create canvas
canvas = tk.Canvas(root, bg='violet', width=320, height=420)
canvas.grid(row=1, column=0, columnspan=4, padx=20, pady=20)

# Place circular buttons
row = 70
col = 40
button_index = 0
for i in range(5):
    for j in range(4):
        if button_index < len(buttons):
            create_circle_button(canvas, col, row, buttons[button_index])
            col += 80  # Adjusted position for the buttons
            button_index += 1
    row += 80
    col = 40  # Adjusted position for the first button in each row


col += 80  # Adjust as needed to control the amount of space


# Function to handle button clicks
def on_button_click(event):
    x, y = event.x, event.y
    for i in range(len(buttons)):
        col = 70 + (i % 4) * 80
        row = 70 + (i // 4) * 80
        if (x - col) ** 2 + (y - row) ** 2 <= 30 ** 2:
            button_click(buttons[i])

# Bind click event to canvas
canvas.bind('<Button-1>', on_button_click)

root.mainloop()



