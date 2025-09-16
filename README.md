# Cancunf Flash Installer 🚀

> ⚠️ **AVISO IMPORTANTE** ⚠️
> **ESTE SCRIPT É APENAS PARA FLASH DE CUSTOM ROMS ANTIGAS COM ANDROID 14 OU AS PRIMEIRAS VERSÕES DE CUSTOM ROM A15 PARA O MOTO G54 (CANCUNF).**
> **NÃO ME RESPONSABILIZO POR QUALQUER DANO AO DISPOSITIVO. USE POR SUA CONTA E RISCO.**

**Cancunf Flash Installer** é um script Python que automatiza o processo de instalação de Custom ROMs no Moto G54 (Cancunf). Ele detecta dispositivos em Fastboot, gerencia slots, permite flash opcional da stock ROM A14 e realiza sideload de arquivos `.zip` da custom ROM de forma segura.

---

## 📌 Funcionalidades

* Detecta dispositivo conectado em **Fastboot** automaticamente.
* Flash opcional da **Stock ROM A14**.
* Configura slot ativo (`a` ou `b`) automaticamente.
* Flash do `vendor_boot.img` da custom ROM.
* Suporte para **boot.img personalizado** opcional.
* Sideload do arquivo `.zip` da custom ROM.
* Mensagens detalhadas e pausas para prevenção de erros.
* Suporte inicial para **Android 15 (versões novas)** — em desenvolvimento.
* Em preparação: suporte para **custom ROMs Android 16**.

---

## 🛠️ Requisitos

* Python 3.x
* Módulos Python: `tkinter`, `colorama`
* `fastboot` e `adb` funcionando no PATH
* Cabo USB compatível
* Backup completo dos dados (o flash **apaga tudo!**)

---

## ⚡ Como usar

1. Conecte o dispositivo via USB em modo **Fastboot**.
2. Execute o script:

```bash
python CancunfFlash.py
```

3. Siga as instruções na tela:

   * Escolha se deseja flashar a **Stock A14**.
   * Configure slots e reinicie no bootloader quando solicitado.
   * Selecione os arquivos da **custom ROM** (`vendor_boot.img`, `.zip`, opcional `boot.img`).
   * Realize o sideload e aguarde o reboot final.

4. Ao final, o dispositivo estará com a **Custom ROM instalada**.

---

## ⚠️ Avisos importantes

* Este script **apaga todos os dados do dispositivo**. Faça backup antes de iniciar.
* Uso **por sua conta e risco**. O autor não se responsabiliza por danos ao dispositivo.
* Destinado apenas a **Android 14 e primeiras builds de A15** para Cancunf.
* Futuras versões podem suportar Android 16, mas **use somente builds testadas**.
* Certifique-se de usar a **ROM correta para o modelo Cancunf**.
> ⚠️ **REQUISITO CRÍTICO** ⚠️  
> Para o funcionamento correto do script, **é necessário ter os arquivos da Stock ROM Android 14 U1TD34.94-12-7** na pasta `A14`.  
> Sem esses arquivos, o flash da Custom ROM **não funcionará corretamente**.

## 👨‍💻 Créditos e Testes

* **Desenvolvedor principal:** Lucas
* Inspirado em práticas comuns de flash de ROMs Motorola / Android.
* Ferramentas utilizadas: Python, ADB, Fastboot, Colorama, Tkinter.
* **Testado com sucesso em:** Moto G54 (Cancunf) com Android 14 e primeiras builds de A15.