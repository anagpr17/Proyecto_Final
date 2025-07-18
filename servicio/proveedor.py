from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.datos.proveedor import ProveedorDao
from src.UI.vtnProyectoFinal import Ui_ProyectoFinal
from src.dominio.proveedor import Proveedor


class ProveedorServicio(QMainWindow):
    def __init__(self):
        super(ProveedorServicio, self).__init__()
        self.ui = Ui_ProyectoFinal()
        self.ui.setupUi(self)
        self.ui.btnNuevo.clicked.connect(self.nuevo)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnBorrarRegistro.clicked.connect(self.borrar_registro)
        self.ui.txtRuc.setValidator(QDoubleValidator())
        self.ui.txtBuscarRuc.setValidator(QDoubleValidator())

    def nuevo (self):
        if self.ui.txtRazonSocial.text() == ''\
                or len(self.ui.txtRuc.text()) < 13 or self.ui.txtEmail.text() == ''\
                or self.ui.cbCiudad.currentText() == 'Seleccionar':
            QMessageBox.warning(self, 'Advertencia', 'Ingrese los datos.')
        else:
            proveedor = Proveedor(RazonSocial=self.ui.txtRazonSocial.text(),
                             Ruc=self.ui.txtRuc.text(),
                             Email=self.ui.txtEmail.text(),
                              Ciudad=self.ui.cbCiudad.currentText()[0])
            print(proveedor)
            if ProveedorDao.insertar_proveedor(proveedor) == -1:
                QMessageBox.critical(self, 'Error', 'No se pudo guardar al proveedor.')
            else:
                self.ui.statusbar.showMessage('Se guardo la información', 3000)
                self.limpiar()

    def limpiar(self):
        self.ui.txtRazonSocial.setText("")
        self.ui.txtRuc.setText("")
        self.ui.txtEmail.setText("")
        self.ui.cbCiudad.setCurrentText("Seleccionar")


    def buscar (self):
        if len(self.ui.txtBuscarRuc.text()) < 13:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese el Ruc del proveedor a buscar.')
        else:
            proveedor = ProveedorDao.seleccionar_proveedor(self.ui.txtBuscarRuc.text())
            if proveedor:
                self.ui.txtRazonSocial.setText(proveedor.RazonSocial)
                self.ui.txtRuc.setText(proveedor.Ruc)
                self.ui.txtEmail.setText(proveedor.Email)
                self.ui.cbCiudad.setCurrentText(proveedor.Ciudad)
            else:
                QMessageBox.information(self, 'Información', 'Ruc Proveedor no encontrada.')

    def actualizar (self):
        if QMessageBox.question(self, 'Pregunta', 'Esta seguro de actualizar?.') ==  QMessageBox.Yes:
            if self.ui.txtRazonSocial.text() == ''\
                    or len(self.ui.txtRuc.text()) < 13 or self.ui.txtEmail.text() == '' \
                    or self.ui.cbCiudad.currentText() == 'Seleccionar':
                QMessageBox.warning(self, 'Advertencia', 'Ingrese los datos.')
            else:
                proveedor = Proveedor(RazonSocial=self.ui.txtRazonSocial.text(),
                                  Ruc=self.ui.txtRuc.text(),
                                  Email=self.ui.txtEmail.text(),
                                  Ciudad=self.ui.cbCiudad.currentText()[0])
                print(proveedor)
                if ProveedorDao.actualizar_proveedor(proveedor) == -1:
                    QMessageBox.critical(self, 'Error', 'No se pudo actualizar al proveedor.')
                else:
                    self.ui.statusbar.showMessage('Se actualizó la información', 3000)
                    self.limpiar()

    def borrar_registro (self):
        if QMessageBox.question(self, 'Pregunta', 'Esta seguro de borrar el registro?.') ==  QMessageBox.Yes:
            Ruc = self.ui.txtRuc.text()
            if ProveedorDao.eliminar_proveedor(Ruc) == -1:
                QMessageBox.critical(self, 'Error', 'No se pudo borrar el regsitro del proveedor.')
            else:
                self.ui.statusbar.showMessage('Se borro el registro.', 3000)
                self.limpiar()