from pomanager.models import Settings, Profile
from pomanager.services import Generator
from pomanager.helpers import SettingsHelper, ProfileHelper
from pomanager_cli import Interface
from googletrans import LANGUAGES
from glob import glob
from pyfiglet import Figlet
import os, click, json

__interface = Interface()
__FILEPATH = os.path.join(os.getcwd(), 'pomgr.settings.json')
__settings_helper = SettingsHelper()
__profile_helper = ProfileHelper()
__generator = Generator(__FILEPATH)

@click.group()
def main():
    pass

@main.command('version', help='Muestra la versión instalada de pomanager')
def print_version():
    __interface.print_version()


@main.command('init', help='Crea un archivo de configuración para generar las traducciónes más rápidamente')
def init():
    """ If settings doesn't exist create the pomgr.settings.json file with default values
    else  ask if want rewrite the file, if yes then create the file else exit"""
    if settings_exist():
        if not __interface.file_exist_prompt():
            exit()
        else:
            generate_settings()
    else:
        generate_settings()
        

@main.command('set', help='Asigna el valor a la propiedad dada, con este comando puedes asignar sólo una propiedad de tu pomgr.seetings.json')
@click.option('--profile', '--p', help='Nombre del perfil (opcional)', default=False, required=False)
@click.option('--key', '--k', prompt='Nombre', help='Nombre de la propiedad que deseas asignar')
@click.option('--value', '--v', prompt='Valor', help='Valor que deseas asignar')
def set_value(profile: str, key: str, value):
    """Sets the value to the given property name if exist and print the file
    data, if not then raise an error.

    Arguments:
        key {str} -- the name of the property to change
        value {[type]} -- the value to set
    """    
    if settings_exist():
        if not profile:
            __settings_helper.set_value(key, value, __FILEPATH)
            __interface.value_setted_echo(__settings_helper.read(__FILEPATH))



@main.command('settings', help='Imprime el contenido del archivo pomgr.settings.json')
def print_settings():
    if settings_exist():
        settings = __settings_helper.read(__FILEPATH)
        if settings:
            __interface.print_current_file(settings)
        else:
            click.echo('El archivo no tiene valores', err=True)



@main.command('cp', help='Crea un perfil dentro del archivo pomgr.settings.json')
@click.option('--name', '-n', help='El nombre del perfil a crear', required='')
def create_profile(name: str):
    """If the file pomgr.settings.json exist create a new profile with optional
    name and prints the profile at the end.

    Arguments:
        name {str} -- The name of profile (optional)
    """ 
    if settings_exist():
        profile = Profile({'entries': '', 'lang': '', 'output':'', 'name': name})
        __profile_helper.create_profile(profile, __FILEPATH)
        __interface.creation_success(f'perfil {name}')
        click.echo(profile.serialize())

        

@main.command('translate', help='Genera las traducciones')
@click.option('--profile-name', '--p', required=True, help='perfil para generar las traducciones')
def translate(profile_name: str):
    """if settings exist gets the profile (--p) search for the coincidences in files and generate the translations for those
    
    Arguments:
        profile_name {str} -- the name of the profile with the properties to generate translations
    """    
    if settings_exist():
        profile_dict = __profile_helper.get_profile(profile_name, __FILEPATH)
        if not profile_dict:
            __interface.profile_dont_exist(profile_name)
        else:
            profile = Profile(profile_dict)
            if is_valid_profile(profile):
                files = []
                for entry in profile.entries:
                    for ext in profile.file_exts:
                        files.extend(glob(f'{entry}/**/*.{ext}'))
                if len(files) > 1:
                    __generator.generate(files, profile)
            else:
                __interface.invalid_profile(profile.name)
    else:
        __interface.file_not_exist_echo()

        
def generate_settings():
    """ Calls settings helper to generate the file with default values """    
    default_profile = Profile({})
    settings = Settings({'profiles': [default_profile.serialize()]}).serialize()
    __settings_helper.generate(__FILEPATH, settings)
    __interface.creation_success('archivo pomgr.settings.json')
    

def is_valid_profile(profile: Profile) -> bool:
    """Check if the profile has the correct properties to generate translations
    
    Arguments:
        profile {Profile} -- the profile to evaluate
    
    Returns:
        bool -- True if it's properties are not empty
    """    
    return profile.entries != [] and profile.file_exts != []

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

@main.command('langs', help='Imprime todos los lenguajes disponibles para la traducción')
def print_available_langs():
    __interface.print_langs(LANGUAGES)


def settings_exist():
    """Check if the file pomgr.settings.json exist.      
    Returns:
        [boolean] -- True if settings file exist
    """    
    return os.path.exists(__FILEPATH)
    

if __name__ == "__main__":
    main()
