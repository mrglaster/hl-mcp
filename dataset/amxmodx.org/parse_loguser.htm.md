arse_loguser
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
parse_loguser - Parses log data about a user. 
Syntax
parse_loguser ( const text[], name[], nameLen, [ &userid, authid[], authidLen, team[], teamLen ] ) 
Type
Native 
Notes
Example:   
Text[] = "Butcher<5<bot<terrorist"   
  
name will contain for a maximum of nameLen characters, "Butcher".   
userid will have 5 stored into it.   
authid will contain for a maximum of authidLen characters, "BOT".   
team will contain, for a maximum of teamLen characters, TERRORIST.
