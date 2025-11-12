# Релиз плагина - Chat_Info
[Готовые скрипты](http://amxxmodx.ru/scripts/)
**Автор:** [Valer4](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L3VzZXIvVmFsZXI0Lw%3D%3D)  
**Версия:** 1.0 специально для http://amxxmodx.ru  
**Плагин:** показывает цветные сообщения с нужной Вам информацией в чат игрокам,через некоторое время после смерти, если игрок ещё мёртв.  
Для работы необходимы плагин colorchat и инклуд chatcolor.  
Количество сообщений не ограничено.  
Квар - ci_delay - через сколько секунд после смерти показывать сообщения, по умолчанию 13.  
Команда для игроков - ci - включить/отключить показ сообщений, в общий или командный чат, со слешем или без. Её значение сохраняется в конфиге у игроков - setinfo chat_info ci_on/ci_off.  
  
В папку **\cstrike\addons\amxmodx\data\lang** добавляем файл **chat_info.txt** и записываем в него:  

[ru]  
CI_ON = Показ сообщений об особенностях сервера - Включен!  
CI_OFF = Показ сообщений об особенностях сервера - Отключен!  
TEXT_1 = Ваше !gсообщение !t1  
TEXT_2 = Ваше !gсообщение !t2  
TEXT_3 = Ваше !gсообщение !t3  
TEXT_4 = Ваше !gсообщение !t4  
TEXT_5 = Ваше !gсообщение !t5  
  
[en]  
CI_ON = Показ сообщений об особенностях сервера - Включен!  
CI_OFF = Показ сообщений об особенностях сервера - Отключен!  
TEXT_1 = Ваше !gсообщение !t1  
TEXT_2 = Ваше !gсообщение !t2  
TEXT_3 = Ваше !gсообщение !t3  
TEXT_4 = Ваше !gсообщение !t4  
TEXT_5 = Ваше !gсообщение !t5
  
  
Заменяем "Ваше сообщение N" на нужное и сохраняем.  
Если ваше сообщение на русском, Вам понадобиться текстовый редактор(например AkelPad) позволяющий сохранять в кодировке 65001(UTF-8) без галочки BOM.  
Доступные цвета: красный по умолчанию и зелёный.  
Чтобы изменить цвет файле **chat_info.txt** перед нужным словом поставьте !g - зелёный или !t - красный.  
  
Исходный код плагина:  
```
#include<amxmodx>  
#include<chatcolor>  
  
new g_CI_Deaths[32]  
  
new c_CI_Delay  
  
public plugin_init()  
{  
    register_plugin("[http://amxxmodx.ru] Chat_Info", "1.0", "Valer4")  
    c_CI_Delay = register_cvar("ci_delay", "13.0")  
    register_clcmd("say ci", "ci_switch")  
    register_clcmd("say /ci", "ci_switch")  
    register_clcmd("say_team ci", "ci_switch")  
    register_clcmd("say_team /ci", "ci_switch")  
    register_dictionary("chat_info.txt")  
}  
  
public client_death(CI_Not_Used, CI_User_Dead_A)  
{  
    new CI_Chat_Info_A[32]  
    get_user_info(CI_User_Dead_A, "chat_info", CI_Chat_Info_A, 31)  
    if(!equali(CI_Chat_Info_A, "ci_off"))  
    {  
        set_task(get_pcvar_float(c_CI_Delay), "ci_message", CI_User_Dead_A)  
    }  
}  
  
public ci_message(CI_User_Dead_B)  
{  
    if(!is_user_alive(CI_User_Dead_B))  
    {  
        new CI_Data[192], CI_Data_B[192]  
        g_CI_Deaths[CI_User_Dead_B] ++  
        format(CI_Data, 191, "TEXT_%d", g_CI_Deaths[CI_User_Dead_B])  
        format(CI_Data_B, 191, "%L", CI_User_Dead_B, CI_Data)  
        if(!equali(CI_Data_B, "ML_NOTFOUND: TEXT_%d", g_CI_Deaths[CI_User_Dead_B]))  
        {  
            client_print_color(CI_User_Dead_B, Red, CI_Data_B)  
        }  
    }  
}  
  
public ci_switch(CI_PID)  
{  
    new CI_Chat_Info_B[32]  
    get_user_info(CI_PID, "chat_info", CI_Chat_Info_B, 31)  
    if(!equali(CI_Chat_Info_B, "ci_off"))  
    {  
        client_cmd(CI_PID, "setinfo chat_info ci_off")  
        client_print_color(CI_PID, Red, "%L", CI_PID, "OFF")  
        return PLUGIN_HANDLED  
    }  
    else  
    {  
        client_cmd(CI_PID, "setinfo chat_info ci_on")  
        client_print_color(CI_PID, Red, "%L", CI_PID, "ON")  
        return PLUGIN_HANDLED  
    }  
    return PLUGIN_CONTINUE  
}
```
  
Вы не можете скачивать файлы с нашего сервера
