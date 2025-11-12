# Более кастомный худ, можно задавать цвет для эффекта и прозрачность.

```
/*
* id
* Player to send the message to.
*   0 = everyone
*
* text[]
*   Text to send.
*
* Float:X
*   X position on screen.
*
* Float:Y
*   Y position on screen.
*
* R
*   Red color.
*
* G
*   Green color.
*
* B
*   Blue color.
*
* A
*   Alpha.
*   Default value: 255
*
* Float:holdtime
*   Float:fadeintime
*   Time to fade in message
*   Default value: 0.1
*
* Float:fadeouttime
*   Time to fade out message
*   Default value: 0.1
*
* channel
*   Textchannel
*   -1 = auto choose.
*   Default value: -1
*
* effect
*   Effect of message.
*   1 = Flicker with 2nd color.
*   2 = Print out as 2nd color, fade into 1st color.
*     effecttime decides fade time between colors.
*     fadeintime decides how fast the letters should be printed out.
*   Default value: 0
*
* effect_R
*   Red color of effect.
*   Default value: 0
*
* effect_G
*   Green color of effect.
*   Default value: 0
*
* effect_B
*   Blue color of effect.
*   Default value: 0
*
* effect_A
*   Alpha of effect.
*   Default value: 255
*
* Float:effecttime
*   Only for effect 2.
*   Default value: 0.0
*/

stock send_hudmessage(id,text[],Float:X,Float:Y,R,G,B,A=255,Float:holdtime=5.0,Float:fadeintime=0.1,Float:fadeouttime=0.1,channel=-1,effect=0,effect_R=0,effect_G=0,effect_B=0,effect_A=255,Float:effecttime=0.0) {
    if ( id )
        message_begin(MSG_ONE_UNRELIABLE, SVC_TEMPENTITY, {0,0,0}, id);
    else
        message_begin(MSG_BROADCAST, SVC_TEMPENTITY);
    write_byte(TE_TEXTMESSAGE)
    write_byte(channel)
    write_short(coord_to_hudmsgshort(X))
    write_short(coord_to_hudmsgshort(Y))
    write_byte(effect)
    write_byte(R)  
    write_byte(G)
    write_byte(B)
    write_byte(A)
    write_byte(effect_R)
    write_byte(effect_G)
    write_byte(effect_B)
    write_byte(effect_A)
    write_short(seconds_to_hudmsgshort(fadeintime))
    write_short(seconds_to_hudmsgshort(fadeouttime))
    write_short(seconds_to_hudmsgshort(holdtime))
    if ( effect == 2 )
        write_short(seconds_to_hudmsgshort(effecttime));
    write_string(text)
    message_end()
}

/* 0.0 - 255.99609375 seconds */
stock seconds_to_hudmsgshort(Float:sec) {
    new output = floatround(sec * 256);
    return output < 0 ? 0 : output > 65535 ? 65535 : output;
}

stock coord_to_hudmsgshort(Float:coord) {
    new output = floatround(coord * 8192);
    return output < -32768 ? -32768 : output > 32767 ? 32767 : output;
}
```

Взято отсюда
https://forums.alliedmods.net/showthread.php?t=69263
