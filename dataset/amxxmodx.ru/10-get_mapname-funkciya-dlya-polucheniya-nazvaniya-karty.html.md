# get_mapname Функция для получения названия карты
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
**get_mapname** - При помощи данной функции, вы сможете узнать название карты которая сейчас на сервере.  
Часто используется в различных информерах.  
  
Инфо из **amxmodx.inc:**  
```
/* Returns a name of currently played map. */  
native get_mapname(name[],len);
```
  
  
**Синтаксис:**  
get_mapname ( name[],len )  
name[] - Массив куда записывается название  
len - размер массива  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
  
#define PLUGIN "Map name info"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    register_clcmd("say /map","map_name")  
}  
public map_name(id){  
      
    new MapName[32]  
    get_mapname(MapName,31)  
      
    client_print(id,print_chat,"Map Name is: %s",MapName)  
  
}
```
  
  
Работа данного примера:  
При написание в чате **/map**  
Так же в чат будет выведена информация о текущей карте (ее название)
