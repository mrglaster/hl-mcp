# Урок 22. Работа с сокетами (TCP http 80 порт)
[Уроки по скриптингу для начинающих](http://amxxmodx.ru/lessons-on-pawn/)
Модуль дает возможность использовать как **TCP** так и **UDP** соединение:  
```
// Use SOCKET_TCP for TCP Socket connections  
  
#define SOCKET_TCP 1  
  
// Use SOCKET_UDP for UDP Socket connections  
  
#define SOCKET_UDP 2
```
  
**Какая разница между ними?**  

    * **TCP** - расшифровывается как Transmission Control Protocol и осуществляет полную и правильную передачу данных между конечными устройствами, но единственная проблема это то, что если данные между конечными устройствами будут повреждены то будет повторена передача. В связи с этим этот протокол иногда может быть более медленным.   

    * **UDP** - означает User Datagram Protocol и не имеет контроля целостности данных. В связи с этим быстрее.   

Более подробную информацию можно получить в поиске ;)  
  
**Функции:**  

    * [socket_open](http://amxxmodx.ru/sockets/socketsinc/480-socket_open-funkciya-otkryvaet-soedinenie-s-udalennym-hostom.html) - открывает новое соединение к удаленному серверу  

    * [socket_close](http://amxxmodx.ru/sockets/socketsinc/481-socket_close-funkciya-zakryvaet-soedinenie-s-udalennym-hostom.html) - закрывает соединение  

    * [socket_recv](http://amxxmodx.ru/sockets/socketsinc/482-socket_recv-funkciya-poluchaet-dannye-i-zapisyvaet-v-massivstroku.html) - получает данные в строку  

    * [socket_send](http://amxxmodx.ru/sockets/socketsinc/483-socket_send-funkciya-otpravlyaet-dannye-v-soket-zapros.html) - отправляет данные в сокет/запрос  

    * [socket_send2](http://amxxmodx.ru/sockets/socketsinc/484-socket_send2-funkciya-otpravki-zaprosa-na-udalennyy-server-s-vozmozhnostyu-otpravki-pustyh-baytov.html) - отправляет данные в сокет/запрос с возможностью содержания нулевых байтов  

    * [socket_change](http://amxxmodx.ru/sockets/socketsinc/485-socket_change-funkciya-prvoeryaet-izmeneniya-v-bufere.html) - возвращает истину если в ответе сокета были изменения в течении заданного таймаута  

  
В принципе если вы знаете все о чем было описано выше, то с помощью этих функций не сложно самому написать простой скрипт. Но раз вы еще читаете, то продолжим.  
  
Прежде чем что либо создавать, нужно определиться что мы хотим получить в итоге.  
Для примера можно попробовать получить версию этого урока, она указана в мета теге **description** данной статьи **Lesson v1**.  
Что бы получить эти данные необходимо знать:  

    * Адрес сервера  

    * Порт  

    * Протокол  

  
Адрес сервера (имя хоста) уже указан в ссылке в http://**amxxmodx.ru** /lessons-on-pawn/479-urok-hh-rabota-s-soketami.html   
выделено зеленым цветом. Теперь по поводу порта, это также указано в ссылке **http://** amxxmodx.ru/lessons-on-pawn/479-urok-hh-rabota-s-soketami.html порт **HTTP** (Hyper Text Transfer Protocol) значение этого порта для доступа к серверу - 80.  
  
Теперь по поводу протокола. Ну это то, что вам нужно искать в сети, чтобы увидеть, какой тип используется протокол HTTP. В нашей ситуации TCP.   
Насчет последней части ссылки: http://amxxmodx.ru/**lessons-on-pawn/479-urok-hh-rabota-s-soketami.html**. Эта информация будет использоваться для доступа к нужной странице.  
И так список выглядит теперь так:  

    * **amxxmodx.ru**  

    * **80**  

    * **TCP**  

  
  
**Теперь перейдем к написанию плагина:**  
Прежде всего давайте определимся с данными:  
  
```
//Наши данные  
#define PLUGIN_PAGE                "/lessons-on-pawn/479-urok-hh-rabota-s-soketami.html"   
#define PLUGIN_HOST                    "amxxmodx.ru"   
  
//Константы для функций set_task   
#define TASKID_GETANSWER            0   
#define TASKID_CLOSECONNECTION        1
```
  
  
Вот и добрались до интересного, подключение к удаленному серверу ( в данном случае к amxxmodx.ru)  
```
g_Socket = socket_open(PLUGIN_HOST, 80, SOCKET_TCP, error)
```
  
**g_Socket** Заранее созданная глобальная переменная, в которую будет записан идентификатор открытого соединения.  
Далее все понятно: Хост, порт, тип протокола и переменная для записи ошибки (значение отличное от 0), если таковая возникнет и если необходимо знать что случилось пишем следующее:  
```
 switch (error)   
    {   
        case 1:   
        {   
            //Не возможно создать сокет  
            log_amx("[http://amxxmodx.ru] Unable to create socket.")   
            return   
        }   
        case 2:   
        {   
            //Невозможно подключиться к хосту  
            log_amx("[http://amxxmodx.ru] Unable to connect to hostname.")   
            return   
        }   
        case 3:   
        {  
             //Невозможно подключиться к указанному порту  
            log_amx("[http://amxxmodx.ru Unable to connect to the HTTP port.")   
            return   
        }   
    } 
```
  
  
Если соединение прошло успешно, то сформируем и передадим запрос к серверу:  
```
  
    //Массив для запроса  
    new sendbuffer[512]   
      
    //Формирование запроса  
    format(sendbuffer, 511, "GET %s HTTP/1.1^nHost:%s^r^n^r^n", PLUGIN_TOPIC, PLUGIN_HOST)   
      
     //Отсылка запроса  
    socket_send(g_Socket, sendbuffer, 511)  

```
Тут хочется отдельно прокомментировать сам запрос:  
**format(sendbuffer, 511, "GET %s HTTP/1.1^nHost:%s^r^n^r^n", PLUGIN_TOPIC, PLUGIN_HOST)**  

    * **sendbuffer** - массив куда запишется сформированная запрос  

    * **511** - его длина  

    * **GET** - Это тип запроса ( для веб серверов есть GET и POST запросы, читайте об этом на соответствующих ресурсах или [тут](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL3J1Lndpa2lwZWRpYS5vcmcvd2lraS9IVFRQ).)(GET - запрос в одну строку, POST - передача блока данных)  

    * **HTTP/1.1 b ^nHost:** тоже относится к синтаксису GET запроса   

GET /list.html HTTP/1.1  
Host: www.example.org
  

То есть если вы будите использовать какой другой порт, например порт сервера для получения данных о игроках, то запрос будет совсем другой, и эту информацию можно получить и в справочных материалах сервера или документации компании разработчика или в других источниках.  
Для CS серверов можно посмотреть тут: [Server_Queries Goldsource_servers_2](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2RldmVsb3Blci52YWx2ZXNvZnR3YXJlLmNvbS93aWtpL1NlcnZlcl9RdWVyaWVzI0dvbGRzb3VyY2Vfc2VydmVyc18y)  
  
Далее мы должны использовать **set_task** функции для того, чтобы ждать ответа от сервера. Это необходимо так как сетевой трафик может быть огромным, и ответ сервера может занять некоторое время. Нам просто нужно убедиться, что больше данных не будет получено. Именно поэтому будут использованы 2 задачи. Одна для получения ответа сервера, а другая для закрытия соединения.  
  
```
/ / Мы повторяем первую задачу 15 раз, чтобы проверить, 15 раз каждую секунду, если мы получим ответ и чтобы убедиться, что информация, которую мы хотим искать это в том, что ответом.  
    //Данная задача будет выполнена 15 раз, что бы проверить каждый раз не получена ли еще информация от сервера,  
    // как только информация будет такой же как и в прошлом ответе, будет выполнена вторая задача  
    set_task ( 1,0 ,  "task_waitanswer" ,  TASKID_GETANSWER ,  "" ,  0 ,  "а" ,  15 )   
    / / Вторая задача закрывает подключение, если в первой задаче ничего не было сделано.   
    set_task ( 16,0 ,  "task_closeconnection" ,  TASKID_CLOSECONNECTION ,  "" ,  0 ,  "" ,  0 )
```
  
  
  
**Теперь переходим к функции которая будет получать и проверять ответы от сервера:**  
С самого начала необходимо проверить были ли изменения в в ответе сервера.  
```
socket_change ( g_Socket ) 
```
  
И если это так, то мы должны получить данные из него и посмотреть, если буфер уже имеет метатег description и версию урока что ыб была достигнута наша цель.  
```
socket_recv ( g_Socket ,  g_Data ,  999 )
```
  

    * **g_Socket** Идентифигактор сокета  

    * **g_Data** Массив для данных  

    * **999** Длина массива  

  
Если вывести содержимое массива с данными - то вы получите вот что:  

HTTP/1.1 200 OK  
Date: Wed, 26 Dec 2012 21:04:22 GMT  
Server: Apache/2.2.22 (Win32) PHP/5.2.3  
X-Powered-By: PHP/5.2.3  
Set-Cookie: PHPSESSID=cd67e50sdafasdfafs2950edfface2b727; path=/  
Expires: Thu, 19 Nov 1981 08:52:00 GMT  
Cache-Control: no-store, no-ca  
ml xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">  
<head>  
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251" />  
<title>&#9561;Ёюъ її &#9576;рсюЄр ё ёюъхЄрьш &raquo; AmxModX &#9572;ъЁшяЄшэу фы эютшўъют т яЁшьхЁрї</title>  
<meta name="description" content="
  
Это ответ сервера, и если дать время, то в этот ответ будет загружена вся данная статья, но мы ищем определенный html тег в начале страницы.  
Который уже есть в ответе, мы это проверим и остановим дальнейшее выполнение заданий, так как остальные данные со страницы нам не нужны, а так же закроем соединение.  
```
    socket_close ( g_Socket )   
               
    remove_task ( TASKID_GETANSWER )   
    remove_task ( TASKID_CLOSECONNECTION )
```
  
  
**А теперь весь код целиком:**  
```
  
#include <amxmodx>   
#include <sockets>   
  
#define PLUGIN    "[http://amxxmodx.ru] lesson about sockets"  
#define AUTHOR    "Admin"   
#define VERSION    "1.0"   
  
// Host and topics   
#define PLUGIN_TOPIC    "/lessons-on-pawn/479-urok-hh-rabota-s-soketami.html"   
#define PLUGIN_HOST    "amxxmodx.ru"  
  
// Tasks   
#define TASKID_GETANSWER            0   
#define TASKID_CLOSECONNECTION        1   
  
// Глобальный идентификатор сокета  
new g_Socket   
  
// Глобальный массив для данных   
new g_Data[1000]   
  
public plugin_init(){   
      
    register_plugin(PLUGIN, VERSION, AUTHOR)   
      
}   
public plugin_cfg()   
{   
    // Соединение   
    new error, sendbuffer[512]   
    g_Socket = socket_open(PLUGIN_HOST, 80, SOCKET_TCP, error)   
      
    // If we get error   
    switch (error)   
    {   
        case 1:   
        {   
            log_amx("[http://amxxmodx.ru] Unable to create socket.")   
            return   
        }   
        case 2:   
        {   
            log_amx("[http://amxxmodx.ru] Unable to connect to hostname.")   
            return   
        }   
        case 3:   
        {   
            log_amx("[http://amxxmodx.ru] Unable to connect to the HTTP port.")   
            return   
        }   
    }   
      
    log_amx("[http://amxxmodx.ru] Connection with %s has been established", PLUGIN_HOST)   
      
    // Форматирование и отсылка запроса  
    format(sendbuffer, 511, "GET %s HTTP/1.1^nHost:%s^r^n^r^n", PLUGIN_TOPIC, PLUGIN_HOST)   
    socket_send(g_Socket, sendbuffer, 511)   
      
    log_amx("[http://amxxmodx.ru] Sending page request")   
      
    // Задания для првоерки результатов  
    set_task(1.0, "task_waitanswer", TASKID_GETANSWER, "", 0, "a", 15)   
    set_task(16.0, "task_closeconnection", TASKID_CLOSECONNECTION, "", 0, "", 0)   
  
}   
  
public task_waitanswer(id){   
      
      
    //Отступ в консоли сервера  
    static count  
    if(count == 0){  
        server_print("^n^n^n")  
        count++  
    }  
      
    // Изменились ли данные?   
    if (socket_change(g_Socket))   
    {   
        // Получение информации  
        socket_recv(g_Socket, g_Data, 999)   
          
        //Вывод данных для наглядности  
        server_print("%s",g_Data)  
          
        // Ищем нужную нам строку   
        new Position = containi(g_Data, "Lesson v1")   
          
        // Если нашли   
        if (Position >= 0)   
        {   
            log_amx("[http://amxxmodx.ru] Lesson v1 found")   
              
              
      
            // Закрытие соединения  
            socket_close(g_Socket)   
              
            // Остановка заданий  
            remove_task(TASKID_GETANSWER)   
            remove_task(TASKID_CLOSECONNECTION)   
        }   
    }   
}   
  
public task_closeconnection(id)   
{   
    // закрытие соединения через 16 секунд.  
    socket_close(g_Socket)   
}  
```
  
  
За основу была взята статья: [[TUT] Introduction to sockets](http://amxxmodx.ru/engine/go.php?url=aHR0cDovL2ZvcnVtcy5hbGxpZWRtb2RzLm5ldC9zaG93dGhyZWFkLnBocD90PTE1MTQwMQ%3D%3D)  
В следующий раз, напишу пример как получать данные с другого CS сервера.  
надеюсь вы хоть немного разобрались как это работает и осознали, что главная проблема знать синтаксис запросов к серверу, а так же что сервер будет отдавать, так как далеко не всегда все отдается в таком просто виде как html код.
