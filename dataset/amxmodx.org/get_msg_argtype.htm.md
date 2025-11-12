et_msg_argtype
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
get_msg_argtype - Returns the type of an message's argument. 
Syntax
get_msg_argtype ( argn ) 
Type
Native 
Notes
Argn starts from 1.   
  
Argument types are:   
  
enum {   
ARG_BYTE = 1, /* int */   
ARG_CHAR, /* int */   
ARG_SHORT, /* int */   
ARG_LONG, /* int */   
ARG_ANGLE, /* float */   
ARG_COORD, /* float */   
ARG_STRING, /* string */   
ARG_ENTITY, /* int */   
}
