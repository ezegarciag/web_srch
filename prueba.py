
import requests
from bs4 import BeautifulSoup

# URL de la que quieres extraer el texto
url = "https://tn.com.ar/economia/2025/03/18/dolar-hoy-a-cuanto-cotizan-el-oficial-y-las-otras-opciones-cambiarias-este-martes-18-de-marzo/"


# only testing

# Realizamos la solicitud HTTP
response = requests.get(url)

# Comprobamos que la solicitud fue exitosa
if response.status_code == 200:
    # Parseamos el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraemos todo el texto visible de la página
    text = soup.get_text(separator=" ", strip=True)
    
    # Imprimimos el texto extraído
    print(text)
else:
    print(f"Error al obtener la página: {response.status_code}")
