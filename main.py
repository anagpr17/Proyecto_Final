import sys

from PySide6.QtWidgets import QApplication

from src.servicio.proveedor import ProveedorServicio

app = QApplication()
vtn_principal = ProveedorServicio()
vtn_principal.show()
sys.exit(app.exec())