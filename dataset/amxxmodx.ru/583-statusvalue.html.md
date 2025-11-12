# StatusValue
[Готовые скрипты](http://amxxmodx.ru/scripts/)
Всем привет !  
Сейчас я вам расскажу про такой интересный **event** StatusValue  
И как его использовать   
  
```
#include <amxmodx>  
  
new weapon[][] = {"", "P228", "", "Scout", "He grenade", "XM1014", "C4", "Mac 10", "Aug", "Smoke grenade", "Dual elite", "Fiveseven", "Ump 45", "SG550", "Galil", "Famas", "Usp", "Glock 18", "Awp", "mp5", "M249", "M3", "M4A1", "Tmp", "g3sg1", "Flash grenade", "Deagle", "sg552", "АК - 47", "Knife", "p90"}  
  
new gMsgHud  
  
public plugin_init()  
{  
    register_event("StatusValue", "EventStatusValueShow", "be", "1=2", "2!0") // Если игрока смотрит на какого то человека   
    register_event("StatusValue", "EventStatusValueHide", "be", "1=1", "2=0") // Если туда куда он смотрит нету человека  
  
    gMsgHud = CreateHudSyncObj() // Создаем Hud  
}  
  
public EventStatusValueShow(id)  
{  
    if(is_user_connected(id)) // Проверяем подключен ли игрока  
    {  
        new aimid = read_data(2) // Получаем ид того на кого смотрим   
          
        if(get_user_team(id) == get_user_team(aimid)) // Если их команды совпадают   
        {   
            static red, green, blue, szName[32]  
            get_user_name(aimid, szName, 31)  
              
            if(get_user_team(aimid) == 1)  
            {  
                red = 255  
                green = 50  
                blue = 0  
            }else if(get_user_team(aimid) == 2)  
            {  
                red = 0  
                green = 50  
                blue = 255  
            }  
              
            new weaponid = get_user_weapon(aimid) // Получаем оружие которое в руках у игрока   
              
            set_hudmessage(red, green, blue, -1.0, 0.60, 1, 0.01, 3.0, 0.01, 0.01, -1)  
            ShowSyncHudMsg(id, gMsgHud, "%s / Hp %d / Ar %d / %s", szName, get_user_health(aimid), get_user_armor(aimid), weapon[weaponid]) // Показываем сообщение игроку   
        }  
    }  
}  
  
public EventStatusValueHide(id)  
{  
    ClearSyncHud(id, gMsgHud) // Очищаем созданный нами Hud  
}  

```
  
  
То есть   
Если вы зайдете на сервер и посмотрите на игрока то вы увидите его   
Здоровье Броню и оружие которое он держит в руках   
  
Все на этом вынужден проститься  
Всем спасибо
