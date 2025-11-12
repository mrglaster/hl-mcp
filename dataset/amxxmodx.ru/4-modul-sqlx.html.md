# Модуль SQLx
[SQLx](http://amxxmodx.ru/sqlx/)
**SQlx** - Официальный модуль для работы с базой данных MySQL. Поддерживается AMXX начиная с версии 1,72.  
  
**Подключение:**   
```
#include <sqlx>
```
  
**SQLx** - Это с нуля написанный модуль, призван стать заменой устаревшего **DBI**. SQLx Значительно лучше работает ( по словам разработчиков)  
  
**Различия DBI и SQLx:**  

    * Возможность подготавливать запросы, перед их выполнением  

    * Информация о соединение с БД кэшируется в блоке "кортеж"  

    * Итерация результата более интуитивна чем dbi_nextrow.  

  
В SQLx появились поточные запросы, это очень важно для тех, у кого медленное соединение с базой данных, не будет лагов из за медленного соединения или большого запроса. Старый модуль работал не устойчиво и часто мог вызывать ошибку.  
  

## Функции модуля SQLx
  
**Nativs:**  
[**Handle:SQL_MakeDbTuple**](http://amxxmodx.ru/sqlx/6-sql_makedbtuple.html) Кэширует настроки к базе данных  
[**Handle:SQL_Connect**](http://amxxmodx.ru/sqlx/5-handlesql_connect.html) устанавливает соединение с базой данных  
[**Handle:SQL_PrepareQuery**](http://amxxmodx.ru/sqlx/7-sql_preparequery.html) подготавливает запрос к базе данных  
[**SQL_FreeHandle**](http://amxxmodx.ru/sqlx/16-sql_freehandle-funkciya.html) освобождает дескриптор SQL  
[**SQL_QuoteString**](http://amxxmodx.ru/sqlx/383-sql_quotestring-funkciya-ekraniruet-odinarnye-kavychki-v-zaprose.html) экранирует одинарные кавычки в запросе  
[**SQL_QuoteStringFmt**](http://amxxmodx.ru/sqlx/384-sql_quotestringfmt-funkciya-ekraniruet-odinarnye-kavychki-dlya-zaprosa-s-vozmozhnostyu-formatirovaniya.html) экранирует одинарные кавычки для запроса с возможностью форматирования  
[**SQL_ThreadQuery**](http://amxxmodx.ru/sqlx/381-sql_threadquery-funkciya-gotovit-i-vypolnyaet-potochnyy-zapros-k-baze-dannyh.html) готовит и выполняет поточный запрос к базе данных  
[**SQL_Execute**](http://amxxmodx.ru/sqlx/9-sql_execute-funkciya-vypolneniya-zaprosa-k-bd.html) Выполняет подготовленный запрос к базе данных  
[**SQL_QueryError**](http://amxxmodx.ru/sqlx/385-sql_queryerror-funkciya-poluchaet-tekst-oshibki-zaprosa-k-baze-dannyh.html) получает текст ошибки запроса к базе данных  
[**SQL_MoreResults**](http://amxxmodx.ru/sqlx/186-sql_moreresults-funkciya-poluchet-rezultativnost-zaprosa.html) получает результативность запроса  
[**SQL_IsNull**](http://amxxmodx.ru/sqlx/386-sql_isnull.html) возвращает Null значение ячейки или нет.  
[**SQL_ReadResult**](http://amxxmodx.ru/sqlx/191-sql_readresult-funkcya-poluchaet-rezultaty-sql-zaprosa.html) получает результаты SQL запроса  
[**SQL_NextRow**](http://amxxmodx.ru/sqlx/192-sql_nextrow-i-sql_readresult-chast-2-poluchenie-mnozhestva-rezultatov-zaprosa.html) получение множества результатов запроса  
[**SQL_AffectedRows**](http://amxxmodx.ru/sqlx/199-sql_affectedrows-funkciya-vozvraschaet-kolichestvo-strok-s-kotorymi-vzamodeystvoval-zapros.html) возвращает количество строк, с которыми взамодействовал запрос  
[**SQL_NumResults**](http://amxxmodx.ru/sqlx/197-sql_numresults-funkciya-poluchaet-kolichestvo-rezultatov-zaprosa.html) получает количество результатов запроса  
[**SQL_NumColumns**](http://amxxmodx.ru/sqlx/198-sql_numcolumns-funkcya-vozvraschaet-kolichestvo-stolbcov-v-rezultate-zaprosa.html) возвращает количество столбцов в результате запроса  
[SQL_FieldNumToName](http://amxxmodx.ru/sqlx/429-sql_fieldnumtoname.html) возвращает имя столбца.  
[SQL_FieldNameToNum](http://amxxmodx.ru/sqlx/430-sql_fieldnametonum-funkciya-vozvraschaet-nomer-kolonki-po-ee-imeni.html) возвращает номер колонки по ее имени  
[**SQL_Rewind**](http://amxxmodx.ru/sqlx/431-sql_rewind-funkciya-vozvrata-k-pervoy-stroke-rezultatov.html) функция возврата к первой строке результатов  
[**SQL_GetInsertId**](http://amxxmodx.ru/sqlx/432-sql_getinsertid-funkciya-vozvraschaet-id-stroki-poslednego-insert-zaprosa.html) возвращает id строки последнего INSERT запроса  
[**SQL_GetAffinity**](http://amxxmodx.ru/sqlx/433-sql_getaffinity-funkciya-vozvraschaet-s-kakim-drayverom-rabotaet-dannyy-plagin.html) возвращает с каким драйвером работает данный плагин  
[SQL_SetAffinity](http://amxxmodx.ru/sqlx/434-sql_setaffinity-funkciya-zadaet-kakoy-drayver-ispolzovat.html) задает какой драйвер использовать  
[**SQL_GetQueryString**](http://amxxmodx.ru/sqlx/382-sql_getquerystring-funkciya-poluchaet-vypolnennyy-zapros-k-baze-dannyh-tekst-samogo-zaprosa.html) получает выполненный запрос к базе данных ( текст самого запроса)  
[bool:SQL_NextResultSet](http://amxxmodx.ru/sqlx/435-sql_nextresultset-funkciya-aktiviruet-sleduyuschiy-rezaltset-v-zaprose.html) активирует следующий резалтсет в запросе  
  
**Stocks:**  
[bool:sqlite_TableExists](http://amxxmodx.ru/sqlx/436-sqlite_tableexists-funkciya-proveryaet-suschestvuet-li-tablica-sqlite.html) проверяет существует ли таблица (sqlite)  
[SQL_SimpleQuery](http://amxxmodx.ru/sqlx/437-sql_simplequery-funkciya-vypolnyaet-zapros-k-baze-dannyh-kto-vam-ne-vazhen-rezultat-ee-vypolneniya.html) отправляет запрос где не важен результат  
[SQL_SimpleQueryFmt](http://amxxmodx.ru/sqlx/438-sql_simplequeryfmt-funkciya-otpravki-zaprosa-gde-nevazhen-rezultat-s-vozmozhnostyu-formatirovaniya-zaprosa.html) отправляет запрос где не важен результат с возможность форматирования запроса.  
[SQL_QueryAndIgnore](http://amxxmodx.ru/sqlx/439-sql_queryandignore-funkciya-dlya-vypolneniya-zaprosa-i-ne-zabotitsya-ob-oshibkah.html) для выполнения запроса без забот о ошибках  
[Handle:SQL_MakeStdTuple](http://amxxmodx.ru/sqlx/440-sql_makestdtuple-funkciya-sozdaet-deskriptor-bd-iz-kvarov-amx_sql_.html) для создания дескриптора из кваров amx_sql_* ( файл sql.cfg)
