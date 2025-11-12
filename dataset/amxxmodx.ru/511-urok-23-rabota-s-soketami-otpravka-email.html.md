# Урок 23. Работа с сокетами (отправка email)
[Уроки по скриптингу для начинающих](http://amxxmodx.ru/lessons-on-pawn/)
[![Урок 23. Работа с сокетами \(отправка email\)](http://amxxmodx.ru/uploads/posts/2013-02/thumbs/1360267281_t.jpeg)](http://amxxmodx.ru/uploads/posts/2013-02/1360267281_t.jpeg)В прошлом уроке мы с вами разобрали пример как получить web страницу с помощью сокетов.В этом уроке я расскажу о плагине от PomanoB`а. А точнее о функционале который он предоставляет, а именно набор функций:  
**
    * smtp_connect - Коннект к серверу smtp  

    * smtp_auth - авторизация  

    * smtp_send - отправка письма  

    * smtp_quit - закрытие соединения  

**  
  
На самом деле, этот плагин ни что иное как прошлый урок, по результатам которого можно было бы написать собственный такой плагин, до Дядька Романыч позаботился о нас. По этому я расскажу только как применять эти функции, а тем кому интересно более детально узнать как работает плагин, сам изучит исходник. Который в конце данной статьи приложен.  
  
И так для работы нам потребуется:  

    1. Плагин **Amx Mail v 0.1.0**  

    2. Инклуд **amxmail** ( в комплекте с плагином)  

    3. Нами написанный **мини пример**  

  
  
Будем считать что все файлы находятся в нужных местах. Приступим к написанию примера, который будет отправлять на определенный электронный адрес письмо с определенным содержанием, ну скажем с именем сервера и текущей картой при его старте.  
  
Давайте подумаем как вы отправляете письмо другу? Скорее всего так:
    1. Заходите на страничку вашей почтовой системы или открываете программу клиент. ( то етсь соединяетесь с сервером)  

    2. Далее вводится логин и пароль ( авторизация на сервере)  

    3. Написание и отправка письма  

    4. Закрытие странички или программы (закрытие соединения)  

  
Будущий плагин будет делать все тоже самое в той же самой последовательности. Не правда ли все просто?  
  
**Начнем с коннекта к серверу:**  
```
/*   
 * Подключиться к SMTP серверу  
 *  
 * server - адрес сервера  
 * port - порт сервера  
 *  
 * В случае успеха функция вернёт идентификатор сервера,   
 * его надо использовать в первом параметре остальных функций  
 *  
 * В случае неудачи возвращает -1  
 *  
 */  
native smtp_connect(server[], port);
```
  
В описании функции и так все предельно понятно, но на всякий случай поясню что данные настройки вы можете посмотреть в справочных материалах ваших почтовых служб, вот пример [Хелп mail.ru](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2hlbHAubWFpbC5ydS9tYWlsLWhlbHAvbWFpbGVyL3BvcHNtdHA%3D)   
Из которого следует что адрес сервера **smtp.mail.ru** и нужный нам порт SMTP — 25, 587 или 2525 ( любой на выбор )  
  
**Далее следует авторизация:**  
```
/*   
 * Авторизация на SMTP сервере  
 *  
 * socket - идентификатор сервера  
 * username - имя пользователя (Например username@mail.ru)  
 * password - пароль  
 *   
 */  
native smtp_auth(socket, username[], password[]);
```
  
Обратите внимание, что первая функция возвращает идентификатор сокет соединения соединения, который будет первым аргументов функции.  
Логин и пароль указываются точно такими же как вы привыкли входить в свою почту.  
  
**Наконец подошли к самой отправке письма:**  
```
/*   
 * Отправить письмо  
 *  
 * socket - идентификатор сервера  
 * from - от кого письмо (для большинства серверов должно совпадать с именем пользователя)  
 * to - кому письмо  
 * subject - тема письма  
 * mail - содержимое письма  
 * addHeaders - дополнительные заголовки (Например Reply-To:)  
 *   
 */  
native smtp_send(socket, from[], to[], subject[], mail[], addHeaders[]);
```
  
Функция не поддерживает форматирование, по этому передаваемые данные необходимо подготовить заранее, например с помощью функции [**format**](http://amxxmodx.ru/core/stringinc/63-format-funkciya-dlya-redaktirovaniya-soobscheniy-strok.html)  
  
После успешной отправки ( а может и не отправки) необходимо закрыть открытое соединение с сервером:  
```
/*   
 * Отключиться от сервера  
 *  
 * socket - идентификатор сервера  
 */  
native smtp_quit(socket);
```
  
  
**Теоретически разобрались, посмотрим как это будет выглядеть в коде:**  
```
#include <amxmodx>  
#include <amxmisc>  
#include <amxmail>  
  
#define PLUGIN "[http://amxxmodx.ru] Send Mail"  
#define VERSION "1.0"  
#define AUTHOR "Admin"  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    set_task(5.0,"send",0)  
}  
public send(){  
  
    //Подготавливаем текст для письма  
    new text[1024],MapName[32],ServerName[32]  
    get_user_name(0,ServerName,31)  
    get_mapname(MapName,31)  
    format(text,charsmax(text),"Hello Admin! From server:%s , map in server [%s]",ServerName,MapName)  
      
      
    new connect // Создаем переменную для хранения идентификатора соединения  
    connect = smtp_connect("smtp.mail.ru",587)//Соедиенние и получение идентификатора  
      
    if(connect != -1){// Проверяем что соединение установлено  
        smtp_auth(connect,"login","pass")// Авторизация  
        smtp_send(connect,"TVOI@mail.ru","KOMY@list.ru","TeMa: Server start",text,"To:")//Отправка письма  
        smtp_quit(connect)//Закрытие соединения  
    }else{  
        server_print("ERROR Connect to SMTP")          
    }  
      
}
```
  
Вот тут: **"TVOI@mail.ru","KOMY@list.ru"**  
Можете ввести свой почтовый адрес в двух местах, и тогда получится что вы пришлете письмо самому себе.  
Надеюсь теперь вы понимаете как использовать данный плагин. Ах да, функция [**set_task**](http://amxxmodx.ru/core/amxmodxinc/70-set_task-vyzyvaet-druguyu-funkciyu-cherez-trebuemoe-vremya.html) там необходимо для того, что бы плагин amx_mail точно успел загрузиться. ( мало ли он у вас ниже в списке плагинов окажется)  
  
Теперь исходный код плагина **amx_mail** :  

![](http://amxxmodx.ru/templates/3week92/dleimages/spoiler-plus.gif) [Показать / Скрыть текст](javascript:ShowOrHide\('sp04c729c65a302c2e83a35fd485f9b056'\))
```
/* Plugin generated by AMXX-Studio */  
  
#include <amxmodx>  
#include <sockets>  
#include <amxmail>  
  
#define PLUGIN "Amx Mail"  
#define VERSION "0.1.0"  
#define AUTHOR "PomanoB"  
  
#define MAX_CONNECTIONS 3  
  
#define MAIL_TIMEOUT 10.0  
  
#define MAIL_DEBUG  
  
enum mailStatus  
{  
    mail_status_send,  
    mail_status_quit  
}  
  
new g_sockets[MAX_CONNECTIONS]  
new mailStatus:g_status[MAX_CONNECTIONS]  
  
new Array:g_mailData[MAX_CONNECTIONS]  
  
public plugin_init()   
{  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
      
    set_task(1.0, "recvTask", _, _, _, "b")  
      
    new i  
    for (i = 0; i < MAX_CONNECTIONS; i++)  
        g_mailData[i] = ArrayCreate(512, 32)  
  
}  
  
public plugin_natives()  
{  
    register_library("amxmail")  
      
    register_native("smtp_connect","_smtp_connect");  
    register_native("smtp_auth","_smtp_auth");  
    register_native("smtp_send","_smtp_send");  
    register_native("smtp_quit","_smtp_quit");  
}  
  
public _smtp_connect(plugin, params)  
{  
    new i, error, server[32]  
      
    for (i = 0; i < MAX_CONNECTIONS; i ++)  
    {  
        if (!g_sockets[i])  
            break  
    }  
    if (i == MAX_CONNECTIONS)  
        return -1  
      
    get_string(1, server, charsmax(server))  
    server_print("[%s][%d]",server,get_param(2))  
    g_sockets[i] = socket_open(server, get_param(2), SOCKET_TCP, error)  
      
    if (error)  
    {  
        server_print("[%s]",error)  
        g_sockets[i] = 0  
        return -1  
    }      
    return i  
}  
  
public _smtp_auth(plugin, params)  
{  
    new socket, username[64], password[64], data[512]  
      
    socket = get_param(1)  
    get_string(2, username, charsmax(username))  
    get_string(3, password, charsmax(password))  
      
    ArrayPushString(g_mailData[socket], "EHLO AmxMailer^r^n")  
    ArrayPushString(g_mailData[socket], "AUTH LOGIN^r^n")  
      
    base64encode(username, data)  
    add(data, charsmax(data), "^r^n")  
    ArrayPushString(g_mailData[socket], data)  
      
    base64encode(password, data)  
    add(data, charsmax(data), "^r^n")  
    ArrayPushString(g_mailData[socket], data)  
      
    g_status[socket] = mail_status_send      
    return 0  
}  
  
public _smtp_send(plugin, params)  
{  
    new socket, from[64], to[64], subject[64], mail[512], addHeaders[64], data[512]  
      
    socket = get_param(1)  
    get_string(2, from, charsmax(from))  
    get_string(3, to, charsmax(to))  
    get_string(4, subject, charsmax(subject))  
    get_string(5, mail, charsmax(mail))  
    get_string(6, addHeaders, charsmax(addHeaders))  
      
    formatex(data, charsmax(data), "MAIL FROM: %s^r^n", from)  
    ArrayPushString(g_mailData[socket], data)  
      
    formatex(data, charsmax(data), "RCPT TO: %s^r^n", to)  
    ArrayPushString(g_mailData[socket], data)  
      
    formatex(data, charsmax(data), "DATA^r^n")  
    ArrayPushString(g_mailData[socket], data)  
      
      
    formatex(data, charsmax(data), "To: %s^r^nFrom: %s^r^nSubject: %s^r^n",  
        to, from, subject)  
    if (strlen(addHeaders))  
        add(data, charsmax(data), addHeaders)  
    format(data, charsmax(data), "%s^r^n%s^r^n.^r^n", data, mail)      
    ArrayPushString(g_mailData[socket], data)  
}  
  
public _smtp_quit(plugin, params)  
{  
    ArrayPushString(g_mailData[get_param(1)], "QUIT^r^n")  
}  
  
public base64encode(str[], outStr[])  
{  
    static const base64[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"  
    new index1, index2, byte, mul, ch, out  
    new len  
      
    len = strlen(str)  
      
    while (len--)  
    {  
        byte = str[ch++]  
        index1 = index2|((byte>>(1+mul)*2)&0x3F)  
        index2 = (byte<<(2 - mul)*2)&0x3F  
        outStr[out++] = base64[index1]  
        if (mul++ == 2)  
        {  
            outStr[out++] = base64[index2]  
            mul = index2 = 0  
        }  
    }  
      
    if (mul != 0)  
    {  
        outStr[out++] = base64[index2]  
      
        while (3 - mul++)  
            outStr[out++] = '='  
    }  
  
    outStr[out] = 0  
      
}  
  
public recvTask()  
{  
    static i, socket, data[512], replyCode  
    static Float:lastDataRecv[MAX_CONNECTIONS], curDataNumber[MAX_CONNECTIONS]  
      
    for(i = 0; i < MAX_CONNECTIONS; i++)  
    {  
        socket = g_sockets[i]  
        if (socket)  
        {  
          
            if (socket_change(socket, 1))  
            {  
                lastDataRecv[i] = get_gametime()  
                setc(data, charsmax(data), 0)  
                socket_recv(socket, data, charsmax(data))  
#if defined MAIL_DEBUG                  
                log_amx("<-^n%s", data)  
#endif                  
                replyCode = str_to_num(data)  
                switch (replyCode)  
                {  
                    case 220, 250, 334, 235, 354:  
                    {  
                        if (g_status[i] == mail_status_send)  
                        {  
                            ArrayGetString(  
                                g_mailData[i],   
                                curDataNumber[i],  
                                data, charsmax(data))  
                              
                            curDataNumber[i]++   
#if defined MAIL_DEBUG  
                            log_amx("->^n%s", data)  
#endif                              
                            socket_send(socket, data, 0)  
                        }  
                          
                    }  
                    case 221:  
                    {  
                        closeSocket(i)  
                    }  
                    default:  
                    {  
                        log_amx("[AMXX MAIL] Socket %d error: %s", i, data)  
                        closeSocket(i)  
                    }  
                }  
            }  
            else  
            if (lastDataRecv[i] + MAIL_TIMEOUT < get_gametime())  
            {  
                log_amx("[AMXX MAIL] Socket %d timeout!", i)  
                closeSocket(i)  
                  
            }  
        }  
        else if (curDataNumber[i])  
                curDataNumber[i] = 0  
    }  
}  
  
public closeSocket(i)  
{  
    socket_close(g_sockets[i])  
    ArrayClear(g_mailData[i])  
    g_sockets[i] = 0  
#if defined MAIL_DEBUG      
    log_amx("Socket %d closed", i)  
#endif  
}  
  
public plugin_end()  
{  
    new i  
    for (i = 0; i < MAX_CONNECTIONS; i++)  
    {  
        if (g_sockets[i])  
            closeSocket(i)  
              
        ArrayDestroy(g_mailData[i])      
    }  
}  

```

  
Тут я уже раскоментировал строчку что бы в консоль сервера шли логи действий плагина, это даст вам возможность более подробно изучить процесс работы плагина. Но для полного понимания вам конечно же необходимо прочитать материалы о работе email.  
**Рекомендую прочитать эту статью:** [PHP Email](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL3d3dy5waHAuc3UvYXJ0aWNsZXMvP2NhdD1lbWFpbCZhbXA7cGFnZT0wMDc%3D)  
И содержание инклуда amxmail:  
```
#if defined AMX_MAIL_INCLUDED  
  #endinput  
#endif  
#define AMX_MAIL_INCLUDED  
  
#if AMXX_VERSION_NUM >= 175  
 #pragma reqlib amxmail  
 #if !defined AMXMODX_NOAUTOLOAD  
  #pragma loadlib amxmail  
 #endif  
#else  
 #pragma library amxmail  
#endif  
  
native smtp_connect(server[], port);  
  
native smtp_auth(socket, username[], password[]);  
  
native smtp_send(socket, from[], to[], subject[], mail[], addHeaders[]);  
  
native smtp_quit(socket);  

```
  
**Источник плагина:**[amxmodx.su](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2FteG1vZHguc3UvZm9ydW0vdmlld3RvcGljLnBocD9mPTUmYW1wO3Q9MjAx)  
Надеюсь теперь вы всегда будите получат необходимые уведомления с вашего сервера.
