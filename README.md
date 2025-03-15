# Web Scraper en Python

Este es un **web scraper** en Python que extrae información de una página web y la guarda en una carpeta con el nombre del dominio. Extrae:

✅ **Títulos**
✅ **Párrafos**
✅ **Enlaces**
✅ **Imágenes** (las guarda en una subcarpeta)

## 🚀 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install requests beautifulsoup4
   ```

## 🛠 Uso

Ejecuta el script y proporciona la URL de la página que deseas scrapear:

```bash
python scraper.py
```

El script creará una carpeta con el nombre del dominio de la web ingresada y guardará los datos en `data.txt`. Las imágenes se almacenarán en una subcarpeta `Images`.

## 📂 Estructura de archivos

```
📁 tu_repositorio/
│── scraper.py  # Código del scraper
│── README.md   # Este archivo
│── 📁 dominio.com/  # Carpeta con los datos extraídos
│   ├── data.txt  # Archivo con los títulos, párrafos y enlaces
│   ├── 📁 Images/  # Carpeta con las imágenes descargadas
```

## ⚠️ Notas
- Asegúrate de que la web que vas a scrapear permite la extracción de datos revisando su `robots.txt`.
- Algunas webs pueden bloquear solicitudes automáticas; en ese caso, puedes probar usando `headers` en la petición.

