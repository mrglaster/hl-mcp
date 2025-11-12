et_pdata_int
[Fakemeta](http://127.0.0.1:8000/content/index.htm) (fakemeta.inc) 
Description
get_pdata_int - Gets private data from an entity's memory block 
Syntax
get_pdata_int ( index, offset, [ linuxdiff = 5 ] ) 
Type
Native 
Notes
Gets private data from an entity's void *pvPrivateData memory block.   
  
index is the numerical entity index.   
offset is the numerical offset into the memory block, as an C-type integer.   
  
If the server is running linux, the linuxdiff parameter is added to the offset.
