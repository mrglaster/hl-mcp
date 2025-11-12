# cs_get_user_deaths Функция возвращает количество смертей игрока
[CStrike](http://amxxmodx.ru/cstrike/)
**cs_get_user_deaths** - Получение количества смертей игрока.  
Данная функция часто употребляется для ведения статистик.  
  
Инфо из **csrike.inc** :  
```
/* Returns player deaths. */  
native cs_get_user_deaths(index);
```
  
  
**Синтаксис:**  

cs_get_user_deaths ( index )
  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <cstrike>  
  
#define PLUGIN "Get user deaths"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    register_clcmd("say /deaths","my_deaths")  
      
}  
public my_deaths(id){  
      
    //Регистрируем массив  
    new MyDeaths[32]   
    //Получаем количество смертей для игрока и запсываем в массив  
    MyDeaths[id] = cs_get_user_deaths(id)  
      
    //Выводим количество смертей в HuD сообщении  
    set_hudmessage(0, 255, 0, -1.0, 0.25, 0, 6.0, 12.0)  
    show_hudmessage(id, "You Deaths is %d",MyDeaths[id] )  
      
    //Выводим количество смертей в чат  
    client_print(id,print_chat,"TbI yMep %d pa3",MyDeaths[id])  
}  

```
  
  
**Описание:**  
В коде добавлены комментарии, думаю отдельного описание не требуется. Но для тех кому все таки необходимо, пар слов скажу.  
И так мы зарегистрировали команду **say /deaths** , которая вызывает функцию **my_deaths(id)** , в которй мы получаем необходимые нам данные, а именно количество смертей игрока (в данном случае наших) и выводим их в HuD сообщении и затем дублируем в чат.
