# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnProyectoFinal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_ProyectoFinal(object):
    def setupUi(self, ProyectoFinal):
        if not ProyectoFinal.objectName():
            ProyectoFinal.setObjectName(u"ProyectoFinal")
        ProyectoFinal.resize(450, 603)
        self.centralwidget = QWidget(ProyectoFinal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbBuscarRuc = QLabel(self.centralwidget)
        self.lbBuscarRuc.setObjectName(u"lbBuscarRuc")
        self.lbBuscarRuc.setGeometry(QRect(20, 50, 81, 16))
        self.lbRazonSocial = QLabel(self.centralwidget)
        self.lbRazonSocial.setObjectName(u"lbRazonSocial")
        self.lbRazonSocial.setGeometry(QRect(20, 90, 61, 16))
        self.lbRuc = QLabel(self.centralwidget)
        self.lbRuc.setObjectName(u"lbRuc")
        self.lbRuc.setGeometry(QRect(20, 130, 35, 10))
        self.lbEmail = QLabel(self.centralwidget)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setGeometry(QRect(20, 170, 35, 10))
        self.lbCiudad = QLabel(self.centralwidget)
        self.lbCiudad.setObjectName(u"lbCiudad")
        self.lbCiudad.setGeometry(QRect(20, 210, 35, 10))
        self.txtBuscarRuc = QLineEdit(self.centralwidget)
        self.txtBuscarRuc.setObjectName(u"txtBuscarRuc")
        self.txtBuscarRuc.setGeometry(QRect(140, 50, 151, 20))
        self.txtBuscarRuc.setMaxLength(13)
        self.txtRazonSocial = QLineEdit(self.centralwidget)
        self.txtRazonSocial.setObjectName(u"txtRazonSocial")
        self.txtRazonSocial.setGeometry(QRect(140, 90, 151, 20))
        self.txtRazonSocial.setMaxLength(50)
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(140, 170, 151, 20))
        self.txtEmail.setMaxLength(50)
        self.cbCiudad = QComboBox(self.centralwidget)
        self.cbCiudad.addItem("")
        self.cbCiudad.addItem("")
        self.cbCiudad.addItem("")
        self.cbCiudad.setObjectName(u"cbCiudad")
        self.cbCiudad.setGeometry(QRect(140, 210, 151, 22))
        self.btnNuevo = QPushButton(self.centralwidget)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setGeometry(QRect(30, 290, 56, 17))
        self.btnActualizar = QPushButton(self.centralwidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(120, 290, 56, 17))
        self.btnBorrarRegistro = QPushButton(self.centralwidget)
        self.btnBorrarRegistro.setObjectName(u"btnBorrarRegistro")
        self.btnBorrarRegistro.setGeometry(QRect(210, 290, 71, 17))
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(320, 290, 56, 17))
        self.btnBuscar = QPushButton(self.centralwidget)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(340, 50, 56, 17))
        self.txtRuc = QLineEdit(self.centralwidget)
        self.txtRuc.setObjectName(u"txtRuc")
        self.txtRuc.setGeometry(QRect(140, 130, 151, 21))
        self.txtRuc.setMaxLength(13)
        ProyectoFinal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProyectoFinal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 22))
        ProyectoFinal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ProyectoFinal)
        self.statusbar.setObjectName(u"statusbar")
        ProyectoFinal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtBuscarRuc, self.btnBuscar)
        QWidget.setTabOrder(self.btnBuscar, self.txtRazonSocial)
        QWidget.setTabOrder(self.txtRazonSocial, self.txtEmail)
        QWidget.setTabOrder(self.txtEmail, self.cbCiudad)
        QWidget.setTabOrder(self.cbCiudad, self.btnNuevo)
        QWidget.setTabOrder(self.btnNuevo, self.btnActualizar)
        QWidget.setTabOrder(self.btnActualizar, self.btnBorrarRegistro)
        QWidget.setTabOrder(self.btnBorrarRegistro, self.btnLimpiar)

        self.retranslateUi(ProyectoFinal)

        QMetaObject.connectSlotsByName(ProyectoFinal)
    # setupUi

    def retranslateUi(self, ProyectoFinal):
        ProyectoFinal.setWindowTitle(QCoreApplication.translate("ProyectoFinal", u"MainWindow", None))
        self.lbBuscarRuc.setText(QCoreApplication.translate("ProyectoFinal", u"Buscar Ruc", None))
        self.lbRazonSocial.setText(QCoreApplication.translate("ProyectoFinal", u"Razon Social", None))
        self.lbRuc.setText(QCoreApplication.translate("ProyectoFinal", u"Ruc", None))
        self.lbEmail.setText(QCoreApplication.translate("ProyectoFinal", u"Email", None))
        self.lbCiudad.setText(QCoreApplication.translate("ProyectoFinal", u"Ciudad", None))
        self.cbCiudad.setItemText(0, QCoreApplication.translate("ProyectoFinal", u"Seleccionar", None))
        self.cbCiudad.setItemText(1, QCoreApplication.translate("ProyectoFinal", u"Guayaquil", None))
        self.cbCiudad.setItemText(2, QCoreApplication.translate("ProyectoFinal", u"Quito", None))

        self.btnNuevo.setText(QCoreApplication.translate("ProyectoFinal", u"Nuevo", None))
        self.btnActualizar.setText(QCoreApplication.translate("ProyectoFinal", u"Actualizar", None))
        self.btnBorrarRegistro.setText(QCoreApplication.translate("ProyectoFinal", u"Borrar Registro", None))
        self.btnLimpiar.setText(QCoreApplication.translate("ProyectoFinal", u"Limpiar", None))
        self.btnBuscar.setText(QCoreApplication.translate("ProyectoFinal", u"Buscar", None))
    # retranslateUi

