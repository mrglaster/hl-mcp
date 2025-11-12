# SQL_NextResultSet функция активирует следующий резалтсет в запросе
[SQLx](http://amxxmodx.ru/sqlx/)
Инфо из **sql.inc:**  
```
/**  
 * For queries which return multiple result sets, this advances to the next   
 * result set if one is available.  Otherwise, the current result set is   
 * destroyed and will no longer be accessible.  
 *  
 * This function will always return false on SQLite, and when using threaded   
 * queries in MySQL.  Nonetheless, it has the same effect of removing the last   
 * result set.  
 *  
 * @param query        Query Handle.  
 * @return            True on success, false on failure.  
 */  
native bool:SQL_NextResultSet(Handle:query);
```
  
  
**Синтаксис:**  

SQL_NextResultSet(Handle:query)
  

    * **Handle:query** - Идентификатор запроса  

  
  
**Тип функции:**  
Native   
  
**Пример:**  
[code=pawn][/code]  
--  
**Описание:**  
--
