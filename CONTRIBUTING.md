# Guía de Contribución 🐍✨

Gracias por tu interés en contribuir al blog de la comunidad Python Chile! 🚀

El sitio está hecho con el framework [Pelican](https://getpelican.com/) y los post están escritos ocupando **Markdown**.

Por favor seguir los siguientes puntos para contribuir con un nuevo post o para mejorar el sitio.

# Tabla de contenido

1. [Primer Paso Fork de Proyecto](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#1--primer-paso-fork-de-proyecto)
2. [Estructura del Proyecto](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#2--estructura-del-proyecto)
3. [Crear un Post](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#3--crear-un-post)
4. [Agregar Contenido de Post](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#4--agregar-contenido-de-post)
5. [Ambiente de Desarrollo Local](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#5-%EF%B8%8F-ambiente-de-desarrollo-local)
6. [Pull Request Revisón](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#6--pull-request-revis%C3%B3n)
7. [¿Primera contribución al blog?](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#7--primera-contribuci%C3%B3n-al-blog)
8. [Buenas Prácticas](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#8--buenas-pr%C3%A1cticas)
9. [¿Consultas?](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#9--consultas)
10. [Creación de Issue](https://github.com/python-chile/blogpythonchile?tab=contributing-ov-file#10--creaci%C3%B3n-de-issue)


---

# 1. 🍴 Primer Paso Fork de Proyecto

### 1. Crear un Fork

Dentro del proyecto, en el lado derecho a la altura del nombre de este, clickear **Fork** que debe estar entre los elementos **Watch** y **Star**.

>[!NOTE]
> Considera tener siempre actualizado tu fork respecto al proyecto original.
> Evita conflictos en el desarrollo por no sincronizar tu repo.


### 2. Clonar proyecto

Por ejemplo:

```bash
git clone https://github.com/<user-github>/blogpythonchile.git
```

### 3. Crear una rama para post

Nomenclatura debe ser `feature-<titulo>` donde `feature` indica que se agrega nuevo contenido (para correciones se ocupa prefijo `fix`) 
y `<titulo>` indica el nombre del post, cuyo valor depende de quién contribuya.

```bash
git checkout -b feature-hello-world
```

### 4. Agregar post

Crear archivo **Markdown** en `content/post/` y las imágenes a ocupar en `content/img/`.

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

### 1. Nuevo archivo

Crear archivo **Markdown** (extensión `.md`) en ruta `content/post/` con el formato `AAAA-MM-DD-titulo-mi-post.md`.

Ejemplo:

```bash
content/post/2025-08-25-hello-world.md
```

>[!WARNING]
> Favor respetar formato fecha

### 2. Agregar metadata

Se debe agregar **metada** al inicio del archivo **Markdown** ya que esta se ocupan como variables para crear contenido.

Seguir siguiente formato:

```bash
---
date: 2025-08-22
title: Titulo Post
summary: Resumen de Post
author: Nombre
image: img/otros/default.webp
tags: python, pelican, tutorial
---

Contenido del post comienza aquí...
```

>[!WARNING]
> Toda metadata es obligatoria como también el formato y orden de esta.

Descripción de metada:

- **date**: fecha de la creación del post. La misma ocupada en el nombre del archivo con formato AAAA-MM-DD.
- **title**: Título del post.
- **summary**: Breve resumen del post.
- **author**: Nombre de quién creó el post.
- **image**: ruta de la imagen para la prevista del post.
- **tags**: Conceptos que representen tu post. Máximo 5 y en minúsculas.

>[!NOTE]
> Si no se tiene una imagen para la prevista del post, se puede ocupar la imagen `img/otros/default.jpg`

La metadata debe estar seguida de un **salto de línea**. Una vez cumplido lo anterior 
se puede comenzar a escribir el contenido del post.


# 4. 🎨 Agregar Contenido de Post

### 1. Texto

Usar formato de **Markdown** para crear el cuerpo del post.

### 2. Bloque de código

Para mostrar código seguir el siguiente formato:

```bash
   texto ...

    ```python
    def hello():
      print("Hello world!")
    ```
    
    texto ...
```

>[!NOTE]
> Por defecto todo bloque de código tiene botón de copiar código.

El bloque de código debe situarse en la **columna 0**, es decir, no se le debe aplicar ningún tab.

Al momento de crear el sitio estático, todo bloque de código estará centrado horizontalmente

Es importante también agregar un espacio en blanco antes y después del bloque de código.

El lenguaje que se utiliza en el bóque de código se debe definir al principio de este, como en el ejemplo que se ocupa **python** en **```python**.

### 3. Imágenes

Toda imagen guardada en el proyecto y ocupada en un post, debe ser tipo **webpg**.

No hay un estandar actualmente de cómo integrar imágenes en un post, se puede agregar el estilo y 
dimensiones que se quiera. Queda a gusto personal este punto.

Ejemplo de imagen en un post:

```bash
<img src="{static}/img/mi-post/mi-post.webp" width="480" height="380" />
```

Toda imagen que se ocupe en el post debe estar guardada en la ruta `content/img/<sub-carpeta>/`. Donde `<sub-carpeta>` debe tener el mismo nombre que el post a publicar. Esta se 
crear en el momento de la contribución del post.


# 5. ⚙️ Ambiente de Desarrollo Local

### 1. Versión de Python

Ocupar versión que sea igual o mayor a versión 3.11

### 2. Instalación de dependencias

>[!NOTE]
> 
> **Importante**
> 
> Para el manejo de dependencias se recomienda ocupar un entorno virtual de python. Por ejemplo [virtualenv](https://virtualenv.pypa.io/en/latest/).

```bash
pip install -r requirements.txt
```

### 3. Build de Proyecto

```bash
pelican content
```

también puede ser

```bash
pelican content -s pelicanconf.py -o output
```

El comando anterior ocupa la configuración que se encuentra en el archivo **pelicanconf.py** 
para generar el sitio estático en la carpeta **output/**

### 4. Prevista en local

URL de sitio `http://localhost:8000`

```bash
pelican -l
```


# 6. 🔄 Pull Request Revisón

Cuando los cambios estén listos y subidos en el fork creado anteriormente, se debe abrir una pull request.

Considerar los siguientes puntos para la revisión:

- Respetar cada punto definido en la guía.
- Tiempo de revisón es de **5 días** por motivos de disposición del equipo.
- Considerar toda sugerencia que pueda aparecer en la revisión. 
- La pull request se puede rechazar si no cumple con la normativa de la comunidad.
- Procurar revisar checklist al momento de abrir PR (template PR).


# 7. ⭐ ¿Primera contribución al blog?

Si es el primer aporte por favor considerar agregar algunos datos del perfil de github para poder mostrarlo junto al resto
de contribuidores.

En archivo `contributors.py` agregar los siguientes valores llave-valor siguiendo formato **json**:

- **id**: número positivo incremental (tipo **int**)
- **username**: nombre usuario de github (tipo **string**)
- **profileUrl**: URL de tu perfil de github. Ejemplo `https://github.com/<username>` (tipo **string**)
- **avatarUrl**: URL de tu imagen de perfil de usuario. Puede ser desde `https://github.com/<username>.png` o `https://avatars.githubusercontent.com/u/<id>?v=4` (tipo **string**)

Debes agregar los datos indicados al final de la lista de perfiles, respetando que campo **id** sea consecutivo respecto del último usuario ya incluido.

Por ejemplo

```bash
{
    "id": 3,
    "username": "octocat",
    "profileUrl": "https://github.com/octocat",
    "avatarUrl": "https://avatars.githubusercontent.com/u/1234567?v=4"
}
```


# 8. ✅ Buenas Prácticas

- Texto con coherencia, buena ortografía y ordenada.
- Usar ejemplos, códigos o diagramas para complementar.
- Revisa cómo se muestra tu post en el sitio de forma local antes de la PR.


# 9. 🤔 ¿Consultas?

En caso de cualquier duda, consulta o cualquier inconveniente, puedes escribir a la comunidad de Python Chile en 
el servidor oficial de Discord **Python Chile**.


# 10. 💬 Creación de Issue

Si hay algo relacionado al proyecto, ya sea algún bug, documentación, diseño de sitio, post con contenido erróneo, flujo de trabajo, o cualquier 
otra cosa que no sea respecto a crear un post, puedes crear un **issue** en el repositorio **blogpythonchile**, solo debes agregar la información necesaria para que 
cualquier persona pueda entender el contexto como también el objetivo de la issue. Una vez definido bien el detalle, ya cualquier persona se puede asignar a esta y 
comenzar a contribuir.

