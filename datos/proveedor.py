from src.datos.conexion import Conexion
from src.dominio.proveedor import Proveedor


class ProveedorDao:
    _ERROR = -1
    _INSERT = ("insert into Proveedor(RazonSocial, Ruc, Ciudad, Email) "
               "VALUES (?,?,?,?)")
    _SELECT = ("SELECT RazonSocial, Ruc, Ciudad, Email FROM Proveedor "
               "where Ruc=?")
    _UPDATE = ("update Proveedor set RazonSocial=?, Ciudad=?, Email=? "
               "where Ruc=?")
    _DELETE = "delete from Proveedor where Ruc=?"

    @classmethod
    def insertar_proveedor(cls, proveedor):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (proveedor.RazonSocial,
                         proveedor.Ruc, proveedor.Ciudad, proveedor.Email,)
                registros = cursor.execute(cls._INSERT, datos)
                return registros.rowcount
        except Exception as e:
            print(f"Error al insertar proveedor: {e}")
            cursor.rollback()
            return cls._ERROR

    @classmethod
    def seleccionar_proveedor(cls, Ruc):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (Ruc,)
                registro = cursor.execute(cls._SELECT, datos).fetchone()
                print(registro)
                if registro[2] == 'G':
                    Ciudad =  'Guayaquil'
                else:
                    Ciudad = 'Quito'
                proveedor = Proveedor(RazonSocial=registro[0],
                                  Ruc=registro[1],
                                  Email=registro[3],
                                  Ciudad=Ciudad)
                return proveedor
        except Exception as e:
            print(f"Error al consultar proveedor: {e}")
            return None

    @classmethod
    def actualizar_proveedor(cls, proveedor):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (proveedor.RazonSocial,
                         proveedor.Ciudad, proveedor.Email, proveedor.Ruc,)
                registros = cursor.execute(cls._UPDATE, datos)
                return registros.rowcount
        except Exception as e:
            print(f"Error al actualizar proveedor: {e}")
            cursor.rollback()
            return cls._ERROR

    @classmethod
    def eliminar_proveedor(cls, Ruc):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (Ruc,)
                registros = cursor.execute(cls._DELETE, datos)
                return registros.rowcount
        except Exception as e:
            print(f"Error al eliminar al proveedor: {e}")
            cursor.rollback()
            return cls._ERROR

if __name__ == '__main__':
    p = Proveedor('ProyectoFinal S.A.', '0951570050001', 'G', 'proyecto.final@mail.com')
    # r = ProveedorDao.insertar_proveedor(p)
    r = ProveedorDao.actualizar_proveedor(p)
    print(r)