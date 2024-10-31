import time
import os
from random import choice, randint
from colorama import init, Fore
from datetime import datetime


init(autoreset=True)

def main():
    n = 0
    r = ""

    while n <= 100:
        print(r, f"{Fore.LIGHTRED_EX}%{n}")
        n += randint(1, 5)
        r += "="
        time.sleep(0.1)

    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")

    print(f"""{Fore.LIGHTRED_EX}
    .%%%%%...%%%%%%..%%%%%%...%%%%..
    .%%..%%....%%......%%....%%..%%.
    .%%..%%....%%......%%....%%%%%%.
    .%%..%%....%%......%%....%%..%%.
    .%%%%%...%%%%%%....%%....%%..%%.
    ................................
    ⠀⠀⠀
    """)

    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    pink = "\033[95m"
    blue = "\033[94m"
    white = "\033[0m"
    link_sexy = ["link1", "link2", "link3"]

    time.sleep(1)
    print("")
    print(f"            {red}✪ {green}START TIME --->", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f"{red}✪ ")

    time.sleep(1)
    print("")
    print("")
    print(f"{yellow}―――‣{pink} im MR_DITA")
    time.sleep(0.4)
    print(f"{yellow}―――――‣{pink} MR_DITA REPORT ")
    time.sleep(0.3)
    print(f"{yellow}―――――――‣{pink} 09130756432")
    time.sleep(0.2)
    print(blue)
    print(" ")
    print(" ")
    os.system("echo MR_DITA TO AND")
    print(" ")
    print(" ")
    options = [
        "code account",
        "code group",
        "code channel",
        "link sexy",
        "link mokharab",
        "code hasas be server",
        "code tor",
        "link virus",
        "ip rubika"
    ]

    for i, option in enumerate(options, start=1):
        print(f"{red}[{green}{i}{red}] {yellow}―――‣ {red}{option} ")

    print(" ")
    print(" ")

    while True:
        try:
            ii = int(input(f"{red}[{green}?{red}] {green}لطفاً گزینه مورد نظر را وارد کنید --->{white} "))
            if 1 <= ii <= len(options):
                break
            else:
                print(f"{red}لطفاً یک گزینه معتبر وارد کنید.")
        except ValueError:
            print(f"{red}لطفاً یک عدد وارد کنید.")

    time.sleep(2)
    print(" ")
    print(" ")

    code = {
        1: "کد حساب: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2jEofU_oZSgmuTJ_jjCwp5fX0OMNHnzak2Q&usqp=CAU()http://ffmodmenu.page.link/Anti-Vhttps://B//L./A/C.K/P/a",
        2: "کد گروه: https://example.com/group_code",
        3: "کد کانال: https://example.com/channel_code",
        4: f"لینک sexy: {choice(link_sexy)}",
        5: "لینک مخرب: https://bit.ly/3ild93L",
        6: "کد حساس به سرور: (Server.online/server.offline.online/)",
        7: datetime.now().strftime('%d %H:%M:%S'),
        8: "لینک ویروس: http://Hackweb.xyz/python.html.cs",
        9: "آی‌پی روبیکا: 5.106.8.151"
    }

    print(f"{blue}{code[ii]}{white}")

    time.sleep(3)
    print(" ")
    print(" ")
    print(f"                  \033[0;102m {red} مخلوط کنید و بعد بزنید{white}")
    time.sleep(1)
    print(f"""{pink}
    python cod-filtering-MR_DITA.py""")
    print(" ")
    time.sleep(1)
    print(" ")
    print(" ")
    print(white)
    print("                  THE END")
    print(" ")

if __name__ == "__main__":
    main()
