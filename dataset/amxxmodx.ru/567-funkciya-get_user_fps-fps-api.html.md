# Функция get_user_fps [FPS Api]
[Готовые скрипты](http://amxxmodx.ru/scripts/)
**Авторы:** .csF Dev Team  
**Версия:** 1.2  
  
**Описание:**  
С помощью этого плагина вы сможете измерить количество FPS игрока, я максимально уменьшил количество ложных показаний(их фактически нет).  
Использовать просто:  
1. Скачать исходник плагина get_user_fps.  
2. Скомпилировать его.  
3. Закинуть скомпилированый плагин в папку plugins у вас на сервере.  
4. Прописать плагин в plugins.ini(желательно в самом верху).  
5. Закинуть инклюд fps.inc в папку include.  
6. Дописать в своём плагине строчку #include  .  
7. И в вашем плагине, где нужно узнать fps игрока просто пишем get_user_fps(id) .  
  
**Используемые модули:**  
Engine  
  
**Список изменений:**  

1.0b - Релиз  
1.0 - get_maxplayers() - в глобальную, убрана проверка на коннект(стормозил) //Спасибо TurangaLeela  
1.1 - Забил выделенную память //Спасибо TurangaLeela, переместил корректировку fps из натива.
  
  
```
  
/* Отдельное спасибо TurangaLeela с amx-x.ru */  
#include <amxmodx>  
#include <engine>  
  
#define A "FPS"  
#define B "1.2"  
#define C ".csF Dev Team"  
  
#define TASK_ID 55055  
#define g_Maxplayers Fps[0][CONST]  
  
enum _:FPS_DATA  
{  
    COUNT,  
    CONST  
};  
  
new Fps[33][FPS_DATA];  
  
public plugin_init()  
{   
    register_plugin(A, B, C);  
      
    g_Maxplayers = get_maxplayers();  
    set_task(1.0, "Clear", TASK_ID, "", 0, "b");  
}  
  
public plugin_natives()  
    register_native("get_user_fps", "native_get_user_fps", 1);  
  
public native_get_user_fps(id)  
    return Fps[id][CONST];  
  
public client_PreThink(id)  
    Fps[id][COUNT]++;  
  
public Clear()  
{  
    for(new id = 1; id <= g_Maxplayers; id++)  
    {  
        Fps[id][CONST] = Fps[id][COUNT]+=3;  
        Fps[id][COUNT] = 0;  
    }  
}  
  
public client_connect(id)  
    Fps[id][COUNT] = 0;  
  
public client_disconnect(id)  
    Fps[id][COUNT] = 0;  

```
  
  
**Использование API в своём плагине или как я использую FPS Api:**  
  
```
  
#include <amxmodx>  
#include <amxmisc>  
#include <fps>  //Подключаем fps.inc в свой плагин  
  
#define A "FPS Controler"  
#define B "1.2"  
#define C ".csF Group"  
#define TASK 9999  
  
new max_fps;     //Создаём 2 глобальные переменные  
new task_time;  
  
public plugin_init()   
{   
    register_plugin(A, B, C);  
      
    register_cvar("csf_fps_control", "60");     //Регистрируем квар "csf_fps_control", он будет отвечать за время, через которое проверит фпс у игрока, после входа на сервер  
    register_cvar("csf_fps_max", "101");       //Регистрируем квар "csf_fps_max", он будет отвечать за максимальное количество fps у игрока  
}  
  
public plugin_cfg()  
{  
    task_time = get_cvar_float("csf_fps_control");    //Записываем в глобальную переменную число квара "csf_fps_control"  
    fps_max = get_cvar_num("csf_fps_max");    //Аналогично с "csf_fps_max"  
}  
  
public client_putinserver(id)  
    set_task(task_time, "FpsControl", id + TASK);         //Запускаем задание на функцию "FpsControl" через время, указанное в глобальной переменной "task_time" и с id игрока, к которому прибавили 9999  
  
public client_disconnect(id)  
    remove_task(id + TASK);     //Удаляем задание, если игрок выходит с сервера  
      
public FpsControl(id)  
{  
    id -= TASK;   //Вычитаем из id 9999, чтобы получить id игрока  
    new fps = get_user_fps(id);     //Создаём локальную переменную и в неё записываем значение fps игрока  
    if(fps > max_fps)    //Делаем проверку, если количество fps игрока больше, чем указанно в глобальной переменной "max_fps", то  
    {  
        new userid = get_user_userid(id);  //Создаём локальную переменную, записав в неё userid игрока  
        new name[32];  //Создаём массив, в него мы впишем ник игрока  
        get_user_name(id, name, charsmax(name));  //Вписываем ник игрока  
        client_print(0, print_chat, "Количество FPS игрока %s превысило ограничения сервера, FPS: %d!", name, fps);   //Выводим в чат информацию  
        client_print(0, print_chat, "Игрок %s удален с сервера!", name);  
        client_cmd(id, "developer 0");  //Выставляем игроку значение developer в 0  
        client_cmd(id, "fps_max 101");  //Выставляем игроку значение fps_max в 101  
        log_to_file("addons/amxmodx/logs/fps_control.log","Name: %s | ID: %d | SteamID: %d | IP: %d | FPS: %d", name, userid, fps) //Логируем действия  
        server_cmd("kick #%d ^"Обнаружены запрещенные настройки^"", userid);  //Кикаем игрока  
    }  
    return PLUGIN_HANDLED;  
}  

```
  
  
**Вложения:**  
Вы не можете скачивать файлы с нашего сервера  
Вы не можете скачивать файлы с нашего сервера  
Вы не можете скачивать файлы с нашего сервера  
  
Вот собственно и всё, я думаю, что Вы сами придумаете, как использовать функцию get_user_fps :)  
До встречи!
