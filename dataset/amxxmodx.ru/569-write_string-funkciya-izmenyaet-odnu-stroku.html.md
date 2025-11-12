# write_string Функция изменяет одну строку
[Ядро AMXx](http://amxxmodx.ru/core/) [messages.inc ](http://amxxmodx.ru/core/messagesinc/)
Функция write_string используется только совместно с функцией [message_begin](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteHhtb2R4LnJ1L2NvcmUvbWVzc2FnZXNpbmMvMzEyLW1lc3NhZ2VfYmVnaW4tZnVua2NpeWEtZ2VuaXJpcnVldC1rbGllbnRza2llLXNvb2JzY2hlbml5YS5odG1s)  
  
Инфо из **messages.inc** :  
```
  
native write_string(const x[])
```
  
  
**Натив :**  
write_string(const x[])  
  
const x[] = переменная должна содержать строку  
  
Тип функции :   
**Native**  
  
Пример :  
```
  
...  
stock PrintMessageUser(id, msg[], any:...) // Будем отсылать сообщение игроку  
{  
 message_begin(MSG_ONE, get_user_msgid("SayText"), _, id)  
 write_byte(id) // Игрок   
 write_string(msg) // Сообщение   
 message_end() // Конец сообщения   
}  
  

```

