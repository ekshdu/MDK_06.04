import tkinter as tk

PREF_OPTS = [("пляж", 1), ("горы", 2), ("история", 3), ("экзотика", 4), ("отдых", 5)]
BUDG_OPTS = [("низкий", 1), ("средний", 2), ("высокий", 3)]
SEAS_OPTS = [("зима", 1), ("лето", 3), ("любое", 5)]
VISA_OPTS = [("нет", 0), ("да", 1)]

RULES = {
    (1, 3, 3, 1): "мальдивы",
    (2, 2, 1, 0): "красная поляна",
    (3, 3, 5, 1): "италия",
    (4, 3, 1, 1): "тайланд",
    (5, 1, 3, 0): "беларусь"
}

def onconsultation():
    richtext.delete(1.0, tk.END)
    p = pref_var.get()
    b = budg_var.get()
    s = seas_var.get()
    v = visa_var.get()
    rec = RULES.get((p, b, s, v), "не найдено")
    richtext.insert(tk.END, f"рекомендация: {rec}")

root = tk.Tk()
root.title("консультация по подбору тура")

pref_var = tk.IntVar(value=0)
budg_var = tk.IntVar(value=0)
seas_var = tk.IntVar(value=0)
visa_var = tk.IntVar(value=0)

tk.Label(root, text="предпочтение:").pack(anchor='w')
f1 = tk.Frame(root)
f1.pack(anchor='w')
for t, val in PREF_OPTS:
    tk.Radiobutton(f1, text=t, variable=pref_var, value=val).pack(side=tk.LEFT)

tk.Label(root, text="бюджет:").pack(anchor='w')
f2 = tk.Frame(root)
f2.pack(anchor='w')
for t, val in BUDG_OPTS:
    tk.Radiobutton(f2, text=t, variable=budg_var, value=val).pack(side=tk.LEFT)

tk.Label(root, text="время года:").pack(anchor='w')
f3 = tk.Frame(root)
f3.pack(anchor='w')
for t, val in SEAS_OPTS:
    tk.Radiobutton(f3, text=t, variable=seas_var, value=val).pack(side=tk.LEFT)

tk.Label(root, text="виза:").pack(anchor='w')
f4 = tk.Frame(root)
f4.pack(anchor='w')
for t, val in VISA_OPTS:
    tk.Radiobutton(f4, text=t, variable=visa_var, value=val).pack(side=tk.LEFT)

tk.Button(root, text="консультация", command=onconsultation).pack(pady=5)

richtext = tk.Text(root, height=10, width=60)
richtext.pack(padx=10, pady=10)

root.mainloop()