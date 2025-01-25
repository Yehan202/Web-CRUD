import mysql.connector 

database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='informatica.iesquevedo.es',
    port = 3333,
    ssl_disabled = True,
    user ='yehan.xue', #USUARIO QUE USAMOS NOSOTROS
    password ='yehanXUE2002', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='yehan'
) 