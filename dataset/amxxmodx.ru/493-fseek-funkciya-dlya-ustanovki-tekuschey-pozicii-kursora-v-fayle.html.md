# fseek Функция для установки текущей позиции курсора в файле
[Ядро AMXx](http://amxxmodx.ru/core/) [file.inc](http://amxxmodx.ru/core/fileinc/)
Инфо из **file.inc:**  
```
//Sets the current position in a file (see SEEK_ values above)  
native fseek(file, position, start);
```
  
  
**Синтаксис:**  

fseek(file, position, start)
  

    * **file** - Индекс открытого файла  

    * **position** - Позиция относительно start  

    * **start** :
      * SEEK_SET - начало файла  

      * SEEK_CUR - текущая позиция курсора  

      * SEEK_END - конец файла  

  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--  

