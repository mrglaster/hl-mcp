# Ham_IsPlayer Проверка на "игрок ли?"
[Ham Sandwich](http://amxxmodx.ru/hamsandwich/) [ham_const.inc](http://amxxmodx.ru/hamsandwich/ham_constinc/)
Проверим энтити, игрок ли оно?  
  
Инфо из **ham_const.inc:**  
```
/**   
* Description:        Whether or not the entity is a player.  
* Forward params:    function(this);  
* Return type:        Integer (boolean) .  
* Execute params:    ExecuteHam(Ham_IsPlayer, this);  
*/
```
  
  
**Разберём:**  
```
/**   
* Описание:            Проверяет является энтити игроком или нет.  
* Параметры форварда:    function(this);  
* Возвращает тип:        Целое (булева).  
* Параметры выполнения:    ExecuteHam(Ham_IsPlayer, this);  
*/
```
  
  
И так, у нас параметр для функции [ExecuteHam](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2hhbXNhbmR3aWNoL2hhbXNhbmR3aWNoaW5jLzI3OC1leGVjdXRlaGFtLXZ5cG9sbnlhZXQtdmlydHVhbG51eXUtZnVua2NpeXUtbmEtaWdyb2tlLW9iZWt0ZS5odG1s)([ExecuteHamB](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2hhbXNhbmR3aWNoL2hhbXNhbmR3aWNoaW5jLzM1My1leGVjdXRlaGFtYi12eXBvbG55YWV0LXZpcnR1YWxudXl1LWZ1bmtjaXl1LW5hLWlncm9rZS1vYmVrdGUuaHRtbA%3D%3D)), если вы не знаете о чём речь, то быстрее изучите их!  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <hamsandwich> //Подключаем инклюды  
  
public plugin_init()  
{  
    register_plugin(".csF Dev Team", "0.1", "Test Ham_IsPlayer"); //Регистрируем плагин  
    RegisterHam(Ham_Touch, "weaponbox", "TouchWeapon"); //Регистрируем событие прикосновения энтити с оружием  
}  
  
public TouchWeapon(Ent, id)  
{  
    if(ExecuteHam(Ham_IsPlayer, id)) //Если энтити - игрок  
        return HAM_SUPERCEDE; //Блокируем  
    return HAM_IGNORED;  
}
```
  
  
**Описание:**  
Плагин блокирует поднятие выкинутого оружия.  
Обычно никто не использует Ham_IsPlayer, так как лучше использовать:  
```
#define IsPlayer(%1)    (1 <= %1 <= g_MaxPlayers)
```

