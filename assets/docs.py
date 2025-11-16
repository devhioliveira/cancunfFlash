import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def open_docs_window(L, root):
    win = tk.Toplevel(root)

    # evita roubo de foco
    win.attributes("-alpha", 0)
    win.update_idletasks()
    win.attributes("-alpha", 1)

    win.title("Cancunf Flash - Documentação")
    win.geometry("700x600")

    ttk.Label(
        win,
        text=L["docs_title"],
        font=("Segoe UI", 14, "bold")
    ).pack(pady=10)

    text_area = ScrolledText(win, wrap=tk.WORD, font=("Consolas", 11))
    text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    text_area.insert(tk.END, L["docs_body"])
    text_area.config(state=tk.DISABLED)


    return win
