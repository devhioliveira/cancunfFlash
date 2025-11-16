# lang.py
LANG = {
    "pt": {
        "title": "Cancunf Flash",
        "warn": "[AVISO] > NÃO nos responsabilizamos por danos ao dispositivo.",
        "menu_main": "=== MENU PRINCIPAL ===",
        "menu1": "1. Flash Custom ROM",
        "menu2": "2. Documentários (Docs)",
        "menu3": "3. Instalar KSU (KernelSU)",
        "menu4": "4. Instalar KSU Next",
        "menu0": "0. Sair",

        # docs
        "docs_title": "\n=== DOCUMENTÁRIOS ===\n",
        "docs_body": (
            "Melhor custom ROM:\n"
            "- Para o modelo com 4GB de RAM: infelizmente você ficará preso na YAAP. "
            "O desempenho é limitado e personalizar demais o sistema é sofrimento. Eu (dev.hioliveira) tenho um, e é horrível.\n"
            "- Para o modelo com 8GB de RAM: você tem várias opções — Infinity X, Clover, DerpFest, Axion e muitas outras.\n\n"

            "Onde baixar CUSTOM ROMs:\n"
            "- Canal oficial do G54 Updates: https://t.me/motorolag54updates\n\n"

            "GAPPS vs VANILLA:\n"
            "- GAPPS → vem com apps da Google (Play Store, Contatos, etc).\n"
            "- VANILLA → totalmente limpo, sem apps da Google.\n\n"

            "IMPORTANTE:\n"
            "- Se você baixou a versão GAPPS, deve baixar também a versão GAPPS no Initial ZIP.\n"
            "- O Initial ZIP contém tudo que a ROM precisa para ser instalada, é o pacote fundamental.\n\n"

            "Se a ROM não mostrar GAPPS / VANILLA:\n"
            "- Procure por algo como \"Build Variant\".\n"
            "- Caso não encontre, peça suporte no canal oficial:\n"
            "  Suporte do DevHiOliveira: https://t.me/devhioliveirasupport\n"
            "  Grupo Global G54: https://t.me/motorolag54official\n"
            "  Grupo Brasil G54: https://t.me/MotoG54BR\n\n"

            "=====================\n"
            "   COMO FAZER ROOT\n"
            "=====================\n\n"

            "Você tem duas opções para obter root: **Magisk** ou **KSU (KernelSU)**.\n"
            "Ambas podem quebrar aplicativos sensíveis (banco, WhatsApp, apps corporativos). Use por sua conta e risco.\n\n"

            "🔥 Método 1 — Magisk:\n"
            "1. Extraia o boot.img da sua custom ROM.\n"
            "2. Abra o Magisk e faça o patch no boot.img.\n"
            "3. Reinicie o dispositivo em fastbootd.\n"
            "4. Execute no PC:\n"
            "   fastboot flash boot <seu-magisk-boot.img>\n"
            "5. Reinicie.\n\n"

            "🔥 Método 2 — KSU (KernelSU):\n"
            "Se quiser usar KSU, basta selecionar a opção 'Instalar KSU' no menu principal.\n"
            "O script cuida do processo automaticamente.\n"
        ),
        "docs_back": "\nPressione ENTER para voltar ao menu...",

        # flash step messages
        "install_rom": "=== INSTALAÇÃO DE CUSTOM ROM ===",
        "detect_dev": "[INFO] > Detectando dispositivo...",
        "adb_found": "[INFO] > Dispositivo detectado via ADB",
        "fastboot_found": "[INFO] > Dispositivo já está no FASTBOOT",
        "no_device": "[ERRO] > Nenhum dispositivo ADB/FASTBOOT detectado.",
        "reboot_bootloader_msg": "[INFO] > Reiniciando para bootloader...",
        "boot_check": "[INFO] > Verificando estado do bootloader...",
        "boot_unlocked": "[INFO] > dispositivo está com bootloader desbloqueado",
        "boot_locked": "[ERRO] > Bootloader BLOQUEADO. Pesquise como desbloquear o bootloader",
        "fastbootd_enter": "[INFO] > Reiniciando para fastbootd...",
        "ask_fastbootd": "O dispositivo reiniciou no fastbootd? (s/n)",
        "select_initial": "\nAgora selecione o INITIAL ZIP correspondente à ROM (GAPPS/Vanilla).",
        "open_selector": "Pressione ENTER para abrir o seletor...",
        "select_initial_file_title": "Selecione o INITIAL ZIP",
        "select_rom": "\nAgora selecione o ZIP da Custom ROM.",
        "select_rom_file_title": "Selecione o ZIP da Custom ROM",
        "check_fastboot": "[INFO] > Verificando conexão com fastboot...",
        "no_fastboot": "[ERRO] > Dispositivo não detectado no fastboot.",
        "install_initial": "[INFO] > Aplicando INITIAL ZIP (fastboot --skip-reboot update)...",
        "reboot_recovery": "[INFO] > Reiniciando para o recovery...",
        "ask_recovery": "O dispositivo iniciou no recovery? (s/n)",
        "wipe_info": "No aparelho, selecione: Wipe data / Factory reset",
        "ask_wipe": "Você realizou o Wipe Data? (s/n)",
        "apply_update_info": "No aparelho, selecione: Apply update from ADB / ADB sideload (ou Install update -> ADB Sideload)",
        "ask_apply_update": "Você selecionou Apply update from ADB / ADB sideload? (s/n)",
        "check_sideload": "[INFO] > Verificando modo sideload (adb devices)...",
        "not_sideload": "[ERRO] > Dispositivo NÃO está em sideload.",
        "time_warning": "\nEsse processo pode levar vários minutos. Se aparecer prompt contendo 'reboot' no recovery, selecione 'No'.",
        "sideload_start": "[INFO] > Iniciando ADB sideload...",
        "sideload_done": "[SUCESSO] > Sideload finalizado. Selecione Reboot System no aparelho.",
        "return_menu": "\nPressione ENTER para voltar ao menu...",
        "no_file": "[ERRO] > Nenhum arquivo selecionado.",
        "ksu_dev": "[INFO] > A opção Instalar KSU está em desenvolvimento.",
        "ksu_next_dev": "[INFO] > A opção Instalar KSU Next está em desenvolvimento."
    },

    "en": {
        "title": "Cancunf Flash",
        "warn": "[WARNING] > We are NOT responsible for any damage to your device.",
        "menu_main": "=== MAIN MENU ===",
        "menu1": "1. Flash Custom ROM",
        "menu2": "2. Documentaries (Docs)",
        "menu3": "3. Install KSU (KernelSU)",
        "menu4": "4. Install KSU Next",
        "menu0": "0. Exit",

        # docs EN
        "docs_title": "\n=== DOCUMENTATION ===\n",
        "docs_body": (
            "Best custom ROM:\n"
            "- For the 4GB RAM model: you are basically stuck with YAAP. Performance is limited and heavy customization is painful.\n"
            "- For the 8GB RAM model: many options — Infinity X, Clover, DerpFest, Axion, among others.\n\n"

            "Where to download CUSTOM ROMs:\n"
            "- Official G54 Updates channel: https://t.me/motorolag54updates\n\n"

            "GAPPS vs VANILLA:\n"
            "- GAPPS → includes Google apps (Play Store, Contacts etc.).\n"
            "- VANILLA → clean, without Google apps.\n\n"

            "IMPORTANT:\n"
            "- If you downloaded the GAPPS version, you must also download the GAPPS version in the Initial ZIP.\n"
            "- The Initial ZIP contains the essential files for installation.\n\n"

            "If the ROM doesn't show GAPPS / VANILLA:\n"
            "- Look for 'Build Variant'.\n"
            "- If you can't find it, ask for support:\n"
            "  DevHiOliveira Support: https://t.me/devhioliveirasupport\n"
            "  G54 Global: https://t.me/motorolag54official\n"
            "  G54 Brazil: https://t.me/MotoG54BR\n\n"

            "=====================\n"
            "   HOW TO GET ROOT\n"
            "=====================\n\n"

            "You have two main options: Magisk or KSU (KernelSU).\n"
            "Both may break sensitive apps (banking, WhatsApp, corporate apps). Use at your own risk.\n\n"

            "🔥 Method 1 — Magisk:\n"
            "1. Extract boot.img from the ROM.\n"
            "2. Patch it via Magisk.\n"
            "3. Boot to fastbootd.\n"
            "4. Run:\n"
            "   fastboot flash boot <your-magisk-boot.img>\n"
            "5. Reboot.\n\n"

            "🔥 Method 2 — KSU:\n"
            "Use the 'Install KSU' option in the main menu (when implemented).\n"
        ),
        "docs_back": "\nPress ENTER to return to the menu...",

        # flash step strings EN
        "install_rom": "=== CUSTOM ROM INSTALLATION ===",
        "detect_dev": "[INFO] > Detecting device...",
        "adb_found": "[INFO] > Device detected via ADB",
        "fastboot_found": "[INFO] > Device already in FASTBOOT",
        "no_device": "[ERROR] > No ADB/FASTBOOT device detected.",
        "reboot_bootloader_msg": "[INFO] > Rebooting to bootloader...",
        "boot_check": "[INFO] > Checking bootloader state...",
        "boot_unlocked": "[INFO] > Device bootloader is unlocked",
        "boot_locked": "[ERROR] > Bootloader LOCKED. Search how to unlock it.",
        "fastbootd_enter": "[INFO] > Rebooting to fastbootd...",
        "ask_fastbootd": "Did the device enter fastbootd? (y/n)",
        "select_initial": "\nNow select the INITIAL ZIP matching the ROM (GAPPS/Vanilla).",
        "open_selector": "Press ENTER to open file selector...",
        "select_initial_file_title": "Select the INITIAL ZIP",
        "select_rom": "\nNow select the Custom ROM ZIP.",
        "select_rom_file_title": "Select the Custom ROM ZIP",
        "check_fastboot": "[INFO] > Checking fastboot connection...",
        "no_fastboot": "[ERROR] > Device not detected in fastboot.",
        "install_initial": "[INFO] > Applying INITIAL ZIP (fastboot --skip-reboot update)...",
        "reboot_recovery": "[INFO] > Rebooting to recovery...",
        "ask_recovery": "Did the device enter recovery? (y/n)",
        "wipe_info": "On the device, select: Wipe data / Factory reset",
        "ask_wipe": "Did you perform the Wipe Data? (y/n)",
        "apply_update_info": "On the device, select: Apply update from ADB / ADB sideload (or Install update -> ADB Sideload)",
        "ask_apply_update": "Did you select Apply update from ADB / ADB sideload? (y/n)",
        "check_sideload": "[INFO] > Checking sideload mode (adb devices)...",
        "not_sideload": "[ERROR] > Device NOT in sideload mode.",
        "time_warning": "\nThis process can take several minutes. If a prompt contains 'reboot', choose 'No'.",
        "sideload_start": "[INFO] > Starting ADB sideload...",
        "sideload_done": "[SUCCESS] > Sideload finished. Select Reboot System on device.",
        "return_menu": "\nPress ENTER to return to the menu...",
        "no_file": "[ERROR] > No file selected.",
        "ksu_dev": "[INFO] > Install KSU option is in development.",
        "ksu_next_dev": "[INFO] > KSU Next option is in development."
    }
}
