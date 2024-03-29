# Photographer Personal Portfolio

Este es un proyecto de portafolio personal para fotógrafos, diseñado para exhibir su trabajo de manera atractiva y profesional. El portafolio está construido utilizando Django, un marco web de Python, que facilita la creación y administración de contenido dinámico.

## Características

- **Galería de imágenes:** Muestra tus mejores trabajos a través de una elegante galería de imágenes.
- **Formulario de contacto:** Permite a los visitantes ponerse en contacto contigo fácilmente para consultas o contrataciones.
- **Sección de biografía:** Comparte tu historia y experiencia como fotógrafo para conectarte con tu audiencia.
- **Diseño receptivo:** Garantiza que tu portafolio se vea impresionante en dispositivos de todos los tamaños.

## Uso de Bootstrap

Este proyecto utiliza Bootstrap, un marco de diseño de código abierto que agiliza el desarrollo web. Bootstrap proporciona estilos predefinidos y componentes que facilitan la creación de interfaces modernas y receptivas.

## Configuración del Proyecto

Requisitos:

- Python
- Django

Instalación:

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Visita http://localhost:8000 en tu navegador.

Personalización

## Contenido:
Modifica la galería de imágenes en el modelo Images en portfolio/models.py.
Personaliza la información biográfica en la vista home en portfolio/views.py.

## Estilos y Plantillas:
Personaliza los estilos en los archivos CSS en la carpeta static/css.
Modifica las plantillas HTML en la carpeta templates.

## Configuración del Correo Electrónico:
Configura las variables de entorno para el correo electrónico en tu entorno de desarrollo.

## Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejoras o encuentras problemas, no dudes en abrir un problema o enviar una solicitud de extracción.

