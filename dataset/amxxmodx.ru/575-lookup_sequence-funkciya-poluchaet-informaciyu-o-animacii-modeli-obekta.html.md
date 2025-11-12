# lookup_sequence Функция получает информацию о анимации модели объекта.
[The Fakemeta Module](http://amxxmodx.ru/fakemeta/) [fakemeta.inc](http://amxxmodx.ru/fakemeta/fakemetainc/)
Инфо из **fakemeta.inc**  
```
/**  
* Looks up the sequence for the entity.  
*  
* @param entity The entity id to lookup.  
* @param name The sequence name to lookup, case insensitive. ("JUMP" would match "jump")  
* @param framerate The framerate of the sequence, if found.  
* @param loops Whether or not the sequence loops.  
* @param groundspeed The groundspeed setting of the sequence.  
* @return -1 on failed lookup, the sequence number on successful lookup.  
*/  
native lookup_sequence(entity, const name[], &Float:framerate = 0.0, &bool:loops = false, &Float:groundspeed = 0.0)
```
  
  
**Синтаксис:**  

lookup_sequence(entity, const name[], &Float:framerate = 0.0, &bool:loops = false, &Float:groundspeed = 0.0)
  
  

    * **entity** - индекс объекта  

    * **const name[]** - название анимации для поиска(например "run").  

    * **& Float:framerate** - частота кадров.  

    * **& bool:loops** - цикличность анимации.  

    * **& Float:groundspeed** - скорость передвижения по земле?  

  
  
Функция вернёт номер анимации если всё верно и -1 если нет.  
  
Тип функции: **Native**  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <fakemeta>  
  
public plugin_init()  
{  
    register_clcmd("say", "info")  
}  
public info(id)  
{  
    new arg[33]; read_argv(1, arg, 32)  
    new num = lookup_sequence(id, arg)  
    if(num >= 0) client_print(id, print_chat, "number of animation %d", num)  
    return PLUGIN_HANDLED  
}
```
  
  
**Описание:**  
  
При вводе верного названия анимации модели игрока,в чат выдаст её номер.  
  

Названия анимаций:  
dummy  
idle1  
crouch_idle  
walk  
run  
crouchrun  
jump  
longjump  
swim  
treadwater  
head  
gutshot  
left  
back  
right  
forward  
и т.д.
