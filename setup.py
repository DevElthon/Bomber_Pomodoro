import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base, targetName="BomberPomodoro")]

cx_Freeze.setup(
    name="NAME_OF_EXE",
    options={"build_exe": {"packages": ["tkinter", "math", "PIL"], "include_files": [
        "blackbox.png","work_img.png", "finish_img.png", "procrastinate_img.png", "recover_img.png"
        , "rest_img.png",
    ]}},
    version="1.0",
    description="DESCRIBE YOUR PROGRAM",
    executables=executables
)