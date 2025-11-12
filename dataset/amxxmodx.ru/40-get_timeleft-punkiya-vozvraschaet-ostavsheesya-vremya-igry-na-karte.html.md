# get_timeleft Функия возвращает оставшееся время игры на карте
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
**get_timeleft** - Простенькая функция, которая часто используется в различных информерах, картменеджерах и тому подобных плагинах.  
  
Инфо из **amxmodx.inc:**  
```
/* Returns time remaining on map in seconds. */  
native get_timeleft();
```
  
  
**Синтаксис:**  

get_timeleft ( )
  
  
**Пример:**  
```
  
#include <amxmodx>  
#include <amxmisc>  
   
#define PLUGIN "Get time left"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
   
   
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
       
    register_clcmd("say /time-left","map_timeleft")  
}  
public map_timeleft(id){  
       
    new MapTime = get_timeleft()  
       
    client_print(id,print_center,"Time left is: %d:%02d",(MapTime / 60), (MapTime % 60))  
   
}
```
  
  
**Описание:**  
Скорее всего у вас стоит стандартный набор amxmodx плагинов, в котором tсть уже команда timeleft,  
По этому мы ее немного изменим на say /time-left  
И выведем результаты в чат по центру экрана.  
Да да, именно так работает стандартный плагин :), только там еще добавлено голосовое сопровождение.  
  
Самые внимательные наверняка заметили странную запись %d:%02d",(MapTime / 60), (MapTime % 60).  
Давайте немного поясню:  
Компьютер получает оставшееся время в секундах, и эти прсотые математические действия вычисляют минуты и оставшиеся секунды.
