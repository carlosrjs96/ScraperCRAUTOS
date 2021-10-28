import Util  
import Classes
#import datetime
from datetime import datetime
import SQL
from os import system

Meses = {
    "Enero"      : 'January'   , 
    "Febrero"    : 'February'  , 
    "Marzo"      : 'March'     , 
    "Abril"      : 'April'     , 
    "Mayo"       : 'May'       , 
    "Junio"      : 'June'      , 
    "Julio"      : 'July'      , 
    "Agosto"     : 'August'    , 
    "Septiembre" : 'September' , 
    "Setiembre" : 'September' , 
    "Octubre"    : 'October'   , 
    "Noviembre"  : 'November'  , 
    "Diciembre"  : 'December'
}

#-----------------------------------------------------------------------
def scrapPage(auto):
    try:                    
        # Config a Web Driver
        driver = Util.selenium_WebDriver_config()
        url = "https://crautos.com/autosusados/"
        driver.get(url)
        (driver.page_source).encode('utf-8')
        Util.staticDelay(10,11)

        # Apply Filter to search Auto
        apply_Filters(auto,driver)

        # Get all links of autos y in the search
        urls = get_all_Links(driver)
        print("Total Urls: "+str(len(urls)))

        timestamp = Util.get_Timestamp()
        print(F'TIMESTAMP: {timestamp}')

        # Do scraping for each url founded
        results = []
        for url in urls:
            driver.get(url)
            Util.staticDelay(2,3)
            Publicacion : Classes.Publicacion = scrapAuto(auto.Marca,driver,timestamp)
            results.append(Publicacion.to_JSON())
            insert_DB(publicacion = Publicacion)

    finally:
        driver.quit()

    return timestamp#results,timestamp
