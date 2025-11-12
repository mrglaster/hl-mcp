# SQL_SimpleQueryFmt Функция отправки запроса где неважен результат с возможностью форматирования запроса
[SQLx](http://amxxmodx.ru/sqlx/)
Функция аналогична функции [SQL_SimpleQuery](http://amxxmodx.ru/sqlx/437-sql_simplequery-funkciya-vypolnyaet-zapros-k-baze-dannyh-kto-vam-ne-vazhen-rezultat-ee-vypolneniya.html), но имеет возможность форматирования запроса.  
  
Инфо из **sql.inc:**  
```
/**  
 * Use this for executing a query where you don't care about the result.  
 * Returns 0 on failure, 1 on success  
 */  
stock SQL_SimpleQueryFmt(Handle:db, error[]="", maxlength=0, &rows=0, const fmt[], any:...)  
{  
    static query_buf[2048];  
    vformat(query_buf, 2047, fmt, 6);  
      
    new Handle:hQuery = SQL_PrepareQuery(db, "%s", query_buf);  
      
    if (!SQL_Execute(hQuery))  
    {  
        SQL_QueryError(hQuery, error, maxlength);  
        SQL_FreeHandle(hQuery);  
        return 0;  
    }  
      
    rows = SQL_NumResults(hQuery);  
      
    SQL_FreeHandle(hQuery);  
      
    return 1;  
}
```
  
  
**Синтаксис:**  

SQL_SimpleQueryFmt(Handle:db, error[]="", maxlength=0, &rows=0, const fmt[], any:...)
  

    * **Handle:db** - Дескриптор БД  

    * **error[]=""** - Массив ошибок  

    * **maxlength=0** - его длина  

    * **& rows=0** -   

    * **const fmt[]** - Массив с запросом  

    * **any:...** - данные для форматирования  

  
  
**Тип функции:**  
stock  
  
**Пример:**  
--  
  
**Описание:**  
--
