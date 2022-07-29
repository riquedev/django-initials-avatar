django-initials-avatar
---
<dl>
<table>
<tr>
    <th>Summary</th>
    <td>A ridiculously simple avatar generator with initials from names.</td>
  </tr>
  <tr>
    <th>Original Repository</th>
    <td><a href="https://github.com/eddiejibson/avatars">eddiejibson/avatars</a></td>
  </tr> 
    <tr>
        <th>Django Packages</th>
        <td><a href="https://djangopackages.org/packages/p/djangoletteravatar/">packages/djangoletteravatar</a></td>
    </tr>
</table>
</dl>

[![Upload Python Package](https://github.com/riquedev/DjangoLetterAvatar/actions/workflows/python-publish.yml/badge.svg)](https://github.com/riquedev/DjangoLetterAvatar/actions/workflows/python-publish.yml)
[![Python package](https://github.com/riquedev/DjangoLetterAvatar/actions/workflows/python-package.yml/badge.svg)](https://github.com/riquedev/DjangoLetterAvatar/actions/workflows/python-package.yml)

## Installing
First add the application to your Python path. The easiest way is to use pip:

```shell
pip install django-initials-avatar
```

Check the [Release History](https://pypi.org/project/django-initials-avatar/#history) tab on the PyPI package page for
pre-release versions. These can be downloaded by specifying the version.

You can also install by downloading the source and running:

```shell
python setup.py install
```

## Configuring

Make sure you have add the django_initials_avatar application to your INSTALLED_APPS list:

```python
INSTALLED_APPS = (
    ...
    'django_initials_avatar',
)
```

Then ensure that your project URL conf is updated.

```python
from django.urls import path, include

urlpatterns = [
    ...
    path("initials-avatar/", include('django_initials_avatar.urls'))
]
```

### Default Background Colors

```python
INITIALS_AVATAR_BG_COLORS = [
    "#E284B3", "#FFED8B", "#681313", "#F3C1C6", "#735372", "#009975", "#FFBD39", "#B1E8ED", "#52437B", "#F76262",
    "#216583", "#293462", "#DD9D52", "#936B93", "#6DD38D", "#888888", "#6F8190", "#BCA0F0", "#AAF4DD", "#96C2ED",
    "#3593CE", "#5EE2CD", "#96366E", "#E38080"
]
```

### Default Text Color

```python
INITIALS_AVATAR_TEXT_COLOR = '#fff'
```

### Default Text Length

```python
INITIALS_AVATAR_TEXT_LENGTH = 2
```

### Default Avatar Width

```python
INITIALS_AVATAR_WIDTH = 500
```

### Default Avatar Height

```python
INITIALS_AVATAR_HEIGHT = 500
```

### Default Avatar Font Size

```python
INITIALS_AVATAR_FONT_SIZE = 250
```

### Avatar Rounded By Default

```python
INITIALS_AVATAR_ROUNDED = False
```

### Avatar Capitalize by Default

```python
INITIALS_AVATAR_CAPITALIZE = False
```

### Avatar Lowercase by Default

```python
INITIALS_AVATAR_LOWERCASE = False
```

### Avatar Bold by Default

```python
INITIALS_AVATAR_BOLD = False
```

### Cache timeout

```python
INITIALS_AVATAR_CACHE_TIMEOUT = 60 * 60
```

Usage Overview
---

In most cases it will probably be more efficient to use the template tag to get the avatar's reverse url
```django
{% load initials_avatar %}
{% render_initials_avatar "Your Name Here" %}
```
You can also pass parameters
```django
{% load initials_avatar %}
{% render_initials_avatar "Your Name Here" background="transparent" %}
```
Available parameters:
- name
- background
- color
- length
- width
- height
- size
- rounded
- capitalize
- lowercase
- bold