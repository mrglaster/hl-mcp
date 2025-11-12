# Изменение отдачи оружия
[Готовые скрипты](http://amxxmodx.ru/scripts/)
Всем привет,недавно меня натолкнуло на мысль о изменении отдачи оружия и я написал библиотеку в которой всего одна **stock** функция,но она очень сильно упрощает код  
**Как пользоваться ?**  
```
set_user_recoil(const Player,Float:recoil)
```
**stock** функция принимает два параметра,```
const Player
```
- id игрока у которого будем менять отдачу и ```
Float:recoil
```
- дробное число отвечающее за повышение/уменьшение отдачи  
**Пример кода:**  
```
  
#include <amxmodx>  
#include <amxmisc>  
#include <recoil>  
#include <Hamsandwich>  
#include <fakemeta>  
new bool:user_enabled_norecoil[33] = false  
  
#define PLUGIN "Test Recoiling System"  
#define VERSION "1.0"  
#define AUTHOR "True_Hacker"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    register_clcmd("say !admin_norecoil_on", "nron")  
    register_clcmd("say !admin_norecoil_off", "nroff")  
    RegisterHam(Ham_Weapon_PrimaryAttack, "weapon_ak47", "no_recoil_func", 1)  
}  
  
public no_recoil_func(weapon)  
{  
    new id = pev(weapon,pev_owner)  
    if( user_enabled_norecoil[id] == true )  
    {  
        set_user_recoil(id,0.0)  
    }  
}  
  
public nron(id)  
{  
    if( get_user_flags(id) & ADMIN_BAN )  
    {  
        user_enabled_norecoil[id] = true  
        set_hudmessage(255, 255, 0, 0.0, 0.9, 0, 6.0, 12.0)  
        show_hudmessage(id, "[Admin No-Recoil Enabled]")  
    }  
}  
  
public nroff(id)  
{  
    if( get_user_flags(id) & ADMIN_BAN )  
    {  
        user_enabled_norecoil[id] = false  
        set_hudmessage(255, 255, 0, 0.0, 0.9, 0, 6.0, 12.0)  
        show_hudmessage(id, "[Admin No-Recoil Disabled]")  
    }  
}  
  

```
  
  
**Разбор кода по частям:**  
1. ```
#include <recoil>
```
как вы уже заметили я уже включил нужную нам библиотеку,думаю **#include** не нуждается в объяснении и вы уже прочли все уроки по скриптингу(на этом сайте)  
2. ```
RegisterHam(Ham_Weapon_PrimaryAttack, "weapon_ak47", "no_recoil_func", 1)
```
- регистрируем хам который будет выполнять ```
no_recoil_func
```
функцию при стрельбе с **ak47**  
3. ```
new id = pev(weapon,pev_owner)
```
- узнаём кто хозяин оружия и записываем в переменную **id**  
4. ```
set_user_recoil(id,0.0)
```
устанавливаем отдачу у игрока при стрельбе с отлавливаемого оружия  
Остальная часть кода надеюсь вам ясна и не нуждается в обьяснении  
**Ссылка на скачивание**  
Вы не можете скачивать файлы с нашего сервера (442 байта)  
  
**Я не жадный,у меня лишь одна просьба,не меняйте в чужих плагинах авторов,экспериментируйте на здоровье** ![fellow](http://amxxmodx.ru/engine/data/emoticons/fellow.gif)
