from flask import Flask, jsonify
from flask_restful import request
import CRAutosScraper
import traceback
import json
import Classes
import Util
#region Global Methods and Variables
#-----------------------------------------------------------------------
app = Flask(__name__)

# Load Json Config
with open('Config.json', 'r') as j:
    json_Config = json.load(j)

# Global Settings
port = json_Config['port']
host = json_Config['host']
#-----------------------------------------------------------------------
#endregion Global Methods and Variables

#region Routes Methods
#-----------------------------------------------------------------------
# GET route to response json request
@app.route('/crautos') # Route Decorator   localhost:5001/crautos?AnnoDesde=2001
def CRAutos():
    # Get json query
    AnnoDesde    = request.args.get('AnnoDesde'   , default = None , type = str)
    AnnoHasta    = request.args.get('AnnoHasta'   , default = None , type = str)
    Kilometros   = request.args.get('Kilometros'  , default = None , type = str)
    Tipo         = request.args.get('Tipo'        , default = None , type = str)
    Transmision  = request.args.get('Transmision' , default = None , type = str)
    Combustible  = request.args.get('Combustible' , default = None , type = str)
    Localizacion = request.args.get('Localizacion', default = None , type = str)
    Marca        = request.args.get('Marca'       , default = None , type = str)
    PrecioDesde  = request.args.get('PrecioDesde' , default = None , type = str)
    PrecioHasta  = request.args.get('PrecioHasta' , default = None , type = str)
    Motor        = request.args.get('Motor'       , default = None , type = str)
    Estilo       = request.args.get('Estilo'      , default = None , type = str)
    Asientos     = request.args.get('Asientos'    , default = None , type = str)
    Chasis       = request.args.get('Chasis'      , default = None , type = str)
    # Create new Auto
    auto = Classes.Auto()

    # Assigne data from json to object
    auto.Anno         = [AnnoDesde,AnnoHasta]        
    auto.Kilometros   = Kilometros  
    auto.Tipo         = Tipo        
    auto.Transmision  = Transmision 
    auto.Combustible  = Combustible 
    auto.Localizacion = Localizacion
    auto.Marca        = Marca       
    auto.Precio       = [PrecioDesde,PrecioHasta]      
    auto.Motor        = Motor       
    auto.Estilo       = Estilo      
    auto.Asientos     = Asientos    
    auto.Chasis       = Chasis      
    
    
    try:
        timestamp = CRAutosScraper.scrapPage(auto)                        # Scrap Race and return json Track

    except Exception as err:
        return {"Error": str(err), "Traceback": traceback.format_exc()},400 # Error and TraceBack
    timestamp= Util.get_Timestamp()
    return {"timestamp":timestamp}
#-----------------------------------------------------------------------
#endregion Routes Methods

if __name__ == '__main__':
    # run app in debug mode on port
    # The default value for host is localhost or 127.0.0.1
    app.run(host=host, debug=True, port=port, threaded=True)