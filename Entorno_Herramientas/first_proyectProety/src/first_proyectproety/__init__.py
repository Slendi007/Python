def saludo(nombre):
    print("Hola", nombre)
    x = 10
    return x


saludo("Cesar")

# Ejecutar todos los hooks manualmente "poetry run pre-commit run --all-files"

# Crear proyecto__________ "poetry new tuproyecto"
# ______Configuarar entorno virtual:
# poetry config virtualenvs.in-project true
# poetry install
# poetry env activate (Mostrara el comando necesario para activar el entorno virtual)
# .venv\Scripts\Activate.ps1
# ______Instalar Black, isort y Ruff
# poetry add --group dev black isort ruff
# ______Configuarar el interpretador
# Ctrl + Shift + P
# Buscar: Python: Select Interpreter
# Seleccionar: tuProyecto/.venv/Scripts/python.exe
# ______Configurar Ruff
# [tool.ruff]
# line-length = 88

# [tool.ruff.lint]
# select = ["E","F","I"]

# [tool.ruff.format]
# quote-style = "double"
# indent-style = "space"
# ________Configuarar Black
# [tool.black]
# line-length = 88


# Ejecutar " poetry run black . " para probar Black
# Ejecutar " poetry run isort . " para organizar los imports
# Ejecutar " poetry run ruff check . --fix " para corregir automaticamente
# los problemas que puede solucionar.
