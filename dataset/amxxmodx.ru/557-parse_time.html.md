# parse_time
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Инфо из **amxmodx.inc:**  
```
/* Returns time in input and additionaly fills missing information  
* with current time and date. If time is different than -1 then parsed  
* time is added to given time.  
* Example:  
* parset_time( "10:32:54 04/02/2003", "%H:%M:%S %m:%d:%Y" )  
* For more information see strptime(...) function from C libraries. */  
native parse_time(const input[],const format[], time = -1);
```
  
  
**Синтаксис:**  

parse_time(const input[],const format[], time = -1)
  

    * **const input[]** -   

    * **const format[]** -   

    * **time = -1** -   

  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
