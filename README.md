django-simple-open-graph
========================

Django package for simplicity embed open graph (og:) layout in templates for different objects


Problem
-------

If you use many different objects and you need embed open-graph (e.g. facebook) layout for all pages in site.


Solution
--------

This package help you!
﻿
          /◝o
       (¤_¤)
       .[__].
█▄▄ ███ █▄▄ █▄█▄█ █▄█ ▀█▀


Example of usage
----------------

Add og namespace in your base template:

    <html prefix="og: http://ogp.me/ns#">

or for facebook:

    <html xmlns:fb="http://ogp.me/ns/fb#" lang="en">

And add block in base template:

    <head>
        ...
        {% block extra_head %}{% endblock %}
        ...
    </head>

Aaand! You can use this package in different templates:

    {% load simple_open_graph %}

    {% block extra_head %}
        {% thumbnail object.user.image 150x150 as uimage %} <!-- as example for use easy_thumbnails package -->
        {% get_opengraph_meta "url=object.get_absolute_url, title=object.title, type='website', image=uimage.url" %}
    {% endblock %}

This tag converted in meta html properties:

    <meta property="og:url" content="/users/1">
    <meta property="og:image" content="/media/thumbnails/users/person1.jpg.150x150_q85.jpg">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Profile: user #1">

Excelent!
