#!/usr/bin/env python3
import hashlib
import pyfiglet
import os
import sys
from tqdm import tqdm
import argparse

def display_banner():
    """Muestra un banner ASCII decorativo"""
    ascii_banner = pyfiglet.figlet_format("Hash Cracker Pro\nMD5 Edition")
    print(ascii_banner)

def validate_file(file_path):
    """Valida que el archivo exista y sea legible"""
    if not os.path.isfile(file_path):
        print(f"[!] Error: El archivo {file_path} no existe")
        return False
    if not os.access(file_path, os.R_OK):
        print(f"[!] Error: No se puede leer el archivo {file_path}")
        return False
    return True

def validate_hash(md5_hash):
    """Valida que el hash tenga el formato MD5 correcto"""
    if len(md5_hash) != 32:
        print("[!] Error: El hash no tiene la longitud MD5 válida (32 caracteres)")
        return False
    try:
        int(md5_hash, 16)
    except ValueError:
        print("[!] Error: El hash contiene caracteres no hexadecimales")
        return False
    return True

def crack_hash(wordlist_path, target_hash):
    """Intenta crackear el hash MD5 usando la wordlist proporcionada"""
    try:
        # Obtenemos el tamaño del archivo para la barra de progreso
        file_size = os.path.getsize(wordlist_path)
        
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in tqdm(file, total=file_size, unit='B', unit_scale=True, desc="Procesando"):
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                
                # Generamos el hash MD5
                hash_obj = hashlib.md5(cleaned_line.encode('utf-8'))
                hashed_pass = hash_obj.hexdigest()
                
                if hashed_pass == target_hash.lower():
                    return cleaned_line
                    
    except KeyboardInterrupt:
        print("\n[!] Proceso interrumpido por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error inesperado: {str(e)}")
        sys.exit(1)
    
    return None

def main():
    # Configuración de argumentos
    parser = argparse.ArgumentParser(description='Hash Cracker MD5 Avanzado')
    parser.add_argument('-w', '--wordlist', required=True, help='Ruta al archivo wordlist')
    parser.add_argument('-H', '--hash', required=True, help='Hash MD5 a crackear')
    parser.add_argument('-q', '--quiet', action='store_true', help='Modo silencioso (sin banner)')
    args = parser.parse_args()

    if not args.quiet:
        display_banner()

    # Validaciones
    if not validate_file(args.wordlist):
        sys.exit(1)
        
    if not validate_hash(args.hash):
        sys.exit(1)

    print(f"\n[+] Iniciando ataque contra el hash: {args.hash}")
    print(f"[+] Usando wordlist: {args.wordlist}\n")

    # Proceso de cracking
    result = crack_hash(args.wordlist, args.hash)

    # Mostrar resultados
    if result:
        print(f"\n[+] ¡Contraseña encontrada!: {result}")
    else:
        print("\n[-] La contraseña no se encontró en la wordlist")

if __name__ == "__main__":
    main()
