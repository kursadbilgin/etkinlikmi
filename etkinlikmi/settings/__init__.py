# Standard Library
import getpass

# Local Django
from etkinlikmi.settings.base import *


if getpass.getuser() in ['root']:
    from etkinlikmi.settings.prod import *
else:
    from etkinlikmi.settings.dev import *
