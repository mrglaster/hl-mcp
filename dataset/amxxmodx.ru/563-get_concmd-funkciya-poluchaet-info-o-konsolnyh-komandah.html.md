# get_concmd Функция получает инфо о консольных командах.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Инфо из **amxmodx.inc:**  
```
/* Gets info about console command. If id is set to 0,  
then function returns only server cmds, if positive then  
returns only client cmds. in other case returns all console commands. */  
native get_concmd(index,cmd[],len1,&flags, info[],len2, flag, id = -1);
```
  
  
**Синтаксис:**  

get_concmd(index,cmd[],len1,&flags, info[],len2, flag, id = -1)
  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
