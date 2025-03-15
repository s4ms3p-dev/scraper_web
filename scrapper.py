# Script para sacar los datos de un sitio web
# Author = secnov :)

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Pedir URL al usuario
url = input("Ingrese la URL a scrapear: ")
parsed_url = urlparse(url)
domain_name = parsed_url.netloc  # Extraer el dominio para el nombre de la carpeta

# Crear carpeta con el nombre del dominio si no existe
folder_name = domain_name
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
if not os.path.exists(f"{folder_name}/Images"):
    os.makedirs(f"{folder_name}/Images")

# Hacer la solicitud HTTP
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraer títulos, enlaces y párrafos
    titles = soup.find_all("a", class_="storylink")
    paragraphs = soup.find_all("p")  # Algunos sitios pueden no tener <p>
    links = soup.find_all("a", href=True)
    images = soup.find_all("img")
    
    # Guardar datos en un archivo
    with open(f"{folder_name}/data.txt", "w", encoding="utf-8") as f:
        f.write("--- TITULOS ---\n")
        for title in titles:
            f.write(title.text + "\n")
        
        f.write("\n--- PÁRRAFOS ---\n")
        for paragraph in paragraphs:
            f.write(paragraph.text + "\n")
        
        f.write("\n--- ENLACES ---\n")
        for link in links:
            f.write(f"{link.text}: {link['href']}\n")
    
    # Descargar imágenes
    for img in images:
        img_url = urljoin(url, img.get("src", ""))
        img_name = os.path.basename(img_url).split("?")[0]
        img_path = os.path.join(f"{folder_name}/Images", img_name)
        try:
            img_data = requests.get(img_url).content
            with open(img_path, "wb") as f:
                f.write(img_data)
            print(f"Imagen guardada: {img_name}")
        except:
            print(f"No se pudo descargar: {img_url}")
    
    print(f"Scraping completado. Datos guardados en la carpeta '{folder_name}'.")
else:
    print("Error al acceder a la página.")
