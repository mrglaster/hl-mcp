# BanIP Fakes - защита от фаптимовских фей
[Готовые скрипты](http://amxxmodx.ru/scripts/)
![BanIP Fakes - защита от фаптимовских фей](http://amxxmodx.ru/uploads/posts/2014-08/1407507656_banner.png) ![BanIP Fakes - защита от фаптимовских фей](http://amxxmodx.ru/uploads/posts/2014-08/1407703821_fairy-emoticon.png)
  
**Автор:** Safety1st  
**Версия:** 0.2 от 07.08.2014  
**Скачать:** [официальный топик](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2Mtcy5uZXQudWEvZm9ydW0vaW5kZXgucGhwP2FjdD1maW5kcG9zdCZhbXA7cGlkPTYzODgxNg%3D%3D)  
  
**Плагин банит IP-адрес, с которого одновременно зашло более X игроков. Может использоваться как простая защита от фейков, опубликованных 5-го августа** , которые уже достаточно хорошо эмулируют игроков, обходя проверки dproto.  
  
Плагин будет защищать одинаково хорошо с выпуском новых версий той заразы (занимающей слоты). Его преимущество в том, что у него детект, который можно обойти только использованием пачки IP/проксей. Не волнуйтесь: вряд ли ололошки сумеют 'обойти' защиту до выхода нового dproto.  
  
**Есть возможность указать 'белый список' IP-ников и подсетей**, на которые не распространяется ограничение; по дефолту список выключен. Плагин отписывается в лог AMXX о забаненных IP-никах:  

L 08/07/2014 - 14:00:29: [banip_fakes.amxx] IP 10.3.3.2 has been banned for 30 minutes
  
**Настройка** - в исходнике:  
• **#define MAX_SAME_IP 3** - сколько игроков с одинаковым IP могут быть одновременно на сервере;  
• #define BAN_DURATION 30 - продолжительность бана;  
• new gszKickMsg[] = "Hacker? xD" - с таким сообщением будет кикнут последний зашедший игрок.  
  

![](http://amxxmodx.ru/templates/3week92/dleimages/spoiler-plus.gif) [Дополнительная информация](javascript:ShowOrHide\('sp76d9f79fa71c579f6b24c92816d3a257'\))
• **//#define WHITELIST_SIZE 4** - раскомментируйте, чтобы использовать белый список;  
• **плагин не различает ботов, их адреса в белый список нужно внести явно** (строка для ботов там уже имеется: _"127.0.0.0/8"_ ). Настройте плагин так:  

#if defined WHITELIST_SIZE  
new const gszWhiteList[WHITELIST_SIZE][] = {  
"127.0.0.0/8", // for bots  
}  
#endif
  
• **подробнее про настройку белого списка.**  
Если вы НЕ собираетесь использовать список, информация ниже вам НЕ нужна.  
  

new const gszWhiteList[WHITELIST_SIZE][] = {  
"127.0.0.0/8", // loopback interface (usually assigned IP is 127.0.0.1)  
"192.168.0.0/24", // 192.168.0.0/24 subnet, IPs range 192.168.0.0 ... 192.168.0.255  
"10.3.3.2/16", // 10.3.0.0/16 subnet, IPs range 10.3.0.0 ... 10.3.255.255, we could use any of its IPs here  
"141.101.120.244" // c-s.net.ua IP  
}
  
По одному IP-нику или подсети на строку. В _#define WHITELIST_SIZE_ нужно указать точное число строк в списке. Подсети указываются в [CIDR](http://amxxmodx.ru/engine/go.php?url=aHR0cDovLyZhbXA7cXVvdDtodHRwOi8vYy1zLm5ldC51YS91cmw%2FdT1odHRwcyUzQSUyRiUyRnd3dy5nb29nbGUucnUlMkZzZWFyY2glM0ZxJTNEQ0lEUiZhbXA7cXVvdDs%3D)-нотации. Поясняющие примеры можно спокойно убрать. На месте IP подсети можно указать и один из входящих в неё IP-ников, главное - не ошибиться с диапазоном ;)
  
**В _plugins.ini_ поставьте плагин в конец списка.**
