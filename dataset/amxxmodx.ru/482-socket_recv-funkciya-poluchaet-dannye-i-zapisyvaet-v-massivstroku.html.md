# socket_recv Функция получает данные и записывает в массив(строку)
[The Sockets Module](http://amxxmodx.ru/sockets/) [sockets.inc](http://amxxmodx.ru/sockets/socketsinc/)
Функция для получения результата запроса и записи его в массив.  
  
Инфо из **sockets.inc:**  
```
/* Recieves Data to string with the given length */  
  
native socket_recv(_socket, _data[], _length);
```
  
  
**Синтаксис:**  

socket_recv(_socket, _data[], _length)
  

    * **_socket** - Идентификатор соединения  

    * **_data[]** - Массив куда записывать данные  

    * **_length** - Его длина  

  
  
**Тип функции:**  
Native  
  
**Пример и описание:**  
[**Урок 22. Работа с сокетами**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2xlc3NvbnMtb24tcGF3bi80NzktdXJvay1oaC1yYWJvdGEtcy1zb2tldGFtaS5odG1s)
