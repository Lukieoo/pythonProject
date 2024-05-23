import tkinter as tk
import spell

root = tk.Tk()
root.title("Text Display App")


def show_text():
    entered_text = text_entry.get()
    correction = spell.correction(entered_text)
    candidates = spell.candidates(entered_text)
    # Formatowanie tekstu z nową linią i etykietami
    output = f"Corrected Text: {correction}\nCandidates: {candidates} "

    display_text.config(state=tk.NORMAL)
    display_text.delete(1.0, tk.END)
    display_text.insert(tk.END, output)
    display_text.config(state=tk.DISABLED)


label = tk.Label(root, text="Enter some text:")
label.pack(pady=5)

text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)

show_text_button = tk.Button(root, text="Correct the text", command=show_text)
show_text_button.pack(pady=20)

display_text = tk.Text(root, height=5, width=70, state=tk.DISABLED, bg="lightgrey")
display_text.pack(pady=5)

root.mainloop()
