import os
import subprocess
import sys
import time
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore, Style

init(autoreset=True)

# -------------------------
# Execução de comandos com pausa em caso de erro
# -------------------------
def run_cmd(cmd, capture_output=False):
    try:
        if capture_output:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            return result.decode().strip()
        else:
            subprocess.run(cmd, shell=True, check=True)
            return ""
    except subprocess.CalledProcessError as e:
        print(Fore.RED + Style.BRIGHT + f"\n[ERRO] Comando falhou: {e}")
        input(Fore.YELLOW + "[PAUSA] Pressione Enter após verificar o erro para continuar...")
        return None

# -------------------------
# Mensagens médias e grandes
# -------------------------
def aviso_medio(msg):
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "="*60)
    print(Fore.YELLOW + Style.BRIGHT + msg.center(60))
    print(Fore.YELLOW + Style.BRIGHT + "="*60 + "\n")

def aviso_grande(msg):
    print(Fore.RED + Style.BRIGHT + "\n" + "#"*80)
    for line in msg.splitlines():
        print(Fore.RED + Style.BRIGHT + line.center(80))
    print(Fore.RED + Style.BRIGHT + "#"*80 + "\n")

# -------------------------
# Seleção de arquivo via Tkinter
# -------------------------
def select_file(title="Selecione um arquivo", initial_dir=None):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title=title, initialdir=initial_dir)

# -------------------------
# Confirmação de reboot do usuário
# -------------------------
def wait_for_user_reboot(msg):
    while True:
        resposta = input(msg).strip().lower()
        if resposta == 's':
            break
        elif resposta == 'n':
            print(Fore.YELLOW + "[AGUARDANDO] Verifique o dispositivo e tente novamente...")
            time.sleep(5)
        else:
            print(Fore.RED + "Opção inválida! Digite 's' para sim ou 'n' para não.")

# -------------------------
# Verificador de dispositivo Fastboot
# -------------------------
def check_device():
    while True:
        fastboot_output = run_cmd("fastboot devices", capture_output=True)
        fastboot_lines = fastboot_output.splitlines() if fastboot_output else []
        fastboot_devices = [line for line in fastboot_lines if line.strip()]
        if fastboot_devices:
            device_id = fastboot_devices[0].split()[0]
            print(Fore.GREEN + Style.BRIGHT + f"Dispositivo Fastboot conectado: {device_id}")
            break
        print(Fore.YELLOW + "[AGUARDANDO] Nenhum dispositivo Fastboot encontrado. Conecte via USB...")
        time.sleep(3)

# -------------------------
# Função principal do fluxo de instalação
# -------------------------
def install_custom_a14():
    a14_dir = os.path.join(os.getcwd(), "A14")

    # Pergunta sobre flash da stock
    print(Fore.RED + Style.BRIGHT + "\n[ AVISO: A STOCK ANDROID 14 É NECESSÁRIO PARA DAR BOOT NAS CUSTOM A14 ]")
    flash_stock = input("Deseja fazer o flash da stock A14? (s/n): ").strip().lower()

    if flash_stock == 's':
        # Executa .bat da stock
        stock_script = os.path.join(a14_dir, "stockA14.bat")
        aviso_medio("Executando flash da stock A14...")
        run_cmd(f'"{stock_script}"')

    # -------------------------
    # Fluxo comum após stock ou sem stock
    # -------------------------
    aviso_medio("Setando slot ativo para B")
    run_cmd("fastboot set_active b")

    aviso_medio("Reiniciando no bootloader...")
    run_cmd("fastboot reboot bootloader")
    wait_for_user_reboot("O dispositivo entrou no bootloader corretamente? (s/n): ")

    # Seleção de arquivos custom
    aviso_medio("Selecione os arquivos da custom ROM")
    vendor_boot_custom = select_file("Escolha o vendor_boot.img da custom ROM", initial_dir=a14_dir)
    custom_zip = select_file("Escolha o arquivo .zip da custom ROM", initial_dir=a14_dir)
    boot_custom_option = input("Deseja incluir boot.img personalizado? (s/n): ").strip().lower()
    boot_img_custom = None
    if boot_custom_option == 's':
        boot_img_custom = select_file("Escolha o boot.img personalizado", initial_dir=a14_dir)

    # Flash vendor_boot da custom
    aviso_medio("Flashando vendor_boot da custom ROM")
    run_cmd(f'fastboot flash vendor_boot_a "{vendor_boot_custom}"')
    run_cmd(f'fastboot flash vendor_boot_b "{vendor_boot_custom}"')

    # Reinicia no recovery
    aviso_medio("Reiniciando no recovery...")
    run_cmd("fastboot reboot recovery")
    wait_for_user_reboot("O dispositivo entrou no modo recovery corretamente? (s/n): ")

    aviso_medio("No menu recovery, selecione 'Apply Update', em seguida 'Apply from ADB'")
    aviso_grande("Se aparecer mensagem pedindo reboot, selecione 'NO' para evitar problemas")
    aviso_medio("Caso a porcentagem do sideload não atinja 100%, isso é totalmente normal.")
    input("Pressione Enter quando estiver pronto para iniciar o sideload...")

    # Sideload do zip custom
    aviso_medio("Iniciando sideload da custom ROM")
    run_cmd(f'adb sideload "{custom_zip}"')

    # Reinicia no fastboot
    aviso_medio("Reiniciando no fastbootd...")
    run_cmd("adb reboot fastboot")
    wait_for_user_reboot("O dispositivo entrou no fastbootd corretamente? (s/n): ")

    # Flash opcional do boot.img
    if boot_img_custom:
        aviso_medio("Flashando boot.img personalizado")
        run_cmd(f'fastboot flash boot_a "{boot_img_custom}"')

    # Finaliza reboot system
    aviso_medio("Reiniciando no sistema...")
    run_cmd("fastboot reboot")
    wait_for_user_reboot("O dispositivo iniciou no sistema corretamente? (s/n): ")

    aviso_medio("Parabéns! Custom ROM instalada com sucesso!")

# -------------------------
# Menu principal
# -------------------------
def main():
    aviso_medio("=== Instalador Custom ROM CancunF ===")
    print("Selecione a versão do Android da custom ROM:")
    print("1. A14")
    print("2. A15 (recomendado, em desenvolvimento)")
    choice = input("Escolha (1 ou 2): ").strip()

    if choice == "1":
        install_custom_a14()
    elif choice == "2":
        aviso_medio("A15 ainda está em desenvolvimento. Recomenda-se usar A14")
    else:
        aviso_medio("Opção inválida. Encerrando script")
        sys.exit(0)

# -------------------------
# Execução
# -------------------------
if __name__ == "__main__":
    check_device()
    main()
