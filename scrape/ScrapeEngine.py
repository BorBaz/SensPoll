class ScrapeEngine:
    def __init__(self,url):
        self.url = url




# from bs4 import BeautifulSoup
#
# # Realizar la solicitud GET a la página web
# url = "https://www.example.com"
# response = requests.get(url)
#
# # Verificar si la solicitud fue exitosa (código de estado 200)
# if response.status_code == 200:
#     # Parsear el contenido HTML de la respuesta
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     # Ejemplo de extracción de información
#     # Supongamos que queremos obtener los títulos de los enlaces en la página
#     link_titles = soup.find_all("a")
#     for link in link_titles:
#         print(link.get("title"))
#
# else:
#     print("Error al realizar la solicitud:", response.status_code)