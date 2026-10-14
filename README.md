# Pre-entrega: Automation Testing con Selenium y Pytest
## Tecnologías
- Python 3.10+
- Selenium WebDriver 4
- Pytest
- pytest-html (reporte HTML)
- Git y GitHub
- Google Chrome/Chromium o Firefox

## Estructura
```text
tests/                 # Tests y fixtures de Pytest
utils/                 # Funciones auxiliares reutilizables
reports/screenshots/   # Capturas automáticas cuando falla una prueba
reports/logs/          # Logs de ejecución
requirements.txt       # Dependencias
pytest.ini             # Configuración
README.md              # Instrucciones

## Instalación (Linux)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
cd pre-entrega-automation-testing-miguel-cabrera
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
## Ejecutar pruebas
Desde la **raíz del proyecto**:
```bash
pytest tests/test_saucedemo.py -v -s --html=reports/reporte.html --self-contained-html
```
Modo con navegador visible:
```bash
pytest tests/test_saucedemo.py -v -s --headed --html=reports/reporte.html --self-contained-html
```
Con Firefox:
```bash
pytest tests/test_saucedemo.py -v --browser=firefox --html=reports/reporte.html --self-contained-html
```
## Casos automatizados
1. **Login exitoso:** ingresa `standard_user` / `secret_sauce`, espera redirección a `/inventory.html`, valida `Swag Labs` y `Products`.
2. **Catálogo:** valida encabezado, al menos un producto, menú, selector de orden y muestra nombre/precio del primero.
3. **Carrito:** agrega el primer producto, valida badge `1`, abre el carrito y confirma que el mismo producto aparece.

Cada test crea y cierra su propia instancia del navegador (fixture de alcance `function`). Las interacciones usan esperas explícitas; no se utilizan pausas fijas.

## Evidencias
- `reports/reporte.html`: reporte HTML generado al ejecutar Pytest.
- `reports/screenshots/`: screenshots automáticos en fallos, si el navegador está disponible.
- `reports/logs/execution.log`: logs de los tests y errores.

## Observaciones
El proyecto requiere conexión a Internet para acceder a SauceDemo. Y tener instalado Firefox, Google Chrome.