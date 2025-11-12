# entity_set_origin Функция задает координаты объекту
[The Engine Module](http://amxxmodx.ru/engine/) [engine.inc](http://amxxmodx.ru/engine/engineinc/)
С помощью данной функции, можно задать координаты объекту. Если вы создали объект, то естественно необходимо указать точку, где этот объект должен появиться,иначе сервер просто не будет знать где же этот объект разместить.  
  
Инфо из **engine.inc:**  
```
/* Proper origin setting, keeps updated with Half-Life engine. */  
native entity_set_origin(iIndex, const Float:fNewOrigin[3]);
```
  
  
**Синтаксис:**  

entity_set_origin ( entity, Float:NewOrigin[3] )
  

    * **entity** - id объекта  

    * **Float:NewOrigin[3]** - Массив с тремя координатами X Y Z   

  
  
**Тип функции:**  
Native  
  
**Описание:**  
Использование **entity_set_origin** аналогично функции [set_user_origin](http://amxxmodx.ru/fun/77-set_user_origin.html)  
Что бы показать пример использования, придется изучить еще несколько функций, таких как установка модели и иных свойств.  
По этому не стану приводить полноценный пример сейчас. При изучении следующих функций данного модуля, вы сами все поймете.  
Или изучите аналогичную функцию о которой писалось чуть выше, все практически идентично.  
  
**Пример:**  
```
entity_set_origin(Ent, Origin)
```

