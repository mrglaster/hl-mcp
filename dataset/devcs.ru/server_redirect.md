# Плагин редиректа, который перекинет игроков со старого на новый сервер, уведомив через hud/chat или motd о переезде

- Перед тем как это ставить, перекинь все раскрутки на новый ip, чтобы не получить бан в мс. 
- redirect.txt должен находиться рядом с server.cfg

Код: 

```
#define SVC_DIRECTOR_ID                        51
#define SVC_DIRECTOR_STUFFTEXT_ID            10
stock SVC_DIRECTOR_STUFFTEXT_CMD( text[] , id = 0 ) {

    message_begin( MSG_ONE, SVC_DIRECTOR_ID, _, id )

    write_byte( strlen(text) + 2 )

    write_byte( SVC_DIRECTOR_STUFFTEXT_ID )

    write_string( text )
 
    message_end()

}
```

Использование: 

```
SVC_DIRECTOR_STUFFTEXT_CMD( "cOnneCt 127.0.0.1:27015" , id )
```
