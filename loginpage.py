import tkinter as tk
import json
import requests
import webbrowser
import os
r = requests.get('https://raw.githubusercontent.com/Wayne2004/somefiles/main/db')
jason = json.loads(r.text.lower())
verified = False
def wholelogin():
    global errortext, verified
    logincre = []
    if os.path.exists('login.txt'):
        with open('login.txt','r+') as f:
            stuf = f.readlines()
            logincre.append(stuf[0].replace('\n',''))
            logincre.append(stuf[1])

    else:
        with open('login.txt','w+') as f:
            f.write('Username\nPassword')

    def logincheck():
        global errortext, verified
        usern = username.get()
        passw = password.get()
        if usern.lower() in jason:
            if jason[usern.lower()] == passw.lower():
                errortext['fg'] = 'Green'
                errortext['text'] = 'Login Successful!'
                with open('login.txt', 'w+') as f:
                    f.write(f'{usern}\n{passw}')
                root.after(2000, root.destroy)
                verified = True
            else:
                errortext['text'] = 'Wrong Password!'
        else:
            errortext['text'] = 'Invalid Username!'

    def signupcheck():
        global errortext
        usern = username.get()
        passw = password.get()
        if len(usern) < 1:
            errortext['fg'] = 'Red'
            errortext['text'] = 'Please Enter A Username!'
        elif len(passw) < 1:
            errortext['fg'] = 'Red'
            errortext['text'] = 'Please Enter A Password!'
        else:

            if usern.lower() in jason:
                errortext['fg'] = 'Red'
                errortext['text'] = 'User Already Registered'
            else:
                errortext['fg'] = 'Green'
                errortext['text'] = 'Success!'
                webbrowser.open(f'https://api.whatsapp.com/send?phone=60126289399&text=Username%20:%20{usern}%20,%20Password%20:%20{passw}')

    root = tk.Tk()
    root.title('Messenger Assistance By Wayne')
    root.geometry('400x250+420+200')
    root.minsize(400,250)
    root.maxsize(400,250)
    root.iconbitmap('photos\\svobackground.ico')
    root.configure(bg='#010e24')

    sidebar = tk.Frame(root,height=300,width=600,bg='#010e24')
    sidebar.pack()


    usernametext = tk.Label(sidebar,font=('Bahnschrift SemiCondensed', 14),text='Username',bg='#010e24',fg='White')
    usernametext.place(relx=0.195,rely=0.10)
    username = tk.Entry(sidebar,width=30,bd=0,bg='White',fg='Black',font=('Flamenco', 10))
    username.place(relx=0.2,rely=0.2)

    passwordtext = tk.Label(sidebar,font=('Bahnschrift SemiCondensed', 14),text='Password',bg='#010e24',fg='White')
    passwordtext.place(relx=0.195,rely=0.35)
    password = tk.Entry(sidebar,width=30,bd=0,bg='White',fg='Black',font=('Flamenco', 10))
    password.place(relx=0.2,rely=0.45)

    errortext = tk.Label(sidebar, font=('Bahnschrift SemiCondensed', 9), text='', bg='#010e24',
                                    fg='Red')
    errortext.place(relx=0.5, rely=0.8)

    Login = tk.Button(sidebar, text='    Login    ', bd=1, font=('Bahnschrift SemiCondensed', 15),height=1,bg='#0a2045',fg='White',
                                        relief='flat', activebackground='#0a2045', activeforeground='White',command = logincheck)
    Login.place(relx=0.5,rely=0.6)

    Signup = tk.Button(sidebar, text='  Signup  ', bd=1, font=('Bahnschrift SemiCondensed', 15), height=1,
                      bg='#0a2045', fg='White',
                      relief='flat', activebackground='#0a2045', activeforeground='White', command=signupcheck)
    Signup.place(relx=0.20, rely=0.6)

    if len(logincre) != 0:
        username.insert(tk.END,logincre[0])
        password.insert(tk.END, logincre[1])
    root.mainloop()
    return verified
