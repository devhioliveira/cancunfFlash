def flash_custom_rom(L):
    print(Fore.CYAN + f"\n{L['install_rom']}\n")
    time.sleep(0.8)

    # 1. Detect ADB or fastboot
    print(Fore.CYAN + L["detect_dev"])
    adb_out = subprocess.getoutput("adb devices")
    fastboot_out = subprocess.getoutput("fastboot devices")

    # adb_out includes header "List of devices attached"; a connected device shows "<serial>\tdevice"
    adb_has_device = False
    for line in adb_out.splitlines():
        if "\tdevice" in line:
            adb_has_device = True
            break

    if adb_has_device:
        print(Fore.GREEN + L["adb_found"])
        print(Fore.CYAN + L["reboot_bootloader_msg"])
        os.system("adb reboot bootloader")
    elif fastboot_out.strip() != "":
        print(Fore.GREEN + L["fastboot_found"])
        # ensure bootloader active
        os.system("fastboot reboot bootloader")
    else:
        print(Fore.RED + L["no_device"])
        input(L["return_menu"])
        return

    time.sleep(2.5)

    # 3. At bootloader, check securestate
    ok = bootloader_check(L)
    if not ok:
        # bootloader locked - stop
        input(L["return_menu"])
        return

    # 5. Reboot to fastbootd
    print(Fore.CYAN + L["fastbootd_enter"])
    os.system("fastboot reboot fastboot")
    # ask user to confirm
    ans = input(Fore.YELLOW + L["ask_fastbootd"] + " > ").strip().lower()
    if ans not in ("s", "y"):
        print(Fore.RED + "Operação cancelada pelo usuário.")
        input(L["return_menu"])
        return

    # 6-8: choose initial zip (must match ROM variant)
    print(Fore.CYAN + L["select_initial"])
    input(Fore.YELLOW + L["open_selector"])
    initial_zip = select_file_dialog(L["select_initial_file_title"])
    if not initial_zip:
        print(Fore.RED + L["no_file"])
        input(L["return_menu"])
        return

    # 9-11: choose custom rom zip
    print(Fore.CYAN + L["select_rom"])
    input(Fore.YELLOW + L["open_selector"])
    rom_zip = select_file_dialog(L["select_rom_file_title"])
    if not rom_zip:
        print(Fore.RED + L["no_file"])
        input(L["return_menu"])
        return

    # 12: verify device in fastboot
    print(Fore.CYAN + L["check_fastboot"])
    fastboot_out2 = subprocess.getoutput("fastboot devices")
    if fastboot_out2.strip() == "":
        print(Fore.RED + L["no_fastboot"])
        input(L["return_menu"])
        return

    # 13: fastboot --skip-reboot update {initial zip}
    print(Fore.CYAN + L["install_initial"])
    # use os.system to show progress from fastboot in terminal
    cmd_update = f'fastboot --skip-reboot update "{initial_zip}"'
    os.system(cmd_update)

    # 14: reboot recovery
    print(Fore.CYAN + L["reboot_recovery"])
    os.system("fastboot reboot recovery")

    # 15: ask if entered recovery
    if input(Fore.YELLOW + L["ask_recovery"] + " > ").strip().lower() not in ("s", "y"):
        print(Fore.RED + "Operação cancelada. Entre no recovery e repita o processo.")
        input(L["return_menu"])
        return

    # 16-17: instruct user to Wipe data and confirm
    print(Fore.YELLOW + L["wipe_info"])
    while True:
        if input(Fore.YELLOW + L["ask_wipe"] + " > ").strip().lower() in ("s", "y"):
            break
        else:
            print("Aguardando confirmação do wipe...")

    # 18-19: ask user to select Apply update from ADB (ADB Sideload)
    print(Fore.YELLOW + L["apply_update_info"])
    while True:
        if input(Fore.YELLOW + L["ask_apply_update"] + " > ").strip().lower() in ("s", "y"):
            break
        else:
            print("Aguardando seleção de 'Apply update from ADB' no recovery...")

    # 20: verify adb devices shows sideload
    print(Fore.CYAN + L["check_sideload"])
    adb_out2 = subprocess.getoutput("adb devices")
    if "sideload" not in adb_out2.lower():
        print(Fore.RED + L["not_sideload"])
        input(L["return_menu"])
        return

    # 21: warn about time and reboot prompts
    print(Fore.YELLOW + L["time_warning"])
    time.sleep(1.5)

    # 22: adb sideload {rom zip}
    print(Fore.CYAN + L["sideload_start"])
    cmd_sideload = f'adb sideload "{rom_zip}"'
    os.system(cmd_sideload)

    # 23: ask user to reboot system now
    print(Fore.GREEN + L["sideload_done"])
    print(Fore.CYAN + L["device_reboot"])
    input(L["return_menu"])
    return