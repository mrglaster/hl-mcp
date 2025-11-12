# Плагин блокирует developer 1 режим и fps hack
[Готовые скрипты](http://amxxmodx.ru/scripts/)
Как-то очень давно я обмолвился, что расскажу, как можно заблокировать developer 1 и fps игроков больше 101. Пришло время, рассказываю.  
  
У меня на вооружении есть несколько готовых плагинов. Несколько от моего приятеля специально для <http://amxxmodx.ru>, а и один от всем известного скриптера **Exolent**.  
Но у них у всех есть один недостаток, это использование функции [hide_group=6]**query_client_cvar**[/hide_group], недостаток заключается в том, что если у вас есть плагин который использует данную функцию - то игроки с патчем 24 версии и ниже не смогут заходить на ваш сервер. Но по правде я уже давно не встречал людей играющих на столь древних патчах. И у меня на серверах данные плагины стояли без значимых потерь игроков.  
  
**Исходный код плагина:**  
[hide_group=6]```
#include <amxmodx>   
  
#define PLUGIN "[http://amxxmodx.ru] anti_developer"   
#define VERSION "1.3"   
#define AUTHOR "Leo Wyatt"   
new std_value = 0   
  
public plugin_init() {   
    register_plugin(PLUGIN, VERSION, AUTHOR)   
      
    register_cvar("developer_punish", "1", ADMIN_CVAR) // 0 = OFF; 1=KICK; 2=BAN   
}   
  
public client_command(id) {   
    if(is_user_connected(id) && !is_user_bot(id)) {   
        query_client_cvar(id, "developer", "cvar_check")   
        query_client_cvar(id, "developez", "cvar_check")   
    }   
}   
  
public cvar_check(id, const cvar[], const value[]) {   
    if(str_to_num(value)!=std_value && is_user_connected(id) && !is_user_bot(id)) {   
        new name[32]   
        get_user_name(id, name, 31)   
        server_cmd("say_team ^"@ %s used %s %s^"", name, cvar, value)   
          
        switch(get_cvar_num("developer_punish")) {   
            case 1: server_cmd("amx_kick #%d developer", get_user_userid(id))   
                case 2: server_cmd("amx_ban #%d 0 developer ", get_user_userid(id))   
            }   
          
        client_cmd(id, "%s %d", cvar, std_value)   
    }   
}
```
[/hide_group]  
Приведенный код плагина очень прост, он **выключает developer 1** у клиента, а так же может кикать и банить игрока. Но есть определенные нехороши дядьки, которые используют читы и юзают **developer****z**. По этому еще добавлена проверка и этого квара. Из настроек остается лишь квар **developer_punish** который может принимать значения:
    * 0 = OFF  

    * 1=KICK  

    * 2=BAN (amxban , время - навсегда)  

  
Так же плагин выдает сообщение в игровой чат.  
  
**Автор:** **Leo Wyatt**  
**Плагин:** **anti_developer**  
**Источник:** <http://amxxmodx.ru>  
**Скачать: Вы не можете скачивать файлы с нашего сервера**
