from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from src.web_scrap import scrap
from src.make_presentation import make_presentation
import os
from threading import Thread
import json


# Defaine``
class FirstWindow(Screen):
    
    def start_scrap(self):
        os.chdir('./Prezentacje')
        os.makedirs(self.ids.file_name.text.strip(), exist_ok=True)
        os.chdir(self.ids.file_name.text.strip())
        self.make_data_json()
        thread = Thread(target=scrap, kwargs={
                        'path': self.ids.path.text.strip()})
        thread.start()

    def make_data_json(self):
        data = {}
        data['level'] = None
        data['name_of_route'] = None
        data['leader'] = None
        data['distance'] = None
        data['heightest_point'] = None
        data['elevation'] = None
        data['up'] = None
        data['down'] = None
        data['time'] = None
        data['coutions'] = None
        data['backgrounds_images'] = None
        data['file_name'] = self.ids.file_name.text
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


class SecondWindow(Screen):

    def load_backgrounds(self):
        self.names_of_backgrounds = list(map(
            lambda x: x[:-4], [name for name in os.listdir(os.path.join("../../", "templates")) if ".png" in name]))
        self.background = self.names_of_backgrounds[0]
        self.background_image = f'{os.path.join("templates", self.background)}.png'
        self.ids.background_spinner.text = self.background
        self.ids.background_spinner.values = self.names_of_backgrounds
        self.ids.image.source = f'../../templates/{self.background}.png'

    def change_background(self, value):
        self.background = value
        self.ids.image.reload()
        self.ids.image.source = f'../../templates/{value}.png'
        # self.ids.image.reload()3

    def add_background(self):
        with open('data.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        data['background'] = self.background
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


class ThirdWindow(Screen):
    def add_data(self):
        with open('data.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        data['level'] = self.ids.level.text
        data['leader'] = self.ids.leader.text
        data['name_of_route'] = self.ids.name_of_route.text
        data['coutions'] = list(
            map(str.strip, self.ids.coutions.text.split(',')))
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


class FourthWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        print(os.getcwd())
        with open('settings.json', encoding='utf-8') as f:
            self.settings = json.load(f)

    def edit_labels(self):
        self.ids.path_image.text = f'Krok 9 : Do folderu {os.getcwd()} wrzuć zdjęcie trasy i nazwij go {self.settings["path_route"]}'
        self.ids.first_view.text = f'Krok 10 : Do folderu {os.getcwd()} wrzuć pierwszy widok i nazwij go {self.settings["first_view"]}'
        self.ids.second_view.text = f'Krok 11 : Do folderu {os.getcwd()} wrzuć drugi widok i nazwij go {self.settings["second_view"]}'
        self.ids.third_view.text = f'Krok 12 : Do folderu {os.getcwd()} wrzuć trzeci widok i nazwij go {self.settings["third_view"]}'

    def make_presentation(self):
        make_presentation()


class WindowMenager(ScreenManager):
    pass





class PresentationApp(App):
    def build(self):
        return Builder.load_file('src/program.kv')


# if __name__ == '__main__':
def run_app():
    # os.chdir(os.path.dirname(__file__))
    print(os.getcwd(), '----------------------------------')
    kv = Builder.load_file('src/program.kv')
    Window.size = (1000, 800)
    
    # print( [ name for name in os.listdir('templates') if 'Orla'  in name and 'pptx' in name] )
    # with open('settings.json') as f:
    #     settings = json.load(f)
    print(os.getcwd())
    PresentationApp().run()
    return
    
