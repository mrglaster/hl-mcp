# cs_set_hostage_foll Функция указывает заложнику за каким объектом ему следовать
[CStrike](http://amxxmodx.ru/cstrike/)
Инфо из **cstrike.inc:**  
```
/* Set hostage to follow entity specified in followedindex. Does not have to be a player. If followedindex is 0 the hostage will stop following.  
 * Note: this native does not work on Condition Zero, which has a different hostage AI than CS.  
 */  
native cs_set_hostage_foll(index, followedindex = 0);
```
  
  
**Синтаксис:**  

cs_set_hostage_foll(index, followedindex = 0)
  

    * **index** - id _заложника_  

    * **followedindex = 0** - id объекта  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
#include <fakemeta>  
#include <cstrike>  
  
#define PLUGIN "[http://amxxmodx.ru] return"  
#define VERSION "1.0"  
#define AUTHOR "VEN"  
  
//#define THIS_WILL_NOT_WORK  
  
new g_hostage_entity[] = "hostage_entity"  
  
#define ENT_CLASS "info_target"  
  
new g_ent  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    register_clcmd("test", "test_func")  
}  
public plugin_precache() {  
          
  
#if defined THIS_WILL_NOT_WORK  
        set_task(3.0, "create_ent")  
#else  
        create_ent()  
#endif  
}  
  
public create_ent() {  
        g_ent = engfunc(EngFunc_CreateNamedEntity, engfunc(EngFunc_AllocString, ENT_CLASS))  
}  
  
public test_func(id) {  
        new ent, hit  
        get_user_aiming(id, ent, hit)  
        if (is_hostage(ent)) {  
                new Float:origin[3]  
                pev(id, pev_origin, origin)  
                engfunc(EngFunc_SetOrigin, g_ent, origin)  
                cs_set_hostage_foll(ent, g_ent)  
        }  
  
        return PLUGIN_HANDLED  
}  
  
bool:is_hostage(ent) {  
        if (!pev_valid(ent))  
                return false  
  
        static class[sizeof(g_hostage_entity)]  
        pev(ent, pev_classname, class, sizeof(g_hostage_entity) - 1)  
        if (equal(class, g_hostage_entity))  
                return true  
          
        return false  
}
```
  
  
**Описание:**  
Если навести прицел на заложника и выполнить команду test, то заложник будет следовать в вашем направлении.  
Но обратите внимание на код, там создается другой невидимый объект и заложник следует к нему, а не к вам, даже если вы и террорист.
