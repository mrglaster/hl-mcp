# get_distance_f Функция возвращает дистанцию между двумя точками (дробное число)
[Ядро AMXx](http://amxxmodx.ru/core/) [vector.inc](http://amxxmodx.ru/core/vectorinc/)
Функция получает точное расстояние между двумя точками.  
  
Инфо из **vector.inc:**  
```
/* Gets distance between two origins (float). */  
native Float:get_distance_f(const Float:Origin1[3], const Float:Origin2[3]);
```
  
  
**Синтаксис:**  

get_distance_f(const Float:Origin1[3], const Float:Origin2[3])
  

    * **const Float:Origin1[3]** - Массив с координатами точки №1 (дробные значения)  

    * **const Float:Origin2[3]** - Массив с координатами точки №2 (дробные значения)  

Функция вернет точное расстояние между точками 1 и 2.  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <fakemeta>  
  
#define PLUGIN "[http://amxxmodx.ru] get_distance_f"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
  
    register_clcmd("say t1","t1")  
    register_clcmd("say t2","t2")  
    register_clcmd("say dis","dis")  
}  
  
new Float:forigin[3]  
new Float:sorigin[3]  
  
public t1(id){  
    pev( id, pev_origin,forigin)  
}  
  
public t2(id){  
    pev( id, pev_origin,sorigin)  
}  
  
public dis(id){  
      
    new Float:distance = get_distance_f(forigin,sorigin)  
      
    client_print(0,print_chat,"Dist:%f",distance)  
      
}  

```
  
  
**Описание:**  
Функция аналогична функции [**get_distance**](http://amxxmodx.ru/core/vectorinc/424-get_distance-funkciya-vozvraschaet-distanciyu-mezhdu-dvumya-tochkami.html) единственная разница в получаемых и возвращаемых данных, они дробные что обеспечивает большую точность.
