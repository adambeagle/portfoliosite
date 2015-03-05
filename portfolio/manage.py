#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Make sure default setting is production if in production!
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings.production")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
