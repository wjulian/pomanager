from pomanager import FileGenerator, ProfilesManager, Profile
from glob import glob
from pyfiglet import Figlet
import os
import json


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
    profile_manager = ProfilesManager()
    return profile_manager.get_profile(profile_name)


def create_profile():
    profile_manager = ProfilesManager()
    profile = {}
    print('inserta el nombre del perfil: ')
    profile['name'] = input()
    print('inserta la ruta para extraer los archivos: ')
    profile['path_to_extract'] = input()
    print('inserta la ruta donde se guardaran los archivos: ')
    profile['path_to_save'] = input()
    print('inserta el idioma de destino: ')
    profile['lang'] = input()
    profile_manager.create_profile(Profile(profile))
    print("Perfil creado!")
    list_profiles()
    print_choices()


def list_profiles():
    profiles = get_profiles_names()
    if profiles == []:
        print("No se encontraron perfiles, desea crear uno? [s: Sí, cualquier tecla menos \'s': No]")
        choice = input()
        if(choice == 's' or 'S'):
            create_profile()
        else:
            print_choices()
    else:
        print('Perfiles: \n')
        counter = 1
        for profile in profiles:
            print(f'#{counter}. #{profile}')
    return profiles


def print_choices():
    print_options()
    print('\nSelecciona una opción: \n')
    option = int(input())

    if option < 1 or option > 4:
        print('Opción inválida')
        print_choices()
    elif option == 1:
        list_profiles()
    elif option == 2:
        create_profile()
    elif option == 3:
        profiles = list_profiles()
        TODO: 'Implementar el menu de generación de traducciones' 
    elif option == 4:
        print('\nSuerte! \n')
        exit()

def run_menu():
    print_header()
    print_choices()


def print_header():
    title = Figlet(font='taxi____')
    print(title.renderText('POMANAGER \n'))


def print_options():
    print('Bienvenido al manejador de archivos .po')
    print('\nComencemos...')
    print('1. Listar perfiles.')
    print('2. Crear perfil.')
    print('3. Generar traducciones.')
    print('4. Salir.')


def get_profiles_names():
    profiles_names = []
    profiles_manager = ProfilesManager()
    profiles = profiles_manager.get_profiles()
    for profile in profiles:
        profiles_names.append(profile['name'])
    return profiles_names


if __name__ == "__main__":
    main()
