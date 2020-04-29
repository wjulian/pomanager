# pomanager
Una herramienta para generar archivos .po traducidos por Google Translator.
``pomgr`` es una interfaz de linea de comandos que usa un archivo de configuración ``pomgr.settings.json`` para generar archivos .po.
En este archivo de configuración se guardan valores como: lenguaje de destino, directorio de destino para los archivos .po,
directorio de entrada donde se extraeran los textos a traducir, etc...

**Instalación**
 - Descargar el ejecutable desde https://drive.google.com/open?id=1mkGxURpSIUf895rfl19ivc_WbMVnZ8X9.
 - Ejecutar e instalar.
 - Una vez instalado agregar la ruta del directorio donde se instaló a la variable de entorno ``Path``.
 
**Uso**
 
En la consola de comandos (cmd | powershell) ubicarse en la ruta donde se quiere guardar el archivo de configuración.

```
 PS C:/Users/myuser/src> pomgr init
```

Se creará el archivo pomgr.settings.json con los valores por defecto:
```
  {
    "profiles": [
        {
            "name": "default",
            "entries": [
                "./"
            ],
            "file_exts": [],
            "output": "",
            "lang": "",
            "pattern": "((?<=T\\(\").+?(?=\"\\))|(?<=T\\(\").+?(?=\",))",
            "filename": "translation"
        }
    ],
    "author": "",
    "author_email": ""
}
```
El archivo cuenta con una lista de perfiles. En cada perfil puede definirse los parametros de generación de cada archivo, enfocado a
el lenguaje de traducción.

 **name:** Nombre del perfil.
 
 **entries:** Lista de rutas donde se extraeran los archivos ().

 **file_exts:** Extensiones de los archivos a buscar en las rutas especificadas.
 
 **output:** Directorio donde se guardará el archivo generado.
 
 **lang:** Idioma de destino.
 
 **pattern:** Patrón regex para encontrar el localizador de textos en este caso 'T("Texto a traducir")'.
 
 **filename:** Nombre del archivo que se generará.
 
 **author:** Nombre del autor de las traducciones.
 
 **author_email:** Correo electrónico del autor 
 
 
 Para listar los idiomas de traducción disponibles:
 ```
    PS C:/Users/myuser/src> pomgr langs
```
 
 Elegir un lenguaje y colocar alguna de las llaves mostradas en pantalla, ejemplo: ``es`` y modificar el archivo pomgr.settings.json 
 para generarlo adecuadamente
 
 Se puede revisar el contenido del archivo con el comando:
```
    PS C:/Users/myuser/src> pomgr settings
```

Para este ejemplo, usando el siguiente perfil: 

```     {
            "name": "es",
            "entries": [
                "./"
            ],
            "output": "App_data/Localization/es",
            "file_exts": [
                "cshtml",
                "cs"
            ],
            "lang": "es",
            "pattern": "((?<=T\\(\").+?(?=\"\\))|(?<=T\\(\").+?(?=\",))",
            "filename": "orchard.module"
        }
```


generar el archivo de traducción usando el comando:


```
  PS C:/Users/myuser/src> pomgr translate --p es
```

**--p** es la opción para elegir el perfil que se usara para generar el archivo con la traducción en este caso ``es``
