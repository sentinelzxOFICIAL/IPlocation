import os
import json
import requests
from colorama import init, Fore, Style

# Inicializar o colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    print(Fore.RED + "    ____         __                 __" + Style.RESET_ALL)
    print(Fore.YELLOW + "   /  _/___     / /___  _________ _/ /" + Style.RESET_ALL)
    print(Fore.GREEN + "   / // __ \   / / __ \\/ ___/ __ `/ / " + Style.RESET_ALL)
    print(Fore.CYAN + " _/ // /_/ /  / / /_/ / /__/ /_/ / /  " + Style.RESET_ALL)
    print(Fore.MAGENTA + "/___/ .___/  /_/\\____/\\___/\\__,_/_/   " + Style.RESET_ALL)
    print(Fore.BLUE + "   /_/                                " + Style.RESET_ALL)
    
    print(Fore.YELLOW + """
|==========================================
|                                          |
|    developed: sentinelzxofc </>          |
|    Instagram: @sentinelzxofc.            | 
|                                          |
|==========================================|
""" + Style.RESET_ALL)

def display_main_menu():
    print(Fore.RED + "Enter IP :" + Style.RESET_ALL, end=' ')

def fetch_ip_data(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    return response.json()

def display_ip_info(geo_data):
    print(Fore.GREEN + f"""
  _____        __             _       
 |_   _|      / _|           (_)      
   | |  _ __ | |_ ___  _ __   _ _ __  
   | | | '_ \\|  _/ _ \\| '__| | | '_ \\ 
  _| |_| | | | || (_) | |    | | |_) |
 |_____|_| |_|_| \\___/|_|    |_| .__/ 
                               | |    
                               |_|    

Obs: Arquivo json criado 
Dev: @sentinelzxofc 

    IP: {geo_data['query']}
    Cidade: {geo_data['city']}
    Região: {geo_data['regionName']}
    País: {geo_data['country']}
    Código do País: {geo_data['countryCode']}
    ISP: {geo_data['isp']}
    Organização: {geo_data['org']}
    AS (Autonomous System): {geo_data['as']}
    Latitude: {geo_data['lat']}
    Longitude: {geo_data['lon']}
    Código Postal: {geo_data['zip']}
    Fuso Horário: {geo_data['timezone']}
    Localização do ISP: {geo_data['isp']}
""" + Style.RESET_ALL)

def main():
    while True:
        clear_screen()
        display_banner()
        display_main_menu()
        
        ip = input().strip()
        if not ip:
            continue
        
        clear_screen()
        geo_data = fetch_ip_data(ip)
        display_ip_info(geo_data)
        
        input(Fore.RED + "\nPressione Enter para retornar ao menu principal." + Style.RESET_ALL)

if __name__ == "__main__":
    main()