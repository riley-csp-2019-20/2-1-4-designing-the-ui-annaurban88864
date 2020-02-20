##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title("Authorization")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack() 

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=50)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack() 

ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack(padx=50)

def button_test():
    print("test")
    frame_auth.tkraise()

    password = ent_password.get()
    lbl_display_pass.config(text = password)

btn_login= tk.Button(frame_login, text='Login', command=button_test)
btn_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row = 0, column = 0, sticky = "news")

lbl_display_pass = tk.Label(frame_auth, text = "test")
lbl_display_pass.pack()

frame_login.tkraise()

root.mainloop()