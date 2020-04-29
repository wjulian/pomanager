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
    """Evaluate if the program is runing as admin
    Returns:
        [bool] -- if user is admin return true, else false
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def create_main_win(prgm_path: str) -> sg.Window:
    layout = [  
        [sg.Text(key='-LBL1-', text='Instala pomanager!')],
        [sg.Text(key='-LBL_LOCATE-', text='Donde deseas instalarlo?')],
        [sg.In(prgm_path), sg.FolderBrowse('buscar')],
        # [sg.Checkbox(key='-ADD_ENV_VAR_CHECK-', text='Agregar variable de entorno (pomgr)')],
        [sg.Button(key='install_btn', button_text='Instalar'), sg.Button(key='cancel', button_text='Cancel')] 
    ]

    return sg.Window('Instalación pomanager', layout)


def create_sucss_win() -> sg.Window:
    success_layout = [
        [sg.Text('Pomanager se ha instaldo correctamente')],
        [sg.Button('Finalizar', key='-DONE-')]
    ]
    return sg.Window('Pomanager instalado', success_layout)


def get_prgm_path() -> str:
    prgm_path = os.environ.get('PROGRAMFILES(X86)') if not os.environ.get('PROGRAMFILES(X86)') else os.environ.get("PROGRAMFILES")
    prgm_path = os.path.join(prgm_path, 'pomanager')
    return prgm_path


def get_dest_path(main_vals: list) -> str:
    dest_path = main_vals[0] if 'pomanager' in main_vals[0] else os.path.join(main_vals[0], 'pomanager')
    return dest_path


def create_prgrss_win(src_files: list) -> sg.Window:
    layout2 = [
        [sg.Text(key='-LBL1-', text='Iniciando..')],
        [sg.ProgressBar(len(src_files), orientation='h', size=(20, 20), key='-PROGRESSBAR-')],
        [sg.Cancel('Cancelar')] 
    ]

    return sg.Window('Instalando...', layout2)


def get_src():
    src = os.path.join(os.getcwd(), 'bin' if not __debug__ else 'bin\dist\pomgr')
    src_files = os.listdir(src)
    return src_files, src


def copy_files(src: str, src_files: str, dest_path: str, prgrss_win: sg.Window):
    prgrss_bar = prgrss_win['-PROGRESSBAR-']

    #reading files in dist folder to install it
    for file_name in src_files:
        pw_event, pw_values = prgrss_win.read(timeout=30)
        prgrss_win['-LBL1-'].update(f'copiando... {file_name}')
        
        full_file_name = os.path.join(src, file_name)
        dest = os.path.join(dest_path, file_name)
        #if is directory copy tree else copy single file
        if os.path.isdir(full_file_name):
            shutil.copytree(full_file_name, dest, symlinks=True)
        else:
            shutil.copy(full_file_name, dest)

        if pw_event in (None, 'Cancelar'):
            break

        prgrss_bar.UpdateBar(src_files.index(file_name) + 1)


def install(dest_path: str, succs_win: sg.Window):
    src_files, src = get_src()
    is_prgrs_w_active = True

    prgrss_win = create_prgrss_win(src_files)

    try:
        copy_files(src, src_files, dest_path, prgrss_win)
    except PermissionError as error:
        sg.popup_error('Ha ocurrido un error', error)
    except shutil.Error as error:
        sg.popup_error('Ha ocurrido un error', error)
    else:
        prgrss_win.close()
        while True:
            is_succs_w_active = True
            sw_e, sw_vals = succs_win.read()
            if sw_e in (None, '-DONE-'):
                break
    finally:
        prgrss_win.close()

def run():
    make_dpi_aware()
    sg.theme('DarkBlue2')
    #getting current program files folder of windows os
    prgm_path = get_prgm_path()

    #creating windows
    main_win = create_main_win(prgm_path)
    succs_win = create_sucss_win()

    is_prgrs_w_active = False
    is_succs_w_active = False

    #Showing principal window
    while True:
        main_ev, main_vals = main_win.read()
        if main_ev in (None, 'cancel'):
            break
        
        dest_path = get_dest_path(main_vals)
        # add_env_var = None if len(values) > 1 else values[1]
        if main_ev == 'install_btn' and not is_prgrs_w_active:
            if os.path.exists(dest_path):
                if sg.popup_yes_no(f'La carpeta: {dest_path} ya existe, desea sobrescribirla?'):
                    shutil.rmtree(dest_path, ignore_errors=True)
                    os.makedirs(dest_path)
                    install(dest_path, succs_win)
                else:
                  break
            else:
                os.makedirs(dest_path)
                install(dest_path, succs_win)
                
            main_win.close()


if not __debug__: 
    if is_admin():
        run()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    run()