import os

clear = lambda :os.system('cls')

def Socks5_Login():
    with open("socks5_login.txt", newline="") as socks5_login_txt:
        socks5_login = socks5_login_txt.readlines()
        ALL_SOCKS5_LOGIN = [ ]
        for socks5 in socks5_login:
            ALL_SOCKS5_LOGIN.append(socks5.rstrip())
        return ALL_SOCKS5_LOGIN


def US_IPVANISH(All_SOCKS_LOGIN):
    with open("PROXY_BASE/us_proxy_base.txt", newline="") as proxyBase_txt:
        proxyBase = proxyBase_txt.readlines()
        ALL_PROXIES = [ ]
        ALL_PROXIES_WITH_LOGIN = [ ]
        for proxy in proxyBase:
            ALL_PROXIES.append(proxy.rstrip())
        for login in All_SOCKS_LOGIN:
            for proxy in ALL_PROXIES:
                ALL_PROXIES_WITH_LOGIN.append(proxy + login + "\n")
        with open("RESULTS/ipvanish-us.txt", "w") as results:
            results.writelines(ALL_PROXIES_WITH_LOGIN)


def ALL_IPVANISH(All_SOCKS_LOGIN):
    with open("PROXY_BASE/all_proxy_base.txt", newline="") as proxyBase_txt:
        proxyBase = proxyBase_txt.readlines()
        ALL_PROXIES = [ ]
        ALL_PROXIES_WITH_LOGIN = [ ]
        for proxy in proxyBase:
            ALL_PROXIES.append(proxy.rstrip())
        for login in All_SOCKS_LOGIN:
            for proxy in ALL_PROXIES:
                ALL_PROXIES_WITH_LOGIN.append(proxy + login + "\n")
        with open("RESULTS/ipvanish-all.txt", "w") as results:
            results.writelines(ALL_PROXIES_WITH_LOGIN)

def Location(socksLogin):
    LocationOfProxy = input("[1] US Proxies\n[2] ALL Proxies\n\n")
    if LocationOfProxy == '1':
        clear()
        US_IPVANISH(socksLogin)
    elif LocationOfProxy == '2':
        clear()
        ALL_IPVANISH(socksLogin)
    else:
        clear()
        print("[ERROR] INVALID INPUT")
        Location(socksLogin)

if __name__ == "__main__":
    socksLogin = Socks5_Login()
    Location(socksLogin)
    print("Done ... ")
