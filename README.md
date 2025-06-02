# 🚀 HashMD5Vortex - Modo de Uso

## 📦 Requisitos Previos
```bash
pip install pyfiglet tqdm
```
## 💻 Uso
```bash
python3 HashMD5Vortex.py -w [WORDLIST] -H [HASH_MD5]
```

### Ejemplo:
```bash
python3 HashMD5Vortex -w rockyou.txt -H 5f4dcc3b5aa765d61d8327deb882cf99
```

## 🎛️ Parámetros Disponibles
| Parámetro       | Alias | Descripción                              | Valor por Defecto |
|-----------------|-------|------------------------------------------|-------------------|
| `--wordlist`    | `-w`  | Ruta al archivo wordlist                 | **Obligatorio**   |
| `--hash`        | `-H`  | Hash MD5 a crackear                      | **Obligatorio**   |
| `--quiet`       | `-q`  | Modo silencioso (sin banner)             | `False`           |
| `--threads`     | `-t`  | Número de hilos (próxima versión)        | `1`               |
| `--output`      | `-o`  | Archivo para guardar resultados          | `resultados.txt`  |

## 📌 Ejemplos Avanzados

### 1. Crackeo con salida a archivo
```bash
python3 HashMD5Vortex -w passwords.txt -H e99a18c428cb38d5f260853678922e03 -o cracked.txt
```

### 2. Modo silencioso (para scripts)
```bash
python3 HashMD5Vortex.py -q -w darkweb2017.txt -H d077f244def8a70e5ea758bd8352fcd8
```

### 3. Usar múltiples hilos (CPU)
```bash
python3 HashMD5Vortex.py -w big_list.txt -H 5f4dcc3b5aa765d61d8327deb882cf99 -t 4
```

## 🖥️ Salida Esperada
```plaintext
  ____            __  __       ____              
 |  _ \          |  \/  |     |  _ \             
 | | | |_ __ ___ | \  / | __ _| |_) | __ _ _ __  
 | | | | '_ ` _ \| |\/| |/ _` |  _ < / _` | '_ \ 
 | |_| | | | | | | |  | | (_| | |_) | (_| | | | |
 |____/|_| |_| |_|_|  |_|\__,_|____/ \__,_|_| |_|

[+] Target Hash: 5f4dcc3b5aa765d61d8327deb882cf99
[+] Wordlist: rockyou.txt (14,344,391 entries)

Procesando: 100%|█████████| 143M/143M [05:21<00:00, 445k claves/s]

[+] ¡Contraseña encontrada!: password
[+] Tiempo de ejecución: 5 minutos 21 segundos
[+] Velocidad: 445,000 hashes/segundo
```

## 🚨 Troubleshooting
| Error                          | Solución                              |
|--------------------------------|---------------------------------------|
| `Wordlist not found`           | Verifica la ruta del archivo          |
| `Invalid MD5 hash format`      | Asegúrate que el hash tenga 32 chars  |
| `Permission denied`            | Ejecuta con `sudo` o corrige permisos|
| `UnicodeDecodeError`           | Usa wordlists con encoding UTF-8      |

## 📊 Rendimiento
| Wordlist Size | Hilos | Tiempo Estimado |
|---------------|-------|-----------------|
| 1M claves     | 1     | ~15 segundos    |
| 10M claves    | 4     | ~2 minutos      |
| 100M claves   | 8     | ~25 minutos     |

> 💡 **Tip**: Para wordlists >1GB usa el parámetro `-t` para multi-hilo

## 📜 Licencia
`MIT License` - Uso ético únicamente. El desarrollo de esta herramienta es para el uso en un entorno controlado el desarrollador no se responsabiliza como lo utilice.
