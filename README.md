# AccessControl 


## Event log types

The Access Control system logs diferent events. Them are classified as

1. Card not found
    Format: LogId, date, time, card number: %s not found in the database
2. Card not Assigned 
    Format: LogId, Date, time, card with card_id %s has not yet assigned 
3. User is disabled
    Format: LogId, Date, time, User %s %s with user_id %s is disabled 
4. Access Success 
    Format: LogId, Date, time, Access Granted for user %s %s with user_id %s
5. Apertura manual
6. Usuario Registrado:
7. Usuario Modificado:
8. Usuario Eliminado:
10. Tarjeta Agregada:
11. Tarjeta Modificada:
12. Tarjeta eliminada

## Estructura del proyecto

El proyecto posee scripts python para implementar los drivers con los dispositivos y una aplicación web en php para implementar la gui. En la carpeta principal se encuentra este documento Readme.md, la carpeta source que contiene los scripts python y la carpeta webapp que contiene la aplicación web. dentro de webapp esta también la base de datos database.db

 

todo:

[] Terminar de incluir logs
[] Hacer front-end web
[]  
