import time
from datetime import datetime as dt

temp_host = "hosts"
host_url = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = ["facebook.com","google.com","dev.to"]
while True:
    
    if dt(dt.now().year,dt.now().month,dt.now().day,14) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours..")

        with open(temp_host,'r+') as file:
            content = file.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+'  '+website+"\n")
                    
    else:
        print("fun hours..")
        with open(temp_host,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
           
    time.sleep(5)
                