#-----------------------------------------------------------------------
def apply_Filters(auto,driver):
    panel = driver.find_element_by_xpath('//div[@class="row padding-10"]//div[@class = "col-xs-12 col-sm-12 col-md-8 col-md-offset-2 searchform"]')
    form  = panel.find_element_by_xpath('.//form[@class="ajax_form"]')
    
    # Marca
    if auto.Marca        != None:
        #print("MARCA<<<<<<<<<<<<<<<<<<<<<")
        select = form.find_element_by_xpath('.//select[@name="brand"]')
        for option in select.find_elements_by_tag_name('option'):
            #print(option.text)
            if option.text == str(auto.Marca).strip():
                #print("X")
                option.click() # select() in earlier versions of webdriver
                #print("Click")
                break
        Util.staticDelay(1,2)
    
    # Marca
    if auto.Tipo        != None:
        input = form.find_element_by_xpath('.//input[@name="modelstr"]')
        input.send_keys(str(auto.Tipo).strip())

    # Estilo
    if auto.Estilo       != None:
        #print("ESTILO<<<<<<<<<<<<<<<<<<<<<")
        select = form.find_element_by_xpath('.//select[@name="style"]')
        for option in select.find_elements_by_tag_name('option'):
            #print(option.text)
            if option.text == str(auto.Estilo).strip():
                #print("X")
                option.click() # select() in earlier versions of webdriver
                #print("Click")
                break
        Util.staticDelay(1,2)
    
    # Combustible
    if auto.Combustible  != None:
        #print("COMBUSTIBLE<<<<<<<<<<<<<<<<<<<<<")
        select = form.find_element_by_xpath('.//select[@name="fuel"]')
        for option in select.find_elements_by_tag_name('option'):
            #print(option.text)
            if option.text == str(auto.Combustible).strip():
                #print("X")
                option.click() # select() in earlier versions of webdriver
                #print("Click")
                break
        Util.staticDelay(1,2)
    
    # Transmision
    if auto.Transmision  != None:
        #print("TRANSMISION<<<<<<<<<<<<<<<<<<<<<")
        select = form.find_element_by_xpath('.//select[@name="trans"]')
        for option in select.find_elements_by_tag_name('option'):
            #print(option.text)
            if option.text == str(auto.Transmision).strip():
                #print("X")
                option.click() # select() in earlier versions of webdriver
                #print("Click")
                break
        Util.staticDelay(1,2)
    
    # Localizacion
    if auto.Localizacion != None:
        #print("LOCALIZACION<<<<<<<<<<<<<<<<<<<<<")
        select = form.find_element_by_xpath('.//select[@name="province"]')
        for option in select.find_elements_by_tag_name('option'):
            #print(option.text)
            if option.text == str(auto.Localizacion).strip():
                #print("X")
                option.click() # select() in earlier versions of webdriver
                #print("Click")
                break
        Util.staticDelay(1,2)

    # Chasis
    if auto.Chasis       != None:
        select = form.find_element_by_xpath('.//select[@name="doors"]')
        for option in select.find_elements_by_tag_name('option'):
            #print(option.text)
            if option.text == str(auto.Chasis).strip():
                #print("X")
                option.click() # select() in earlier versions of webdriver
                #print("Click")
                break
        Util.staticDelay(1,2)

    # Anno
    if auto.Anno         != None:
        # Anno Desde
        if auto.Anno[0]!= None:
            #print("AÑO<<<<<<<<<<<<<<<<<<<<<")
            select = form.find_element_by_xpath('.//select[@name="yearfrom"]')
            for option in select.find_elements_by_tag_name('option'):
                #print(option.text)
                if option.text == str(auto.Anno[0]):
                    #print("X")
                    option.click() # select() in earlier versions of webdriver
                    #print("Click")
                    break
            Util.staticDelay(1,2)

        # Anno Hasta
        if auto.Anno[1]!= None:
            select = form.find_element_by_xpath('.//select[@name="yearto"]')
            for option in select.find_elements_by_tag_name('option'):
                #print(option.text)
                if option.text == str(auto.Anno[1]):
                    #print("X")
                    option.click() # select() in earlier versions of webdriver
                    #print("Click")
                    break
            Util.staticDelay(1,2)
    
    # Precio
    if auto.Precio != None:
        # Precio Desde
        if auto.Precio[0]       != None:
            #print("PRECIO<<<<<<<<<<<<<<<<<<<<<")
            select = form.find_element_by_xpath('.//select[@name="pricefrom"]')
            for option in select.find_elements_by_tag_name('option'):
                #print(option.text)
                if option.text == str(auto.Precio[0]).strip():
                    #print("X")
                    option.click() # select() in earlier versions of webdriver
                    #print("Click")
                    break
            Util.staticDelay(1,2)

        # Precio Hasta
        if auto.Precio[1]       != None:
            select = form.find_element_by_xpath('.//select[@name="priceto"]')
            for option in select.find_elements_by_tag_name('option'):
                #print(option.text)
                if option.text == str(auto.Precio[1]).strip():
                    #print("X")
                    option.click() # select() in earlier versions of webdriver
                    #print("Click")
                    break
            Util.staticDelay(1,2)

    # Boton Buscar
    btnBuscar = form.find_element_by_xpath('.//input[@class="btn btn-sm btn-success"]') # //*[@id="sf"]/tbody/tr/td/div/form/div[2]/table/tbody/tr[8]/td/input[3]
    btnBuscar.click()
    print(">>>>>>>>>> BUSCANDO <<<<<<<<<<<<")
    Util.staticDelay(5,6)

    """
    if auto.Kilometros   != None:
        select = form.find_element_by_xpath('.//select[@name="brand"]')
        for option in select.find_elements_by_tag_name('option'):
            print(option.text)
            if option.text == str(auto.Marca).strip():
                print("X")
                option.click() # select() in earlier versions of webdriver
                print("Click")
                break
        Util.staticDelay(1,2)   
    if auto.Tipo         != None:
        select = form.find_element_by_xpath('.//select[@name="style"]')
        for option in select.find_elements_by_tag_name('option'):
            print(option.text)
            if option.text == str(auto.Tipo).strip():
                print("X")
                option.click() # select() in earlier versions of webdriver
                print("Click")
                break
        Util.staticDelay(1,2)   
    if auto.Motor        != None:
        select = form.find_element_by_xpath('.//select[@name="brand"]')
        for option in select.find_elements_by_tag_name('option'):
            print(option.text)
            if option.text == str(auto.Marca).strip():
                print("X")
                option.click() # select() in earlier versions of webdriver
                print("Click")
                break
        Util.staticDelay(1,2)
    if auto.Asientos     != None:
        select = form.find_element_by_xpath('.//select[@name="brand"]')
        for option in select.find_elements_by_tag_name('option'):
            print(option.text)
            if option.text == str(auto.Marca).strip():
                print("X")
                option.click() # select() in earlier versions of webdriver
                print("Click")
                break
        Util.staticDelay(1,2)
    """
