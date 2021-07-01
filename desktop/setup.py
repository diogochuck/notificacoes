from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = ["pypiwin32","pywin32>=223"], 
    excludes = [], 
    includes = ["pypiwin32","pywin32>=223"],
    include_files = [".\config.ini"]
    )

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base)
]

setup(name='hpsmq-client',
      version = '1.0',
      description = 'My GUI application!',
      options = dict(build_exe = buildOptions),
      executables = executables)