import os
import time
import subprocess
import platform
import shutil
from colorama import init, Fore, Style

# Tenta importar Tkinter
try:
    import tkinter as tk
    from tkinter import filedialog
    TK_AVAILABLE = True
except ImportError:
    TK_AVAILABLE = False

init(autoreset=True)

def run_cmd(command, capture_output=False):
    """Executa um comando no shell."""
    try:
        if capture_output:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            return result.strip()
        else:
            subprocess.run(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[ERRO] Comando falhou: {e}")
        if capture_output:
            return ""

def confirm_step(message):
    """Pergunta ao usuário se deseja prosseguir."""
    resp = input(Fore.YELLOW + f"{message} (s/n): ").strip().lower()
    if resp != "s":
        print(Fore.RED + "[ABORTADO] Usuário cancelou esta etapa.")
        exit(0)

def ask_file_input(description, extension):
    """Entrada manual para Termux."""
    filename = input(Fore.CYAN + f"[ARQUIVO] Digite o nome do {description} ({extension}): ").strip()
    if not os.path.isfile(filename):
        print(Fore.RED + f"[ERRO] Arquivo '{filename}' não encontrado no diretório atual.")
        exit(1)
    return filename

def select_file_gui(title, filetypes):
    """Interface gráfica de seleção de arquivo."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    root.destroy()
    return file_path.strip() if file_path else None

def get_file(description, extension):
    """Decide se usa Tkinter ou input manual."""
    os_name = platform.system().lower()
    termux_detected = shutil.which("termux-info") is not None

    if termux_detected or not TK_AVAILABLE:
        return ask_file_input(description, extension)
    else:
        file = select_file_gui(f"Selecione o {description}", [(extension.upper(), extension)])
        if not file:
            print(Fore.RED + f"[ERRO] Nenhum arquivo selecionado para {description}. Abortando.")
            exit(1)
        return file

def check_adb_device():
    """Confere se tem dispositivo ADB conectado."""
    output = run_cmd("adb devices", capture_output=True)
    lines = [l for l in output.splitlines() if l.strip() and not l.startswith("List")]
    return any("device" in l for l in lines)

def check_fastboot_device():
    """Confere se tem dispositivo Fastboot conectado."""
    output = run_cmd("fastboot devices", capture_output=True)
    lines = [l for l in output.splitlines() if l.strip()]
    return len(lines) > 0

def wait_user_confirmation(state_name):
    """Pergunta explicitamente se o dispositivo entrou no modo esperado."""
    confirm_step(f"O dispositivo entrou em {state_name}?")

def install_custom_a16():
    print(Fore.CYAN + Style.BRIGHT + "\n=== Cancunf Flash - Instalação Android 16 ===\n")

    # Seleção dos arquivos
    init_zip = get_file("Initial Install ZIP", "*.zip")
    custom_zip = get_file("Custom ROM ZIP", "*.zip")

    flash_boot = input(Fore.YELLOW + "Deseja flashar um boot.img personalizado? (s/n): ").strip().lower()
    boot_img = None
    if flash_boot == "s":
        boot_img = get_file("boot.img", "*.img")

    # Verificar dispositivo
    print(Fore.CYAN + "[INFO] Verificando dispositivos conectados...")

    if check_fastboot_device():
        print(Fore.GREEN + "[INFO] Dispositivo detectado em Fastboot.")
    elif check_adb_device():
        print(Fore.GREEN + "[INFO] Dispositivo detectado via ADB. Reiniciando em Fastboot...")
        confirm_step("Reiniciar dispositivo em bootloader?")
        run_cmd("adb reboot bootloader")
        time.sleep(5)
        wait_user_confirmation("bootloader (fastboot)")
        if not check_fastboot_device():
            print(Fore.RED + "[ERRO] Nenhum dispositivo em fastboot detectado após reboot.")
            return
    else:
        print(Fore.RED + "[ERRO] Nenhum dispositivo detectado. Conecte via ADB ou Fastboot.")
        return

    # Entrar em fastbootd
    confirm_step("Reiniciar em fastbootd?")
    run_cmd("fastboot reboot fastboot")
    time.sleep(5)
    wait_user_confirmation("fastbootd")

    # Flashar initial zip
    confirm_step(f"Flashar o initial install zip '{init_zip}'?")
    run_cmd(f"fastboot update \"{init_zip}\"")

    # Recovery
    confirm_step("Reiniciar no recovery?")
    run_cmd("fastboot reboot recovery")
    wait_user_confirmation("recovery")
    input(Fore.YELLOW + "No dispositivo, selecione: Apply Update > Apply from ADB. Pressione ENTER aqui quando pronto.")

    # ADB sideload da ROM
    confirm_step(f"Iniciar sideload da ROM '{custom_zip}'?")
    run_cmd(f"adb sideload \"{custom_zip}\"")

    # Boot.img opcional
    if flash_boot == "s" and boot_img:
        confirm_step(f"Flashar boot.img '{boot_img}'?")
        run_cmd("adb reboot bootloader")
        time.sleep(5)
        wait_user_confirmation("bootloader (fastboot)")
        run_cmd("fastboot reboot fastboot")
        time.sleep(5)
        wait_user_confirmation("fastbootd")
        run_cmd(f"fastboot flash boot \"{boot_img}\"")

    print(Fore.GREEN + "\n[SUCESSO] Instalação concluída com sucesso!")
    confirm_step("Deseja reiniciar o dispositivo agora?")
    run_cmd("fastboot reboot")
