# engclient_print Функция отправляет сообщение игрок от движка
[Ядро AMXx](http://amxxmodx.ru/core/) [amxmodx.inc](http://amxxmodx.ru/core/amxmodxinc/)
Инфо из **amxmodx.inc:**  
```
/* Sends message to player by engine. Set index to 0 to send text globaly. */  
native engclient_print(player,type,const message[],any:...);
```
  
  
**Синтаксис:**  

engclient_print(player,type,const message[],any:...)
  

    * **player** - id игрока или 0 для всех  

    * **type** - Тип сообщения  

    * **const message[]** - Текст сообщения  

    * **any:...** - Данные для подстановки  

  
  
**Тип функции:**  
Native  
  
**Пример:**  
--  
  
**Описание:**  
Лучше используйте [**client_print**](http://amxxmodx.ru/core/amxmodxinc/39-client_print-tekstovoe-soobschenie-igrokam.html)
