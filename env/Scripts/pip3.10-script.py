#!D:\Proyecto\hades\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==22.3','console_scripts','pip3.10'
__requires__ = 'pip==22.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==22.3', 'console_scripts', 'pip3.10')()
    )
