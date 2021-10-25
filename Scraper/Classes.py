import enum
import json
#-------------------------------------------------------------------
# Using enum class create enumerations
class PagesEnum(enum.Enum):
    CRAUTOS    = 'www.crautos.com'                # 
#-------------------------------------------------------------------
class Publicacion:
    # Contructor 
    def __init__(self):
        self.Auto             : Auto = Auto()
        self.Pagina           : str = None
        self.FechaPublicacion : str = None
        self.FechaScraping    : str = None  
        self.Url              : str = None

    # Methods
    def toString(self): #Print Atributtes
        result = ""
        result += "\n /////////////////////////////////////////////////////" 
        result += "\n Auto             : " + self.Auto                 
        result += "\n Pagina           : " + self.Pagina           
        result += "\n FechaPublicacion : " + self.FechaPublicacion     
        result += "\n FechaScraping    : " + self.FechaScraping    
        result += "\n Url              : " + self.Url                     
        result += "\n /////////////////////////////////////////////////////"
        return result
        
    # Convert to JSON String
    def to_JSON(self):
        json = {
            'Auto'             : self.Auto.to_JSON()   , 
            'Pagina'           : self.Pagina           ,
            'FechaPublicacion' : self.FechaPublicacion ,
            'FechaScraping'    : self.FechaScraping    , 
            'Url'              : self.Url                    
        }
        return json 
#-------------------------------------------------------------------
class Auto:
    # Contructor 
    def __init__(self):
        self.Vendedor     : Vendedor = Vendedor() # Vendedor
        self.Anno         : str = None       # str
        self.Kilometros   : int = None       # int
        self.Tipo         : str = None       # str
        self.Transmision  : str = None       # str
        self.Combustible  : str = None       # str
        self.Localizacion : str = None       # str
        self.Marca        : str = None       # str
        self.Precio       : int = None       # int
        self.Motor        : str = None       # str
        self.Estilo       : str = None       # str
        self.Asientos     : int = None       # int
        self.Chasis       : str = None       # str
        
    # Methods
    def toString(self): #Print Atributtes
        result = ""
        result += "\n   /////////////////////////////////////////////////////" 
        result += "\n   Vendedor     : " + self.Vendedor     
        result += "\n   Anno         : " + str(self.Anno)         
        result += "\n   Kilometros   : " + str(self.Kilometros)   
        result += "\n   Tipo         : " + self.Tipo         
        result += "\n   Transmision  : " + self.Transmision  
        result += "\n   Combustible  : " + self.Combustible  
        result += "\n   Localizacion : " + self.Localizacion 
        result += "\n   Marca        : " + self.Marca        
        result += "\n   Precio       : " + str(self.Precio)       
        result += "\n   Motor        : " + self.Motor        
        result += "\n   Estilo       : " + self.Estilo       
        result += "\n   Asientos     : " + str(self.Asientos)     
        result += "\n   Chasis       : " + self.Chasis        
        result += "\n   /////////////////////////////////////////////////////"
        return result
    # Convert to JSON String
    def to_JSON(self):
        json = {
            'Vendedor'    : self.Vendedor.to_JSON() , 
            'Anno'        : self.Anno               , 
            'Kilometros'  : self.Kilometros         , 
            'Tipo'        : self.Tipo               , 
            'Transmision' : self.Transmision        , 
            'Combustible' : self.Combustible        , 
            'Localizacion': self.Localizacion       , 
            'Marca'       : self.Marca              , 
            'Precio'      : self.Precio             , 
            'Motor'       : self.Motor              , 
            'Estilo'      : self.Estilo             , 
            'Asientos'    : self.Asientos           , 
            'Chasis'      : self.Chasis             , 
        }
        return json 
#-------------------------------------------------------------------
class Vendedor:
    # Contructor 
    def __init__(self):
        self.Nombre    : str = None 
        self.Appellido : str = None 
        self.Contacto  : list[Contacto] = [] 
        
    # Methods
    def toString(self): #Print Atributtes
        result = ""
        result += "\n       /////////////////////////////////////////////////////" 
        result += "\n       Nombre       : " + self.Vendedor   
        result += "\n       Appellido    : " + self.Vendedor     
        for x in range(len(self.Contacto)):
            result += self.Contacto[x].toString()       
        result += "\n       /////////////////////////////////////////////////////"
        return result
    # Convert to JSON String
    def to_JSON(self):
        json = {
            'Nombre'    : self.Nombre    , 
            'Appellido' : self.Appellido ,
            'Contacto'  : []     
        }

        for contacto in self.Contacto:
            json['Contacto'].append(contacto.to_JSON())

        return json 
#-------------------------------------------------------------------
class Contacto:
    # Contructor 
    def __init__(self):
        self.Dato : str = None
        self.Tipo : str = None  
        
    # Methods
    def toString(self): #Print Atributtes
        result = ""
        result += "\n           /////////////////////////////////////////////////////" 
        result += "\n           Dato : " + self.Dato     
        result += "\n           Tipo : " + self.Tipo         
        result += "\n           /////////////////////////////////////////////////////"
        return result

    # Convert to JSON String
    def to_JSON(self):
        json = {
            'Dato' : self.Dato , 
            'Tipo' : self.Tipo      
        }
        return json 
