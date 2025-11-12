# socket_open Функция открывает соединение с удаленным хостом
[The Sockets Module](http://amxxmodx.ru/sockets/) [sockets.inc](http://amxxmodx.ru/sockets/socketsinc/)
Функция **socket_open** открывает соединение с нужным сервером по определенному порту и протоколу.  
  
Инфо из **socets.inc:**  
```
/* Opens a new connection to hostname:port via protocol (either SOCKET_TCP or SOCKET_UDP),  
 * returns a socket (positive) or negative or zero on error.  
 * States of error:  
 * 0 - no error  
 * 1 - error while creating socket  
 * 2 - couldn't resolve hostname  
 * 3 - couldn't connect to given hostname:port   
*/  
  
native socket_open(const _hostname[], _port, _protocol = SOCKET_TCP, &_error);
```
  
  
**Синтаксис:**  

socket_open(const _hostname[], _port, _protocol = SOCKET_TCP, &_error)
  

    * **const _hostname[]** - Имя хоста или ip адреса   

    * **_port,** - Порт   

    * **_protocol = SOCKET_TCP** - Тип протокола TCP/UTP:  
```
// Используйте SOCKET_TCP для TCP Socket соединения  
#define SOCKET_TCP 1  
// Используйте SOCKET_UDP для UDP Socket соединения  
#define SOCKET_UDP 2  

```

    * **& _error** - Переменная для сохранения ошибки, если таковая есть. Возможные ошибки:
      * 0 - no error  

      * 1 - error while creating socket  

      * 2 - couldn't resolve hostname  

      * 3 - couldn't connect to given hostname:port   

  

Функция вернет идентификатор сокета при успешном соединении, 0 при ошибке  
  
**Тип функции:**  
Native   
  
**Пример и описание:**  
[**Урок 22. Работа с сокетами**](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2xlc3NvbnMtb24tcGF3bi80NzktdXJvay1oaC1yYWJvdGEtcy1zb2tldGFtaS5odG1s)
