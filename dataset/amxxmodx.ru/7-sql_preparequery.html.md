# SQL_PrepareQuery Функция подготавливает запрос к базе данных
[SQLx](http://amxxmodx.ru/sqlx/)
**SQL_PrepareQuery** - Функция подготовки (составления) запроса  
Инфо из **sql.in** :  
```
/**  
 * Prepares a query.  
 * The query must always be freed.  
 * This does not actually do the query!  
 */  
native Handle:SQL_PrepareQuery(Handle:db, const fmt[], any:...);
```
  
  
**Синтаксис:**  
Handle:SQL_PrepareQuery ( Handle:db, const fmt[], {Float,_}:... )  
  
**Пример:**  
```
  
public sqlx_select(id){  
  
    new Handle:query = SQL_PrepareQuery(SQL_Connection,"SELECT * FROM `test` WHERE name = '%d'",username)  
  
}
```
  
  
**Внимание:**  
SQL_PrepareQuery - не выполняет запрос, а только его подготавливает!  
Для выполнения подготовленного запроса используйте **SQL_Execute**
