import PySimpleGUI as sg
import os, shutil
import ctypes
import platform
import sys


def make_dpi_aware():
    """Fix blurred fonts in windows 10"""    
    if int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if True:
    sg.theme('DarkBlue2')
    prgm_path = os.environ.get('PROGRAMFILES(X86)') if not os.environ.get('PROGRAMFILES(X86)') else os.environ.get("PROGRAMFILES")
    prgm_path = os.path.join(prgm_path, 'pomanager')
    layout = [  
        [sg.Text(key='-LBL1-', text='Instala pomanager!')],
        [sg.Text(key='-LBL_LOCATE-', text='Donde deseas instalarlo?')],
        [sg.In(prgm_path), sg.FolderBrowse('buscar')],
        [sg.Checkbox(key='-ADD_ENV_VAR_CHECK-', text='Agregar variable de entorno (pomgr)')],
        [sg.Button(key='install_btn', button_text='Instalar'), sg.Button(key='cancel', button_text='Cancel')] 
    ]

    make_dpi_aware()

    window1 = sg.Window('Instalación pomanager', layout)
    window2_active = False

    while is_admin():
        event1, values = window1.read()

        if event1 in (None, 'cancel'):
            break
        
        dest_path = values[0]
        add_env_var = None if len(values) > 1 else values[1]

        if event1 == 'install_btn' and not window2_active:
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            else:
                if not sg.popup_yes_no(f'La carpeta: {dest_path} ya existe, desea sobreescribirla?'):
                    break
                else:
                    src = './dist/pomgr'
                    src_files = os.listdir(src)
                    
                    window2_active = True
                    layout2 = [
                        [sg.Text(key='-LBL1-', text='Iniciando..')],
                        [sg.ProgressBar(len(src_files), orientation='h', size=(20, 20), key='-PROGRESSBAR-')],
                        [sg.Cancel('Cancelar')] 
                    ]

                    window2 = sg.Window('Instalando...', layout2)
                    progress_bar = window2['-PROGRESSBAR-']

                    for file_name in src_files:
                        event2, values2 = window2.read(timeout=100)
                        window2['-LBL1-'].update(f'copiando... {file_name}')
                        full_file_name = os.path.join(src, file_name)
                        dest = os.path.join(dest_path, file_name)

                        if os.path.isdir(full_file_name):
                            shutil.copytree(full_file_name, dest, symlinks=True)
                        else:
                            shutil.copy(full_file_name, dest)

                        if event2 in (None, 'Cancelar'):
                            break

                        progress_bar.UpdateBar(src_files.index(file_name) + 1)

                window2.close()
        window1.close()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

