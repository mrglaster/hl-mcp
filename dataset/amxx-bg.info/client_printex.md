# client_printex
#### Syntax
```
stock client_printex(index, type, const msg_name[], const msg_param1[] = "", const msg_param2[] = "", const msg_param3[] = "", const msg_param4[] = "")
```

#### Usage
index | ```Index of the player, use 0 to send to all players.```
---|---
type | ```The message destination. See print_* constants.```
msg_name | ```The custom or predefined message to send.```
msg_param1 | ```Optional message argument.```
msg_param2 | ```Optional message argument.```
msg_param3 | ```Optional message argument.```
msg_param4 | ```Optional message argument.```
#### Description
```
Sends a predefined text message to player.
Predefined texts are default game messages which will be translated
to player's game language, e.g. #Game_join_ct.
```

#### Note
```
Set index to 0 to send text globally.
```

#### Note
```
There does not necessarily have to be a total of 6 arguments.
It will depend if message takes arguments, e.g.:
  client_printex(id, print_chat, "#Game_join_ct", "Pimp Daddy")
  client_printex(id, print_chat, "1", "#Game_radio", "Pimp Daddy", "Hello world!")
```

#### Return
```
This function has no return value.
```


This code is a part of message_stocks.inc. To use this code you should include message_stocks.inc as ```#include <message_stocks>```


  
  

