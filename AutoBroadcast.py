import tkinter
import tkinter as tk
from tkinter import ttk
import random
from tkinter import filedialog
import os
import requests
import speedtest
from threading import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows
import time
from os import system
from io import BytesIO
from PIL import Image
import win32clipboard
import pyperclip
import loginpage
if loginpage.wholelogin() == True:
    sendingmessage = False
    txtboxmsg = ''
    pauseornot = False
    clear = lambda: system('cls')
    pagelist = []
    sidebarcl = '#04142e'
    theme = ('Bahnschrift SemiCondensed', 12)
    currentpage = ''
    ids = []
    if os.path.exists('credentials.txt'):
        with open('credentials.txt','r+') as f:
            stuf = f.readlines()
            ids.append(stuf[0].replace('\n',''))
            ids.append(stuf[1])

    else:
        with open('credentials.txt','w+') as f:
            f.write('Email\nPassword')
    def on_enter(e):
        MainButton.configure(fg='White',bg='#0a2045')

    def on_leave(e):
        MainButton.configure(fg='White',bg=sidebarcl)

    def on_enter2(e):
        InfoButton.configure(fg='White', bg='#0a2045')

    def on_leave2(e):
        InfoButton.configure(fg='White', bg=sidebarcl)

    def addpicture():
        global pictureselected
        global filename
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a Picture!",
                                              filetypes=[("all files","*.*")])
        if len(filename) > 4:
            selectpicturebutton.configure(text='Change Picture')
            selectpicturebutton.place(relx=0.493)
            pictureselected = True
        else:
            selectpicturebutton.configure(text='Add Picture')
            selectpicturebutton.place(relx=0.523)
            pictureselected = False
    def threading():
        # Call work function
        t1=Thread(target=fetch_page)
        t1.start()
    def threading2():
        modeselected = modedropdown.get()
        if modeselected == 'Whatsapp Web':
            t2 = Thread(target=whatsapbroadcast)
            t2.start()

        else:
            boxhe = tkinter.messagebox.askyesno(title='Auto Broadcaster', message='Broadcast Will Not Work On Page With Less Than 10 Enquiries\nDo You Wish To Continue?')
            if boxhe:
                # Call work function
                t2=Thread(target=startbroadcast)
                t2.start()

    def threading3():
        t3 = Thread(target=wifispeed)
        t3.start()
    def wifispeed():
        while True:
            try:
                speed_test = speedtest.Speedtest(secure=True)
                download_speed = speed_test.download()
                wifival["text"] = f'{int(download_speed * 0.000001)} MB/S'
                if int(download_speed * 0.000001) > 25:
                    wifival["fg"] = 'Green'
                else:
                    wifival["fg"] = 'Red'
            except:
                wifival["text"] = '0 MB/S'
                wifival["fg"] = 'Red'

    def pausey():
        global pauseornot
        if not pauseornot:
            pauseornot = True
            pausebutton.configure(text='   Resume   ')
        else:
            pauseornot = False
            pausebutton.configure(text='    Pause    ')
    pictureselected = False
    def fetch_page():
        with open('credentials.txt','w') as f:
            f.write(fbemail.get()+'\n')
            f.write(fbpass.get())

        mobile_emulation = {
            "deviceMetrics": {"width": 450, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_argument("--disable-notifications")

        chrome_service = ChromeService("chromedriver.exe")
        chrome_service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome("chromedriver.exe", options=chrome_options,service=chrome_service)
        driver.set_window_size(1050, 810)
        driver.get("https://www.facebook.com/")

        # enter email and pass
        driver.execute_script(f'document.getElementsByName("email")[0].value="{fbemail.get()}"')
        time.sleep(0.2)
        passinput = driver.find_element(By.XPATH, '//*[@id="m_login_password"]')
        passinput.send_keys(fbpass.get())
        driver.execute_script('document.getElementsByName("login")[0].click()')
        time.sleep(5)
        if "checkpoint" not in driver.current_url:
            pass
        else:
            msgbox = tk.messagebox.showinfo(title='2FA Detected', message='Please Solve 2FA And Click Ok')
            if msgbox == 'ok':
                while True:
                    if "home.php" in driver.current_url or '?paipv=' in driver.current_url:
                        break
                    else:
                        pass

        driver.get('https://business.facebook.com/latest/home?nav_ref=profile_plus_admin_tool')

        #collect page
        actions = ActionChains(driver)
        # click the X button if something pops up
        time.sleep(5)
        actions = ActionChains(driver)
        try:
            driver.find_element(By.XPATH,
                                "//div[@class = 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x16tdsg8 xggy1nq x1ja2u2z x1t137rt x6s0dn4 x1ejq31n xd10rxx x1sy0etr x17r0tee x3nfvp2 xdl72j9 x1q0g3np x2lah0s x193iq5w x1n2onr6 x1hl2dhg x87ps6o xxymvpz xlh3980 xvmahel x1lku1pv x1lcm9me x1yr5g0i xrt01vj x10y3i5r xo1l8bm xbsr9hj x1v911su x1y1aw1k xwib8y2 xn6708d x1ye3gou']").click()
        except:
            actions.send_keys(Keys.ENTER)
            actions.perform()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@class='xhk9q7s x1otrzb0 x1i1ezom x1o6z2jb x1ypdohk x1a2a7pz xh8yej3 xgbp5tv x17q9amd xqhdjmb x1pknkcx x9f619 x1vqgdyp xjbqb8w xadangi x1n5bzlp x1gv0dy9 x8x9e93 x1nwzcet x1hjarm2 x1i74pvw _3qn7 _61-0 _2fyi _3qng']").click()
        while True:
            pns = driver.find_elements(By.XPATH,'//span[@class="xmi5d70 x1fvot60 xxio538 xbsr9hj xq9mrsl x1mzt3pk x1vvkbs x13faqbe x1fcty0u xeuugli"]')
            if pns != []:
                break
            else:
                pass
        for _ in pns:
            if _.get_attribute('innerText').lower() == 'create a business account':
                pns.remove(_)

        for _ in pns:
            pagelist.append(_.get_attribute('innerText'))
        pagelist.sort()
        pagedropdown["value"] = pagelist
        driver.close()


    def whatsapbroadcast():
        global sendingmessage, pageselected
        message = textbox.get("1.0", 'end-1c')
        pageselected = "Whatsapp Web"

        if pictureselected:
            photo = filename
        else:
            photo = 0

        sendingmessage = True
        infopage()
        mobile_emulation = {
            "deviceMetrics": {"width": 1000, "height": 620, "pixelRatio": 1.0},

            "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        # "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19"
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_argument("--disable-notifications")
        chrome_service = ChromeService(r"C:\Users\wayne\AppData\Local\Programs\AutoBroadcaster\chromedriver.exe")
        chrome_service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(r"C:\Users\wayne\AppData\Local\Programs\AutoBroadcaster\chromedriver.exe",
                                  options=chrome_options, service=chrome_service)
        driver.set_window_size(1050, 810)
        driver.get("https://web.whatsapp.com/")

        # check if logged in or not
        while True:
            try:
                driver.find_element(By.XPATH, "//div[@data-testid='chat-list-search']")
                break
            except:
                pass

        time.sleep(2)

        searchbar = driver.find_element(By.XPATH, "//div[@data-testid='chat-list-search']")
        searchbar.click()
        action = ActionChains(driver)
        currentname = ''
        numberofclient = 0
        # loop until bottom of chat
        while True:
            action.send_keys(Keys.ARROW_DOWN)
            action.perform()
            time.sleep(0.5)
            try:
                driver.find_element(By.XPATH, '//div[@title="Disappearing messages"]')
                buttons = driver.find_elements(By.XPATH, '//div[@class = "tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd gjuq5ydh"]')
                for x in buttons:
                    if x.get_attribute("innerText").lower() == 'ok':
                        x.click()
                    else:
                        pass
                time.sleep(0.3)
                driver.execute_script("document.getElementById('side').click()")
            except:
                pass
            try:
                name = driver.find_element(By.XPATH,
                                           "//div[@class='_2rlF7']/div[@class='_21nHd']/span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
                name = name.get_attribute('innerText')
            except:
                name = driver.find_element(By.XPATH,"//span[@class='_3vLho']/span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
                name = name.get_attribute('innerText')
            if currentname != name:
                currentname = name
                numberofclient += 1
            else:
                break
        numberofusersent = 0
        sentliao = []
        # start sending messages
        while True:
            searchbar.click()
            for _ in range(int(numberofclient * 1.5)):
                action.send_keys(Keys.ARROW_DOWN)
                action.perform()
                time.sleep(0.1)


            try:
                name = driver.find_element(By.XPATH,
                                           "//div[@class='_2rlF7']/div[@class='_21nHd']/span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
                name = name.get_attribute('innerText')
            except:
                try:
                    name = driver.find_element(By.XPATH,
                                               "//span[@class='_3vLho']/span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
                    name = name.get_attribute('innerText')
                except:
                    name = 'Unable to get name'
            chatplace = driver.find_element(By.XPATH, '//div[@data-testid="conversation-compose-box-input"]')
            if name not in sentliao:
                if photo != 0:
                    image = Image.open(photo)
                    output = BytesIO()
                    image.convert('RGB').save(output, 'BMP')

                    data = output.getvalue()[14:]
                    output.close()

                    win32clipboard.OpenClipboard()
                    win32clipboard.EmptyClipboard()
                    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
                    win32clipboard.CloseClipboard()
                    chatplace.send_keys(Keys.LEFT_CONTROL + 'v')
                    time.sleep(1)
                    if pauseornot:
                        while pauseornot:
                            if not pauseornot:
                                break
                            else:
                                pass
                    action.send_keys(Keys.ENTER)
                    action.perform()
                    time.sleep(1)

                pyperclip.copy(message)
                chatplace.send_keys(Keys.LEFT_CONTROL + 'v')
                if pauseornot:
                    while pauseornot:
                        if not pauseornot:
                            break
                        else:
                            pass
                time.sleep(1)
                action.send_keys(Keys.ENTER)
                action.perform()


                numberofusersent += 1
                sentliao.append(name)
                processbox.configure(state='normal')
                processbox.insert(tk.END, str(numberofusersent) + '. ' + name + ' || ' + 'Sent!\n')
                processbox.configure(state='disabled')
                guides8['text'] = numberofusersent
            else:
                break
        driver.close()
        sendingmessage = False
        processbox.configure(state='normal')
        processbox.insert(tk.END, '----------------------------------------\n')
        processbox.insert(tk.END, 'Finished!!')
        processbox.configure(state='disabled')




    def startbroadcast():
        global pageselected,usersentcount,txtboxmsg,sendingmessage
        usersentcount = 0
        email = fbemail.get()
        password = fbpass.get()
        pageselected = pagedropdown.get()
        txtboxmsg = textbox.get("1.0",'end-1c')
        message = textbox.get("1.0",'end-1c')
        retry_count = 0

        if pictureselected:
            picture = filename
        else:
            picture = 0

        if wifival['fg'] == 'Red':
            tk.messagebox.showinfo(title='Auto Broadcaster', message='Slow Wifi Speed, Auto Broadcaster Might Not Work Properly.')

        if len(pageselected) < 1:
            tk.messagebox.showinfo(title='Select A Page', message='Please Select The Page That You Want To Broadcast')
            return
        else:
            sendingmessage = True
            infopage()
            mobile_emulation = {
                "deviceMetrics": {"width": 700, "height": 640, "pixelRatio": 1.0},

                "userAgent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19'}
            #"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19"
            chrome_options = Options()
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            chrome_options.add_argument("--disable-notifications")
            chrome_service = ChromeService("chromedriver.exe")
            chrome_service.creationflags = CREATE_NO_WINDOW
            driver = webdriver.Chrome("chromedriver.exe", options=chrome_options, service=chrome_service)
            driver.set_window_size(1050, 810)
            driver.get("https://www.facebook.com/")
            # enter email and pass
            driver.execute_script(f'document.getElementsByName("email")[0].value="{email}"')
            time.sleep(0.2)
            passinput = driver.find_element(By.XPATH, '//*[@id="m_login_password"]')
            passinput.send_keys(password)
            driver.execute_script('document.getElementsByName("login")[0].click()')
            time.sleep(5)
            if "checkpoint" not in driver.current_url:
                pass
            else:
                msgbox = tk.messagebox.showinfo(title='2FA Detected', message='Please Solve 2FA And Click Ok')
                if msgbox == 'ok':
                    while True:
                        if "home.php" in driver.current_url or '?paipv=' in driver.current_url:
                            break
                        else:
                            pass

            time.sleep(0.5)
            driver.get('https://business.facebook.com/latest/home?nav_ref=profile_plus_admin_tool')

            # collect page

            #click the X button if something pops up
            time.sleep(5)
            actions = ActionChains(driver)
            try:
                driver.find_element(By.XPATH, "//div[@class = 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x16tdsg8 xggy1nq x1ja2u2z x1t137rt x6s0dn4 x1ejq31n xd10rxx x1sy0etr x17r0tee x3nfvp2 xdl72j9 x1q0g3np x2lah0s x193iq5w x1n2onr6 x1hl2dhg x87ps6o xxymvpz xlh3980 xvmahel x1lku1pv x1lcm9me x1yr5g0i xrt01vj x10y3i5r xo1l8bm xbsr9hj x1v911su x1y1aw1k xwib8y2 xn6708d x1ye3gou']").click()
            except:
                actions.send_keys(Keys.ENTER)
                actions.perform()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                "//div[@class='xhk9q7s x1otrzb0 x1i1ezom x1o6z2jb x1ypdohk x1a2a7pz xh8yej3 xgbp5tv x17q9amd xqhdjmb x1pknkcx x9f619 x1vqgdyp xjbqb8w xadangi x1n5bzlp x1gv0dy9 x8x9e93 x1nwzcet x1hjarm2 x1i74pvw _3qn7 _61-0 _2fyi _3qng']").click()
            while True:
                pns = driver.find_elements(By.XPATH,
                                           '//span[@class="xmi5d70 x1fvot60 xxio538 xbsr9hj xq9mrsl x1mzt3pk x1vvkbs x13faqbe x1fcty0u xeuugli"]')
                if pns != []:
                    break
                else:
                    pass
            for _ in pns:
                if _.get_attribute('innerText').lower() == 'create a business account':
                    pns.remove(_)

            #click page
            for _ in pns:
                if _.get_attribute('innerText').lower() == pageselected.lower():
                    _.click()
                    break

            # click the X button if something pops up
            time.sleep(5)
            actions = ActionChains(driver)
            try:
                driver.find_element(By.XPATH,
                                    "//div[@class = 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x16tdsg8 xggy1nq x1ja2u2z x1t137rt x6s0dn4 x1ejq31n xd10rxx x1sy0etr x17r0tee x3nfvp2 xdl72j9 x1q0g3np x2lah0s x193iq5w x1n2onr6 x1hl2dhg x87ps6o xxymvpz xlh3980 xvmahel x1lku1pv x1lcm9me x1yr5g0i xrt01vj x10y3i5r xo1l8bm xbsr9hj x1v911su x1y1aw1k xwib8y2 xn6708d x1ye3gou']").click()
            except:
                actions.send_keys(Keys.ENTER)
                actions.perform()
            time.sleep(2)

            #check page name correct
            checkifpagenamecorrect = driver.find_element(By.XPATH,'//div[@class="xmi5d70 x1fvot60 xxio538 xbsr9hj xuxw1ft x6ikm8r x10wlt62 xlyipyv x1h4wwuj x1fcty0u"]')
            while True:
                if pageselected.lower() != checkifpagenamecorrect.get_attribute('innerText').lower():
                    time.sleep(1)
                else:
                    break

            time.sleep(3)
            try:
                driver.find_element(By.XPATH,"//div[@class = 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x16tdsg8 xggy1nq x1ja2u2z x1t137rt x6s0dn4 x1ejq31n xd10rxx x1sy0etr x17r0tee x3nfvp2 xdl72j9 x1q0g3np x2lah0s x193iq5w x1n2onr6 x1hl2dhg x87ps6o xxymvpz xlh3980 xvmahel x1lku1pv x1lcm9me x1yr5g0i xrt01vj x10y3i5r xo1l8bm xbsr9hj x1v911su x1y1aw1k xwib8y2 xn6708d x1ye3gou']").click()
            except:
                pass
            time.sleep(2)
            # open inbox
            inbox = driver.find_elements(By.XPATH, '//div[@class = "_7pon"]')
            inboxfound = []
            for x in inbox:
                if 'inbox' in x.get_attribute('innerText').lower():
                    inboxfound.append(x)
                else:
                    pass
            inboxfound[0].click()


            # test scrollbar
            time.sleep(4)
            while True:
                try:
                    driver.find_element(By.XPATH, "//div[@aria-label='Messenger']").click()
                    break
                except:
                    pass

            while True:
                try:
                    scrollbar = driver.find_element(By.XPATH, "//div[@class='_1t0w _1t0z _1t0_']")
                    scrollbar.click()
                    break
                except:
                    pass


            #scroll to bottom
            actions = ActionChains(driver)
            isitlastuser = []
            while True:
                while True:
                    try:
                        for n in range(0,20):
                            driver.execute_script(f"document.getElementsByClassName('_a6ag _a6ah clearfix _ikh')[{n}].click()")
                            time.sleep(random.randint(20,40)/100)
                        #chats = driver.find_elements(By.XPATH, '//div[@class="_4k8w _8gcz _a6a4 _5_n1 _5m10"]')
                        #chats[-1].click()
                        break
                    except Exception as e:
                        print(e)
                        break
                time.sleep(1)
                names = driver.find_elements(By.XPATH,
                                             '//span[@class="xdpxx8g x117nqv4 x1jchvi3 xwz9qih x1lliihq xn9d7h7"]')
                isitlastuser.append(names[-1].get_attribute('innerText'))

                scrollbar.click()
                for _ in range(250):
                    actions.send_keys(Keys.ARROW_DOWN)
                    actions.perform()
                    time.sleep(0.05)

                try:
                    for n in range(0, 20):
                        driver.execute_script(f"document.getElementsByClassName('_a6ag _a6ah clearfix _ikh')[{n}].click()")
                        time.sleep(random.randint(20,40)/100)
                except:
                    pass
                #chats = driver.find_elements(By.XPATH, '//div[@class="_4k8w _8gcz _a6a4 _5_n1 _5m10"]')
                #chats[-1].click()
                time.sleep(1)
                names = driver.find_elements(By.XPATH,
                                             '//span[@class="xdpxx8g x117nqv4 x1jchvi3 xwz9qih x1lliihq xn9d7h7"]')

                if names[-1].get_attribute('innerText') in isitlastuser:
                    break

                else:
                    isitlastuser.pop()

            users_sent = []
            numbersforprocessbox = 1
            #start sending message
            while True:
                # click the last chat
                try:
                    for n in range(0, 20):
                        driver.execute_script(f"document.getElementsByClassName('_a6ag _a6ah clearfix _ikh')[{n}].click()")
                        time.sleep(random.randint(20,40)/100)
                except:
                    pass
                #chats = driver.find_elements(By.XPATH, '//div[@class="_4k8w _8gcz _a6a4 _5_n1 _5m10"]')
                #chats[-1].click()
                time.sleep(2)

                names = driver.find_elements(By.XPATH,'//span[@class="xdpxx8g x117nqv4 x1jchvi3 xwz9qih x1lliihq xn9d7h7"]')

                if names[-1].get_attribute('innerText') not in users_sent:
                    users_sent.append(names[-1].get_attribute('innerText'))
                    try:

                        textarea = driver.find_element(By.XPATH, "//textarea[@type='text']")
                        if picture != 0:
                            image = Image.open(picture)
                            output = BytesIO()
                            image.convert('RGB').save(output, 'BMP')

                            data = output.getvalue()[14:]
                            output.close()

                            win32clipboard.OpenClipboard()
                            win32clipboard.EmptyClipboard()
                            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
                            win32clipboard.CloseClipboard()
                            textarea.send_keys(Keys.LEFT_CONTROL + 'v')

                        pyperclip.copy(message)
                        textarea.send_keys(Keys.LEFT_CONTROL + 'v')

                        if picture != 0:
                            while True:
                                try:
                                    driver.find_element(By.XPATH,'//div[@class="xeuugli x2lwn1j x6s0dn4 x78zum5 x1q0g3np x1iyjqo2 xozqiw3 x19lwn94 x1lcm9me x1yr5g0i xrt01vj x10y3i5r x1y1aw1k xwib8y2 x1sxyh0 xurb0ha x1n2onr6 xo1l8bm xbsr9hj x1v911su"]')
                                    try:
                                        driver.find_element(By.XPATH,'//i[@class="x1lcm9me x1yr5g0i xrt01vj x10y3i5r x2lah0s img sp_V779FjldKLL sx_e00fae"]')
                                        break
                                    except:
                                        pass
                                except:
                                    image = Image.open(picture)
                                    output = BytesIO()
                                    image.convert('RGB').save(output, 'BMP')

                                    data = output.getvalue()[14:]
                                    output.close()

                                    win32clipboard.OpenClipboard()
                                    win32clipboard.EmptyClipboard()
                                    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
                                    win32clipboard.CloseClipboard()
                                    textarea.send_keys(Keys.LEFT_CONTROL + 'v')
                                    retry_count += 1
                                    if retry_count == 4:
                                        driver.execute_script("alert('Facebook Blocked You From Sending Pictures');")
                                        time.sleep(10)
                                        while True:
                                            try:
                                                driver.close()
                                                processbox.configure(state='normal')
                                                processbox.insert(tk.END, '----------------------------------------\n')
                                                processbox.insert(tk.END, 'Facebook Blocked You, Use Saved Reply Mode')
                                                processbox.configure(state='disabled')
                                                sendingmessage = False
                                                break
                                            except:
                                                pass



                        time.sleep(0.3)
                        if pauseornot:
                            while pauseornot:
                                if not pauseornot:
                                    break
                                else:
                                    pass
                        sendbutton = driver.find_element(By.XPATH, "//div[@aria-label='Send']").click()
                        usersentcount+=1
                        processbox.configure(state='normal')
                        processbox.insert(tk.END,str(numbersforprocessbox)+'. '+names[-1].get_attribute('innerText')+' || '+'Sent!\n')
                        processbox.configure(state='disabled')
                        numbersforprocessbox+=1
                        guides8['text'] = usersentcount
                        time.sleep(1)

                    except Exception as e:
                        print(e)
                        try:
                            driver.find_element(By.XPATH,"//div[@class='x1f6kntn x1o14lzj x9jhf4c x30kzoy xgqcy7u x1lq5wgf xgjrlqd x1b9h4xk xxpdul3 xbaz6xv x6x52a7 x9orja2 x2b8uid']/span[@class='xmi5d70 x1fvot60 xo1l8bm xxio538 xbsr9hj xq9mrsl x1h4wwuj xeuugli']")
                            if 'you are no longer' in driver.find_element(By.XPATH,"//div[@class='x1f6kntn x1o14lzj x9jhf4c x30kzoy xgqcy7u x1lq5wgf xgjrlqd x1b9h4xk xxpdul3 xbaz6xv x6x52a7 x9orja2 x2b8uid']/span[@class='xmi5d70 x1fvot60 xo1l8bm xxio538 xbsr9hj xq9mrsl x1h4wwuj xeuugli']").get_attribute('innerText').lower():
                                processbox.configure(state='normal')
                                processbox.insert(tk.END,str(numbersforprocessbox)+'. '+names[-1].get_attribute('innerText')+' || '+'Moved to Spam!\n')
                                processbox.configure(state='disabled')
                                driver.find_element(By.XPATH, "//div[@class='_3bwy']/div[@class='_3bwx']/div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x16tdsg8 xggy1nq x1ja2u2z x6s0dn4 x1ejq31n xd10rxx x1sy0etr x17r0tee x3nfvp2 xdl72j9 x1q0g3np x2lah0s x193iq5w x1n2onr6 x1hl2dhg x87ps6o xxymvpz xlh3980 xvmahel x1lku1pv x1lcm9me x1yr5g0i xrt01vj x10y3i5r x1q00v2l xaatb59 x1qgsegg xo1l8bm xbsr9hj x1djdxrh x1y1aw1k xwib8y2 xn6708d x1ye3gou']").click()
                                time.sleep(0.1)
                                spambut = driver.find_elements(By.XPATH, "//div[@class='xeuugli x2lwn1j x6s0dn4 x78zum5 x1q0g3np x1iyjqo2 xozqiw3 x19lwn94 x1lcm9me x1yr5g0i xrt01vj x10y3i5r x1y1aw1k xwib8y2 x1sxyh0 xurb0ha xo1l8bm xbsr9hj x1v911su']")
                                spambut[0].click()

                                #driver.execute_script('document.getElementsByClassName("qi72231t tav9wjvu flwp5yud tghlliq5 gkg15gwv frfouenu bonavkto djs4p424 r7bn319e bdao358l fsf7x5fv s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk dnr7xe2t aeinzg81 cr00lzj9 s3jn8y49 g4tp4svg i85zmo3j pkdwr69g sc980dfb kq3l28k4 rc95jfaf fxk3tzhb tgm57n0e jl2a5g8c jez8cy9q gvxzyvdx om3e55n1 rn8ck1ys f14ij5to bq6c9xl4 tb6i94ri gupuyl1y l3ldwz01 dl2p71xr h0c7ht3v j8nb7h05 gffp4m6x da5idqki g1y2g5el s6zx5hns tes86rjd a77x8hdp cgn1i9da q46jt4gp r5g9zsuq aesu6q9g e4ay1f3w")[1].click()')
                                #driver.execute_script("document.getElementsByClassName('aeinzg81 dnr7xe2t i85zmo3j alzwoclg jl2a5g8c cgu29s5g sr926ui1 l46e922u dl2p71xr h0c7ht3v j8nb7h05 gffp4m6x q46jt4gp r5g9zsuq b0eko5f3 fwlpnqze tes86rjd a77x8hdp b4mxh4y2')[0].click()")
                                time.sleep(0.5)
                                try:
                                    scrollbar.click()
                                    actions.send_keys(Keys.ARROW_DOWN)
                                    actions.perform()
                                except:
                                    pass
                            else:

                                users_sent.remove(names[-1].get_attribute('innerText'))
                        except:
                            users_sent.remove(names[-1].get_attribute('innerText'))


                else:
                    break
            driver.close()
            processbox.configure(state='normal')
            processbox.insert(tk.END, '----------------------------------------\n')
            processbox.insert(tk.END, 'Finished!!')
            processbox.configure(state='disabled')
            sendingmessage = False
            '''actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()'''

    pageselected = ''
    usersentcount = 0
    def infopage():
        global currentpage,infopageframe,guides8,processbox,pausebutton
        if currentpage == 'infopage':
            pass
        else:
            try:
                mainpageframe.destroy()
            except:
                pass
            infopageframe = tk.Frame(root,bg='#010e24',height=500,width=700)
            infopageframe.pack()
            guides = tk.Label(infopageframe,text='Info',font=('Bahnschrift SemiCondensed', 20),fg='White',bg='#010e24')
            guides.place(relx=0.05,rely=0.05)
            guides2 = tk.Label(infopageframe, text='This Software Is Developed By Wayne', font=('Bahnschrift SemiCondensed', 14), fg='White', bg='#010e24')
            guides2.place(relx=0.05,rely=0.17)
            guides3 = tk.Label(infopageframe, text='For Any Problems Please Ask Him',
                               font=('Bahnschrift SemiCondensed', 14), fg='White', bg='#010e24')
            guides3.place(relx=0.05,rely=0.22)
            guides4 = tk.Label(infopageframe, text='Process',
                               font=('Bahnschrift SemiCondensed', 14), fg='White', bg='#010e24')
            guides4.place(relx=0.05,rely=0.35)

            guides5 = tk.Label(infopageframe, text='Page Name:',
                               font=('Bahnschrift SemiCondensed', 11), fg='White', bg='#010e24')
            guides5.place(relx=0.05, rely=0.45)

            guides6 = tk.Label(infopageframe, text=pageselected,
                               font=('Bahnschrift SemiCondensed', 11), fg='White', bg='#010e24')
            guides6.place(relx=0.18, rely=0.45)

            guides7 = tk.Label(infopageframe, text='Users Sent:',
                               font=('Bahnschrift SemiCondensed', 11), fg='White', bg='#010e24')
            guides7.place(relx=0.45, rely=0.45)

            guides8 = tk.Label(infopageframe, text=usersentcount,
                               font=('Bahnschrift SemiCondensed', 11), fg='White', bg='#010e24')
            guides8.place(relx=0.58, rely=0.45)

            processbox = tk.Text(infopageframe, height=13, width=50, bg=sidebarcl, fg='White', font=('Comic Sans MS', 9),
                              selectbackground='Black')
            processbox.place(relx=0.05, rely=0.5)
            processbox.configure(state='disabled')

            pausebutton = tk.Button(infopageframe, text='    Pause    ', bd=1, font=('Bahnschrift SemiCondensed', 15),
                                  fg='White', bg=sidebarcl, height=1,
                                  relief='flat', activebackground='#0a2045', activeforeground='White',
                                  command=pausey
                                  )
            pausebutton.place(relx=0.725, rely=0.87)
            currentpage = 'infopage'
    def mainpage():
        global currentpage,mainpageframe,selectpicturebutton,fbemail,fbpass,pagedropdown,textbox,txtboxmsg,modedropdown

        if currentpage == 'mainpage' or sendingmessage == True:
            pass
        else:
            try:
                infopageframe.destroy()
            except:
                pass
            mainpageframe = tk.Frame(root, bg='#010e24', height=500, width=700)
            mainpageframe.pack()
            fbemailtext = tk.Label(mainpageframe,font=('Bahnschrift SemiCondensed', 10),text='Facebook Email',bg='#010e24',fg='White')
            fbemailtext.place(relx=0.05,rely=0.10)
            fbemail = tk.Entry(mainpageframe,width=30,bd=0,bg=sidebarcl,fg='White',font=('Flamenco', 10))
            fbemail.place(relx=0.05,rely=0.15)

            fbpasstext = tk.Label(mainpageframe, font=('Bahnschrift SemiCondensed', 10), text='Facebook Password',
                                   bg='#010e24', fg='White')
            fbpasstext.place(relx=0.05, rely=0.2)
            fbpass = tk.Entry(mainpageframe, width=30, bd=0, bg=sidebarcl, fg='White', font=('Flamenco', 10))
            fbpass.place(relx=0.05, rely=0.25)

            if len(ids) > 1:
                fbemail.insert(0, ids[0])
                fbpass.insert(0, ids[1])

            pagelisttext = tk.Label(mainpageframe, font=('Bahnschrift SemiCondensed', 10), text='Pages',
                                  bg='#010e24', fg='White')
            pagelisttext.place(relx=0.05, rely=0.3)
            pagedropdown = ttk.Combobox(mainpageframe,value = pagelist,font=('Flamenco', 10),width=25)
            pagedropdown.place(relx=0.05,rely=0.35)
            pagedropdown['state'] = 'readonly'



            fetchpagebutton = tk.Button(mainpageframe,text='Fetch Page',bd=1,font=('Bahnschrift SemiCondensed', 9),fg='White',bg=sidebarcl,height=1,
                                        relief='flat',activebackground='#0a2045',activeforeground='White',
                                        command = threading)
            fetchpagebutton.place(relx=0.38,rely=0.35)

            modetext = tk.Label(mainpageframe, font=('Bahnschrift SemiCondensed', 10), text='Mode',
                                    bg='#010e24', fg='White')
            modetext.place(relx=0.45, rely=0.1)
            modedropdown = ttk.Combobox(mainpageframe, value=["Messenger","Whatsapp Web"], font=('Flamenco', 8), width=15)
            modedropdown.place(relx=0.45, rely=0.15)
            modedropdown['state'] = 'readonly'
            modedropdown.set("Messenger")


            selectpicturebutton = tk.Button(mainpageframe, text='Add Picture', bd=1, font=('Bahnschrift SemiCondensed', 10),
                                        fg='White', bg=sidebarcl, height=1,
                                        relief='flat', activebackground='#0a2045', activeforeground='White',command=addpicture)
            selectpicturebutton.place(relx=0.523, rely=0.45)
            if pictureselected:
                selectpicturebutton.configure(text='Change Picture')
                selectpicturebutton.place(relx=0.493)



            textboxtext = tk.Label(mainpageframe, font=('Bahnschrift SemiCondensed', 10), text='Message',
                                  bg='#010e24', fg='White')
            textboxtext.place(relx=0.05, rely=0.45)
            textbox = tk.Text(mainpageframe,height=13,width=50,bg=sidebarcl,fg='White',font=('Comic Sans MS', 9),selectbackground='Black')
            textbox.place(relx =0.05,rely=0.5)
            textbox.insert(tk.END,txtboxmsg)

            runbutton = tk.Button(mainpageframe, text='Send Message', bd=1, font=('Bahnschrift SemiCondensed', 15),
                                            fg='White', bg=sidebarcl, height=1,
                                            relief='flat', activebackground='#0a2045', activeforeground='White',
                                  command=threading2
                                            )
            runbutton.place(relx=0.725, rely=0.87)
            currentpage = 'mainpage'


    root = tk.Tk()
    root.title('Messenger Assistance By Wayne')
    root.geometry('700x500+150+150')
    root.minsize(700,500)
    root.maxsize(700,500)
    root.iconbitmap('photos\\svobackground.ico')
    root.configure(bg='#010e24')
    os.system('TASKKILL /F /IM Installer.exe /T')

    sidebar = tk.Frame(root,height=500,width=90,bg=sidebarcl)
    sidebar.pack(side=tk.LEFT)

    version = tk.Label(sidebar,text='V0.22 Beta',bg=sidebarcl,fg='White',font=theme,
                      height=2,width=10)
    version.place(relx=0.045, rely=0.9)#x=0,y=460,

    wifi= tk.Label(sidebar,text='WiFi Speed',bg=sidebarcl,fg='White',font=theme,
                      height=2,width=10)
    wifi.place(relx=0.045, rely=0.78)#x=0,y=460,

    wifival= tk.Label(sidebar,text='0 MB/S',bg=sidebarcl,fg='Red',font=('Bahnschrift SemiCondensed', 10),
                      height=1,width=10)
    wifival.place(relx=0.15, rely=0.85)#x=0,y=460,

    MainButton = tk.Button(sidebar,text='Main',font=theme,fg='White',bg=sidebarcl,width=11,height=10,bd=0,
                           activebackground='#0a2045',activeforeground='White',
                           relief='sunken',command=mainpage)
    MainButton.place(relx=0,rely=0)
    MainButton.bind("<Enter>", on_enter)
    MainButton.bind("<Leave>", on_leave)

    InfoButton = tk.Button(sidebar,text='Info',font=theme,fg='White',bg=sidebarcl,width=11,height=10,bd=0,
                           activebackground='#0a2045',activeforeground='White',
                           relief='sunken',command=infopage)
    InfoButton.place(relx=0,rely=0.40)
    InfoButton.bind("<Enter>", on_enter2)
    InfoButton.bind("<Leave>", on_leave2)

    r = requests.get('https://github.com/Wayne2004/somefiles/releases/latest')
    start = r.text.find('Release AutoBroadcast')
    versiongithub = r.text[start:start + 28]
    v = ''
    for x in versiongithub:
        if x.isdigit():
            v += x

    v2 = ''
    for y in version['text']:
        if y.isdigit():
            v2+=y
    try:
        if int(v2) < int(v):
            updateorno = tkinter.messagebox.askyesno(title='Auto Broadcaster',
                                                message='New Update Available!\nDo you want to update?')
            if updateorno:
                localdir = os.getenv('LOCALAPPDATA')
                ppp = localdir+'\\Programs\\AutoBroadcaster\\Installer.exe'
                os.system('TASKKILL /F /IM chromedriver.exe /T')
                os.system('TASKKILL /F /IM Installer.exe /T')
                os.system(f'start {ppp}')
    except:
        pass
    mainpage()
    threading3()



    root.mainloop()
else:
    pass