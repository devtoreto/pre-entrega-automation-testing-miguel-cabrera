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
```

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

## Instalación (Windows CMD y PowerShell)
1. Instalar **Python 3.10 o superior** desde https://www.python.org/downloads/windows/ y habilitar **Add Python to PATH** durante la instalación. Instalar Git y Chrome o Firefox.
2. Abrir PowerShell o CMD dentro de la carpeta del proyecto.

**PowerShell:**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
Si PowerShell bloquea la activación, usar CMD (sin modificar las políticas de seguridad), o ejecutar directamente `.\.venv\Scripts\python.exe -m pytest ...`.

**CMD:**
```bat
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

## Ejecutar pruebas
Desde la **raíz del proyecto**:
```bash
python -m pytest tests/test_saucedemo.py -v -s --html=reports/reporte.html --self-contained-html
```
Modo con navegador visible:
```bash
python -m pytest tests/test_saucedemo.py -v -s --headed --step-delay=2 --html=reports/reporte.html --self-contained-html
```
Con Firefox:
```bash
python -m pytest tests/test_saucedemo.py -v --browser=firefox --headed --step-delay=2 --html=reports/reporte.html --self-contained-html
```
## Casos automatizados
1. **Login exitoso:** ingresa `standard_user` / `secret_sauce`, espera redirección a `/inventory.html`, valida `Swag Labs` y `Products`. Captura OK del inventario.
2. **Catálogo:** valida encabezado, al menos un producto, menú, selector de orden y muestra nombre/precio del primero. Captura OK del Catálogo.
3. **Carrito:** agrega el primer producto, valida badge `1`, abre el carrito y confirma que el mismo producto aparece y toma una captura.

Cada test abre su propio navegador. Las capturas OK se guardan **después de las validaciones** y las capturas FAIL se toman automáticamente al detectar un fallo cuando el navegador está disponible.

## Evidencias
```text
reports/
├── reporte.html
├── screenshots/
│   ├── OK/
│   │   ├── test_login_exitoso.png
│   │   ├── test_catalogo_productos.png
│   │   ├── carrito_01_producto_agregado.png
│   │   └── carrito_02_producto_verificado.png
│   └── FAIL/
└── logs/
    └── execution.log
```

## Observaciones
El proyecto requiere conexión a Internet para acceder a SauceDemo. Y tener instalado Firefox, Google Chrome.
Las capturas se guardan como archivos PNG independientes; el reporte HTML muestra los resultados de Pytest. Las evidencias anteriores con el mismo nombre se reemplazan en cada ejecución. El reporte se genera solo al ejecutar las pruebas.
- Selenium Manager gestiona automáticamente el driver compatible, normalmente con conexión a Internet la primera vez.
- Las credenciales son las públicas del sitio de demostración.