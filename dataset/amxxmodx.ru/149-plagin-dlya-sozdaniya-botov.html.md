# Плагин для создания ботов
[Готовые скрипты](http://amxxmodx.ru/scripts/)
Плагин для создания ботов, которых использую для тестирования функций.  
Это не совсем обычные боты, у них есть 4 варианта поведения:  

    * 1 Ничего не делать  

    * 2 Копирование движений создателя бота  

    * 3 Тоже самое что и 2 + стрельба   

    * 4 Противоположные действия  

  
Так же я закоментировал строки, которые отвечают за то, что бы нельзя было создать более одного бота одним игроком.  
Хотя у меня есть второй компьютер, и могу всегда проверить функцию где нужны именно 2 игрока, зачастую бывает проще все проверить с ботом.  
  
  
```
/************************************************************************************************  
*  
*                Potti v1.40, by p3tsin  
*  
*************************************************************************************************  
*  
*    Description:  
*        Allows admins to create a bot which can be fully controlled,  
*        e.g. move it and handle its menus  
*  
*    Commands:  
*        amx_botadd <name>    - create a new bot  
*        amx_botexec <cmd>    - execute a command on your bot  
*        amx_botmove <0-3>    - 0: off  
*                      1: copy your movements  
*                      2: same as #1 + aim the same spot when shooting  
*                      3: look the opposite way and do the opposite moves  
*        amx_botcmds <1/0>    - when enabled, all owner commands are sent to his/her bot  
*        amx_botdel        - kick your bot off the server  
*  
*    Server cvars:  
*        potti_hudcolor <r g b>    - changes the color of the hud message  
*        potti_hudpos <x y>    - changes the position of the hud message  
*  
*    Note:  
*        When executing commands, only engine cmds will work, so for example cvars cannot  
*        be changed. Also, I recommend you bind a button to "messagemode amx_botexec",  
*        it will be more comfortable to use than opening console every time :)  
*  
*  
*    To Do:  
*        - nothing really (don't feel like messing with buyzone)  
*  
*    Known bugs:  
*        - (cs) when owner is dead, pressing duck will open the specmenu which is really annoying :(  
*        - (cs) can't open buymenu via fullcontrol mode if not in buyzone (or dead)  
*  
*  
*    Changelog:  
*        1.00 - Initial release  
*        1.10 - Added full control mode  
*             - Shows money left on a bot when a buymenu is opened  
*        1.20 - Modified so everyone (with access) can have their own bot  
*             - Cstrike-module is no more needed to display money  
*             - After dying, the owner will automatically move to spectating to his/her bot if botmove is on  
*             - Messages printed to a bot (to center and chat) are shown to its owner too  
*             - Fixed bot latency to show as "BOT"  
*             - More efficient msec calculations  
*             - Other little improvements  
*        1.30 - Added support for The Specialists (press 6 to switch to kungfu when in fullcontrol mode)  
*             - Added botmove 3 to make the bot do the opposite of the owner  
*             - Added a hudtext to show player health, weapon, etc.  
*             - Access level changed from "m" to "p" ^_^  
*             - Removed mod specific definitions  
*        1.40 - Changed owner input hooking style, making it possible for bots to walk and use impulses (flashlight, spray, ..)  
*             - A little tweaking here and there  
*  
*  
*    Credits:  
*        Botman - the source of PODBots helped alot while doing this  
*        Lord of Destruction - aim_at_origin() base taken from set_client_aiming()  
*        THE_STORM - more efficient msec calculations (from ePODbot)  
*        strelomet - display bot latency as "BOT" (from YaPB)  
*        Orangutanz - thanks for pointing out the few improvements;)  
*        Karko - thanks for helping with adding support for TS  
*  
*  
************************************************************************************************/  
  
  
#define ACCESS        ADMIN_LEVEL_D    //access level for bot commands, D is "p" in users.ini  
#define HUD_CHANNEL    4        //hud channel for showing bot info  
  
#include <amxmodx>  
#include <amxmisc>  
#include <fakemeta>  
  
new const plugin[] =    "Potti"  
new const version[] =    "1.40"  
new const author[] =    "p3tsin"  
  
new using_mod        //1: cstrike, 2: specialists, 0: other  
new money_offset    //didnt want to include cstrike just for cs_get_user_money, so i used fakemeta  
  
new botindex[33], botowner[33]  
new botinfo[33], hasmenu[33]  
new copymovements[33]  
new bool:fullcontrol[33]  
  
new Float:botmove[33][3]  
new Float:botangles[33][3]  
new botbuttons[33]  
new botimpulses[33]  
  
new botsnum  
new gMsg_ShowMenu  
new gMsg_TextMsg  
  
new cv_hudcolor  
new cv_hudpos  
  
new fow_serverframe  
new fow_cmdstart  
new fow_clientkill  
  
/* botinfos */  
enum {  
    info_none = 0,  
    info_motd  
}  
  
new slotsnum  
new slotmenukeys  
new currentweapon[33][3]  
new weapon_slots[6][32]  
  
const TASK_BOTINFO = 54387        //random task id for check_botinfo  
  
/* commands which are not blocked/executed in fullcontrol mode */  
new const fullcontrol_cmds[7][] = {  
    "amx_botadd", "amx_botexec", "amx_botmove", "amx_botcmds", "amx_botdel",  
    "specmode", "follow"  
}  
  
// ================================================================================================  
// ================================================================================================  
  
#define get_user_money(%1) get_pdata_int(%1,money_offset)  
#define Distance2D(%1,%2) floatsqroot((%1*%1) + (%2*%2))  
#define Radian2Degree(%1) (%1 * 180.0 / M_PI)            //(%1 * 360.0 / (2 * M_PI))  
  
// ================================================================================================  
// ================================================================================================  
  
public plugin_init() {  
    register_plugin(plugin,version,author)  
    register_clcmd("amx_botadd",    "makebot",ACCESS, "<name> - Create a new bot")  
    register_clcmd("amx_botexec",    "execbot",ACCESS, "<cmd> - Execute a command on your bot")  
    register_clcmd("amx_botmove",    "movebot",ACCESS, "<0-2> - Make the bot copy your movements")  
    register_clcmd("amx_botcmds",    "cmdsbot",ACCESS, "<0/1> - Send all commands to your bot")  
    register_clcmd("amx_botdel",    "removebot",ACCESS, "- Kicks your bot")  
  
    register_clcmd("say",        "catch_say")  
    register_clcmd("say_team",    "catch_say")  
  
    static mod[20]  
    get_modname(mod,19)  
    if(equal(mod,"cstrike") || equal(mod,"czero") || equal(mod,"csv15") || equal(mod,"cs13")) using_mod = 1  
    else if(equal(mod,"ts")) using_mod = 2  
  
    register_event("DeathMsg",    "event_deathmsg", "a")  
    register_event("MOTD",        "event_motd", "b")  
    register_event("ResetHUD",    "event_resethud", "be")  
    register_event("ShowMenu",    "event_showmenu", "b")  
    register_event("TextMsg",    "event_textmsg", "b", "1=4")        //take only print_center  
  
    switch(using_mod) {        //mod specific events  
        case 1: register_event("Spectator",    "event_spectator", "a", "2=1")  
        case 2: {  
            register_event("ClipInfo",    "event_clipinfo", "be")  
            register_event("WeaponInfo",    "event_weaponinfo", "be")    //ts_getuserwpn didnt work right (for a bot)  
            register_event("WStatus",    "event_wstatus", "be")        //updates pev_weapons to make slotmenu work  
        }  
    }  
  
    gMsg_ShowMenu = get_user_msgid("ShowMenu")  
    gMsg_TextMsg = get_user_msgid("TextMsg")  
  
    cv_hudcolor = register_cvar("potti_hudcolor","50 150 200")  
    cv_hudpos = register_cvar("potti_hudpos","0.82 0.85")  
}  
  
public plugin_cfg() {  
    switch(using_mod) {        //mod specific weapons and other settings  
        case 1: {  
            slotsnum = 5  
            set_weaponslot(1,{ 3,5,7,8,12,13,14,15,18,19,20,21,22,23,24,27,28,30,0 })  
            set_weaponslot(2,{ 1,10,11,16,17,26,0 })  
            set_weaponslot(3,{ 29,0 })  
            set_weaponslot(4,{ 4,9,25,0 })  
            set_weaponslot(5,{ 6,0 })  
            money_offset = is_amd64_server() ? 140 : 115  
        }  
        case 2: {  
            slotsnum = 6  
            set_weaponslot(1,{ 24,25,34,35,0 })  
            set_weaponslot(2,{ 1,9,12,14,22,28,31,0 })  
            set_weaponslot(3,{ 3,6,7,17,19,23,0 })  
            set_weaponslot(4,{ 4,5,11,13,15,18,20,26,27,32,33,0 })  
            set_weaponslot(5,{ 8,10,16,21,30,0 })  
            set_weaponslot(6,{ 36,0 })    //kungfu id is 0, so i had to make a special case for it  
        }  
//        default: slotsnum = 0  
    }  
    for(new i = 0; i < slotsnum; i++) slotmenukeys |= (1<<i)  
}  
  
set_weaponslot(slot,weapons[]) {  
    slot--  
    new len = strlen(weapons)  
    for(new i = 0; i < len; i++) weapon_slots[slot][i] = weapons[i]  
}  
  
public client_disconnect(id) {  
    if(is_user_bot(id)) {  
        new owner = botowner[id]  
        if(owner) {  
            copymovements[owner] = 0, botowner[id] = 0  
            botindex[owner] = 0  
            if(!--botsnum) bot_delforwards()  
        }  
    }  
    else {  
        new bot = botindex[id]  
        if(is_user_connected(bot)) server_cmd("kick #%d",get_user_userid(bot))  
        fullcontrol[id] = false, copymovements[id] = 0  
        hasmenu[id] = 0, botindex[id] = 0  
    }  
}  
  
// ================================================================================================  
// ================================================================================================  
  
public makebot(id,level,cid) {  
    if(!cmd_access(id,level,cid,2))  
        return PLUGIN_HANDLED  
  
    /*if(is_user_connected(botindex[id])) {  
        console_print(id, "[%s] You already have a bot connected!",plugin)  
        return PLUGIN_HANDLED  
    }*/  
  
    static name[32]  
    read_args(name,31)  
    remove_quotes(name)  
    trim(name)  
    new bot = engfunc(EngFunc_CreateFakeClient,name)  
    if(!bot) {  
        console_print(id, "[%s] Couldn't create a bot, server full?",plugin)  
        return PLUGIN_HANDLED  
    }  
  
    engfunc(EngFunc_FreeEntPrivateData,bot)  
    bot_settings(bot)  
  
    if(!botsnum) bot_addforwards()  
  
    static szRejectReason[128]  
    dllfunc(DLLFunc_ClientConnect,bot,name,"127.0.0.1",szRejectReason)  
    if(!is_user_connected(bot)) {  
        if(!botsnum) bot_delforwards()  
        console_print(id, "[%s] Connection rejected: %s",plugin,szRejectReason)  
        return PLUGIN_HANDLED  
    }  
  
    dllfunc(DLLFunc_ClientPutInServer,bot)  
    set_pev(bot,pev_spawnflags, pev(bot,pev_spawnflags) | FL_FAKECLIENT)  
    set_pev(bot,pev_flags, pev(bot,pev_flags) | FL_FAKECLIENT)  
  
    reset_controls(id)  
    fullcontrol[id] = false, copymovements[id] = 0  
    botindex[id] = bot, botowner[bot] = id  
    hasmenu[id] = 0, botsnum++  
  
    console_print(id, "[%s] Bot successfully created! Id: %d, name: %s",plugin,bot,name)  
    return PLUGIN_HANDLED  
}  
  
public execbot(id,level,cid) {  
    if(!cmd_access(id,level,cid,2))  
        return PLUGIN_HANDLED  
  
    new bot = botindex[id]  
    if(!is_user_connected(bot)) {  
        console_print(id, "[%s] You have no bot connected..",plugin)  
        return PLUGIN_HANDLED  
    }  
  
    static cmd[32], name[32]  
    read_argv(1, cmd,31)  
    get_user_name(bot, name,31)  
  
    if(equal(cmd,"say") || equal(cmd,"say_team")) {  
        static saytext[128], team  
        new len = strlen(cmd) + 1  
        read_args(saytext,127)  
        if(equal(cmd,"say_team")) team = 1  
        bot_say(bot,team,saytext[len])  
        console_print(id, "[%s] Executed on %s: %s %s",plugin,name,cmd,saytext)  
        return PLUGIN_HANDLED  
    }  
  
    static args[2][32]  
    new num = read_argc()-2  
    args[0][0] = 0, args[1][0] = 0  
    for(new i = 0; i < num; i++) read_argv(i+2, args[i],31)  
  
    if(equal(cmd,"kill")) dllfunc(DLLFunc_ClientKill, bot)  
    else if(equal(cmd,"name")) set_user_info(bot,"name",args[0])  
    else if(equal(cmd,"model")) set_user_info(bot,"model",args[0])  
    else bot_command(bot,cmd,args[0],args[1])  
  
    console_print(id, "[%s] Executed on %s: %s %s %s",plugin,name,cmd,args[0],args[1])  
    return PLUGIN_HANDLED  
}  
  
public movebot(id,level,cid) {  
    if(!cmd_access(id,level,cid,2))  
        return PLUGIN_HANDLED  
  
    if(!is_user_connected(botindex[id])) {  
        console_print(id, "[%s] You have no bot connected..",plugin)  
        return PLUGIN_HANDLED  
    }  
  
    static arg[2], message[64]  
    read_argv(1, arg,1)  
  
    new num = str_to_num(arg)  
    if(num < 0 || num > 3) num = 0  
  
    switch(num) {  
        case 0: formatex(message,63, "not copying your moves at all")  
        case 1: formatex(message,63, "copying your movements")  
        case 2: formatex(message,63, "copying your movements and aiming the same spot when shooting")  
        case 3: formatex(message,63, "copying your movements in reverse mode")  
    }  
  
    copymovements[id] = num  
    console_print(id, "[%s] Your bot is now %s",plugin,message)  
    return PLUGIN_HANDLED  
}  
  
public cmdsbot(id,level,cid) {  
    if(!cmd_access(id,level,cid,2))  
        return PLUGIN_HANDLED  
  
    if(!is_user_connected(botindex[id])) {  
        console_print(id, "[%s] You have no bot connected..",plugin)  
        return PLUGIN_HANDLED  
    }  
  
    new arg[2]  
    read_argv(1, arg,1)  
    new bool:value = str_to_num(arg) ? true : false  
  
    fullcontrol[id] = value  
    console_print(id, "[%s] Fullcontrol mode: %s",plugin,value?"ON (you can't control yourself now)":"OFF")  
    slotmenu(id,value)  
    return PLUGIN_HANDLED  
}  
  
public removebot(id,level,cid) {  
    if(!cmd_access(id,level,cid,1))  
        return PLUGIN_HANDLED  
  
    new bot = botindex[id]  
    if(is_user_connected(bot)) {  
        static name[32]  
        get_user_name(bot, name,31)  
        console_print(id, "[%s] Bot %s kicked!",plugin,name)  
        server_cmd("kick #%d",get_user_userid(bot))  
    }      
    else console_print(id, "[%s] You have no bot connected..",plugin)  
    return PLUGIN_HANDLED  
}  
  
// ================================================================================================  
// ================================================================================================  
  
public check_botinfo() {  
    static text[192], len, weapon  
    static players[32], inum, bot, owner  
    get_players(players,inum, "dh")  
  
    static temp[3][10], color[3], Float:pos[2], i  
    get_pcvar_string(cv_hudcolor, text,20)  
    parse(text, temp[0],3, temp[1],3, temp[2],3)  
    for(i = 0; i < 3; i++) color[i] = str_to_num(temp[i])  
  
    get_pcvar_string(cv_hudpos, text,20)  
    parse(text, temp[0],9, temp[1],9)  
    for(i = 0; i < 2; i++) pos[i] = floatstr(temp[i])  
  
    new Float:holdtime = (using_mod == 2) ? 120.0 : 1.0    //TS handles hudmessages differently  
    set_hudmessage(color[0],color[1],color[2], pos[0],pos[1], 0, 0.0, holdtime, 0.0, 0.2, HUD_CHANNEL)  
  
    static bool:was_alive[33]  
    static name[32], weaponname[20], clip, ammo  
    for(i = 0; i < inum; i++) {  
        bot = players[i], owner = botowner[players[i]]  
        if(!owner) continue        //no owner, so this might be some other bot :o  
  
        switch(botinfo[owner]) {  
            case info_motd: {  
                set_pev(bot,pev_button,IN_ATTACK)  
                //client_print(owner,print_chat, "[%s] Note: a MOTD window was closed on your bot",plugin)  
            }  
        }  
        botinfo[owner] = info_none  
  
        if(!is_user_alive(bot)) {  
            if(was_alive[bot]) {    //hide hudmessage after death (mainly for TS)  
                //show_hudmessage(owner,"^n")  
                was_alive[bot] = false  
            }  
            continue  
        }  
        was_alive[bot] = true  
  
        if(using_mod == 2) weapon = get_ts_weapon(bot,clip,ammo)  
        else weapon = get_user_weapon(bot,clip,ammo)  
  
        get_user_name(bot, name,31)  
        get_weaponname(weapon, weaponname,19)  
        if(using_mod == 1) copy(weaponname,19, weaponname[7])    //cut off the "weapon_" tag  
  
        len = formatex(text,191, "Name: %s, Health: %d",name,get_user_health(bot))  
        len += formatex(text[len],191-len, "^nWeapon: %s, Ammo: %d/%d",weaponname,clip,ammo)  
  
        if(using_mod == 1) formatex(text[len],191-len, "^nMoney left: $%d",get_user_money(bot))  
        //show_hudmessage(owner,"%s",text)  
    }  
}  
  
public client_command(id) {  
    new bot = botindex[id]  
    if(!bot) return PLUGIN_CONTINUE  
  
    static cmd[32]  
    read_argv(0, cmd,31)  
  
    new menu = hasmenu[id]  
    if(menu && equal(cmd,"menuselect")) {  
        new num[3]                //no need to check if menu even has this key,  
        read_argv(1, num,2)            //coz menuselect wont be called if it doesnt  
  
        hasmenu[id] = 0  
        if(fullcontrol[id]) slotmenu(id,true)  
  
        switch(menu) {  
            case 1: engclient_cmd(bot,"menuselect",num)  
            case 2: change_to_weapon(bot,str_to_num(num))  
        }  
        return PLUGIN_HANDLED  
    }  
    else if(fullcontrol[id]) {  
        new num = sizeof(fullcontrol_cmds)  
        for(new i = 0; i < num; i++) {  
            if(!equali(cmd,fullcontrol_cmds[i])) continue  
            return PLUGIN_CONTINUE  
        }  
  
        if(!contain(cmd,"say")) {  
            static saytext[128], team  
            read_args(saytext,127)  
            remove_quotes(saytext)  
            if(equal(cmd,"say_team")) team = 1  
            bot_say(bot,team,saytext)  
        }  
        else {  
            static arg1[32], arg2[32]  
            read_argv(1, arg1,95)  
            read_argv(2, arg2,31)  
            bot_command(bot,cmd,arg1,arg2)  
        }  
        return PLUGIN_HANDLED  
    }  
    return PLUGIN_CONTINUE  
}  
  
// ================================================================================================  
// ================================================================================================  
  
public fm_cmdstart(id,uc_handle,random_seed) {  
    new bot = botindex[id], movement = copymovements[id]  
    if(!bot || !movement) return FMRES_IGNORED  
  
    new alive = is_user_alive(id), button = get_uc(uc_handle,UC_Buttons)  
    if(!alive) set_uc(uc_handle,UC_Buttons, button & ~IN_JUMP & ~IN_ATTACK & ~IN_ATTACK2 & ~IN_FORWARD & ~IN_BACK & ~IN_MOVELEFT & ~IN_MOVERIGHT)  
  
    if(is_user_alive(bot)) {  
        get_uc(uc_handle,UC_ForwardMove, botmove[id][0])  
        get_uc(uc_handle,UC_SideMove, botmove[id][1])  
        get_uc(uc_handle,UC_UpMove, botmove[id][2])  
  
        static Float:angles[3]  
        if(movement == 2 && alive && button&IN_ATTACK) {  
            static Float:target[3]  
            get_user_aim(id,target)  
            aim_at_origin(bot,target,angles)  
        }  
        else {  
            get_uc(uc_handle,UC_ViewAngles, angles)  
            if(movement == 3 && alive) {  
                angles[1] += (angles[1] < 180.0) ? 180.0 : -180.0  
                if(button&IN_JUMP) button = button & ~IN_JUMP | IN_DUCK  
                else if(button&IN_DUCK) button = button & ~IN_DUCK | IN_JUMP  
            }  
        }  
        botangles[id][0] = angles[0]  
        botangles[id][1] = angles[1]  
        botangles[id][2] = angles[2]  
        botbuttons[id] = button  
        botimpulses[id] = get_uc(uc_handle,UC_Impulse)  
    }  
    return FMRES_IGNORED  
}  
  
public fm_serverframe() {  
    static players[32], inum  
    get_players(players,inum, "dh")  
  
    static Float:msecval  
    global_get(glb_frametime, msecval)  
    new msec = floatround(msecval * 1000.0)  
  
    static bot, owner, Float:angles[3]  
    for(new i = 0; i < inum; i++) {  
        bot = players[i], owner = botowner[bot]  
        if(!owner) continue        //no owner, so this might be some other bot :o  
  
        if(is_user_alive(bot)) {  
            angles[0] = botangles[owner][0]  
            angles[1] = botangles[owner][1]  
            angles[2] = botangles[owner][2]  
  
            set_pev(bot,pev_v_angle,angles)  
            angles[0] /= -3.0  
            set_pev(bot,pev_angles,angles)  
        }  
        engfunc(EngFunc_RunPlayerMove,bot,angles,botmove[owner][0],botmove[owner][1],botmove[owner][2],botbuttons[owner],botimpulses[owner],msec)  
    }  
    return FMRES_IGNORED  
}  
  
public fm_clientkill(id) {  
    new bot = botindex[id]  
    if(bot && fullcontrol[id]) {  
        if(is_user_alive(bot)) dllfunc(DLLFunc_ClientKill, bot)  
        else console_print(id, "[%s] Can't suicide -- your bot is already dead",plugin)  
        return FMRES_SUPERCEDE  
    }  
    return FMRES_IGNORED  
}  
  
// ================================================================================================  
// ================================================================================================  
  
public catch_say(id) {  
    if(!botsnum) return  
  
    static cmd[10], said[128]  
    read_argv(0, cmd,9)  
    read_args(said,127)  
    remove_quotes(said)  
  
    new teamsay = equal(cmd,"say_team") ? 1 : 0  
    handle_saytext(id,said,teamsay)  
}  
  
public event_deathmsg() {  
    new id = read_data(2)  
    if(!botindex[id]) {  
        id = botowner[id]  
        if(id) reset_controls(id)  
        return  
    }  
  
    new len  
    static message[128]  
    if(copymovements[id]) len = formatex(message,127, "botmove (you can't control yourself completely), ")  
  
    if(fullcontrol[id]) len += formatex(message[len],127-len, "botcmds (all of your commands are sent to the bot)")  
    else if(len) message[len-2] = 0  
  
    if(len) ucfirst(message)  
    else formatex(message,127, "None")  
  
    client_print(id,print_chat, "[%s] You have the following modes enabled:",plugin)  
    client_print(id,print_chat, "* %s",message)  
}  
  
public event_motd(id) {  
    new owner = botowner[id]  
    if(owner) botinfo[owner] = info_motd  
}  
  
public event_resethud(id) {  
    new owner = botowner[id]  
    if(owner) {  
        //client_print(owner,print_chat, "[%s] Your bot has spawned",plugin)  
        if(using_mod == 2) {  
            set_pev(id,pev_weapons,0)  
            currentweapon[id][0] = 0  
            currentweapon[id][1] = 0  
            currentweapon[id][2] = 0  
        }  
    }  
}  
  
public event_showmenu(id) {  
    new owner = botowner[id]  
    if(!owner) return  
  
    static menu[32]  
    new keys = read_data(1)  
    read_data(4, menu,31)  
    if(!strlen(menu)) return  
  
    hasmenu[owner] = 1        //keypress is catched in client_command()  
    message_begin(MSG_ONE,gMsg_ShowMenu,{0,0,0},owner)  
    write_short(keys)  
    write_char(-1)  
    write_byte(0)  
    write_string(menu)  
    message_end()  
  
    //client_print(owner,print_chat, "[%s] A menu was opened on your bot: %s",plugin,menu)  
}  
  
public event_spectator() {  
    new id = read_data(1)  
    if(copymovements[id]) {  
        client_cmd(id, "specmode 4")        //first person  
        set_task(0.3,"next_spectarget",id)  
    }  
}  
  
public next_spectarget(id) {  
    new bot = botindex[id]  
    if(is_user_alive(bot)) {  
        static name[32]  
        get_user_name(bot, name,31)  
        client_cmd(id, "follow ^"%s^"",name)  
    }  
}  
  
public event_textmsg(id) {  
    new owner = botowner[id]  
    if(!owner || !is_user_alive(id)) return  
  
    static message[32]  
    new datanum = read_datanum()  
    read_data(2, message,31)  
  
    message_begin(MSG_ONE,gMsg_TextMsg,{0,0,0},owner)  
    write_byte(4)  
    write_string(message)  
  
    for(new i = 3; i < datanum; i++) {  
        read_data(i, message,31)  
        write_string(message)  
    }  
  
    message_end()  
    return  
}  
  
public event_clipinfo(id) {  
    if(botowner[id]) currentweapon[id][1] = read_data(1)  
}  
  
public event_weaponinfo(id) {  
    if(botowner[id]) {  
        currentweapon[id][0] = read_data(1)  
        currentweapon[id][1] = read_data(2)  
        currentweapon[id][2] = read_data(3)  
    }  
}  
  
public event_wstatus(id) {  
    new owner = botowner[id]  
    if(!owner) return  
  
    new wp = read_data(1), status = read_data(2)  
    new wlist = pev(id,pev_weapons), weapon = (1<<wp)  
    if(status) set_pev(id,pev_weapons, wlist | weapon)  
    else set_pev(id,pev_weapons, wlist & ~weapon)  
    return  
}  
  
// ================================================================================================  
// ================================================================================================  
  
stock get_user_aim(id,Float:aimorig[3]) {  
    static Float:origin[3], Float:view_ofs[3]  
    pev(id,pev_origin, origin)  
    pev(id,pev_view_ofs, view_ofs)  
    origin[0] += view_ofs[0]  
    origin[1] += view_ofs[1]  
    origin[2] += view_ofs[2]  
  
    static Float:vec[3]  
    pev(id,pev_v_angle, vec)  
    engfunc(EngFunc_MakeVectors,vec)  
    global_get(glb_v_forward,vec)  
    vec[0] = origin[0] + vec[0] * 9999.0  
    vec[1] = origin[1] + vec[1] * 9999.0  
    vec[2] = origin[2] + vec[2] * 9999.0  
  
    static line  
    engfunc(EngFunc_TraceLine,origin,vec,0,id,line)  
    get_tr2(line,TR_vecEndPos, aimorig)  
}  
  
stock aim_at_origin(id,const Float:origin[3],Float:angles[3]) {            //stock base by Lord of Destruction  
    static Float:DeltaOrigin[3], Float:orig[3]  
    pev(id,pev_origin, orig)  
    DeltaOrigin[0] = orig[0] - origin[0]  
    DeltaOrigin[1] = orig[1] - origin[1]  
    DeltaOrigin[2] = orig[2] - origin[2] + 16.0    //bot keeps aiming too high  
  
    angles[0] = Radian2Degree(floatatan(DeltaOrigin[2] / Distance2D(DeltaOrigin[0], DeltaOrigin[1]),0))  
    angles[1] = Radian2Degree(floatatan(DeltaOrigin[1] / DeltaOrigin[0],0))  
    if(DeltaOrigin[0] >= 0.0) angles[1] += 180.0  
}  
  
stock change_to_weapon(id,slot) {  
    if(slot > slotsnum) return 0  
  
    if(using_mod == 2 && slot == 6) {  
        engclient_cmd(id,"weapon_0")  
        return 1  
    }  
  
    new wnum  
    static weapons[32], a  
    get_user_weapons(id,weapons,wnum)  
    new weapon, num = strlen(weapon_slots[--slot])  
  
    for(new i = 0; i < wnum; i++) {  
        for(a = 0; a < num; a++) {  
            if(weapons[i] != weapon_slots[slot][a]) continue  
            weapon = weapons[i]  
            break  
        }  
        if(weapon) break  
    }  
  
    if(weapon) {  
        static weaponname[20]  
        if(using_mod == 2) formatex(weaponname,19, "weapon_%d",weapon)  
        else get_weaponname(weapon,weaponname,19)  
        engclient_cmd(id,weaponname)  
        return 1  
    }  
    return 0  
}  
  
stock get_ts_weapon(id,&clip,&ammo) {  
    if(!is_user_bot(id)) return 0  
    clip = currentweapon[id][1]  
    ammo = currentweapon[id][2]  
    return currentweapon[id][0]  
}  
  
// ================================================================================================  
// ================================================================================================  
  
handle_saytext(id,said[],teamsay) {  
    static name[32], text[192], teamname[20]  
    get_user_name(id, name,31)  
  
    new len, alive = is_user_alive(id)  
    if(!alive) len = formatex(text,191, "*DEAD*")  
    if(teamsay) {  
        get_user_team(id, teamname,19)  
        len += formatex(text[len],191-len, "(%s)",teamname)  
    }  
    else teamname[0] = 0  
  
    if(len) text[len++] = ' '        //add a space;)  
    formatex(text[len],191-len, "%s :  %s",name,said)  
  
    static players[32], inum, owner, flags[5]  
    formatex(flags,4, "dh%c%c",alive ? 'a' : 'b',teamsay ? 'e' : 0)  
    get_players(players,inum, flags,teamname)    //teamname is set only if teamsay is on  
  
    for(new i = 0; i < inum; i++) {  
        owner = botowner[players[i]]  
        if(owner && alive != is_user_alive(owner)) client_print(owner,print_chat, "%s",text)  
    }  
}  
  
bot_command(id,cmd[],arg1[]="",arg2[]="") {  
    if(strlen(arg2)) engclient_cmd(id,cmd,arg1,arg2)  
    else if(strlen(arg1)) engclient_cmd(id,cmd,arg1)  
    else engclient_cmd(id,cmd)  
}  
  
slotmenu(id,bool:mode) {  
    hasmenu[id] = mode ? 2 : 0  
    message_begin(MSG_ONE,gMsg_ShowMenu,{0,0,0},id)  
    write_short(mode ? slotmenukeys : 0)  
    write_char(-1)  
    write_byte(0)  
    write_string("^n")  
    message_end()  
}  
  
bot_addforwards() {  
    fow_cmdstart = register_forward(FM_CmdStart,"fm_cmdstart",0)  
    fow_serverframe = register_forward(FM_StartFrame,"fm_serverframe",1)  
    fow_clientkill = register_forward(FM_ClientKill,"fm_clientkill",0)  
  
    set_task(1.0,"check_botinfo",TASK_BOTINFO, "",0, "b")  
}  
  
bot_delforwards() {  
    unregister_forward(FM_CmdStart,fow_cmdstart,0)  
    unregister_forward(FM_StartFrame,fow_serverframe,1)  
    unregister_forward(FM_ClientKill,fow_clientkill,0)  
  
    remove_task(TASK_BOTINFO)  
}  
  
bot_settings(id) {  
    set_user_info(id, "model",        "gordon")  
    set_user_info(id, "rate",        "3500")  
    set_user_info(id, "cl_updaterate",    "30")  
    set_user_info(id, "cl_lw",        "0")  
    set_user_info(id, "cl_lc",        "0")  
    set_user_info(id, "tracker",        "0")  
    set_user_info(id, "cl_dlmax",        "128")  
    set_user_info(id, "lefthand",        "1")  
    set_user_info(id, "friends",        "0")  
    set_user_info(id, "dm",            "0")  
    set_user_info(id, "ah",            "1")  
  
    set_user_info(id, "*bot",        "1")  
    set_user_info(id, "_cl_autowepswitch",    "1")  
    set_user_info(id, "_vgui_menu",        "0")        //disable vgui so we dont have to  
    set_user_info(id, "_vgui_menus",    "0")        //register both 2 types of menus :)  
}  
  
bot_say(id,team,text[]) {  
    engclient_cmd(id,team ? "say_team" : "say",text)  
    handle_saytext(id,text,team)  
}  
  
reset_controls(owner) {  
    botmove[owner][0] = 0.0  
    botmove[owner][1] = 0.0  
    botmove[owner][2] = 0.0  
    botangles[owner][0] = 0.0  
    botangles[owner][1] = 0.0  
    botangles[owner][2] = 0.0  
    botbuttons[owner] = 0  
    botimpulses[owner] = 0  
}  

```

