======================
README - portfoliosite
======================

**Author: Adam Beagle**

This repository contains the source for my portfolio/blog website, made with Django 1.7. 

Layout
------

Repository root
^^^^^^^^^^^^^^^
:/docs: Project-wide documentation lives here.

:/portfolio: The Django project root directory.

:requirements.txt: Lists required python packages and their versions. Useful in conjunction with ``pip.``

Django Project Directory (/portfolio)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:/blog: Django app for the blog portion of the site. 

:/core: Django app for the core pages and functionality of the site. 

:/portfolio: Configuration for the entire project. The root urlconfs and Django settings are here.

:/projects: Django app for the Projects index page (and potential future detail pages).

:/staticfiles: Used in production by ``collectstatic``. Empty in this repository.

:/templates: Templates from all apps are in this directory. The directory structure and naming patterns are modeled after those found in "Two Scoops of Django" 12.2.1.

:/util: Utility scripts that are independent of Django.

Legal
-----

See ``docs/LICENSE.txt`` for license information. 