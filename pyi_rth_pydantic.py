# PyInstaller runtime hook for Pydantic V2
# This fixes the 'compiled' attribute error in Pydantic V2

import sys

# Patch pydantic to avoid the 'compiled' attribute error
if 'pydantic' in sys.modules:
    import pydantic
    if not hasattr(pydantic, 'compiled'):
        pydantic.compiled = False
