# socket_change Функция проверяет изменения в буфере
[The Sockets Module](http://amxxmodx.ru/sockets/) [sockets.inc](http://amxxmodx.ru/sockets/socketsinc/)
Функция необходима для проверки получены данные от запроса или нет (в течении определенного времени).  
То есть функция проверяет изменение в буфере относительно последней проверки. Грубо говоря так:  
1) Есть пустой буфер  
2) Проверяем его - в буфер было что то (допустим 1) помещено в результате запроса, функция вернет что были изменения.  
3) Запускаем снова и теперь ни чего не приходило и в буфере по прежнему осталась 1, функция вернет что изменений не было.  
  
Инфо из **sockets.inc:**  
```
/* This function will return true if the state (buffer content) have changed within the last recieve or  
* the timeout, where timeout is a value in µSeconds, (1 sec =1000000 µsec).   
* Use to check if new data is in your socket. */  
  
native socket_change(_socket, _timeout=100000);
```
  
  
**Синтаксис:**  

socket_change(_socket, _timeout=100000)
  

    * **_socket** - Идентификатор открытого соединения  

    * **_timeout=100000** - Таймаут ( по умолчанию 1 секунда = 1000000 мкс)  

  
  
**Тип функции:**  
Native  
  
**Пример и описание:**  
[**Урок 22. Работа с сокетами**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2xlc3NvbnMtb24tcGF3bi80NzktdXJvay1oaC1yYWJvdGEtcy1zb2tldGFtaS5odG1s)
