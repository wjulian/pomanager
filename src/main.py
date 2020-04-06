from pomanager.models import Settings
from pomanager.services import FileGenerator, PoCreator
from pomanager.helpers import SettingsHelper
from pomanager_cli import Interface
from googletrans import LANGUAGES
from glob import glob
from pyfiglet import Figlet
import os, click

_interface = Interface()

@click.group()
def main():
    pass

@main.command('version', help='Muestra la versión instalada de pomanager')
def print_version():
    _interface.print_version()

@main.command('init', help='Crea un archivo de configuración para generar las traducciónes más rápidamente')
def init():
    
    if settings_exist(FILEPATH):
        if not _interface.file_exist_prompt():
            exit()
        else:
            __settings_helper.generate(FILEPATH, Settings().serialize())


@main.command('set', help='Asigna el valor a la propiedad dada, con este comando puedes asignar sólo una propiedad de tu pomgr.seetings.json')
@click.option('--key', prompt='Nombre', help='Nombre de la propiedad que deseas asignar')
@click.option('--value', prompt='Valor', help='Valor que deseas asignar')
def setValue(key: str, value):
    """Set the value to the given property name if exist and print the file data, if not then raise an error

    Arguments:
        key {str} -- the name of the property to change
        value {[type]} -- the value to set 
    """    
    if not __settings_helper.settings_exist():
        _interface.file_not_exist_echo()
        exit()
    else:
        __settings_helper.set_value(key, value, FILEPATH)
        _interface.value_setted_echo(__settings_helper.read())



# def load_profile(profile_name: str) -> Config:
#     return __settings_helper.get_profile(profile_name)


# def input_settings_values() -> dict:
#     settings = dict()
#     settings['name'] = click.prompt('inserta el nombre del perfil')
#     settings['path_to_extract'] = click.prompt('inserta la ruta para extraer los archivos')
#     settings['path_to_save'] = click.prompt('inserta la ruta donde se guardaran los archivos')
#     settings['lang'] = choice_language()
#     return settings


# def choice_language():
#     print_available_langs()
#     lang_selected = click.prompt('Elige el idioma de destino')
#     if lang_selected in LANGUAGES:
#         return lang_selected
#     else:
#         print('El lenguaje seleccionado no se encuentra en la lista displonible')
#         print('1. Elegir de nuevo\n2. Volver al menú')
#         lang_selected = click.prompt()
#         if lang_selected == '2':
#             print_choices()
#         else:
#             choice_language()


def print_available_langs():
    for key, value in LANGUAGES:
        print(f'{key}: {value}')


def settings_exist(filepath: str):
    current_dir = filepath
    if os.path.exists(current_dir):
        return True
    else:
        return False

    

if __name__ == "__main__":
    FILEPATH = f'{os.getcwd()}/pomgr.settings.json'
    __settings_helper = SettingsHelper()
    main()
