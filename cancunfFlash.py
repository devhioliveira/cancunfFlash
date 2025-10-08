import sys
import time
import shutil
import platform
from colorama import init, Fore, Style
from flashA16 import install_custom_a16

init(autoreset=True)

def inicial_messages():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*70)
    print(Fore.CYAN + Style.BRIGHT + "Cancunf Flash v3 - Instalador de Custom ROM".center(70))
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.YELLOW + Style.BRIGHT + "\n[AVISO] Este script é apenas um AUXILIAR para instalação de Custom ROMs.")
    print(Fore.YELLOW + "[AVISO] NÃO nos responsabilizamos por danos ao dispositivo.\n")
    print(Fore.GREEN + "[CREDITOS] Desenvolvido por DevHiOliveira.\n")
    time.sleep(1)

def check_environment():
    print(Fore.CYAN + "[INFO] Checando ambiente do sistema...")

    os_name = platform.system().lower()
    termux_detected = shutil.which("termux-info") is not None

    if "windows" in os_name:
        print(Fore.GREEN + "[INFO] Sistema operacional: Windows")
    elif "linux" in os_name or termux_detected:
        print(Fore.GREEN + "[INFO] Sistema operacional: Linux / Termux")
    else:
        print(Fore.RED + "[ERRO] Sistema não suportado. Use Windows, Linux ou Termux.")
        sys.exit(1)

    # Checar se adb e fastboot estão disponíveis
    for tool in ["adb", "fastboot"]:
        if shutil.which(tool) is None:
            print(Fore.RED + f"[ERRO] {tool} não encontrado no sistema.")
            print(Fore.YELLOW + "Instale os pacotes necessários antes de prosseguir.")
            sys.exit(1)
        else:
            print(Fore.GREEN + f"[OK] {tool} encontrado.")

def alert_messages():
    print(Fore.RED + Style.BRIGHT + "\n[ALERTA] CERTIFIQUE-SE DE QUE:")
    print(Fore.RED + Style.BRIGHT + " - O BOOTLOADER está desbloqueado.")
    print(Fore.RED + Style.BRIGHT + " - A bateria está carregada (>60%).")
    print(Fore.RED + Style.BRIGHT + " - ESTE SCRIPT FOI TESTADO APENAS NO MOTOROLA G54 5G (CANCUNF).")
    print(Fore.RED + Style.BRIGHT + "   NÃO USE EM OUTROS DISPOSITIVOS!\n")

    confirm = input(Fore.YELLOW + "Deseja continuar mesmo assim? (s/n): ").strip().lower()
    if confirm != "s":
        print(Fore.RED + "[ABORTADO] Usuário cancelou a execução.")
        sys.exit(0)

def main():
    inicial_messages()
    check_environment()
    alert_messages()

    print(Fore.CYAN + "\n[INFO] Iniciando instalação da ROM Android 16...\n")
    install_custom_a16()

if __name__ == "__main__":
    main()
