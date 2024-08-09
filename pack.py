import os
import shutil
import subprocess
from colorama import init, Fore, Style  # type: ignore

init(autoreset=True)

__author__ = 'Furkan Güçlü'
__version__ = 'B-1.0.0'

def process_pack_directory(directory_name):
    """
    Belirtilen dizindeki pack dosyalarını işleyip, uygun yere taşıyan fonksiyon.
    """
    print(f'\n{Fore.YELLOW}"{directory_name}" klasörü işleniyor...{Style.RESET_ALL}')
    result = subprocess.run(['PackMakerLite', '--nolog', '-p', directory_name], capture_output=True, text=True)
    if result.returncode == 0:
        # Dosyaları kontrol et
        pack_files = [f for f in os.listdir('.') if f.startswith(directory_name) and (f.endswith('.eix') or f.endswith('.epk'))]
        if pack_files:
            for pack_file in pack_files:
                source = os.path.join('.', pack_file)
                destination = os.path.join('..', '..', 'Client', 'pack', pack_file)
                if os.path.exists(source):
                    print(f'{Fore.CYAN}"{pack_file}" dosyası bulundu. Taşınıyor...{Style.RESET_ALL}')
                    if not os.path.exists(os.path.dirname(destination)):
                        print(f'{Fore.CYAN}Hedef dizin "{os.path.dirname(destination)}" oluşturuluyor...{Style.RESET_ALL}')
                        os.makedirs(os.path.dirname(destination))
                    shutil.move(source, destination)
                    print(f'{Fore.GREEN}"{pack_file}" dosyası "{destination}" konumuna başarıyla taşındı.{Style.RESET_ALL}')
                else:
                    print(f'{Fore.RED}"{source}" dosyası bulunamadı.{Style.RESET_ALL}')
            print(f"{Fore.GREEN}Taşıma işlemi başarılı.{Style.RESET_ALL}")
        else:
            print(f'{Fore.RED}Dizinde "{directory_name}.*" dosyası bulunamadı veya taşınamadı: "{os.path.abspath(".")}".{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}"{directory_name}" klasörünü işlerken bir hata oluştu: {result.stderr.strip()}{Style.RESET_ALL}')

def process_all_directories():
    """
    Tüm ana dizinleri işleyip pack dosyalarını taşıyan fonksiyon.
    """
    print(f'\n{Fore.YELLOW}Tüm klasörler işleniyor...{Style.RESET_ALL}')
    unpacked_dir = os.path.join('..', '..', 'UnPacked', 'Ymir Work')
    for item in os.listdir(unpacked_dir):
        item_path = os.path.join(unpacked_dir, item)
        if os.path.isdir(item_path):
            print(f'{Fore.CYAN}"{item_path}" dizini işleniyor...{Style.RESET_ALL}')
            process_pack_directory(item)

def main():
    """
    Kullanıcıdan giriş alarak pack işleme işlemlerini gerçekleştiren ana fonksiyon.
    """
    print(f"\n{Fore.GREEN}Çıkış yapmak için [Q]'ya basın, toplu işlem yapmak için [All] yazın.{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Geliştirici: {Fore.RED}{__author__}{Style.RESET_ALL} | Versiyon: {__version__}")
    while True:
        user_input = input(f"{Fore.WHITE}Pack İsmi : {Style.RESET_ALL}").strip()
        
        if user_input.lower() == "q":
            print(f"\n{Fore.CYAN}Programdan çıkılıyor...{Style.RESET_ALL}")
            break
        elif user_input.lower() == "all":
            process_all_directories()
        else:
            process_pack_directory(user_input)

if __name__ == "__main__":
    main()
