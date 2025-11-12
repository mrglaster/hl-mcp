# entity_get_string Функция получает строковые параметры объекта
[The Engine Module](http://amxxmodx.ru/engine/) [engine.inc](http://amxxmodx.ru/engine/engineinc/)
Те, кто знаком с маппингом, знают, что у всех объектов есть различные параметры: класс, имя, прозрачность и т.д, функция entity_get_string помогает получить эти параметры в виде строки.  
  
Инфо из **engine.inc:**  
```
native entity_get_string(iIndex, iKey, szReturn[], iRetLen);
```
  
  
  
**Синтаксис:**  

entity_set_string ( entity, key, const String[])
  

    * **entity** - id объекта  

    * **key** - Получаемое значение (константа):   
```
enum {  
    EV_SZ_classname = 0,  
    EV_SZ_globalname,  
    EV_SZ_model,  
    EV_SZ_target,  
    EV_SZ_targetname,  
    EV_SZ_netname,  
    EV_SZ_message,  
    EV_SZ_noise,  
    EV_SZ_noise1,  
    EV_SZ_noise2,  
    EV_SZ_noise3,  
    EV_SZ_viewmodel,  
    EV_SZ_weaponmodel,  
}
```
  

    * **const String[]** - Получаемое значение  

  
  
**Описание:**  
Синтаксис этой функции похож на синтаксис entity_set_string, только, в отличие от неё, функция entity_get_string получает параметр, а не устанавливает его.
