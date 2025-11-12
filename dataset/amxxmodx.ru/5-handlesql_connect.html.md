# SQL_Connect Функция устанавливает соединение с базой данных
[SQLx](http://amxxmodx.ru/sqlx/)
**Handle:SQL_Connect**  
Инфо из **sql.inc** :  
```
/**  
 * Opens a database connection.  
 * Returns an SQL handle, which must be freed.  
 * Returns Empty_Handle on failure.  
 */  
native Handle:SQL_Connect(Handle:cn_tuple, &errcode, error[], maxlength);
```
  
  
**Handle:SQL_Connect** - открывает соединение с базой данных  
**Синтаксис:**  
Handle:SQL_Connect ( Handle:cn_tuple, &errcode, error[], maxlength )  
  
**Пример:**  
```
  
new Handle:SQL_Connection   
/*...*/  
public plugin_cfg(){  
  
    /*...*/  
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
  
  
[Функция SQL_MakeDbTuple и для чего она нужна](http://amxxmodx.ru/sqlx/6-sql_makedbtuple.html).
