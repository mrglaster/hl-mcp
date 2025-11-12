# socket_send2 Функция отправки запроса на удаленный сервер с возможностью отправки пустых байтов
[The Sockets Module](http://amxxmodx.ru/sockets/) [sockets.inc](http://amxxmodx.ru/sockets/socketsinc/)
Функция **socket_send2** отличается от **socket_send** только тем, что может отправлять запросы с нулевыми/пустыми байтами ( честно говоря я в этом не силен)  
  
Инфо из **sockets.inc:**  
```
/* Same as socket_send but Data can contain null bytes */  
  
native socket_send2(_socket, const _data[], _length);
```
  
  
**Синтаксис:**  

socket_send2(_socket, const _data[], _length)
  

    * **_socket** - Идентификатор открытого соединения  

    * **const _data[]** - Запрос  

    * **_length** - Длина запроса  

  
  
**Тип функции:**  
Native   
  
**Пример и описание:**  
[**Урок 22. Работа с сокетами**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2xlc3NvbnMtb24tcGF3bi80NzktdXJvay1oaC1yYWJvdGEtcy1zb2tldGFtaS5odG1s)
