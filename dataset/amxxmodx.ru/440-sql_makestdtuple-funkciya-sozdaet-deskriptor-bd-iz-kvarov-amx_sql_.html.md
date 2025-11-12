# SQL_MakeStdTuple Функция создает дескриптор БД из кваров amx_sql_*
[SQLx](http://amxxmodx.ru/sqlx/)
Функция создает дескриптор БД из файла конфига sql.cfg  
Инфо из **sql.inc:**  
```
stock Handle:SQL_MakeStdTuple(timeout = 0)  
{  
    static host[64], user[32], pass[32], db[128];  
    static get_type[12], set_type[12];  
      
    get_cvar_string("amx_sql_host", host, 63);  
    get_cvar_string("amx_sql_user", user, 31);  
    get_cvar_string("amx_sql_pass", pass, 31);  
    get_cvar_string("amx_sql_type", set_type, 11);  
    get_cvar_string("amx_sql_db", db, 127);  
      
    SQL_GetAffinity(get_type, 12);  
      
    if (!equali(get_type, set_type))  
    {  
        if (!SQL_SetAffinity(set_type))  
        {  
            log_amx("Failed to set affinity from %s to %s.", get_type, set_type);  
        }  
    }  
      
    return SQL_MakeDbTuple(host, user, pass, db, timeout);  
}  

```
  
  
**Синтаксис:**  

SQL_MakeStdTuple(timeout = 0)
  
  
  
**Тип функции:**  
Native   
  
**Пример:**  
--  
  
**Описание:**  
--
