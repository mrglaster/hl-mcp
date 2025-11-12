# sqlite_TableExists Функция проверяет существует ли таблица (sqlite)
[SQLx](http://amxxmodx.ru/sqlx/)
Инфо из **sql.inc:**  
```
/**  
 * This function can be used to find out if a table in a Sqlite database exists.  
 * (updated for newer API)  
 */  
stock bool:sqlite_TableExists(Handle:db, const table[])  
{  
    new Handle:query = SQL_PrepareQuery(  
                    db,  
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='%s' LIMIT 1;",   
                    table);  
                      
    if (!SQL_Execute(query) || !SQL_NumResults(query))  
    {  
        SQL_FreeHandle(query);  
        return false;  
    }  
      
    SQL_FreeHandle(query);  
  
    return true;  
}
```
  
  
**Синтаксис:**  

sqlite_TableExists(Handle:db, const table[])
  

    * **Handle:db** - Дескриптор базы данных  

    * **const table[])** - Имя таблицы  

  
  
**Тип функции:**  
stock   
  
**Пример:**  
--  
**Описание:**  
--
