et_vaultdata
[Core](http://127.0.0.1:8000/content/index.htm) (vault.inc) 
Description
get_vaultdata - Reads a key from the vault. 
Syntax
get_vaultdata ( const key[], [ data[] = "", len = 0 ] ) 
Type
Native 
Notes
If length is not specified, the result is returned as a number.   
  
If lengh is specified, the result is copied into data for len maximum characters. 
User Contributed Notes
ferret at gamehavoc dot com | Mar-31-05 05:00:24  
---|---  
The vault code does not appear to like vaultkey strings that begin with a number. Best to make sure you prefix all keys with a character string, such as your plugin name. Say a plugin named Attack Watch.. AW_ to be safe.   
  

