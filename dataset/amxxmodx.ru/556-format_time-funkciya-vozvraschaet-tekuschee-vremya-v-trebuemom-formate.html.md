# format_time Функция возвращает текущее время в требуемом формате.
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Инфо из **amxmodx.inc:**  
```
/* Returns time in given format. The most popular is: "%m/%d/%Y - %H:%M:%S".  
* Last parameter sets time to format. */  
native format_time(output[],len, const format[],time = -1);
```
  
  
**Синтаксис:**  

format_time(output[],len, const format[],time = -1)
  

    * **output[]** - Массив с временем  

    * **len** - Его размер  

    * **const format[]** - Формат времени "%m/%d/%Y - %H:%M:%S"  

    * **time = -1** - Время будет более точным ( дробные значения )  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
