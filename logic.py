from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.temp_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}')
        self.img = self.get_img()
        self.name = self.get_name()
        self.is_hungry = True

        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self) -> tuple:
        if self.temp_response.status_code == 200:
            data = self.temp_response.json()
            return (data['sprites']['front_default']), (data['sprites']['back_default'])
        return (None, None)

    def feed(self) -> str:
        if not self.is_hungry:
            return "Он уже сыт"
        self.is_hungry = False
        return "Он поел"

    def get_name(self) -> str:
        if self.temp_response.status_code == 200:
            data = self.temp_response.json()
            return data['forms'][0]['name']
        else:
            return "Pikachu"

    def info(self) -> str:
        return f"Имя твоего покемона: {self.name}"

    def show_img(self) -> tuple:
        return self.img