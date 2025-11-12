how_menu
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
show_menu - Shows a list of menu options to a client. 
Syntax
show_menu ( index, keys, const menu[], time = -1, title[] = "" ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
keys is a bitwise number totalling the set of menu options. For example, here is a two option menu:   
`    
format(menuBody, 192, "\rCSDM: Armor\R^n^n\y1.\w Yes, armor up^n\y2.\w No armor")   
key = (1<<0)|(1<<1)   
show_menu(id, key, menuBody)   
  `   
  
Optionally you can specify a time, which defaults to infinity (-1) and a title for [register_menu](http://127.0.0.1:8000/content/register_menu.htm). 
User Contributed Notes
devicenul at gmail dot com | Jun-24-04 20:48:42  
---|---  
Defines for the various key's you need ` #define key_one     (1<<0)        //1   
#define key_two     (1<<1)        //2   
#define key_three     (1<<2)        //3   
#define key_four    (1<<3)        //4   
#define key_five     (1<<4)        //5   
#define key_six        (1<<5)        //6   
#define key_seven    (1<<6)        //7   
#define key_eight    (1<<7)        //8   
#define key_nine     (1<<8)        //9   
  `  
  

