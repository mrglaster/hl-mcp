# Урок 20. Что такое Stocks
[Уроки по скриптингу для начинающих](http://amxxmodx.ru/lessons-on-pawn/)
У новичков регулярно возникает вопрос чем отличаются **stock** функции от native, давайте разберемся вместе.  
  
**Stock** функция (в основном, так как может быть и переменной) которая если не используется где-нибудь в плагине, будет попросту проигнорировна компилятором. То есть компилятор как бы не заметит ее вовсе.  
  
Многим новичками приходит идея сделать так:  
```
#include <amxmodx>  
#include <amxmisc>  
  
public plugin_init()  
{  
    register_plugin("The","Matrix","Has You")  
      
    fnDoFunc()  
}  
  
stock fnDoFunc()  
    log_amx("the world has imploded upon itself")
```
  
Хотя фактически та же самая функциональность могла быть достигнута так:  
```
#include <amxmodx>  
#include <amxmisc>  
  
public plugin_init()  
{  
    register_plugin("The","Matrix","Has You")  
      
    fnDoFunc()  
}  
  
fnDoFunc()  
    log_amx("the world has imploded upon itself")
```
  
  
Но для чего тогда нужны эти сток функции? В основном там, где есть инклюды с множеством функций, из которых обычно используется малая часть.  
Например возьмем инклюд **engine_stocks.inc** от модуля [**engine**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2VuZ2luZS80NzQtbW9kdWwtZW5naW5lLmh0bWw%3D).  
  
**Начало файла:**  
```
stock fakedamage(idvictim,const szClassname[],Float:takedmgdamage,damagetype)  
{  
    new entity = create_entity("trigger_hurt");  
    if (entity)  
    {  
        DispatchKeyValue(entity,"classname","trigger_hurt");  
        new szDamage[16];  
        // Takedamages only do half damage per attack (damage is damage per second, and it's triggered in 0.5 second intervals).  
        // Compensate for that.  
        format(szDamage,15,"%f",takedmgdamage * 2);  
        DispatchKeyValue(entity,"dmg",szDamage);  
        format(szDamage,15,"%i",damagetype);  
        DispatchKeyValue(entity,"damagetype",szDamage);  
        DispatchKeyValue(entity,"origin","8192 8192 8192");  
        DispatchSpawn(entity);  
        entity_set_string(entity, EV_SZ_classname, szClassname);  
        fake_touch(entity,idvictim);  
        remove_entity(entity);  
        return 1;  
    }  
    return 0;  
}  
  
//wrapper for find_ent_by_class  
stock find_ent(iStart, const szClassname[])  
{  
    return find_ent_by_class(iStart, szClassname);  
}  
//...
```
  
Если в плагине будет использована функция **find_ent** , то она будет включена в скрипт.  
А функцию **stock fakedamage** в плагин не использовалась в плагине и она не будет включена в скрипт.  
  
**Stock** может быть и переменной:  
```
stock const mystring[] = "hello pm"
```
  
  
Лично я не имел с ними дело, по этому опущу это, если интересно - переведите сами.  
Вот ссылка оригинальный материал: [[TUT] The Use of Stocks](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2ZvcnVtcy5hbGxpZWRtb2RzLm5ldC9zaG93dGhyZWFkLnBocD90PTQwMzQx)
