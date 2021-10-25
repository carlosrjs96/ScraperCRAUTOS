# Import Libraries
import time
import pyodbc
import Util
import Classes

#region General Functions
#-----------------------------------------------------------------------
class DBConnector(object):
    
    def __init__(self):
        _json = Util.load_Json('Config.json')
        self.driver   = _json['driver']
        self.server   = _json['server']
        self.database = _json['database']
        self.user     = _json['user']
        self.password = _json['password']
        self.dbconn   = None

    # Create new connection
    def create_connection(self):
        return pyodbc.connect("DRIVER={};".format(self.driver) + \
                              "SERVER={};".format(self.server) + \
                              "DATABASE={};".format(self.database) + \
                              "UID={};".format(self.user) + \
                              "PWD={};".format(self.password) + \
                              "Trusted_Connection=yes;" + \
                              "CHARSET=UTF8",
                              ansi=True)

    # For explicitly opening database connection
    def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

    def __exit__(self):
        self.dbconn.close()
#-----------------------------------------------------------------------
class DBConnection(object):
    connection = None

    @classmethod
    def get_connection(cls, new=False):
        """Creates return new Singleton database connection"""
        if new or not cls.connection:
            cls.connection = DBConnector().create_connection()
        return cls.connection

    @classmethod
    def execute_query(cls, query,state=True):
        """execute query on singleton db connection"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except pyodbc.ProgrammingError:
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor()
        cursor.execute(query)
        if state == True:
            result = cursor.fetchall()
            cursor.close()
            return result
        else:
            connection.commit()
            cursor.close()
#-----------------------------------------------------------------------
def print_Result(result:list):
    for row in result:
        print(f'Row # {result.index(row)} : {row}')
#-----------------------------------------------------------------------
#endregion General Functions

#region Query Functions

#region Select Query Functions
#-----------------------------------------------------------------------
def query_IDENT_CURRENT(table:str):
    return "SELECT IDENT_CURRENT('"+table+"')"
#-----------------------------------------------------------------------
def query_Select_All_From_AUTO() -> str:
    return "SELECT * FROM [dbo].[AUTO];"
#-----------------------------------------------------------------------
def query_Select_All_From_CONTACTO() -> str:
    return "SELECT * FROM [dbo].[CONTACTO];"
#-----------------------------------------------------------------------
def query_Select_All_From_CONTACTOXVENDEDOR() -> str:
    return "SELECT * FROM [dbo].[CONTACTOXVENDEDOR];"
#-----------------------------------------------------------------------
def query_Select_All_From_PAGINA() -> str:
    return "SELECT * FROM [dbo].[PAGINA];"
#-----------------------------------------------------------------------
def query_Select_All_From_Tipo() -> str:
    return "SELECT * FROM [dbo].[Tipo];"
#-----------------------------------------------------------------------
def query_Select_All_From_VENDEDOR() -> str:
    return "SELECT * FROM [dbo].[VENDEDOR];"
#-----------------------------------------------------------------------
def query_Select_All_From_PUBLICACION() -> str:
    return "SELECT * FROM [dbo].[PUBLICACION];"
#-----------------------------------------------------------------------
def query_Select_All_By_Timestamp(timestamp:str) -> str:
    return f"""
    SELECT  
        [PUBLICACION].FechaPublicacion  ,
        [PUBLICACION].FechaScraping     ,
        [PAGINA].Nombre                 ,
        [PUBLICACION].UrlPublicacion    ,
        [AUTO].Anno                     ,
        [AUTO].Asientos                 ,
        [AUTO].Chasis                   ,
        [AUTO].Combustible              ,
        [AUTO].Estilo                   ,
        [AUTO].Kilometros               ,
        [AUTO].Localizacion             ,
        [AUTO].Marca                    ,
        [AUTO].Motor                    ,
        [AUTO].Precio                   ,
        [AUTO].Tipo                     ,
        [AUTO].Transmision              ,
        [VENDEDOR].Nombre               ,
        [CONTACTO].Contacto             ,
        [Tipo].Tipo
	FROM [PUBLICACION] INNER JOIN [PAGINA] 
	ON [PUBLICACION].IdPagina = [PAGINA].IdPagina INNER JOIN [AUTO]
	ON [PUBLICACION].IdAuto = [AUTO].IdAuto INNER JOIN [VENDEDOR]
	ON [VENDEDOR].IdVendedor = [AUTO].IdVendedor INNER JOIN [CONTACTOxVENDEDOR]
	ON [VENDEDOR].IdVendedor = [CONTACTOxVENDEDOR].IdVendedor INNER JOIN [CONTACTO]
	ON [CONTACTO].IdContacto = [CONTACTOxVENDEDOR].IdContacto_1 INNER JOIN [Tipo]
	ON [CONTACTO].IdTipo = [Tipo].IdTipo
	WHERE [PUBLICACION].FechaScraping = '{timestamp}'
    ;
    """
#-----------------------------------------------------------------------

#endregion Select Query Functions

#region Inserts Query Functions
#-----------------------------------------------------------------------
def query_Insert_Into_tabla_sd(publicacion:Classes.Publicacion,id_con:int,identificador:str):
    return f"""
        DECLARE @check int;

        INSERT INTO [dbo].[tabla_sd] (
             [id_con]
            ,[identificador]
            ,[id_ofe]
            ,[titulo]
            ,[pagina]
            ,[fecha_publicacion]
            ,[url]
            ,[modelo]
            ,[ubicacion]
            ,[dir_exacta]
            ,[geolocalizacion]
            ,[coordenadas]
            ,[precio_total]
            ,[precio_m2_construccion]
            ,[precio_m2_terreno]
            ,[moneda]
            ,[area_terreno]
            ,[area_construccion]
            ,[cant_habitaciones]
            ,[cant_banos]
            ,[parking]
            ,[detalles]
            ,[nombre_vendedor]
            ,[contacto_vendedor] )
        VALUES (
             {id_con}
            ,'{identificador}'
            ,{publicacion.Inmueble.Id} 
            ,'{publicacion.Titulo}'
            ,'{publicacion.Pagina}'
            ,{publicacion.FechaPublicacion}
            ,'{publicacion.Url}'
            ,'{publicacion.Inmueble.Modelo}'
            ,'{publicacion.Inmueble.Ubicacion}'
            ,'{publicacion.Inmueble.DireccionExacta}'
            ,'{publicacion.Inmueble.Geolocalizacion}'
            ,'{publicacion.Inmueble.Coordenadas}'
            ,{publicacion.Inmueble.PrecioTotal}
            ,{publicacion.Inmueble.PrecioPorM2Construccion}
            ,{publicacion.Inmueble.PrecioPorM2Terreno}
            ,'{publicacion.Inmueble.Moneda}'
            ,{publicacion.Inmueble.AreaTerreno}
            ,{publicacion.Inmueble.AreaConstruccion}
            ,{publicacion.Inmueble.CantidadHabitaciones}
            ,{publicacion.Inmueble.CantidadBanos}
            ,'{publicacion.Inmueble.Parking}'
            ,'{publicacion.Inmueble.Detalles}'
            ,'{publicacion.Inmueble.Vendedor.Nombre}'
            ,'{publicacion.Inmueble.Vendedor.Contacto[0].Dato}'
            );
        
        if(@@ROWCOUNT>0)
            SET @check=1
        
        SELECT @check,Scope_Identity();
        """
#-----------------------------------------------------------------------
def query_Insert_Into_tabla_sc(id_main:int,identificador:str,TipoCarga:int,web_origen:str,globalid:int):
    return f"""
        DECLARE @check int;
        DECLARE @PROCESS_ID int;
        INSERT INTO [dbo].[tabla_sc] (
             [id_main]
            ,[identificador]
            ,[ECarga]
            ,[TipoCarga]
            ,[web_origen]
            ,[globalid] )
        VALUES (
             {id_main}
            ,'{identificador}'
            ,{0}
            ,{TipoCarga}
            ,'{web_origen}'
            ,{globalid}
            );
        
        if(@@ROWCOUNT>0)
            SET @check=1
        SET @check=0
        SET @PROCESS_ID= SCOPE_IDENTITY()
        SELECT @check AS CHECK_ROW,@PROCESS_ID AS PROCESS_ID
        """
#-----------------------------------------------------------------------
def query_Insert_Into_Scrapping_Main(id_emp:int,empresa:str,id_pai:int,país:str,tabla_sc:str,tabla_sd:str,ruta_raiz:str):
    return f"""
        DECLARE @check int;

        INSERT INTO [dbo].[Scrapping_Main] (
             [id_emp]
            ,[empresa]
            ,[id_pai]
            ,[país]
            ,[tabla_sc]
            ,[tabla_sd]
            ,[ruta_raiz] )
        VALUES (
             {id_emp}
            ,'{empresa}'
            ,{id_pai}
            ,'{país}'
            ,'{tabla_sc}'
            ,'{tabla_sd}'
            ,'{ruta_raiz}'
            );
        
        if(@@ROWCOUNT>0)
            SET @check=1
        
        SELECT @check,Scope_Identity();
        """
#-----------------------------------------------------------------------
def query_EXE_insertPublicacion(publicacion:Classes.Publicacion):
    return f"""EXECUTE [dbo].[insertPublicacion]
            @Nombre           = '{publicacion.Auto.Vendedor.Nombre}'    ,
            @Apellido         = '{publicacion.Auto.Vendedor.Appellido}' ,
            @Anno             = '{publicacion.Auto.Anno}'               ,
            @Kilometros       =  {publicacion.Auto.Kilometros}          ,
            @Tipo             = '{publicacion.Auto.Tipo}'               ,
            @Transmision      = '{publicacion.Auto.Transmision}'        ,
            @Combustible      = '{publicacion.Auto.Combustible}'        ,
            @Localizacion     = '{publicacion.Auto.Localizacion}'       ,
            @Marca            = '{publicacion.Auto.Marca}'              ,
            @Modelo           = '{publicacion.Auto.Tipo}'               ,
            @Precio           =  {publicacion.Auto.Precio}              ,
            @Motor            = '{publicacion.Auto.Motor}'              ,
            @Estilo           = '{publicacion.Auto.Estilo}'             ,
            @Asientos         =  {publicacion.Auto.Asientos}            ,
            @Chasis           = '{publicacion.Auto.Chasis}'             ,
            @NombrePagina     = '{publicacion.Pagina}'                  ,
            @FechaPublicacion = '{publicacion.FechaPublicacion}'        ,
            @FechaScraping    = '{publicacion.FechaScraping}'           ,
            @UrlPublicacion   = '{publicacion.Url}'                     
           """
#-----------------------------------------------------------------------
def query_EXE_insertContacto(contacto:Classes.Contacto):
    return f"""EXECUTE [dbo].[insertContacto]
            @Contacto = '{contacto.Dato}' ,
            @Tipo     = '{contacto.Tipo}' 
           """
#-----------------------------------------------------------------------
def query_EXE_insertContactoXVendedor(IdVendedor:int,IdContacto:int):
    return f"""EXECUTE [dbo].[insertContactoXVendedor]
            @IdVendedor = {IdVendedor} ,
            @IdContacto = {IdContacto}
           """
#-----------------------------------------------------------------------
#endregion Inserts Query Functions

#endregion Query Functions
