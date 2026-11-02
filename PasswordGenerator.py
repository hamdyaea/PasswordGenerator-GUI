#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Cryptographically secure password generator with Tkinter GUI."""
import argparse
import secrets
import string

ALPHABET = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}:,.?"
MAX_LENGTH = 4096

def generate_password(length: int) -> str:
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("Password length must be an integer")
    if not 1 <= length <= MAX_LENGTH:
        raise ValueError(f"Password length must be between 1 and {MAX_LENGTH}")
    return "".join(secrets.choice(ALPHABET) for _ in range(length))

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--length", type=int, help="Use CLI instead of GUI")
    args = parser.parse_args()
    if args.length is not None:
        try:
            print(generate_password(args.length))
        except ValueError as exc:
            parser.error(str(exc))
        return
    import tkinter as tk
    from tkinter import messagebox, ttk
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("580x185")
    frame = ttk.Frame(root, padding=18)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Password length (1–4096):").pack(anchor="w")
    length_var = tk.StringVar(value="20")
    ttk.Entry(frame, textvariable=length_var, width=12).pack(anchor="w", pady=5)
    password_var = tk.StringVar()
    ttk.Entry(frame, textvariable=password_var, width=65, state="readonly").pack(fill="x", pady=8)
    def generate() -> None:
        try:
            password_var.set(generate_password(int(length_var.get())))
        except ValueError as exc:
            messagebox.showerror("Invalid length", str(exc), parent=root)
    ttk.Button(frame, text="Generate password", command=generate).pack(anchor="w")
    root.mainloop()

if __name__ == "__main__":
    main()
