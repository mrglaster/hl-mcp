# SQL_QueryAndIgnore Функция для выполнения запроса и не заботится об ошибках.
[SQLx](http://amxxmodx.ru/sqlx/)
Используйте данную функцию для того что бы не заботится об ошибки после запроса.  
  
Инфо из **sql.inc:**  
```
stock SQL_QueryAndIgnore(Handle:db, const queryfmt[], any:...)  
{  
    static query[4096];  
    new Handle:hQuery;  
    new ret;  
      
    vformat(query, sizeof(query)-1, queryfmt, 3);  
      
    hQuery = SQL_PrepareQuery(db, "%s", query);  
      
    if (SQL_Execute(hQuery))  
    {  
        ret = SQL_AffectedRows(hQuery);  
    } else {  
        ret = -1;  
    }  
      
    SQL_FreeHandle(hQuery);  
      
    return ret;  
}
```
  
  
**Синтаксис:**  

SQL_QueryAndIgnore(Handle:db, const queryfmt[], any:...)
  

    * **Handle:db** - Дескриптор БД  

    * **const queryfmt[]** - Запрос к базе даных  

    * **any:...** - Данны для форматирования запроса  

Функция вернет -1 если ошибка и 0 или более затронутых рядов в запросе.  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
