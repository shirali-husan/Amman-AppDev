import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime

def log_call(event=None):
    if not all([selected_operator.get(), selected_call_type.get(), selected_reason.get(),
                selected_internal_external.get(), selected_status.get()]):
        error_label.config(text="Please fill in all mandatory fields.")
        return
    error_label.config(text="")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_button.config(state=tk.DISABLED, text="Logging...")
    with open('continuous_call_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            selected_operator.get(), timestamp, selected_call_type.get(),
            selected_reason.get(), selected_internal_external.get(),
            selected_status.get(), note_entry.get("1.0", tk.END).strip()
        ])
    clear_entries()
    root.after(1000, lambda: log_button.config(state=tk.NORMAL, text="Log Call"))

def clear_entries():
    for var in [selected_operator, selected_call_type, selected_reason,
                selected_internal_external, selected_status]:
        var.set("")
    note_entry.delete("1.0", tk.END)

def update_selected_options_label():
    options = f"Operator: {selected_operator.get()}\nCall Type: {selected_call_type.get()}\n" \
              f"Reason: {selected_reason.get()}\nInternal/External: {selected_internal_external.get()}\n" \
              f"Status: {selected_status.get()}"
    selected_options_label.config(text=options)

def on_button_enter(event):
    event.widget.invoke()

root = tk.Tk()
root.title("Call Logger")
root.configure(bg="#f0f0f0")

operator_label = tk.Label(root, text="Select Operator:", bg="#f0f0f0", font=("Arial", 12, "bold"))
operator_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
selected_operator = tk.StringVar()
operators = ["Murad", "Sameeha", "Omar", "SwitchBoard General"]
for i, operator_name in enumerate(operators):
    operator_button = tk.Button(root, text=operator_name, bg="#d9d9d9", font=("Arial", 10),
                                command=lambda name=operator_name: (selected_operator.set(name), update_selected_options_label()))
    operator_button.grid(row=i+1, column=0, padx=10, pady=5)
    operator_button.bind("<Return>", on_button_enter)

call_type_label = tk.Label(root, text="Call Type:", bg="#f0f0f0", font=("Arial", 12, "bold"))
call_type_label.grid(row=0, column=1, sticky="w", padx=5, pady=5)
selected_call_type = tk.StringVar()
call_types = ["Visa", "ACS", "Other"]
for i, call_type in enumerate(call_types):
    call_type_button = tk.Button(root, text=call_type, bg="#d9d9d9", font=("Arial", 10),
                                 command=lambda ct=call_type: (selected_call_type.set(ct), update_selected_options_label()))
    call_type_button.grid(row=i+1, column=1, padx=10, pady=5)
    call_type_button.bind("<Return>", on_button_enter)

reason_label = tk.Label(root, text="Reason:", bg="#f0f0f0", font=("Arial", 12, "bold"))
reason_label.grid(row=0, column=2, sticky="w", padx=5, pady=5)
selected_reason = tk.StringVar()
reasons = ["General Inquiry", "Visa Questions", "Other"]
for i, reason in enumerate(reasons):
    reason_button = tk.Button(root, text=reason, bg="#d9d9d9", font=("Arial", 10),
                              command=lambda r=reason: (selected_reason.set(r), update_selected_options_label()))
    reason_button.grid(row=i+1, column=2, padx=10, pady=5)
    reason_button.bind("<Return>", on_button_enter)

internal_external_label = tk.Label(root, text="Internal/External:", bg="#f0f0f0", font=("Arial", 12, "bold"))
internal_external_label.grid(row=0, column=3, sticky="w", padx=5, pady=5)
selected_internal_external = tk.StringVar()
internal_external_options = ["Internal", "External"]
for i, option in enumerate(internal_external_options):
    i_e_button = tk.Button(root, text=option, bg="#d9d9d9", font=("Arial", 10),
                           command=lambda ie=option: (selected_internal_external.set(ie), update_selected_options_label()))
    i_e_button.grid(row=i+1, column=3, padx=10, pady=5)
    i_e_button.bind("<Return>", on_button_enter)

status_label = tk.Label(root, text="Status:", bg="#f0f0f0", font=("Arial", 12, "bold"))
status_label.grid(row=0, column=4, sticky="w", padx=5, pady=5)
selected_status = tk.StringVar()
statuses = ["In Progress", "Complete", "Need Follow-Up"]
for i, status in enumerate(statuses):
    status_button = tk.Button(root, text=status, bg="#d9d9d9", font=("Arial", 10),
                              command=lambda st=status: (selected_status.set(st), update_selected_options_label()))
    status_button.grid(row=i+1, column=4, padx=10, pady=5)
    status_button.bind("<Return>", on_button_enter)

note_label = tk.Label(root, text="Note:", bg="#f0f0f0", font=("Arial", 12, "bold"))
note_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
note_entry = tk.Text(root, height=5, width=30, font=("Arial", 10))
note_entry.grid(row=6, column=1, columnspan=4, padx=10, pady=5)
note_entry.bind("<Tab>", lambda e: note_entry.tk_focusNext().focus_set() or e.widget.tk_focusNext().focus_set() or "break")

error_label = tk.Label(root, fg="#ff0000", bg="#f0f0f0", font=("Arial", 10))
error_label.grid(row=7, column=0, columnspan=5, padx=10, pady=5)

log_button = tk.Button(root, text="Log Call", bg="#d9d9d9", font=("Arial", 10), command=log_call)
log_button.grid(row=8, column=0, columnspan=5, padx=10, pady=10)
log_button.bind("<Return>", on_button_enter)

selected_options_label = tk.Label(root, text="", bg="#f0f0f0", font=("Helvetica", 12))
selected_options_label.grid(row=9, column=0, columnspan=5, padx=10, pady=10, sticky="w")

root.mainloop()