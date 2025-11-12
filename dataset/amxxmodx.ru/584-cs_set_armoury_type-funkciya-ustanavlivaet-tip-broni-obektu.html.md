# cs_set_armoury_type Функция устанавливает тип оружия обьекту
[CStrike](http://amxxmodx.ru/cstrike/)
Информация из **cstrike.inc** :  
```
/* Set an armoury_entity to be of specified type. You will have to set the appropriate model.  
 * The second argument, type, should be a CSW_* constant. Not all weapons are supported by Counter-strike.  
 * Supported weapons/items: CSW_MP5NAVY, CSW_TMP, CSW_P90, CSW_MAC10, CSW_AK47, CSW_SG552, CSW_M4A1, CSW_AUG, CSW_SCOUT  
 * CSW_G3SG1, CSW_AWP, CSW_M3, CSW_XM1014, CSW_M249, CSW_FLASHBANG, CSW_HEGRENADE, CSW_VEST, CSW_VESTHELM, CSW_SMOKEGRENADE  
 */  
native cs_set_armoury_type(index, type);
```
  
  

    * index - Индекс оружия  

    * type - Тип брони  

  
  
Список доступных типов:  

![](http://amxxmodx.ru/templates/3week92/dleimages/spoiler-plus.gif) [Показать / Скрыть текст](javascript:ShowOrHide\('sp984aeab1b90497917614e6f74892a303'\))
CSW_SCOUT 3  
CSW_HEGRENADE 4  
CSW_XM1014 5  
CSW_MAC10 7  
CSW_AUG 8  
CSW_SMOKEGRENADE 9  
CSW_AWP 18  
CSW_MP5NAVY 19  
CSW_M249 20  
CSW_M3 21  
CSW_M4A1 22  
CSW_TMP 23  
CSW_G3SG1 24  
CSW_FLASHBANG 25  
CSW_SG552 27  
CSW_AK47 28  
CSW_P90 30  
CSW_VEST 31  
CSW_VESTHELM 32
  
  
**Синтаксис:**  

cs_set_armoury_type(index, type)
  
  
**Тип функции:**  
Native  
  
**Пример:**  
```
#include <amxmodx>  
#include <cstrike>  
  
/* engine.inc */  
native find_ent_by_class(iIndex, const szClass[]);  
native entity_set_model(iIndex, const szModel[]);  
  
public plugin_init() {  
    register_plugin("cs_set_armoury_type", "0.1", "Felix_Font")  
    armoury_ent()   
}  
  
public armoury_ent()   
{   
    new iEnt // Создаем переменую для хранения индексов ентити  
  
    while ((iEnt = find_ent_by_class(iEnt, "armoury_entity")) > 0)  // Выполняем функцию изменения свойств обьекта пока iEnt > 0  
    {  
        new armoury_type = cs_get_armoury_type(iEnt) // Получаем тип брони  
        if(armoury_type != CSW_SCOUT) // Если ентити обьект не Scout  
        {   
            cs_set_armoury_type(iEnt, CSW_SCOUT)  // Устанавливаем обьекту свойства Scout  
            entity_set_model(iEnt, "models/w_scout.mdl") // Изменяем w_ модель на модель соответствующую самим свойствам обьекта  
        }   
    }  
    return PLUGIN_CONTINUE;  
}
```
  
  
**Описание:**  
В данном примере я изменил все стандартные оружия которые лежать на земле, на Scout's. Обратите внимание что данная функция не трогает оружия которые выбрасивають игроки, и также ее можно использовать в процессе игры, даже допустим через ```
register_clcmd("say /change_armoury", "armoury_ent")
```
  
Все обьекти меняють свою модель буквально за 0,5 секунд. При зтом ничего не лагает.  
  
Вот собственно результат плагина (тест):  
  
[![cs_set_armoury_type Функция устанавливает тип оружия обьекту](http://amxxmodx.ru/uploads/posts/2014-03/thumbs/1394824452_hl-2014-03-14-21-02-45-639.jpg)](http://amxxmodx.ru/uploads/posts/2014-03/1394824452_hl-2014-03-14-21-02-45-639.jpg)  
  
Также данную функцию можно использовать для удаления пушек с карт и т.д.  
Вобшем на все что только взбредет вам в голову.  
  
Строго не судите. Первая статья.   
Попытался максимально ясно обьяснить что и как.
