import Util  
import Classes
#import datetime
from datetime import datetime
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
        
        # Do scraping for each url founded
        results = []
        for url in urls:
            driver.get(url)
            Util.staticDelay(2,3)
            results.append(scrapAuto(auto.Marca,driver))
        
    finally:
        driver.quit()

    return results
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
def scrapAuto(Marca,driver):
    # >>> DATOS PUBLICACION <<<
    publicacion = Classes.Publicacion()
    publicacion.Pagina         = Classes.PagesEnum.CRAUTOS.value
    publicacion.FechaScraping  = str(datetime.now().strftime('%d/%m/%Y'))
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
    publicacion.FechaPublicacion  = datetime.strptime(dateString,dateFormatter).strftime('%d/%m/%Y')
    publicacion.Auto.Marca        = Marca
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
    contactos=[]
    for type in contactosType:
        if type in dataVendor:
            contact = Classes.Contacto()
            contact.Tipo = type
            contact.Dato = dataVendor[type]
            publicacion.Auto.Vendedor.Contacto.append(contact)

    #print(publicacion.to_JSON())
    return publicacion.to_JSON()
#-----------------------------------------------------------------------
if __name__ == '__main__':
    #auto = Classes.Auto()
    #auto.Marca        = "BMW"
    #auto.Tipo         = "318 IS"
    #auto.Estilo       = "Sedán"
    #auto.Combustible  = "Gasolina"
    
    #auto.Transmision  = "Automática"
    #auto.Localizacion = "San José"
    #auto.Chasis       = "4 o más"
    #auto.Anno         = ["2000","2020"]
    #auto.Precio       = [0,0]
    #scrapPage(auto)
    print(str(datetime.datetime.now().strftime('%d/%m/%Y')))
    