#-----------------------------------------------------------------------
def click_Right_Btn(driver):
    try:
        pagination = driver.find_element_by_xpath('//div[@class="col-xs-12 pagination_container"]')
        RightBtn = pagination.find_element_by_xpath('.//ul[contains(@class, "pagination")]//li//a//i[@class="fa fa-angle-right"]')
        RightBtn.click()
        print("Right Click")
        return True
    except:
        return False
#-----------------------------------------------------------------------
def get_all_Links(driver):
    state = True
    urls = []
    while(state):    
        form = driver.find_element_by_xpath('//form[@name="form"]')
        hrefs = form.find_elements_by_xpath('//div[contains(@class,"inventory")]//a[@class="inventory"]')
        print("hrefs size: "+str(len(hrefs)))
        urls = urls + [href.get_attribute('href') for href in hrefs]
        state = click_Right_Btn(driver)
        Util.staticDelay(1,2)
    return urls
#-----------------------------------------------------------------------
def scrapAuto(Marca,driver,timestamp):
    # >>> DATOS PUBLICACION <<<
    publicacion = Classes.Publicacion()
    publicacion.Pagina         = Classes.PagesEnum.CRAUTOS.name
    publicacion.FechaScraping  = timestamp
    publicacion.Url            = driver.current_url

    # >>> DATOS AUTO <<<

    # Get table with Selenium elements /html/body/section[1]/div/div/div[1]/div[1]/table/tbody/tr[5]/td/div[1]/table/tbody/tr[3]/td[1]/b
    before_XPath = '//table[@class="technical mytext2"]/tbody/tr'
    table = Util.getDymanicContentBodyTable(driver, before_XPath, -1, 0)

    # Get Rows Size
    num_rows = len(table)
    #print("Rows: " + repr(num_rows))

    tbody = []
    for row in table: 
        tbody.append([cell.text for cell in row ])
    #print(tbody)

    data = {}
    for pair in tbody:
        if len(pair) == 2:
            data[ pair[0].strip() ] = pair[1].strip()

    dateString = data['Fecha de ingreso'] #"Monday, July 16, 2018 20:01:56"
    for mes in Meses:
        if mes.upper() in dateString.upper():
            dateString = dateString.replace(mes,Meses[mes])
            break
    #print(dateString)
    dateFormatter = "%d de %B del %Y"
    publicacion.FechaPublicacion  = datetime.strptime(dateString,dateFormatter).strftime('%m/%d/%Y')
    publicacion.Auto.Marca        = Marca
    publicacion.Auto.Asientos        = -1
    publicacion.Auto.Motor        = data['Cilindrada'] if data['Cilindrada'].strip() != 'ND' else None
    publicacion.Auto.Estilo       = data['Estilo'] if data['Estilo'].strip() != 'ND' else None
    publicacion.Auto.Combustible  = data['Combustible'] if data['Combustible'].strip() != 'ND' else None
    publicacion.Auto.Transmision  = data['Transmisión'] if data['Transmisión'].strip() != 'ND' else None
    Kilometraje = data['Kilometraje']
    if "," in Kilometraje:
        Kilometraje =  Kilometraje.replace(',','')
    if "km" in Kilometraje:
        Kilometraje =  Kilometraje.replace('km','')
    publicacion.Auto.Kilometros   = int(Kilometraje.strip()) if Kilometraje.strip() != 'ND' else None
    publicacion.Auto.Chasis       = data['# de puertas'] if data['# de puertas'].strip() != 'ND' else None
    publicacion.Auto.Localizacion = data['Provincia'] if data['Provincia'].strip() != 'ND' else None

    cardetailtitle = driver.find_element_by_xpath('//div[@class="margin-bottom-10 clearfix cardetailtitle"]//div[@class="row"]')
    
    # Tipo
    tipo = cardetailtitle.find_element_by_xpath('.//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12"]//h2') 
    #print(tipo.text)
    tipo = tipo.text
    tipo = tipo.replace("\n"," ")#rstrip()
    tipo = tipo.split(" ")
    tipo = tipo[:-1]
    tipo = " ".join(tipo)
    #print(tipo)
    publicacion.Auto.Tipo = tipo
    
    # Anno
    anno = cardetailtitle.find_element_by_xpath('.//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12"]//h2')
    anno = anno.text
    anno = anno.replace("\n"," ")#rstrip()
    anno = anno.split(" ")
    anno = anno[-1]  
    publicacion.Auto.Anno = anno

    # Precio
    precio = cardetailtitle.find_element_by_xpath('.//div[@class="col-lg-4 col-md-4 col-sm-4 text-right"]//h2')
    precio = precio.text
    precio = precio.replace(',','')
    precio = precio.replace('¢','')
    publicacion.Auto.Precio = int(precio)

    # >>> DATOS VENDEDOR <<<

    # Get table with Selenium elements 
    before_XPath = '//table[@class="table-responsive mytext1"]//table[@class="table-responsive"]/tbody/tr'
    table = Util.getDymanicContentBodyTable(driver, before_XPath, 0, 0)
        
    tbody = []
    for row in table: 
        tbody.append([cell.text for cell in row ])
    #print(tbody)

    dataVendor = {}
    for pair in tbody:
        if len(pair) == 2:
            dataVendor[ pair[0].strip() ] = pair[1].strip()
    #print(dataVendor)
    publicacion.Auto.Vendedor.Nombre   = dataVendor['Nombre']
    contactosType = ['Teléfono','Telefono','Whatsapp']
    for type in contactosType:
        if type in dataVendor:
            contact = Classes.Contacto()
            contact.Tipo = "TELEFONO"
            contact.Dato = dataVendor[type]
            publicacion.Auto.Vendedor.Contacto.append(contact)
            break
    
    return publicacion
