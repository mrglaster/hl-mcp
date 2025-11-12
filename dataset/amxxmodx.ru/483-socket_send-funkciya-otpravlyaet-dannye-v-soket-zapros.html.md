# socket_send Функция отправляет данные в сокет (запрос)
[The Sockets Module](http://amxxmodx.ru/sockets/) [sockets.inc](http://amxxmodx.ru/sockets/socketsinc/)
Что бы получить ответ от удаленного сервера, его нужно о чем то спросить, функция **socket_send** и занимается отправкой запроса к серверу.  
  
Инфо из **sockets.inc:**  
```
/* Sends data to the Socket */  
  
native socket_send(_socket, const _data[], _length);
```
  
  
**Синтаксис:**  

socket_send(_socket, const _data[], _length)
  

    * **_socket** - Идентификатор открытого соект соединения  

    * **const _data[]** - Запрос  

    * **_length** - Длина запроса  

  
  
**Тип функции:**  
Native  
  
**Пример и описание:**  
[**Урок 22. Работа с сокетами**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2xlc3NvbnMtb24tcGF3bi80NzktdXJvay1oaC1yYWJvdGEtcy1zb2tldGFtaS5odG1s)
