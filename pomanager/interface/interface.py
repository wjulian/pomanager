from pyfiglet import Figlet
from core.models import Settings, Profile
import click
import pkg_resources

class Interface:

    def print_version(self):
        """Prints header app"""
        
        title = Figlet(font='taxi____')
        click.secho(title.renderText('\t POMANAGER \n'), fg='red')
        version = pkg_resources.require('pomanager')[0].version
        click.echo(f'Gestor de archivos .po, version: {version}.\n')


    def file_exist_prompt(self):
        return click.confirm('El archivo "pomgr.settings.json" ya existe, desea sobreescribirlo?', default=False)


    def file_not_exist_echo(self):
        click.secho('\nel archivo "pomgr.settings.json" no existe, corra el comando "pomgr init" para crearlo\n',
         bg='red', err=True)


    def value_setted_echo(self, data: dict):
        click.echo('Valor asignado exitosamente!')
        click.echo(data)


    def print_langs(self, langs: dict):
        click.secho('\n Idiomas\n')
        for key, value in langs.items():
            click.echo(f'  {key}: {value}\n')


    def creation_success(self, that: str):
        click.secho(f'\nEL {that} se ha creado exitosamente!\n', fg='green')


    def print_current_file(self, settings: dict):
        click.secho('\n\tSettings\t\n', bg='white', fg='black', nl=True)
        for key, value in settings.items():
            if key == 'profiles':
                click.echo(f'  {key}:\n')
                for item in value:
                    for k, v in item.items():
                        click.echo(f'     {k}: {v}')
                print('\n')
            else:
                click.echo(f'  {key}: {value}')
        print('\n')


    def print_profiles(self, profiles: list):
        click.secho('\nPerfiles\n', fg='blue', nl=True)
        for profile in profiles:
            click.echo(profile.serialize())
            

    def profile_dont_exist(self, name: str):
        click.secho(f'El perfil "{name}" no existe', fg='red', nl=True)

    def invalid_profile(self, name):
        click.secho(f'El perfil "{name}" no es valido.')