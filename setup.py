import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "include_files" : ["error_sound.ogg"]}


setup(
    name="Stroop Test",
    version="0.1",
    description="Stroop test Cue first",
    options={"build_exe": build_exe_options},
    executables=[Executable("stroop_program.py",base="Win32GUI" )],
)

# put in console: python setup.py bdist_msi
