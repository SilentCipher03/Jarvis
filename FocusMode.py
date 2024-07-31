import time 
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time_str = input("Enter the time Eg :- [10:10] :- ")
    stop_time = datetime.datetime.strptime(stop_time_str, "%H:%M")

    host_path = r"C:\Windows\System32\drivers\Lenovo\udc\Service\Hosts"
    redirect = "127.0.0.1"

    print(current_time)

    website_list = ["www.youtube.com", "youtube.com", "www.facebook.com", "facebook.com"]
    if current_time < stop_time.strftime("%H:%M"):
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"\n{redirect} {website}")
                    print("Done")

            print("Website is blocked || Focus Mode On")        

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time >= stop_time.strftime("%H:%M"):
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)

                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)

                file.truncate()

                print("Website are unblocked")
                break

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, -1)


