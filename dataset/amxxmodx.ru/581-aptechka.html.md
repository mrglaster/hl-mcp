# Аптечка
[Готовые плагины](http://amxxmodx.ru/amxx_plugins/)
Написал плагин на аптечку(без наворотов),для новичков отлично пойдет!  
```
  
#include <amxmodx>  
#include <amxmisc>  
#include <fun>  
#include <cstrike>  
  
#define PLUGIN "First Aid Kit"  
#define VERSION "1.0"  
#define AUTHOR "True_Hacker"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    register_clcmd("say /medkit", "medkit") //регистрируем команду для покупки аптечки  
}  
public plugin_precache() //эта функция вызывается при старте сервера,она проверяет есть ли нужные файлы у клиента  
{  
    precache_sound("medkit/medkit.wav") //проверяем есть ли файл у клиента,если нет скачиваем  
}  
  
public medkit(id)  
{  
    new money = cs_get_user_money(id) //получаем текущее количество денег игрока  
    new medkit_cost = 1500 //стоимость аптечки  
    new money2 = money - medkit_cost //получаем кол-во денег после покупки  
    if( money2 < 0 ) //если их меньше нуля  
    {  
        client_print(id,print_chat, "Not Engoy Money") //выдаем сообщение об этом  
    }  
    if( money2 >= 0 ) //если денег хватает  
    {  
        new cur_hp = get_user_health(id) //получаем текущее количество жизней игрока  
        if( cur_hp < 100 ) //если жизней меньше 100,то установим ему эти полные 100HP  
    {  
        emit_sound(id,0,"medkit/medkit.wav",1.0,1.0,0,100) //проигрываем звук  
        cs_set_user_money(id, money2) //устанавливаем кол-во денег которые остались у игрока после покупки  
        client_print(id,print_chat, "You Are Buy MedKit!!!") //оповещаем игрока о покупке(необязательно) т.к уже об этом дает знать звук  
        set_user_health(id, 100) //собственно устанавливаем игроку 100HP  
    }  
}  
}  

```
  
Не забываем говорить спасибо! ![smile](http://amxxmodx.ru/engine/data/emoticons/smile.gif)
