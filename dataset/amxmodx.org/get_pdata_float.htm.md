et_pdata_float
[Fakemeta](http://127.0.0.1:8000/content/index.htm) (fakemeta.inc) 
Description
get_pdata_float - Gets private data from an entity's memory block 
Syntax
Float: get_pdata_float ( index, offset, [ linuxdiff = 5 ] ) 
Type
Native 
Notes
Gets private data from an entity's void *pvPrivateData memory block.   
  
index is the numerical entity index.   
offset is the numerical offset into the memory block, as an C-type float.   
  
If the server is running linux, the linuxdiff parameter is added to the offset.
