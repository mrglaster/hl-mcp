# Functions in cromchat.inc
Function | Description  
---|---  
[CC_SendMessage](https://amxx-bg.info/api/cromchat/CC_SendMessage) | ```
Sends a colored chat message.
```
  
[CC_SendMatched](https://amxx-bg.info/api/cromchat/CC_SendMatched) | ```
Sends a colored chat message matching a specific player's color.
```
  
[CC_GroupMessage](https://amxx-bg.info/api/cromchat/CC_GroupMessage) | ```
Sends a colored chat message to a group of players matching the flags from the get_players() function.
```
  
[CC_SendAdminMessage](https://amxx-bg.info/api/cromchat/CC_SendAdminMessage) | ```
Sends a colored chat message to all players who have the specified admin flags.
```
  
[CC_LogMessage](https://amxx-bg.info/api/cromchat/CC_LogMessage) | ```
Sends a colored chat message and logs it at the same time.
```
  
[CC_ShowActivity](https://amxx-bg.info/api/cromchat/CC_ShowActivity) | ```
Sends a colored chat message to all players that obeys the amx_show_activity cvar.
```
  
[CC_ShowActivityId](https://amxx-bg.info/api/cromchat/CC_ShowActivityId) | ```
Sends a colored chat message to a single client that obeys the amx_show_activity cvar.
```
  
[CC_ShowActivityKey](https://amxx-bg.info/api/cromchat/CC_ShowActivityKey) | ```
Sends a colored chat message to all clients using nromal language keys that obeys the amx_show_activity cvar.
```
  
[CC_RemoveColors](https://amxx-bg.info/api/cromchat/CC_RemoveColors) | ```
Removes the color codes from a message.
```
  
[CC_RemoveExploits](https://amxx-bg.info/api/cromchat/CC_RemoveExploits) | ```
Removes exploits from the message.
```
  
[CC_SetPrefix](https://amxx-bg.info/api/cromchat/CC_SetPrefix) | ```
Sets a global prefix that will be used for all sent messages.
```
  
[CC_RemovePrefix](https://amxx-bg.info/api/cromchat/CC_RemovePrefix) | ```
Removes the global message prefix.
```
  
[CC_SetColor](https://amxx-bg.info/api/cromchat/CC_SetColor) | ```
Sets the team color for the next message that's going to be sent.
```
  
[_CC_WriteMessage](https://amxx-bg.info/api/cromchat/_CC_WriteMessage) | ```
This function is used by the other stocks in order to send a raw message.
```
  
[_CC_ModInit](https://amxx-bg.info/api/cromchat/_CC_ModInit) | ```
Checks if the server is running Counter-Strike.
```
  
[_CC_ActivityInit](https://amxx-bg.info/api/cromchat/_CC_ActivityInit) | ```
Stores the amx_show_activity pointer for use with "ShowActivity" functions.
```
  
[_CC_GetActivityPrefix](https://amxx-bg.info/api/cromchat/_CC_GetActivityPrefix) | ```
Returns the player prefix used with "ShowActivity" functions.
```
  
[_CC_IsActivityAdmin](https://amxx-bg.info/api/cromchat/_CC_IsActivityAdmin) | ```
Checks whether the client has the required flag to be marked as an admin for the "ShowActivity" functions.
```
  

This code is a part of cromchat.inc. To use this code you should include cromchat.inc as ```#include <cromchat>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.