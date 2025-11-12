# plugin_cfg Функция вызывает при перезагрузке или старте сервера после plugin_ini
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
**plugin_cfg** - Вызывается после того как была вызвана функция [plugin_init](http://amxxmodx.ru/core/amxmodxinc/11-plugin_init-funkciya-registracii-plagina.html)  
Вызывается всегда. Используется для обработки Кваров,Коннектов к базам данных, чтение файлов конфига и т.п.  
  
Инфо из **amxmodx.inc**  
```
/* Function is called when all plugin_init from plugins  
* were called, so all commmands and cvars should be already registered. */  
forward plugin_cfg();
```
  
  
**Синтаксис:**  
**public plugin_cfg ( )**  
  
**Пример:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <sqlx>  
  
#define PLUGIN "Plugin config"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
}  
public plugin_cfg(){  
      
    new host[33],dbase[33],user[33],pass[33]  
    get_cvar_string("SQLx_host",host,30)  
    get_cvar_string("SQLx_db",dbase,30)  
    get_cvar_string("SQLx_user",user,30)  
    get_cvar_string("SQLx_password",pass,30)  
          
    SQL_Tuple = SQL_MakeDbTuple(host,user,pass,dbase) // Создание картежа данных для соединения с БД  
    new err, error[256]  
    SQL_Connection = SQL_Connect(SQL_Tuple, err, error, charsmax(error)) // Соединение с БД  
      
}
```

