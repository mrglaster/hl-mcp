# get_user_deaths Функция получает сколько раз умер игрок
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Если вам необходимо узнать количество смертей игрока, то функция в этом вам поможет.  
Думаю вы уже заметили что в разных модулях есть разные функции, результат которых одинаков, данная функция не исключение.  
  
Инфо из **amxmodx.inc:**  
```
/* Returns player deaths. */  
native get_user_deaths(index);
```
  
  
**Синтаксис:**  

get_user_deaths ( index )
  

    * **index** - id игрока,чьи смерти необходимо получить.  

  
  
**Тип функции:**  
Native  
  
**Описание:**  
Принцип работы функции аналогичен функции [cs_get_user_deaths](http://amxxmodx.ru/cstrike/31-cs_get_user_deaths-funkciya-vozvraschaet-kolichestvo-smertey-igroka.html). По этому писать пример отличающийся тремя символами не стану.