#-----------------------------------------------------------------------
def insert_DB(publicacion:Classes.Publicacion):
    #------------------------------------------------------------------
    query  = SQL.query_EXE_insertPublicacion(publicacion=publicacion)
    print(query)
    SQL.DBConnection.execute_query(query,state=False)

    query  = SQL.query_IDENT_CURRENT(table="VENDEDOR")
    result = SQL.DBConnection.execute_query(query,state=True)
    IdVendedor = result[0][0] 
    print(f'IdVendedor: {IdVendedor}')
    SQL.print_Result(result)
    for contacto in publicacion.Auto.Vendedor.Contacto:
        #------------------------------------------------------------------
        query  = SQL.query_EXE_insertContacto(contacto=contacto)
        #print(query)
        SQL.DBConnection.execute_query(query,state=False)

        query  = SQL.query_IDENT_CURRENT(table="CONTACTO")
        result = SQL.DBConnection.execute_query(query,state=True)
        IdContacto = result[0][0] 
        print(f'IdContacto: {IdContacto}')
        SQL.print_Result(result)
        #------------------------------------------------------------------
        query  = SQL.query_EXE_insertContactoXVendedor(IdVendedor,IdContacto)
        #print(query)
        SQL.DBConnection.execute_query(query,state=False)

        query  = SQL.query_IDENT_CURRENT(table="CONTACTOxVENDEDOR")
        result = SQL.DBConnection.execute_query(query,state=True)
        IdContacto = result[0][0] 
        print(f'IdContactoXIdVendedor: {IdContacto}')
        SQL.print_Result(result)
        #------------------------------------------------------------------
#-----------------------------------------------------------------------
def createExcelFile(path:str)->str:
    workbook_name = path + "/Datos.xlsx"
    Util.createExcel(
        workbook_name = workbook_name, 
        title         = 'Resultados Autos'   , 
        headers       = [
                            'FechaPublicacion'    ,
                            'FechaScraping'       ,
                            'Pagina'              ,
                            'Url'                 ,
                            'Anno'                    ,
                            'Asientos'            ,
                            'Chasis'              ,
                            'Combustible'         ,
                            'Estilo'               ,
                            'Kilometros'          ,
                            'Localizacion'        ,
                            'Marca'               ,
                            'Motor'                ,
                            'Precio'              ,
                            'Tipo'                ,
                            'Transmision'         ,
                            'Vendedor Nombre'     ,
                            'Contacto Dato'       , 
                            'Contacto Tipo'
                        ]
    )
    return workbook_name
