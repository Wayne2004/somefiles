import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from os import system
from io import BytesIO
from PIL import Image
import win32clipboard
import pyperclip


def startprocess(email,password,message,picture=0):

    clear = lambda: system('cls')

    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome("C:\\chromedriver.exe",options=chrome_options)
    driver.set_window_size(1050,810)
    driver.get("https://www.facebook.com/")

    time.sleep(2)

    #enter email and pass
    driver.execute_script(f'document.getElementsByName("email")[0].value="{email}"')
    time.sleep(0.2)
    passinput = driver.find_element(By.XPATH, '//*[@id="pass"]')
    passinput.send_keys(password)
    driver.execute_script('document.getElementsByName("login")[0].click()')
    input("Solve 2FA then click ENTER: :D")
#here start test
    time.sleep(2)
    driver.get('https://business.facebook.com/latest/home?nav_ref=profile_plus_admin_tool')
    #driver.get('https://business.facebook.com/')
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='p5mefues j32recxq j94dm2s7 trbvugp6 fsf7x5fv icdlwmnq mfclru0v o0fq7q06 nf8twy9x kt7nmhdu g1rk5lpy bdao358l nq2b4knc nu7423ey ok56jwvq myhqxb6t hi9kr3d2 fyw6oool l27737jg tb9mkqme mhv8me6f _3qn7 _61-0 _2fyi _3qng']").click()
    time.sleep(2)
    while True:
        pns = driver.find_elements(By.XPATH,'//span[@class="qrxcjm7n hmv1tv54 kr054jk4 a77x8hdp qc5lal2y l4uc2m3f gh25dzvf t7p7dqev gh55jysx aeinzg81"]')
        if pns != []:
            break
        else:
            pass
    for _ in pns:
        if _.get_attribute('innerText').lower() == 'create a business account':
            pns.remove(_)
    numberofpages = 0
    for x in pns:
        numberofpages+=1
        print(numberofpages,'. ',x.get_attribute('innerText'))
    print(f"\n{numberofpages} pages found in this account!")


    #selecting which page
    selectedpage = []
    while True:
        pageselect = input("Please Select A Page (example: 2): ")
        try:
            int(pageselect)
            break
        except:
            print("Please Enter Number Only, Nothing else.")
    selectedpage.append(pns[int(pageselect)-1])
    clear()
    print(selectedpage[0].get_attribute('innerText'), " Selected!")
    selectedpagename = selectedpage[0].get_attribute('innerText')
    gayshiet = selectedpage[0].get_attribute('innerText')
    selectedpage[0].click()
    time.sleep(3)

    checkifpagenamecorrect = driver.find_element(By.XPATH,'//div[@class="qrxcjm7n hmv1tv54 kr054jk4 a77x8hdp qm54mken lq84ybu9 hf30pyar oshhggmv nnmaouwa gh55jysx"]')
    while True:
        if selectedpagename != checkifpagenamecorrect.get_attribute('innerText'):
            time.sleep(1)
        else:
            break

    #open inbox
    inbox = driver.find_elements(By.XPATH, '//div[@class = "_7pon"]')
    inboxfound = []
    for x in inbox:
        if 'inbox' in x.get_attribute('innerText').lower():
            inboxfound.append(x)
        else:
            pass
    inboxfound[0].click()




    #send message
    users_sent = []

    #test scrollbar
    time.sleep(4)
    while True:
        try:
            driver.find_element(By.XPATH,"//div[@aria-label='Messenger']").click()
            break
        except:
            pass

    while True:
        try:
            scrollbar = driver.find_element(By.XPATH,"//div[@class='_1t0w _1t0z _1t0_']")
            scrollbar.click()
            break
        except:
            pass
    actions = ActionChains(driver)
    isitlastuser = []
    while True:
        while True:
            try:
                chats = driver.find_elements(By.XPATH, '//div[@class="_a6ag _a6ah clearfix _ikh"]')
                #chats = driver.find_elements(By.XPATH, '//div[@class="a7ki207s fqx7lvqr szxkbqsu sgsj3rsc j14zrrqg b3bz9o9y gng4jb5z k5pgg3kl"]')
                chats[-1].click()
                break
            except Exception as e:
                print(e)
                pass
        time.sleep(1)
        names = driver.find_elements(By.XPATH, '//span[@class="gkum2dnh igjjae4c h3z9dlai h82avkqd b6ax4al1 g2zy4fhw"]')
        isitlastuser.append(names[-1].get_attribute('innerText'))


        scrollbar.click()
        for _ in range(150):
            actions.send_keys(Keys.ARROW_DOWN)
            actions.perform()


        chats = driver.find_elements(By.XPATH, '//div[@class="_a6ag _a6ah clearfix _ikh"]')
        #chats = driver.find_elements(By.XPATH, '//div[@class="a7ki207s fqx7lvqr szxkbqsu sgsj3rsc j14zrrqg b3bz9o9y gng4jb5z k5pgg3kl"]')
        chats[-1].click()
        time.sleep(1)
        names = driver.find_elements(By.XPATH, '//span[@class="gkum2dnh igjjae4c h3z9dlai h82avkqd b6ax4al1 g2zy4fhw"]')


        if names[-1].get_attribute('innerText') in isitlastuser:
            break

        else:
            isitlastuser.pop()




    while True:
        #click the last chat
        chats = driver.find_elements(By.XPATH, '//div[@class="_a6ag _a6ah clearfix _ikh"]')
        #chats = driver.find_elements(By.XPATH,'//div[@class="a7ki207s fqx7lvqr szxkbqsu sgsj3rsc j14zrrqg b3bz9o9y gng4jb5z k5pgg3kl"]')
        chats[-1].click()
        time.sleep(2)

        names = driver.find_elements(By.XPATH,'//span[@class="gkum2dnh igjjae4c h3z9dlai h82avkqd b6ax4al1 g2zy4fhw"]')

        if names[-1].get_attribute('innerText') not in users_sent:
            users_sent.append(names[-1].get_attribute('innerText'))
            try:
                print('\nSending to ',names[-1].get_attribute('innerText'))

                #try find if blocked, if exception means not blocked and loop it until find text area
                #try later


                textarea = driver.find_element(By.XPATH, "//textarea[@type='text']")
                print('t')
                if picture!= 0 :
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
                textarea.send_keys(Keys.LEFT_CONTROL+'v')

                if picture!=0:
                    while True:
                        try:
                            driver.find_element(By.XPATH,'//i[@class="dl2p71xr h0c7ht3v j8nb7h05 gffp4m6x jez8cy9q img sp_vVVftNVsvuT_1_5x sx_c0b91f"]')
                            break
                        except:
                            pass




                time.sleep(0.3)
                sendbutton = driver.find_element(By.XPATH, "//div[@aria-label='Send']").click()
                print('SENT!!!')
                time.sleep(1)
            except Exception as e:
                print('Error: Customer Blocked You!')
                print('Moving Chat To Spam Since Message Cant Send...')
                driver.execute_script('document.getElementsByClassName("qi72231t tav9wjvu flwp5yud tghlliq5 gkg15gwv frfouenu bonavkto djs4p424 r7bn319e bdao358l fsf7x5fv s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk dnr7xe2t aeinzg81 cr00lzj9 s3jn8y49 g4tp4svg i85zmo3j pkdwr69g sc980dfb kq3l28k4 rc95jfaf fxk3tzhb tgm57n0e jl2a5g8c jez8cy9q gvxzyvdx om3e55n1 rn8ck1ys f14ij5to bq6c9xl4 tb6i94ri gupuyl1y l3ldwz01 dl2p71xr h0c7ht3v j8nb7h05 gffp4m6x da5idqki g1y2g5el s6zx5hns tes86rjd a77x8hdp cgn1i9da q46jt4gp r5g9zsuq aesu6q9g e4ay1f3w")[1].click()')
                driver.execute_script("document.getElementsByClassName('aeinzg81 dnr7xe2t i85zmo3j alzwoclg jl2a5g8c cgu29s5g sr926ui1 l46e922u dl2p71xr h0c7ht3v j8nb7h05 gffp4m6x q46jt4gp r5g9zsuq b0eko5f3 fwlpnqze tes86rjd a77x8hdp b4mxh4y2')[0].click()")
                time.sleep(0.5)
                try:
                    scrollbar.click()
                    actions.send_keys(Keys.ARROW_DOWN)
                    actions.perform()
                except:
                    pass
                pass

        else:
            break
    print(f'Finished Sending to {len(users_sent)} people!! in {gayshiet}')
    driver.close()




