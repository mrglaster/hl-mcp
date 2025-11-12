# vformat Функция для преобразование массивов.
[string.inc](http://amxxmodx.ru/core/stringinc/) [ColorChat - Цветные сообщения игрокам](http://amxxmodx.ru/colorchat/)
Из **string.inc**  
```
/* Replacement for format_args.  Much faster and %L compatible.  
 * This works exactly like vsnprintf() from C.  
 * You must pass in the output buffer and its size,  
 *  the string to format, and the number of the FIRST variable  
 *  argument parameter.  For example, for:  
 *  function (a, b, c, ...)  
 *  You would pass 4 (a is 1, b is 2, c is 3, et cetera).  
 * There is no vformatex().  
 */  
native vformat(buffer[], len, const fmt[], vararg);
```
  
  
Тип функции : **Native**  
Используется для перевода массивов без размера в массив с размером   
В примере будет использована stock ChatColor (раскраска чата):  
```
stock ColorChat(const id, const Msg[], any:...) // id = ид игрока , Msg[] = наше сообщение , any:... = означает что ChatColor может содержать мултиязычность и получения разных кваров и т.д.   
{  
 new msg[192] // наш массив который будет содержать сообщение   
 vformat(msg, 191, Msg, 3) // форматируем сообщение   
  
 replace_all(msg, sizeof(msg), "!g", "^4") // Зеленый цвет   
 replace_all(msg, sizeof(msg), "!t", "^3") // Цвет команды  
 replace_all(msg, sizeof(msg), "!y", "^1") // Дефолтный цвет (желтый)  
  
 new index, MsgType // index = массив который будет содержать ид игрока или индексы всех игроков, MsgType = будет содержать тип сообщения   
  
 if(id) // Будем проверять кому отправляется сообщение   
 {  
  MsgType = MSG_ONE // Будем отправлять сообщение одному игрока   
  index = id  
 }else{ // Если отправляем всех игроков  
  MsgType = MSG_ALL // Будем отправлять сообщение всем игрокам   
  index = FindPlayer()  
 }  
   
 message_begin(MsgType, get_user_msgid("SayText"), _, index)  
 write_byte(index)  
 write_string(msg)  
 message_end()  
}  
  
FindPlayer() // Будет получать всех игроков которые находятся на сервере  
{  
 new i = -1 // Индекс последнего игрока  
 while(i <= get_maxplayers())  
  if(is_user_connected(i))  
   return i  
   
 return -1  
}  

```

