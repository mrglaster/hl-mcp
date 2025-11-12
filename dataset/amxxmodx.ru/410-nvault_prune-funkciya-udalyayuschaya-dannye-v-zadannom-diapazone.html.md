# nvault_prune Функция удаляющая данные в заданном диапазоне
[The nVault Module](http://amxxmodx.ru/nvaultinc/)
Чистка данных от старых записей или в определенный момент с функцией **nvault_prune** не станут для вас проблемой.  
  
Инфо из **nvault.inc:**  
```
/* Prunes the vault for entries that are within the given timestamps.  
 * This will not erase values set with pset  
 */  
native nvault_prune(vault, start, end);
```
  
  
**Синтаксис:**  

nvault_prune(vault, start, end)
  

    * **vault** - Идентификатор открытого файла  

    * **start** - Дата **от**  

    * **end** - Дата **до**  

  
  
**Тип функции:**  
Native  
  
**Описание:**  
Признаюсь честно - мне было лень писать пример для столь простой функции.  
Если кто то напишет, пишите в личку или в комментарии, добавлю в новость с пометкой об авторе.
