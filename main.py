from tkinter import Text, Tk, ttk, END
import time

tk = Tk()

tk.title("Disappearing Text Writing App")
tk.geometry("600x600")
tk.config(bg="#203239")
label = ttk.Label(text="Don't Stop Typing...", background="#203239", foreground="white")
textarea = Text(tk, width=50, height=20)
label.place(x=250, y=1)
textarea.place(x=100, y=100)

tk.after_id = None



def checker(event):
    print(word_count())
    if tk.after_id:
        tk.after_cancel(tk.after_id)
        tk.after_id = None
    tk.after_id = tk.after(5000, clear_text)



def clear_text():
    textarea.delete("1.0", END)

def word_count():
    current_text = textarea.get("1.0", 'end-1c')
    words = current_text.split(" ")
    if words[-1] == "":
        words.pop()
    label = ttk.Label(tk, text=f"Word count: {len(words)}", background="#203239", foreground="white")
    label.place(x=260, y=450)

text = textarea.bind('<KeyPress>', checker)



tk.mainloop()
