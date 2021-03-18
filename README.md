# proyecto-analisis-de-datos-JEGY
Pulso Político en 20 ciudades de Ecuador
  Se implementó la recepción de datos con respecto al tema del pulso político en ciudades de Ecuador, con respecto a la opinión de 
  los usuaios acerca de los candidatos a presidencia y demás cargos gubernamentales, de esta forma se puede tener un concomiento más 
  afondo sobre el pensamiento de los ciudadanos ante este tema.
  <br/>
  La segunda parte del script "tweets ciudades.py" para la recolección de datos tanto con respecto a filtrados de búsqueda y geolocalización,
  esto se lo puede desarrollar también incorporando lo que es la ubicación de la ciduad en la que se requiere recopilar los datos.
  <br/>
  Como punto siguiente se tiene los scripts  6 y 8 que permiten enviar los datos entre las bases de couch y mongo, de esta manera se incorpora la
  la base en couch para su posterior envío a ElasticSearch
  <br/>
  Se hizo uso de logstash para enviar los datos de couch hacia Elasticsearch, esto se lo hizo por medio del input con el nombre "couch.conf", 
  en donde se envía la id de la nube de elasticsearch y así registrar en los índices.
  <br/>
  Los tweets tiene una estructura amplia de la cual nos interesa los hashtags, menciones, el texto y el lugar (país, ciudad).  <br/>
  <br/>
  Para usar elasticsearch primero, se procedió a crear cada indice y para cada indice se realizó la configuración de mapping detallada en el archivo "mapping indices elasticseach" donde se definen los formatos de fecha y geolocalización para los tweets.<br/>
  <br/>
  Finalmente en kibana se realizaron las visualizaciones, ya que kibana tiene el benfecio de conectarse con elasticsearch, es aquí donde se realizaron visualizaciones concernientes a los datos almacenados.
  <br/>
Videos Juegos por países
<br/>
Para el análisis de los videos juegos en los países se buscó bases de datos públicas de las siguientes fuentes que son:
Kaggle.com
<br/>
Tableu Public Resource
<br/>
UNdata.com
<br/>
Las bases que contenían los datos que más se asemejaban a la petición del proyecto se recopilaron alrededor de 16638 datos los cuales se dividen en 3 bases. 
<br/>
Las principales datos se procesaron mediante Exel para limpiar datos innecesarios al momento que los datos fueron procesados se pudo realizar el respectivo análisis con las herramientas de Power BI y de Tableu Public. Seleccionando los elementos más idóneos para obtener información relevante.
<br/>
Para la utilización de bases relacionales se realizó la practica con MYsql DB Browser form SQlite y con la base relacional de Acces para enlazar las bases relacionales se utilizó la herramienta de <br/>
Power BI que puede extraer directamente los datos de dichas bases.
