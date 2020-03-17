from pomanager.services.file_generator import FileGenerator
from glob import glob
from profiles.profiles import Profile
from pyfiglet import Figlet
import os, json

PROFILES_PATH = 'profiles\profiles.json'

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
    with open(os.path.join(os.getcwd(), 'profiles\profiles.json'), 'r') as profile_file:
        result = dict(json.loads(profile_file.read()))
        profile = result['profiles'].get(profile_name)
        return Profile(profile["settings"])

def run_menu():
    profiles_names = get_profiles_names()
    print_header()
    print_options()
 
    # count = 1
    # for profile_name in profiles_names:
    #     print(f'{count}. {profile_name}')

def print_header():
    title = Figlet(font='taxi____')
    print(title.renderText('POMANAGER \n'))

def print_options():
    print('Bienvenido al manejador de archivos .po')
    print('\nComencemos...')
    print('1. ')
def get_profiles_names():
    with open(os.path.join(os.getcwd(), PROFILES_PATH), 'r') as profiles_file:
        result = dict(json.loads(profiles_file.read()))
        profiles_names = result['profiles'].keys()
        return profiles_names


if __name__ == "__main__":
    main()