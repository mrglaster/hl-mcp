et_pdata_int
[Fakemeta](http://127.0.0.1:8000/content/index.htm) (fakemeta.inc) 
Description
set_pdata_int - Sets private data from an entity's memory block 
Syntax
set_pdata_int ( index, offset, value, [ linuxdiff = -5 ] ) 
Type
Native 
Notes
Sets private data on an entity's void *pvPrivateData memory block.   
  
index is the numerical entity index.   
offset is the numerical offset into the memory block, as an C-type integer.   
value is the value to set.   
  
If the server is running linux, the linuxdiff parameter is added to the offset.   

