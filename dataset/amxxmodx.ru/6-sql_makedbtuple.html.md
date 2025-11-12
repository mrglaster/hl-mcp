# SQL_MakeDbTuple
[SQLx](http://amxxmodx.ru/sqlx/)
**Handle:SQL_MakeDbTuple** - Создание "коретжа" информации о соединении, для подключения к базе данных.  
**Внимание:** Это не соединение с базой данных, а только кеширвоание данных для соединения  
Инфо из **sqlx.in**  
```
/**  
 * Creates a connection information tuple.  
 * This tuple must be passed into connection routines.  
 * Freeing the tuple is not necessary, but is a good idea if you   
 *  create many of them.  You can cache these handles globally.  
 * !!NOTE!! I have seen most people think that this connects to the DB.  
 *   Nowhere does it say this, and in fact it does not.  It only caches  
 *   the connection information, the host/user/pass/etc.  
 *  
 * The optional timeout parameter specifies how long connections should wait before  
 * giving up.  If 0, the default (which is undefined) is used.  
 *  
 */  
native Handle:SQL_MakeDbTuple(const host[], const user[], const pass[], const db[], timeout=0);
```
  
  
  
**Синтаксис:**  
Handle:SQL_MakeDbTuple ( const host[], const user[], const pass[], const db[], timeout=0 )  
  
**Пример:**  
```
  
new Handle:SQL_Tuple  
new Handle:SQL_Connection   
/*...*/  
public plugin_cfg(){  
    new host[33],dbase[33],user[33],pass[33]  
    get_cvar_string("SQLx_host",host,30)  
    get_cvar_string("SQLx_db",dbase,30)  
    get_cvar_string("SQLx_user",user,30)  
    get_cvar_string("SQLx_password",pass,30)  
    SQL_Tuple = SQL_MakeDbTuple(host,user,pass,dbase) // Создание картежа данных для соединения с БД  
    new err, error[256]  
    SQL_Connection = SQL_Connect(SQL_Tuple, err, error, charsmax(error)) // Соединение с БД  
  
    if(SQL_Connection != Empty_Handle)  
    {  
        log_amx("[SQLx connect ok]") //Если соединение установлено   
        }else{  
        log_amx("[SQLX sql error] %s ",error) //Если нет и выводим причину(ошибку)  
        pause("a")  
    }  
  
}  
/*...*/  

```

