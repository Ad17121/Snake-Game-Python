import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
    name = "Snake",
    options = {"build_exe" : {"packages":["pygame"]}},
    executables = executables
)