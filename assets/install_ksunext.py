#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def install_ksu_next(lang_code="pt"):
    import os, subprocess, shutil
    from colorama import Fore

    # ==============================
    # Idioma
    # ==============================
    lang = lang_code.lower()  # garante minúscula

    T = {
        "pt": {
            "title": "Instalação do KernelSU Next",
            "check": "Iniciando verificação do boot.img...",
            "local_found": "boot.img encontrado localmente em: {path}",
            "adb_found": "boot.img encontrado no dispositivo via ADB em: {path}",
            "adb_missing": "ADB não encontrado — ignorando verificação remota.",
            "adb_error": "Erro ao executar ADB: {error}",
            "not_found": "Nenhum boot.img encontrado em /sdcard. Coloque o arquivo e tente novamente.",
            "ksupusher_start": "Subindo ksupatcher.sh para o dispositivo...",
            "ksupatcher_run": "Executando ksupatcher.sh no dispositivo...",
            "patch_success": "Boot patchado disponível no dispositivo: {path}",
            "patch_fail": "Boot patchado não encontrado no dispositivo.",
            "wip": "Módulo KernelSU ainda em desenvolvimento — calma que o chefe tá codando o resto.",
            "tmp_saved": "Arquivos salvos em: {path}",
            "flash_prompt": "Deseja flashar o boot patchado agora? (s/n): ",
            "boot_ok_prompt": "O dispositivo iniciou corretamente? (s/n): ",
            "fastboot_error": "Dispositivo não detectado em fastboot. Reinicie no bootloader manualmente.",
            "return": "Pressione Enter para voltar ao menu..."
        },
        "en": {
            "title": "KernelSU Next Installation",
            "check": "Starting boot.img verification...",
            "local_found": "boot.img found locally at: {path}",
            "adb_found": "boot.img found on the device via ADB at: {path}",
            "adb_missing": "ADB not found — skipping remote check.",
            "adb_error": "Failed to execute ADB: {error}",
            "not_found": "No boot.img found in /sdcard. Place the file there and try again.",
            "ksupusher_start": "Pushing ksupatcher.sh to the device...",
            "ksupatcher_run": "Running ksupatcher.sh on the device...",
            "patch_success": "Patched boot is available on the device: {path}",
            "patch_fail": "Patched boot not found on the device.",
            "wip": "KernelSU module still under development — boss is coding the rest manually.",
            "tmp_saved": "Files saved at: {path}",
            "flash_prompt": "Do you want to flash the patched boot now? (y/n): ",
            "boot_ok_prompt": "Did the device start correctly? (y/n): ",
            "fastboot_error": "Device not detected in fastboot. Please manually reboot into bootloader.",
            "return": "Press Enter to return to the menu..."
        }
    }[lang]

    print(Fore.YELLOW + "\n" + T["title"])
    print(Fore.CYAN + T["check"])

    # ==============================
    # Detect boot.img local
    # ==============================
    boot_path = "/sdcard/boot.img" if os.path.exists("/sdcard/boot.img") else None
    if boot_path:
        print(Fore.GREEN + T["local_found"].format(path=boot_path))

    # Detect via ADB se não encontrado local
    if boot_path is None and shutil.which("adb"):
        try:
            out = subprocess.run(["adb", "shell", "ls", "/sdcard/boot.img"],
                                 capture_output=True, text=True)
            if out.returncode == 0 and "No such file" not in out.stdout:
                boot_path = "adb:/sdcard/boot.img"
                print(Fore.GREEN + T["adb_found"].format(path="/sdcard/boot.img"))
        except Exception as e:
            print(Fore.RED + T["adb_error"].format(error=str(e)))
    elif boot_path is None:
        print(Fore.YELLOW + T["adb_missing"])

    if boot_path is None:
        print(Fore.RED + T["not_found"])
        input(Fore.YELLOW + T["return"])
        return

    # ==============================
    # Enviar e executar ksupatcher.sh
    # ==============================
    print(Fore.CYAN + T["ksupusher_start"])
    ksu_script_local = os.path.join("scripts", "ksupatcher.sh")
    if not os.path.exists(ksu_script_local):
        print(Fore.RED + f"{ksu_script_local} não encontrado!")
        input(Fore.YELLOW + T["return"])
        return

    subprocess.run(["adb", "push", ksu_script_local, "/data/local/tmp/"], check=False)
    print(Fore.CYAN + T["ksupatcher_run"])
    subprocess.run(["adb", "shell", "cd /data/local/tmp && sh -x ksupatcher.sh ksun"], check=False)

    # ==============================
    # Pull boot original e patchado
    # ==============================
    tmp_dir = os.path.join(os.getcwd(), "tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    # Pull boot original
    subprocess.run(["adb", "pull", "/sdcard/boot.img", tmp_dir], check=False)

    # Inicializa variável antes do try
    boot_patched_path = None

    try:
        out = subprocess.run(["adb", "shell", "ls /sdcard/Download/"],
                             capture_output=True, text=True)
        files = out.stdout.splitlines()
        patched_files = [f for f in files if f.startswith("kernelsu_next_patched_") and f.endswith(".img")]
        if patched_files:
            patched_files.sort()
            boot_patched_path = os.path.join(tmp_dir, patched_files[-1])
            remote_path = f"/sdcard/Download/{patched_files[-1]}"
            subprocess.run(["adb", "pull", remote_path, tmp_dir], check=False)
            print(Fore.GREEN + T["patch_success"].format(path=boot_patched_path))
        else:
            print(Fore.RED + T["patch_fail"])
    except:
        print(Fore.RED + T["patch_fail"])

    print(Fore.YELLOW + T["tmp_saved"].format(path=tmp_dir))

    # ==============================
    # Pergunta para flashar
    # ==============================
    if boot_patched_path:
        flash = input(T["flash_prompt"]).lower()
        if flash in ("s", "y"):
            print(Fore.CYAN + "Reiniciando em fastboot...")
            subprocess.run(["adb", "reboot", "fastboot"], check=False)
            input("Aguarde até o dispositivo entrar em fastboot e pressione Enter...")

            # Loop de flash
            while True:
                fastboot_detect = subprocess.run(["fastboot", "devices"], capture_output=True, text=True)
                if fastboot_detect.stdout.strip() != "":
                    subprocess.run(["fastboot", "flash", "boot", boot_patched_path], check=False)
                    subprocess.run(["fastboot", "reboot"], check=False)

                    boot_ok = input(T["boot_ok_prompt"]).lower()
                    if boot_ok in ("s", "y"):
                        print(Fore.GREEN + "Finalizado! Boot patchado aplicado com sucesso.")
                        break
                    else:
                        print(Fore.YELLOW + "Tentando restaurar boot original...")
                        orig_boot = os.path.join(tmp_dir, "boot.img")
                        while True:
                            fastboot_detect = subprocess.run(["fastboot", "devices"], capture_output=True, text=True)
                            if fastboot_detect.stdout.strip() != "":
                                subprocess.run(["fastboot", "flash", "boot", orig_boot], check=False)
                                subprocess.run(["fastboot", "reboot"], check=False)
                                print(Fore.GREEN + "Boot original restaurado.")
                                break
                            else:
                                input(Fore.RED + T["fastboot_error"] + " Pressione Enter para tentar novamente...")
                        break
                else:
                    input(Fore.RED + T["fastboot_error"] + " Pressione Enter para tentar novamente...")

        input(Fore.YELLOW + T["return"])
