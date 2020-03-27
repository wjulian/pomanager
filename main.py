from pomanager import FileGenerator, ProfilesManager, Profile
from glob import glob
from pyfiglet import Figlet
import os, json

def main(): 
    run_menu()
    # print("Insert the folder to find the files")
    # directory_name = input()
    # files = glob(f'{directory_name}/**/*.cshtml')
    # if(len(files) == 0):
    #     print('The specified directory doesn\'t have any files')
    #     return
    # file_generator = FileGenerator()
    # file_generator.generate(files)


def loadProfile(profile_name: str):
    pass

def run_menu():
    print_header()
    print_options()
    print('\nSelecciona una opción: ')
    option = int(input())
    
    if option < 1 or option > 3 :
        print('Opción inválida')
    elif option == 1:
        print(get_profiles_names())
        print_options()
    elif option == 2:
        profile_manager = ProfilesManager()
        profile = {}
        print('insert profile name: ')
        profile['name'] = input()
        print('insert path to extract: ')
        profile['path_to_extract'] = input()
        print('insert path to save: ')
        profile['path_to_save'] = input()
        print('insert destination lang: ')
        profile['lang'] = input()
        profile_manager.create_profile(Profile(profile))
    elif option == 3:
        print('Pronto!')

def print_header():
    title = Figlet(font='taxi____')
    print(title.renderText('POMANAGER \n'))

def print_options():
    print('Bienvenido al manejador de archivos .po')
    print('\nComencemos...')
    print('1. Listar perfiles.')
    print('2. Crear perfil.')
    print('3. Generar traducciones')
    
def get_profiles_names():
    profiles_names = []
    profiles_manager = ProfilesManager()
    profiles = profiles_manager.get_profiles()
    for profile in profiles:
        profiles_names.append(profile['name'])
    return profiles_names
    



if __name__ == "__main__":
    main()