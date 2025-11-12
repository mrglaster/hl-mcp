# SQL_Execute Функция выполнения запроса к БД
[SQLx](http://amxxmodx.ru/sqlx/)
**SQL_Execute** - Выполняет подготовленный заранее запрос к базе данных.  
  
Инфо из **Sqlx.inc** :  
```
/**  
 * Executes a query.  
 * Returns 1 if the query succeeded.  
 * Returns 0 if the query failed.  
 * NOTE: You can call this multiple times as long as its parent  
 *  connection is kept open.  Each time the result set will be freed  
 *  from the previous call.  
 */  
native SQL_Execute(Handle:query);
```
  
  
**Синтаксис:**  
SQL_Execute ( Handle:query )  
  
**Пример:**  
```
/.../  
public sqlx_select(id){  
      
    //Подготовка Запроса  
    new Handle:query = SQL_PrepareQuery(SQL_Connection,"SELECT * FROM `test`")  
    // Выполняем запрос к базе даанных  
    SQL_Execute (query)  
/.../  
}
```
  
  
Возвращает 1, если запрос успешно выполнен.  
Возвращает 0, если запрос не выполнен.  
  
Данную функцию можно выполнять многократно, при условии что родительское соединение с базой данных еще открыто.
