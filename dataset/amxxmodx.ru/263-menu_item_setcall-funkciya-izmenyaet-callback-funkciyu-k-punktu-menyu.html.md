# menu_item_setcall Функция изменяет callback функцию к пункту меню
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/) [newmenus.inc](http://amxxmodx.ru/core/amxmodxinc/newmenusinc/)
Функция актуально в основном только в тех случаях, когда меню создается статично.  
Она позволяет изменить исполняемую callback функцию для конкретного меню.  
  
Инфо из **newmenus.inc:**  
```
/**  
 * Sets an item's callback.  
 *  
 * @param menu            Menu resource identifier.  
 * @param item            Item identifier.  
 * @param callback        New callback from menu_makecallback(), or -1 to clear.  
 * @return                1 on success, 0 on failure.  
 * @error                Invalid menu resource.  
 */  
native menu_item_setcall(menu, item, callback=-1);
```
  
  
**Синтаксис:**  

menu_item_setcall ( menu, item, callback=-1 )
  

    * **menu** - Идентификатор меню  

    * **item** - Пункт в меню  

    * **callback=-1** - Функция callback  

  
  
**Тип функции:**  
Native   
  
**Пример:**  
```
//None
```
  
**Описание:**  
Работа функции аналогична функции **menu_item_setname** , по этому не буду повторяться и писать одинаковые коды.  
Смотрите пример там.  

