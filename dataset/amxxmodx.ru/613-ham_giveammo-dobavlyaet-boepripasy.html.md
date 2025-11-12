# Ham_GiveAmmo Добавляет боеприпасы
[Ham Sandwich](http://amxxmodx.ru/hamsandwich/) [ham_const.inc](http://amxxmodx.ru/hamsandwich/ham_constinc/)
Добавление боеприпасов.  
  
Инфо из **ham_const.inc:**  
```
/**  
* Description:        Gives ammo to the entity.  
*                    This function is not supported for the following mods:  
*                        Earth's Special Forces.  
*                        Sven-Coop 4.8+, see Ham_SC_GiveAmmo instead.  
*                        Team Fortress Classic, see Ham_TFC_GiveAmmo instead.  
* Forward params:    function(this, Amount, const Name[], Max)  
* Return type:        Integer.  
* Execute params:    ExecuteHam(Ham_GiveAmmo, this, amount, "type", max);  
*/
```
  
  
**Разберём:**  
```
/**  
* Описание:            Добавляет боеприпасы энтити.  
*                        Эта функция не поддерживает моды:  
*                            Earth's Special Forces.  
*                            Sven-Coop 4.8+, смотри Ham_SC_GiveAmmo.  
*                            Team Fortress Classic, смотри Ham_TFC_GiveAmmo.  
* Параметры форварда:    function(this, Amount, const Name[], Max)  
* Возвращает тип:        Integer(целое).  
* Параметры выполнения:    ExecuteHam(Ham_GiveAmmo, this, amount, "type", max);  
*/
```
  
  
Т.е. Ham_GiveAmmo не функция, а параметр для [ExecuteHam](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2hhbXNhbmR3aWNoL2hhbXNhbmR3aWNoaW5jLzI3OC1leGVjdXRlaGFtLXZ5cG9sbnlhZXQtdmlydHVhbG51eXUtZnVua2NpeXUtbmEtaWdyb2tlLW9iZWt0ZS5odG1s)([ExecuteHamB](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2hhbXNhbmR3aWNoL2hhbXNhbmR3aWNoaW5jLzM1My1leGVjdXRlaGFtYi12eXBvbG55YWV0LXZpcnR1YWxudXl1LWZ1bmtjaXl1LW5hLWlncm9rZS1vYmVrdGUuaHRtbA%3D%3D)), если вы не знаете о чём речь, то изучите их.  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <fun>  
#include <hamsandwich> //Подключаем инклюды  
  
public plugin_init()  
{  
    register_plugin(".csF Dev Team", "0.1", "Test Ham_GiveAmmo"); //Регистрируем плагин  
    RegisterHam(Ham_Spawn, "player", "SpawnPlayer", 1); //Регистрируем событие спавна  
}  
  
public SpawnPlayer(id)  
    set_task(0.1, "GiveAmmo", id); //Делаем задание на функцию "GiveAmmo"  
  
public GiveAmmo(id)  
{  
    if(is_user_alive(id)) //Проверяем, если игрок жив, то...  
    {  
        strip_user_weapons(id); //Убираем всё оружие у игрока  
        give_item(id, "weapon_knife"); //Выдаём нож  
        give_item(id, "weapon_p228"); //Выдаём пистолет p228  
        ExecuteHam(Ham_GiveAmmo, id, 52, "357sig", 52); //И патроны к нему  
        //ExecuteHam(Ham_GiveAmmo, айди_игрока, количество_патронов, "тип_патронов", максимальный_боезапас);  
    }  
}
```
  
  
**Описание:**  
Плагин при каждом респавне(возрождении) игрока через 0,1 секунды будет убирать всё оружие у игрока, выдавая ему нож и p228 с патронами.  
  
Тип патронов можно посмотреть тут: [CS Weapons Information](http://amxxmodx.ru/engine/go.php?url=aHR0cHM6Ly93aWtpLmFsbGllZG1vZHMubmV0L0NzX3dlYXBvbnNfaW5mb3JtYXRpb24%3D), в столбе "ANAME", без приставки "ammo_".
