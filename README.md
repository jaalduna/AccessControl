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

Data required for the log regiters: 
tarjeta.id_number
tarjet


todo:

[] Terminar de incluir logs
[] Hacer front-end web
[]  
