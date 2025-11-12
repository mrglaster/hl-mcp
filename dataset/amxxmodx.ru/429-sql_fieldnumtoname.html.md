# SQL_FieldNumToName Функция возвращает имя столбца
[SQLx](http://amxxmodx.ru/sqlx/)
Функция SQL_FieldNumToName возвращает имя столбца.  
  
Инфо из **sql.inc:**  
```
/**   
 * Returns the name of a column.  
 * Errors on a bad field number.  
 */  
native SQL_FieldNumToName(Handle:query, num, name[], maxlength);
```
  
  
**Синтаксис:**  

SQL_FieldNumToName(Handle:query, num, name[], maxlength)
  

    * **Handle:query** - Идентификатор запроса.  

    * **num** - Номер столбца  

    * **name[]** - Массив для его имени  

    * **maxlength** - Максимальная длина  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
--
