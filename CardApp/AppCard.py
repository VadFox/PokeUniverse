from pokemontcgsdk import Card
from pokemontcgsdk import RestClient
import environ
import random
import json

# import requests

env = environ.Env()
environ.Env.read_env()


api_key = env('API_KEY')
archivo_cartas = env('ARCHIVO_CARTAS')


# url_api = "https://api.pokemontcg.io/v2/cards/"

# def obtener_cartas_desde_api():
#     response = requests.get(url_api)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error al obtener datos de la API: {response.status_code}")
#         return []

    
# def guardar_en_json(datos, file_path):
#       with open(file_path, "w") as file:
#         json.dump(datos, file, indent=4)


RestClient.configure(api_key)


class manageCard:
     
    def __init__(self, file_path):
        self.file_path = file_path
        self.cards = self.cargar_cartas()
        self.list_ids = self.extraer_ids(self.cards)
        self.selection_card = []

    def cargar_cartas(self):
        """Carga las cartas desde el archivo JSON."""
        with open(self.file_path, "r") as file:
            datos = json.load(file)
        return datos[0]["data"]

    def extraer_ids(self, cartas):
        """Extrae los IDs de las cartas."""
        return [carta["id"] for carta in cartas]

    def seleccionar_id_aleatorio(self):
        """Selecciona un ID aleatorio de la lista de IDs."""
        number = random.randint(0, len(self.list_ids) - 1)  # Usar self.list_ids
        random_id = self.list_ids[number]
        return random_id

    def register_card(self, card):
        """Registra una carta seleccionada en la colección."""
        self.selection_card.append(card)
        print(f'Carta {card} agregada a su colección')
        
    def show_cards_add(self):
        """Muestra todas las cartas agregadas en la colección."""
        if self.selection_card:
            print("\nCartas en la colección:\n")
            for card in self.selection_card:
               data = Card.find(card)
               print(f"Nombre: {data.name} ID: {card} IMG: {data.images.small}" )
        else:
            print("No hay cartas en la colección.")

manager = manageCard(archivo_cartas)

while True:
     
     print("_______________________________")
     print("\n1. Obtener una carta")
     print("2. Ver lista de cartas")
     print("3. Salir")
     option = input("Seleccione una opción:")
     
     if option == "1":
     
          for _ in range(1):
               random_id = manager.seleccionar_id_aleatorio()
               manager.register_card(random_id)


     elif option == "2":
         manager.show_cards_add()

     
     elif option == "3":
          print("Cerrando App lesgoo")
          break
     
     else:
          print("Opción inválida. Por favor, seleccione una opción")
          