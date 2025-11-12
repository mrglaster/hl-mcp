# [TUT] Изучаем CellTrie
[Присланное](http://amxxmodx.ru/other/)
Урок будем разбирать на примере плагина от ZETA MEN **VSVipPrefix**  
Скачать : Вы не можете скачивать файлы с нашего сервера (Плагин можно скомпилировать [здесь ](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL29ubGluZS1jb21waWxlci5hbXh4bW9keC5ydS8%3D))  
  
```
#include <amxmodx>  
  
#define ACCESS_FLAG ADMIN_MENU // Доступ к чату с приставкой V.I.P  
  
new channels[8][] = // Все каналы общения (чаты) которые есть в кс 1.6  
{  
    "#Cstrike_Chat_CT", // Чат между игроками команды CT (Живые)  
    "#Cstrike_Chat_T", // Чат между игроками команды T (Живые)  
    "#Cstrike_Chat_CT_Dead", // Чат между игроками команды CT (Мертвые)  
    "#Cstrike_Chat_T_Dead", // Чат между игроками команды T (Мертвые)  
    "#Cstrike_Chat_Spec", // Чат между спекторами  
    "#Cstrike_Chat_All", // Чат живых (общий)  
    "#Cstrike_Chat_AllDead", // Чат мертвых (общий)  
    "#Cstrike_Chat_AllSpec" // Чат Всех спекторов  
}  
  
new newChannels[8][] = // Наши приставки   
{  
    "(Менты) [VIP] %s1 :  %s2", // %s1 Наше имя , %s2 наше сообщение  
    "(Террористы) [VIP] %s1 :  %s2",  
    "*Труп*(Менты) [VIP] %s1 :  %s2",  
    "*Труп*(Террористы) [VIP] %s1 :  %s2",  
    "(Наблюдатель) [VIP] %s1 :  %s2",  
    "[VIP] %s1 :  %s2",  
    "*Труп* [VIP] %s1 :  %s2",  
    "*Наблюдатель* [VIP] %s1 :  %s2"  
}  
  
new Trie:vipChannels // Наш Trie  
  
public plugin_init() // Регистрируем плагин   
{  
    register_plugin("VSVipPrefix", "1.3", "ZETA [M|E|N]");  
      
    vipChannels = TrieCreate(); // Наш Trie зарегистрирован , обратите внимание что размер не задается как это делается в Массивах (Array)  
      
    for (new i = 0; i < 8; i++) // Сделаем цикл по всем нашим каналам   
    {  
        TrieSetString(vipChannels, channels[i], newChannels[i]); // vipChannels - наш зарегистрированный Trie , channels[i] Устанавливаем каналы cs , newChannels[i] - наши приставки   
    }  
      
    register_message(get_user_msgid("SayText"), "MessageSayText"); // Ловим отправку сообщения  
}  
  
public MessageSayText(msgid, msgdest, id)  
{  
    new channel[64]; // Получаем какой чат , можно посмотреть в channels  
    get_msg_arg_string(2, channel, charsmax(channel)); // Получаем чат , записываем в массив полученный нами чат   
      
    if(!TrieGetString(vipChannels, channel, channel, charsmax(channel))) // Проверям есть ли такой чат в зарегистрированном нами Trie   
    {  
        return; // Возвращаем если нет   
    }  
  
    new sender = get_msg_arg_int(1); // Получаем id отправлявшего  
  
    if(sender && (get_user_flags(sender) && ACCESS_FLAG)) // Проверяем существует ли id и проверяем флаги на игроке   
    {  
        set_msg_arg_string(2, channel); // Устанавливаем   
    }  
}  
  
public plugin_end()  
{  
    TrieDestroy(vipChannels); // Разрушаем наш Trie    
}  

```
  
  
Так же есть и такие нативы как TrieGetCell и т.д.  
Про некоторые сейчас расскажу   
  
**TrieDeleteKey(Trie:handle, const key[]);**  
  
Удаляем Из Trie строку по ключу   
  
Пример :  
```
#include <amxmodx>  
  
new Trie:gData  
  
public plugin_init()  
{  
 register_clcmd("say /delet", "DeletKey")  
 gData = TrieCreate()  
}  
  
public DeletKey(id)  
{  
 new szName[32]  
 get_user_name(id, szName, 31)  
 if(TrieDeletKey(gData, szName))  
 {  
  client_print(id, print_chat, "Вы были удалены из gData")  
 }else{  
  client_print(id, print_chat, "Вы не найдены в gData")  
 }  
}  

```
  
  
Если вы зайдете на сервер и пропишите в чате **say /delet**  
То вы получите одно из двух сообщений **Вы были удалены из gData** или **Вы не найдены в gData**  
  
Так же есть еще полезная функция   
**TrieKeyExists(Trie:handle, const key[]);**  
Проверяет есть ли Ключ в Trie  
  
```
#include <amxmodx>  
  
new Trie:gData  
  
public plugin_init()  
{  
 register_clcmd("say /exists", "DeletKey")  
 gData = TrieCreate()  
}  
  
public DeletKey(id)  
{  
 new szName[32]  
 get_user_name(id, szName, 31)  
 if(TrieKeyExists(gData, szName))  
 {  
  client_print(id, print_chat, "Вы есть в gData")  
 }else{  
  client_print(id, print_chat, "Вы не найдены в gData")  
 }  
}
```
  
  
Принцип очень прост :  
При написании в чате **say /exists**  
Если вы записаны в **gData** то вы получите сообщение **Вы есть в gData**  
А если нету то **Вы не найдены в gData**  
  
Все надеюсь вы прочли и вам понравилось  
До новых встреч
