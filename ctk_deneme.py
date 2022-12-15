import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("600x600")
root.title("KIE")
BLUE = "#89CFF0"
DARK_BLUE = "#d0ecf9"


frame1 = ctk.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both", expand=True)
#frame2 = ctk.CTkFrame(master=root)

login_label = ctk.CTkLabel(master=frame1, text="LOGIN", text_font=("Bebas", 60))
login_label.pack(side=ctk.TOP, pady=40, padx=10)

username = ctk.CTkEntry(master=frame1, placeholder_text="Username", width=300, height=35, text_font=("Comicsans", 16))
username.pack(pady=12, padx=10)
password = ctk.CTkEntry(master=frame1, placeholder_text="Password", show="*", width=300, height=35, text_font=("Comicsans", 16))
password.pack(pady=12, padx=10)

# geçici bir label oluşturduk password ile aynı konumda sadece biraz daha kenarlardan küçük
temp_label = ctk.CTkLabel(master=password, text= "", width=230, height=25, text_font=("Comicsans", 16), anchor='w')

# her seferinde değişmesi için global bir flag tanımladık
flag = 0
def show_and_hide():
    global flag

    if flag:
        flag = 0
        temp_label.place_forget() # flag 0 olursa şifreyi gösterme
    else:
        flag = 1
        temp_label.configure(text = password.get()) # şifremizi okuyoruz ve geçici label textine aktarıyoruz
        temp_label.place(x = 10, y = 5)

def on_enter(e):
    e.widget['text_color'] = "#d0ecf9"

def on_leave(e):
    e.widget['text_color'] = "black"

show_password = ctk.CTkCheckBox(master=frame1, text="Show Password", command=show_and_hide)
show_password.pack(pady=12, padx=10)

forgot_password = ctk.CTkLabel(master=frame1, text="Forgot Password?", cursor="hand2", text_color=BLUE)
forgot_password.pack(pady=6, padx=5)

create_acc = ctk.CTkLabel(master=frame1, text="Create an Account", cursor="hand2", text_color=BLUE)

forgot_password.bind("<Enter>", on_enter)
forgot_password.bind("<Leave>", on_leave)

login_button = ctk.CTkButton(master=frame1, text="Login").pack(pady=12, padx=10)


root.mainloop()