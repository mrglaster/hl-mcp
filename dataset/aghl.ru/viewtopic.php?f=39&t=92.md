# Half-Life и Adrenaline Gamer форум

## [[TUT] Голографический эффект](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=92)
Категории: [Скриптинг](https://aghlru.ds-servers.com/forum/search.php?keywords=%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B8%D0%BD%D0%B3&terms=all&fid\[\]=19&sc=1&sf=catonly&sr=topics)
Модератор: [KORD_12.7](https://aghlru.ds-servers.com/forum/memberlist.php?mode=viewprofile&u=67)
  
 
  
Если вы проходили Hazard Course в Half-Life, то, наверное, помните голографическую [девушку](http://ru.wikipedia.org/wiki/%D0%94%D0%B6%D0%B8%D0%BD%D0%B0_%D0%9A%D1%80%D0%BE%D1%81%D1%81), которая помогала вам проходить задания. В данной статье речь пойдет, как раз о создании этого эффекта с помощью AMXX.  
  
Данный эффект можно получить, выполнив на нужном объекте код:  
**Код:** ```
// Engine модуль  
set_rendering(i_Ent, kRenderFxDistort, 0, 0, 0, kRenderTransAdd, 127) 
```
или  
**Код:** ```
// Fakemeta модуль  
fm_set_rendering(i_Ent, kRenderFxDistort, 0, 0, 0, kRenderTransAdd, 127) 
```
  
i_Ent - объект, над которым производится действие.  
kRenderFxDistort - стиль изображения.  
0 - цвет R (красный).  
0 - цвет G (зеленый).  
0 - цвет B (синий).  
kRenderTransAdd - тип изображения (прозрачный).  
127 - значение прозрачности.  
  
Пример из Hazard Course:  
![Изображение](http://upload.wikimedia.org/wikipedia/ru/a/ab/Gina_Cross_%28Half-Life%29.jpg)  
  
**[▼](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=92) Примеры плагинов** Engine модуль:  
**Код:**
```
#include <amxmodx>  
#include <engine>  
  
// Номер анимации используемой модели  
const IDDLE7_SEQUENCE = 18  
  
// Имя модели, которая будет использоваться для объекта (модель ученого)  
new g_szModel[ ] = { "models/scientist.mdl" }  
  
// Кэшируем нашу модель  
public plugin_precache()  
    precache_model(g_szModel)  
  
// Создаем команду /hologram для создания объекта с голографическим эффектом  
public plugin_init()  
    register_clcmd("say /hologram", "ClCmd_Hologram")  
  
// Функция, которая выполняет действие при использовании команды /hologram  
public ClCmd_Hologram(id)  
{  
    // Создаем объект класса info_target  
    new i_Ent = create_entity("info_target")  
      
    // Если создание объекта прошло успешно, выполняем нужный код  
    if (is_valid_ent(i_Ent))      
    {  
        // Даем объекту новое имя  
        entity_set_string(i_Ent, EV_SZ_classname, "hlstyle_hologram")  
          
        // Получаем координаты игрока в f_Origin  
        new Float:f_Origin[3]  
        entity_get_vector(id, EV_VEC_origin, f_Origin)  
          
        // Увеличиваем X координату на 50.0  
        f_Origin[0] += 50.0  
          
        // Перемещаем объект в новые координаты f_Origin  
        entity_set_origin(i_Ent, f_Origin)  
  
        // Устанавливаем объекту модель g_szModel  
        entity_set_model(i_Ent, g_szModel)  
          
        // Устанавливаем объекту анимацию IDDLE7_SEQUENCE  
        entity_set_int(i_Ent, EV_INT_sequence, IDDLE7_SEQUENCE)  
          
        // Устаналиваем объекту свойство проходимости  
        entity_set_int(i_Ent, EV_INT_solid, SOLID_NOT)  
          
        // Опускаем объект на землю  
        drop_to_floor(i_Ent)  
          
        // Ставим объекту голографический эффект  
        set_rendering(i_Ent, kRenderFxDistort, 0, 0, 0, kRenderTransAdd, 127)  
    }  
}
```
  
Fakemeta модуль:  
**Код:** 
```
#include <amxmodx>  
#include <fakemeta_util>  
  
const IDDLE7_SEQUENCE = 18  
  
new g_szModel[ ] = { "models/scientist.mdl" }  
  
// Кэшируем нашу модель  
public plugin_precache()  
    precache_model(g_szModel)  
      
// Создаем команду /hologram для создания объекта с голографическим эффектом   
public plugin_init()  
    register_clcmd("say /hologram", "ClCmd_Hologram")      
  
// Функция, которая выполняет действие при использовании команды /hologram  
public ClCmd_Hologram(id)  
{  
   // Создаем объект класса info_target  
   new i_Ent = engfunc(EngFunc_CreateNamedEntity, engfunc(EngFunc_AllocString, "info_target"))  
      
   // Если создание объекта прошло успешно, выполняем нужный код  
   if(pev_valid(i_Ent))  
   {  
      // Даем объекту новое имя  
      set_pev(i_Ent, pev_classname, "hlstyle_hologram")  
        
      // Получаем координаты игрока в f_Origin  
      new Float:f_Origin[3]  
      pev(id, pev_origin, f_Origin)  
        
      // Увеличиваем X координату на 50.0  
      f_Origin[0] += 50.0  
        
      // Перемещаем объект в новые координаты f_Origin  
      set_pev(i_Ent, pev_origin, f_Origin)  
     
      // Устанавливаем объекту модель g_szModel  
      engfunc(EngFunc_SetModel, i_Ent, g_szModel)  
        
      // Устанавливаем объекту анимацию IDDLE7_SEQUENCE  
      set_pev(i_Ent, pev_sequence, IDDLE7_SEQUENCE)  
        
      // Устаналиваем объекту свойство проходимости  
      set_pev(i_Ent, pev_solid, SOLID_NOT)  
        
      // Опускаем объект на землю  
      engfunc(EngFunc_DropToFloor, i_Ent)  
        
      // Ставим объекту голографический эффект  
      fm_set_rendering(i_Ent, kRenderFxDistort, 0, 0, 0, kRenderTransAdd, 127)  
   }  
}
```
