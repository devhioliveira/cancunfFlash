# Cancunf Flash Installer 🚀  

> ⚠️ **AVISO IMPORTANTE** ⚠️  
> Este script foi desenvolvido **exclusivamente para o Moto G54 5G (codinome Cancunf)**.  
> Ele realiza o **flash de Custom ROMs baseadas no Android 16**.  
> **Não me responsabilizo por qualquer dano ao dispositivo. Use por sua conta e risco.**  

---

## 📖 Sobre o projeto  

**Cancunf Flash Installer** é um script em Python que **automatiza o processo de instalação de Custom ROMs** no Moto G54 (Cancunf).  

Ele simplifica tarefas que, normalmente, seriam manuais:  
- Detecção do dispositivo via **ADB / Fastboot**  
- Flash do **initial zip**  
- Flash do **zip da ROM customizada**  
- Flash opcional de um **boot.img personalizado**  
- Reinicialização automática entre **ADB, Fastboot e Recovery**  

O objetivo é deixar o processo mais rápido e menos propenso a erros manuais.  

---

## 🛠️ Requisitos  

- Python 3.x  
- Módulos Python: `tkinter`, `colorama`  
- Ferramentas `adb` e `fastboot` configuradas no **PATH**  
- Cabo USB de boa qualidade  
- **Backup completo dos dados** (o processo apaga tudo)  
- Compatível com **Windows** e **Linux**  
- **Termux:** não oficialmente suportado (pode exigir adaptação manual)  

---

## ⚡ Como usar  

1. **Conecte** o dispositivo via USB.  
   - Modo inicial: **ADB**  
   - O script cuidará da transição para **Fastboot** ou **Recovery** quando necessário.  

2. Execute o script no terminal:  

   ```bash
   python cancunfFlash.py
   ```