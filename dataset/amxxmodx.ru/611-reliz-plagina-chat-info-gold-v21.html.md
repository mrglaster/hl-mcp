# Релиз плагина - Chat Info Gold [v2.1]
[Готовые плагины](http://amxxmodx.ru/amxx_plugins/)
**Автор: Valer4**  
**Версия: 2.1 специально для http://amxxmodx.ru**  
Плагин: показывает написанные Вами цветные сообщения в чат игрокам, через определённое время после смерти.  
**Главное преимущество этого плагина - для добавления сообщений вам не нужно что-либо менять в исходнике.**  
Вы дописываете их в языковой файл chat_info.txt. Плагин автоматически начнёт их показывать!  
![Релиз плагина - Chat Info Gold \[v2.1\]](http://amxxmodx.ru/uploads/posts/2014-10/1413205981_chat-info-gold.png)  
  
  
  
  
  
  
  
**Особенности и настройка:**  

![](http://amxxmodx.ru/templates/3week92/dleimages/spoiler-plus.gif) [Показать / Скрыть текст](javascript:ShowOrHide\('sp31e04fc9893db089413eb016e8b045c8'\))
  
Нужно соблюдать нумерацию, к примеру если последнее сообщение TEXT_5 = "что-то", ваше должно быть TEXT_6 = "что-то".  
Сообщения будут выводиться:  
1 Не в той последовательности как в chat_info.txt, а рандомно!  
2 Если игрок ещё мёртв!  
Квар - ci_delay - через сколько секунд после смерти показывать сообщения, по умолчанию 13.  
Команда для игроков - ci - включить/отключить показ сообщений.  
Её значение сохраняется в конфиге у игроков.  
Для добавления цветов перед словами добавьте ^3 - красный, ^4 - зелёный, ^1 - жёлтый, перед первым словом обязательно должен быть один из них!  

  
**Требования: AMX MOD X 1.8.3**  
Вы не можете скачивать файлы с нашего сервера  
Исходный код плагина:  
```
#include<amxmodx>  
  
new    g_delay,  
    g_count,  
    _hide  
  
#define _is_hide(%1) (_hide & 1<<%1)  
#define _set_hide(%1) _hide |= 1<<%1  
#define _set_no_hide(%1) _hide &= (~1<<%1)  
  
public plugin_init() {  
    register_plugin("[http://amxxmodx.ru] Chat Info Gold", "2.1", "Valer4")  
    g_delay = register_cvar("ci_delay", "13.0")  
    register_clcmd("ci", "switch_show")  
    register_clcmd("say ci", "switch_show")  
    register_clcmd("say /ci", "switch_show")  
    register_clcmd("say \ci", "switch_show")  
    register_clcmd("say_team ci", "switch_show")  
    register_clcmd("say_team /ci", "switch_show")  
    register_clcmd("say_team \ci", "switch_show")  
    register_dictionary("chat_info.txt")  
    static key[8]  
    do {  
        g_count ++  
        formatex(key, 7, "TEXT_%d", g_count)  
    }  
    while(GetLangTransKey(key) != TransKey_Bad)  
    g_count --  
}  
public client_putinserver(id) {  
    static buffer[32]  
    get_user_info(id, "server", buffer, 31)  
    if(buffer[2] == '0')  
        _set_hide(id)  
}  
public client_disconnect(id)  
    if(_is_hide(id))  
        _set_no_hide(id)  
public client_death(killer, victim)  
    set_task(get_pcvar_float(g_delay), "message", victim)  
public message(id)  
    if(is_user_connected(id))  
        if(!is_user_alive(id))  
            if(!_is_hide(id)) {  
                static key[8]  
                formatex(key, 7, "TEXT_%d", random_num(1, g_count))  
                client_print_color(id, print_team_red, "%L", id, key)  
            }  
public switch_show(id) {  
    static buffer[32], len, value[3]  
    value = "10"  
    get_user_info(id, "server", buffer, 31)  
    len = strlen(buffer)  
    if(len < 2)  
        formatex(buffer[len], 31, value[len])  
    if(!_is_hide(id)) {  
        _set_hide(id)  
        buffer[2] = '0'  
        client_cmd(id, "setinfo server %s", buffer)  
        client_print_color(id, print_team_red, "%L", id, "CI_OFF")  
        return PLUGIN_HANDLED  
    }  
    else {  
        _set_no_hide(id)  
        buffer[2] = '1'  
        client_cmd(id, "setinfo server %s", buffer)  
        client_print_color(id, print_team_red, "%L", id, "CI_ON")  
        return PLUGIN_HANDLED  
    }  
}  
public client_infochanged(id) {  
    static buffer[32]  
    get_user_info(id, "server", buffer, 31)  
    if(!_is_hide(id)) {  
        if(buffer[2] == '0')  
            _set_hide(id)  
    }  
    else  
        if(buffer[2] == '1')  
            _set_no_hide(id)  
}
```

