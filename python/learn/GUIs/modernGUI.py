import customtkinter as ck
#most like in tkinter - just try
#
# setup
ck.set_appearance_mode("system") # "dark", "light"
ck.set_default_color_theme("dark-blue")  # "blue", "green"
win = ck.CTk()
win.geometry("500x350")

# test function
def login():
    print("test")

# components
frame = ck.CTkFrame(master=win)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ck.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = ck.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
entry2 = ck.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ck.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkox = ck.CTkCheckBox(master=frame, text="Remember Me")
entry2.pack(pady=12, padx=10)


win.mainloop()
