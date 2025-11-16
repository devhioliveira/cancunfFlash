#!/bin/bash

# --- Verifica se é root ---
if [ "$EUID" -ne 0 ]; then
    echo "Requer privilégios de administrador. Reexecutando com sudo..."
    sudo bash "$0" "$@"
    exit 0
fi

# --- Caminho do script Python ---
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/scripts/setup.py"

# --- Verifica se o python existe ---
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python3 não encontrado. Instale antes de continuar."
    exit 1
fi

# --- Executa o script ---
python3 "$SCRIPT_PATH"
