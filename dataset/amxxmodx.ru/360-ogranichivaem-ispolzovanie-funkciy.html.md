# Ограничиваем использование функций
[Присланное](http://amxxmodx.ru/other/)
Раньше, возможно даже и сейчас на форумах было множество вопросов - "**Как блокировать команду на *n раундов**?".В данном уроке я вам расскажу, как можно ограничивать использование функции для всех игроков, а так же для определенного игрока.  
  
Начнем!  
  
Первое, что мы будем делать - это блокировать команду для всех на определенное количество раундов:  
  
1)Создадим новый массив и назовем его к примеру **block**  
```
new block
```
  
  
2)Далее создадим функцию, в которой будет выполняться какое-либо действие, у меня оно будет **client_cmd(id, "say Hello amxxmodx.ru")**  
  
```
public test(id)  
{  
   client_cmd(id, "say Hello amxxmodx.ru")  
}
```
  
  
3)Далее создаем условия, при котором будет блокировать использование функции **test**. Для этого потребуется создать простое условия, при котором функция будет открываться только первому игроку, который выполнил эту функцию.  
  
**Код проверки будет следующим:**  
```
public test(id)  
{  
   if(block<=0)  
   {  
      client_cmd(id, "say Hello amxxmodx.ru")  
      block = 10  
   }else{  
      client_print(id, print_chat, "Block use command.Wait %d", block)  
      return PLUGIN_HANDLED  
   }  
   return PLUGIN_HANDLED  
}
```
  
  
Что же мы сделали спросите вы?Мы сделали проверку, использовалась ли уже функция или нет.Если же она не использовалась, то мы устанавливаем значение массива **block** равным **10** раундов.При повторном обращении к функции игроку будет заблокирован доступ и указано сколько раундов требуется ждать до следующего возможного запуска.  
  
4)Заключающим этапом нашей работы последует отлов нового раунда и вычитание массива **block**  
  
**Регистрируем новый event в plugin_init**  
  
```
register_event("HLTV", "newround", "a", "1=0", "2=0")
```
  
  
**Создаем функцию вычитание раунда из массива _block_**  
  
```
public newround()  
{  
   --block  
}
```
  
  
Вот и всё, на этом первая часть урока подошла к концу.Вот рабочий пример плагина, можете потренироваться  
  
```
#include <amxmodx>  
   
new block  
  
public plugin_init(){  
    register_plugin("[TUT]Block function all players","1.0","NextPawno")  
  
    register_event("HLTV", "newround", "a", "1=0", "2=0")  
  
    register_clcmd("say /test", "test")  
}  
   
public newround()  
{  
   --block  
}  
  
public test(id)  
{  
   if(block<=0)  
   {  
      client_cmd(id, "say Hello amxxmodx.ru")  
      block = 10  
   }else{  
      client_print(id, print_chat, "Block use command.Wait %d", block)  
      return PLUGIN_HANDLED  
   }  
   return PLUGIN_HANDLED  
}
```
  
  
Не устали?Надеюсь нет, потому что я хотел бы вас научить ограничению использования для каждого игрока  
  
  
1)Создадим новый массив игрока, который назовем **block[33]**  
```
new block[33]
```
  
  
2)Далее создадим функцию, в которой будет выполняться какое-либо действие, у меня оно будет **client_cmd(id, "say Hello amxxmodx.ru")**  
  
```
public test(id)  
{  
   client_cmd(id, "say Hello amxxmodx.ru")  
}
```
  
  
3)Далее создаем условия, при котором будет блокировать использование функции **test**. Для этого потребуется создать простое условия, при котором будет задаваться значение раундов в массив в игрока и проверка  
  
**Код проверки будет следующим:**  
```
public test(id)  
{  
   if(block[id]<=0)  
   {  
      client_cmd(id, "say Hello amxxmodx.ru")  
      block[id] = 10  
   }else{  
      client_print(id, print_chat, "Block use command.Wait %i", block[id])  
      return PLUGIN_HANDLED  
   }  
   return PLUGIN_HANDLED  
}
```
  
  
Сейчас мы сделали почти такую же проверку и присваивание значения в массив игрока.  
  
4)Ну и на последок, как и в прошлый раз - надо создать отлов, но с данным массивом, отлов нужно дополнять.  
  
**Регистрируем новый event в plugin_init**  
  
```
register_event("HLTV", "newround", "a", "1=0", "2=0")
```
  
  
**Создаем функцию вычитание раунда из массива _block[id]_**  
  
```
public newround()  
{  
   new iPlayer[32], iNum  
   get_players(iPlayer, iNum)  
  
   for(new i; i < iNum; i++)   
   {  
      --block[iPlayer[i]]  
   }  
}
```
  
  
Вот и всё, на этом вторая часть урока подошла к концу.Вот рабочий пример плагина, можете потренироваться  
  
```
#include <amxmodx>  
   
new block[33]  
  
public plugin_init(){  
    register_plugin("[TUT]Block function players","1.0","NextPawno")  
  
    register_event("HLTV", "newround", "a", "1=0", "2=0")  
  
    register_clcmd("say /test", "test")  
}  
   
public newround()  
{  
   new iPlayer[32], iNum  
   get_players(iPlayer, iNum)  
   
   for(new i; i < iNum; i++)  
   {  
      --block[iPlayer[i]]  
   }  
}  
public test(id)  
{  
   if(block[id]<=0)  
   {  
      client_cmd(id, "say Hello amxxmodx.ru")  
      block[id] = 10  
   }else{  
      client_print(id, print_chat, "Block use command.Wait %i", block[id])  
      return PLUGIN_HANDLED  
   }  
   return PLUGIN_HANDLED  
}  
  

```
  
  
Если что-то непонятно - обращайтесь в лс, помогу.  
  
Всем спасибо, с вами был NextPawno.До новых встреч
