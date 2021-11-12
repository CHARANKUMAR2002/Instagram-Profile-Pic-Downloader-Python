import instaloader
from tkinter import *
from PIL import Image, ImageTk
load = instaloader.Instaloader()
t=Tk()
t.geometry('230x150')
t.resizable(0, 0)
t.iconbitmap("insta.ico")
t.title('Insta Profile')
background = Image.open('bg.jpg')
render = ImageTk.PhotoImage(background)
bg = Label(t, image=render, cursor='dot').place(x=0, y=0)
Label(t, text='Enter User Name Above ', cursor='dot',font=('brush', 10, 'bold', 'italic'), bg='#CA226B', fg='white').place(x=5, y=45)
user = Entry(t, cursor='dot', width=30, bg='#461B7E', bd=2, fg='white', font=('brush', 10, 'bold', 'italic'))
user.place(x=5, y=20)


def profile_pic():
    User=user.get()
    username=str(User)
    load.download_profile(username, profile_pic_only=True)
    Label(t, text='Downloaded', font=('brush', 10, 'bold', 'italic'), bg='#CA226B', border=0, fg='white').place(x=80, y=100)


Button(t, text='Download Profile Pic!', cursor='dot',command=profile_pic, font=('brush', 8, 'bold', 'italic'), bg='#FFDB58', activebackground='#FDD017').place(x=50, y=125)

t.mainloop()
