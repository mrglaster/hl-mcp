# get_es Функция получает состояние объектов
[The Fakemeta Module](http://amxxmodx.ru/fakemeta/) [fakemeta.inc](http://amxxmodx.ru/fakemeta/fakemetainc/)
В модуле fakemeta есть набор констант **EntityState Constants** и две функции для работы с ними, одна **get_es** для получения значения переменной, вторая **set_es** для изменения. Обратите внимание на то, что функции могут работать только с помощью форварда FM_AddToFullPack, в противном случае может упасть сервер.  
  
Инфо из **fakemeta.inc:**  
```
// These functions are used with the entity_state data structure (FM_AddToFullPack)  
// Get: 0 extra params - Return integer; 1 extra param - by ref float or vector or array  
// Set: Use anything  
// Use 0 for es_handle to specify the global entity_state handle  
native get_es(es_handle, EntityState:member, {Float,_}:...);
```
  
  
Инфо из **fakemeta.inc:**  
```
// These functions are used with the entity_state data structure (FM_AddToFullPack)  
// Get: 0 extra params - Return integer; 1 extra param - by ref float or vector or array  
// Set: Use anything  
// Use 0 for es_handle to specify the global entity_state handle  
native get_es(es_handle, EntityState:member, {Float,_}:...);
```
  
  
**Синтаксис:**  

get_es(es_handle, EntityState:member, {Float,_}:...)
  

    * **es_handle** - Указатель на структуру состояния ( первый аргумент из события FM_AddToFullPack)  

    * **EntityState:member** - Константа из списка **EntityState**  

    * **{Float,_}:...** - Если для константы необходимые какие-то еще значения.  

  
  
**Тип функции:**  
Native  
  
**Описание:**  
Пример и описание посмотрите к функции [set_es](http://amxxmodx.ru/fakemeta/fakemetainc/400-set_es-funkciya-izmenyaet-sostoyanie-obektov.html) которая изменяет значения, а не получает.
