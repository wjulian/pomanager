from pomanager.services.file_generator import FileGenerator
from glob import glob


def main(): 
    print("Insert the folder to find the files")
    directory_name = input()
    files = glob(f'{directory_name}/**/*.cshtml')
    if(len(files) == 0):
        print('The specified directory doesn\'t have any files')
        return
    file_generator = FileGenerator()
    file_generator.generate(files)

if __name__ == "__main__":
    main()