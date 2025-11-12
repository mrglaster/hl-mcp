# entity_set_string Функция устанавливает строковые параметры объекта
[The Engine Module](http://amxxmodx.ru/engine/) [engine.inc](http://amxxmodx.ru/engine/engineinc/)
У каждого объекта есть различные параметры, функция **entity_set_string** устанавливает объекту строковые значения определенного набора констант, таких как Глобальное имя и имя класса, а также с десяток других.  
  
Инфо из **engine.inc:**  
```
native entity_set_string(iIndex, iKey, const szNewVal[]);
```
  
  
**Синтаксис:**  

entity_set_string ( entity, key, const String[] )
  

    * **entity** - id объекта  

    * **key** - Устанавливаемое значение (константа):  
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

    * **const String[]** - Устанавливаемое значение  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
entity_set_string(i_Ent, EV_SZ_classname, "You_class_name")
```
  
  
**Описание:**  
Честно говоря не вижу смысла писать пример, так как визуально все равно ни чего не увидеть, только если с помощью другой функции получить значение обратно.  
  
**Внимание:**  
не устанавливайте модель для объекта с помощью данной функции!!!  
Для установки модели есть функция **entity_set_model** , но о ней поговорим отдельно.
