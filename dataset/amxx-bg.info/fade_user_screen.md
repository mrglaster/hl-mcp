# fade_user_screen
#### Syntax
```
stock fade_user_screen(id, Float:duration = 1.0, Float:fadetime = 1.0, ScreenFadeFlags:flags = ScreenFade_FadeIn, r = 0, g = 0, b = 255, a = 75, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
duration | ```How long (in seconds) the fade is going to stay on the screen (0 - 16)```
fadetime | ```How many seconds is the fade going to fade in (0 - 16)```
flags | ```Screen fade flags:   ScreenFade_FadeIn       - default   ScreenFade_FadeOut      - fade out (not in)   ScreenFade_Modulate     - modulate (don't blend)   ScreenFade_StayOut      - ignores the duration and stays faded out until a new ScreenFade messages is received```
r | ```Red color amount (0 - 255)```
g | ```Green color amount (0 - 255)```
b | ```Blue color amount (0 - 255)```
a | ```Color alpha (brightness) (0 - 255)```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Fades the client's screen.
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.