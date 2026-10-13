# Instalación

## Requisitos

- Python 3.8 o superior
- Git
- MkDocs (solo si quieres generar esta documentación)

## Descarga

````bash
git clone <URL-del-repositorio>
cd conversor
````

## Configuración

El programa no necesita dependencias externas. Para ver la documentación en local:

````bash
python -m pip install mkdocs
````

## Ejecución

````bash
python conversor.py
````

## Comprobación

Para comprobar la documentación:

````bash
mkdocs serve
````

Abre `http://127.0.0.1:8000` en el navegador. Para generar el sitio final:

````bash
mkdocs build
````

El resultado se guarda en la carpeta `site/`.