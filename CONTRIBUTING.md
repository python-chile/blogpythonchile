# Guía de Contribución 🐍✨

Gracias por tu interés en contribuir al blog de la comunidad Python Chile! 🚀

El sitio está hecho con el framework [Pelican](https://getpelican.com/) y los post están escritos ocupando **Markdown**.

Por favor sigue los siguientes puntos para contribuir con un nuevo post o para mejorar el sitio.

# Tabla de contenido

1. Primer Paso Fork de Proyecto
2. Estructura del Proyecto
3. Crear un Post
4. Agregar Contenido de Post
5. Ambiente de Desarrollo Local
6. Pull Request Revisón


---

# 1. 🍴 Primer Paso Fork de Proyecto

1. Crear un Fork

Dentro del proyecto, en el lado derecho a la altura del nombre de este, clickear **Fork** que debe estar entre los elementos **Watch** y **Star**.

2. Clonar proyecto

Por ejemplo:

```bash
git clone https://github.com/<user-github>/blogpythonchile.git
```

3. Crear una rama para post

```bash
git checkout -b mi-primer-post
```

4. Agregar post

Crea un archivo **Markdown** en `content/post/` y las imágenes a ocupar en `content/img/`.

Para más información dirigirse a punto **3** para crear un post y punto **4** para conocer el formato del contenido. 


# 2. 📂 Estructura del Proyecto

```bash
.github/workflows/  # Configuración github actions
content/            # Elementos para crear un post
  img/              # Imágenes que contiene un post incluyend la imagen de su prevista
  post/             # Markdown para el contenido de un post
theme/
  static/           # Estáticos css,img, js.
  templates/        # HTML para construir sitio estático
pelicanconf.py      # Configuración para ambiente de desarrollo o ambiente local
publishconf.py      # Configuración para ambiente de producción
```


# 3. 📝 Crear un Post

1. Crea un nuevo archivo **Markdown** en `content/post`

Ejemplo:

```bash
content/post/mi-post.md
```

2. Agrega la metadata al principio del archivo

Sigue el siguiente formato

```bash
---
date: 2025-08-22
title: Titulo Post
summary: Resumen de Post
author: Nombre
image: img/otros/default.jpg
tags: python, pelican, tutorial
---

Contenido del post comienza aquí...
```

>[!WARNING]
> Toda la metadata es obligatoria como también el formato de esta.

Descripción de metada:

- **date**: fecha de la creación del post. Formato AAAA-dd-MM.
- **title**: Título del post.
- **summary**: Breve resumen del post.
- **author**: Nombre de quién creó el post.
- **image**: ruta de la imagen para la prevista del post.
- **tags**: Conceptos que representen tu post. Máximo 5 y en minúsculas.

>[!NOTE]
> Si no tienes una imagen para la prevista del post, puedes ocupar la imagen `img/otros/default.jpg`

Luego de crear la metadata y seguido de esta un **salto de línea**, ya puedes comenzar a escribir el contenido del post.


# 4. 🎨 Agregar Contenido de Post

1. Texto

Solamente usar formato de **Markdown**.

2. Bloque de código

Para mostrar código seguir el siguiente formato:

```bash
   texto ...

    ```python
    def hello():
      print("Hello world!")
    ```
    
    text ...
```

El bloque de código debe situarse en la **columna 0**, es decir, no se le debe aplicar ni un tab.
Al momento de crear el sitio estático, todo bloque de código estará situadio centrado horizontalmente

Es importante también agregar un espacio en blanco antes y después del bloque de código.

El lenguaje que se utiliza en el bóque de código se debe definir al principio de este, como en el ejemplo que se ocupa **python** en **```python**.

3. Imágenes

Debe ser tipo **webpg** toda imagen ocupada en el contenido.

Para poder mostrar cualquier imagen ocupar el siguiente formato:

```bash

![texto alternativo]({static}/path/de/imagen/nombre-imagen.webp)

```

Toda imagen que se ocupe en el post debe estar guarda en la ruta `content/img/<sub-carpeta>/<año>`. Si `<sub-carpeta>` y/o `<año>` no existe, se puede 
crear en el momento de la contribución del post.


# 5. ⚙️ Ambiente de Desarrollo Local

1. Instalación de dependencias

>[!NOTE]
> Se recomienda ocupar un entorno virtual de python. Por ejemplo [virtualenv](https://virtualenv.pypa.io/en/latest/).

```bash
pip install -r requirements.txt
```

2. Build de Proyecto

```bash
pelican content
```

también puede ser

```bash
pelican content -s pelicanconf.py -o output
```

El comando anterior ocupa la configuración que se encuentra en el archivo **pelicanconf.py** 
para generar el sitio estático en la carpeta **output/**

3. Prevista en local

```bash
pelican -l
```


# 6. 🔄 Pull Request Revisón

Cuando tengas tus cambios listos y pusheados en el fork creado anteriormente, debes abrir una pull request.

Considerar lo siguientes puntos para la revisión:

- Tiempo es de **una semana** por motivos de disposición del equipo.
- Considerar toda sugerencia que pueda aparecer en la revisión. 
- La pull request se puede rechazar si no cumple con la normativa de la comunidad.

---

# ✅ Buenas Prácticas

- Texto con coherencia, buena ortografía y ordenada.
- Usar ejemplos, códigos u diagramas para complementar.
- Revisa cómo se muestra tu post en el sitio de forma local antes de la PR.


# 💬 ¿Tienes Consultas?

En caso de cualquier duda, consulta o cualquier inconveniente, puedes escribir a la comunidad de Python Chile en 
el servidor oficial de Discord **Python Chile**.