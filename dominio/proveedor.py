class Proveedor:
    def __init__(self, RazonSocial, Ruc, Ciudad, Email=None):
        self._RazonSocial = RazonSocial
        self._Ruc = Ruc
        self._Ciudad = Ciudad
        self._Email = Email

    @property
    def RazonSocial(self):
        return self._RazonSocial

    @RazonSocial.setter
    def RazonSocial(self, valor):
        self._RazonSocial = valor

    @property
    def Ruc(self):
        return self._Ruc

    @Ruc.setter
    def Ruc(self, valor):
        self._Ruc = valor

    @property
    def Ciudad(self):
        return self._Ciudad

    @Ciudad.setter
    def Ciudad(self, valor):
        self._Ciudad = valor

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, valor):
        self._Email = valor

    def __str__(self):
        return f'Proveedor: {self.__dict__.__str__()}'

if __name__ == '__main__':
    p = Proveedor('ProyectoFinal', '0951570050001', 'G', 'proyecto.final@mail.com')
    print(p)