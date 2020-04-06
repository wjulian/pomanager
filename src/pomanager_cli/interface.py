from pyfiglet import Figlet
from pomanager.models import Settings 
import click
from tabulate import tabulate
import pkg_resources

class Interface:

    def print_version(self):
        """Prints header app"""
        
        title = Figlet(font='taxi____')
        click.echo(title.renderText('\t POMANAGER \n'))
        version = pkg_resources.require('pomanager')[0].version
        click.echo(f'Gestor de archivos .po, version: {version}')


    def file_exist_prompt(self):
        return click.confirm('El archivo "pomgr.settings.json" ya existe, desea sobreescribirlo?', default=False)
    
    def file_not_exist_echo(self):
        click.echo('el archivo "pomgr.settings.json" no existe, corra el comando "pomgr init" para crearlo')

    def value_setted_echo(self, data: dict):
        click.echo('Valor asignado exitosamente!')
        click.echo(data)

    # def print_profiles(self, profiles: dict):
    #     for item in profiles:
    #         profile = Settings(item)
    #         data = [[profile.name,profile.path_to_extract,
    #                  profile.path_to_save,profile.lang]]
    #         headers = ['Nombre', 'Ruta de entrada', 'Ruta de salida', 'Idioma de destino']
    #         click.echo(tabulate(data, headers=headers))
