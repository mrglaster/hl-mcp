# get_distance Функция возвращает дистанцию между двумя точками.
[Ядро AMXx](http://amxxmodx.ru/core/) [vector.inc](http://amxxmodx.ru/core/vectorinc/)
Функция **get_distance** получает расстояние между двумя точками, например на джамп серверах для определения длины прыжка игрока. Но правда там нужна большая точность и используется аналогичная функция которая возвращает не целое число, а более точное дробное.  
  
Инфо из **vector.inc:**  
```
/* Returns distance between two vectors. */  
native get_distance(const origin1[3], const origin2[3]);
```
  
  
**Синтаксис:**  

get_distance(const origin1[3], const origin2[3])
  

    * **const origin1[3]** - Массив с координатой первой точки  

    * **const origin2[3]** - Массив с координатой второй точки  

Функция вернет целочисленную величину расстояния между двумя точками  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
  
#define PLUGIN "[http://amxxmodx.ru] get_distance"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
  
    register_clcmd("say t1","t1")  
    register_clcmd("say t2","t2")  
    register_clcmd("say dis","dis")  
}  
  
new forigin[3]  
new sorigin[3]  
public t1(id){  
    get_user_origin(id,forigin)  
}  
  
public t2(id){  
    get_user_origin(id,sorigin)  
}  
  
public dis(id){  
    new distance = get_distance(forigin,sorigin)  
      
    client_print(0,print_chat,"Dist:%d",distance)  
      
}  

```
  
  
**Описание:**  
В данном примере есть три команды:  

    1. **say t1** - запоминание первой точки  

    2. **say t2** - запоминание второй точки  

    3. **say dis** - получение расстояния между точками 1 и 2  

  
Можете "запомнить" первую точку и далее перемещаясь по карте сохранять только вторую и смотреть на сколько изменилась дистанция.