#-----------------------------------------------------------------------
def appendRowToExcelFile(workbook_name:str,publicacion:Classes.Publicacion):
    Util.appendRowToExcel( 
                    workbook_name  = workbook_name,
                    row = [
                        publicacion.FechaPublicacion               ,
                        publicacion.FechaScraping                  ,
                        publicacion.Pagina                         ,
                        publicacion.Url                            ,
                        publicacion.Auto.Anno                      ,
                        publicacion.Auto.Asientos                  ,
                        publicacion.Auto.Chasis                    ,
                        publicacion.Auto.Combustible               ,
                        publicacion.Auto.Estilo                    ,
                        publicacion.Auto.Kilometros                ,
                        publicacion.Auto.Localizacion              ,
                        publicacion.Auto.Marca                     ,
                        publicacion.Auto.Motor                     ,
                        publicacion.Auto.Precio                    ,
                        publicacion.Auto.Tipo                      ,
                        publicacion.Auto.Transmision               ,
                        publicacion.Auto.Vendedor.Nombre           ,
                        publicacion.Auto.Vendedor.Contacto[0].Dato , 
                        publicacion.Auto.Vendedor.Contacto[0].Tipo
                        
                    ]
                )
#-----------------------------------------------------------------------
def get_Data_by_timestamp(timestamp:str):  
    query  = SQL.query_Select_All_By_Timestamp(timestamp=timestamp)
    
    result = SQL.DBConnection.execute_query(query,state=True)
    SQL.print_Result(result) 

    # Create directories
    path = f'Resultados de busqueda/{timestamp.replace("/","-").replace(":",";")}'
    Util.create_Directory(path=path)
    
    # create excel file
    workbook_name = createExcelFile(path)

    for row in result:
        publicacion = Classes.Publicacion()
        publicacion.FechaPublicacion               = row[0]
        publicacion.FechaScraping                  = row[1]
        publicacion.Pagina                         = row[2]
        publicacion.Url                            = row[3]
        publicacion.Auto.Anno                      = row[4]
        publicacion.Auto.Asientos                  = row[5]
        publicacion.Auto.Chasis                    = row[6]
        publicacion.Auto.Combustible               = row[7]
        publicacion.Auto.Estilo                    = row[8]
        publicacion.Auto.Kilometros                = row[9]
        publicacion.Auto.Localizacion              = row[10]
        publicacion.Auto.Marca                     = row[11]
        publicacion.Auto.Motor                     = row[12]
        publicacion.Auto.Precio                    = row[13]
        publicacion.Auto.Tipo                      = row[14]
        publicacion.Auto.Transmision               = row[15]
        publicacion.Auto.Vendedor.Nombre           = row[16]
        contacto = Classes.Contacto()
        contacto.Dato = row[17]
        contacto.Tipo = row[18]
        publicacion.Auto.Vendedor.Contacto.append(contacto)
        appendRowToExcelFile(
            workbook_name=workbook_name, 
            publicacion=publicacion
            )
#-----------------------------------------------------------------------

if __name__ == '__main__':
    while True:
        print(f"\
        Presiona 1 para obtener los resultados en formato .xlsx.\n\
        Presiona 2 para ayuda.\n\
        Presiona 3 para salir.")
        opcion = int(input("    Ingrese el número de la opción requerida: "))
        if opcion==1:
            system("cls")
            timestamp = input("    Ingrese el timestamp(YYYY-MM-DD hh:mm): ")
            get_Data_by_timestamp(timestamp)
            print(f"    Realizado con éxito.")
        elif opcion==2:
            system("cls")
            print(f"\n    AYUDA")
            print(f"\n    1.La opción 1 requiere ingresar la fecha del Scraper realizado previamente y dichos resultados se verán reflejado en un documento .xlsx")
            print(f"    2.Para realizar el scraper de los autos se hará meditante la aplicación Postman\n")  
        elif opcion==3:
            print(f"    Gracias por utilizar nuestro programa.\n")
            break
            
        elif opcion!=1 and opcion!=2 and opcion!=3:
            system("cls")
            print("    No tenemos esa opción\n")
    
    