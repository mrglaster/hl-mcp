# SQL_SimpleQuery Функция выполняет запрос к базе данных (используйте если вам не важен результат запроса).
[SQLx](http://amxxmodx.ru/sqlx/)
Иногда нет необходимости в точности данных и результат запроса не столь важен, но зато не страдают ресурсы на перевыполнения запроса.  
Функция **SQL_SimpleQuer** отправил запрос к базе данных:  
Инфо из **sql.inc:**  
```
/**  
 * Use this for executing a query where you don't care about the result.  
 * Returns 0 on failure, 1 on success  
 */  
stock SQL_SimpleQuery(Handle:db, const query[], error[]="", maxlength=0, &rows=0)  
{  
    new Handle:hQuery = SQL_PrepareQuery(db, "%s", query);  
      
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
[code][/code]  

    * **Handle:db** - Дескриптор БД  

    * **const query[]** - Запрос  

    * **error[]=""** - Массив для текста ошибки  

    * **maxlength=0** - Длина массива  

    * ** &rows=0** -   

Функция вернет 1 если запрос удачен и 0 если нет.  
  
**Тип функции:**  
stock  
  
**Пример:**  
--  
  
**Описание:**  
--
