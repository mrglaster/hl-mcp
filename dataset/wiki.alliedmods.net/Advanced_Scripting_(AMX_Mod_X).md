# Advanced Scripting (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#p-search)
This article will briefly summarize some of the more advanced topics of [AMX Mod X Scripting](https://wiki.alliedmods.net/Category:Scripting_\(AMX_Mod_X\) "Category:Scripting \(AMX Mod X\)"). 
## Contents
  * [1 Tasks](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#Tasks)
  * [2 Menus](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#Menus)
  * [3 Events/Messages](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#Events.2FMessages)
  * [4 Catching Log Messages](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#Catching_Log_Messages)
  * [5 Multi-Lingual Support](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#Multi-Lingual_Support)
  * [6 SQL Support](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#SQL_Support)
  * [7 Regular Expressions](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#Regular_Expressions)
  * [8 Entities](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#Entities)
  * [9 FakeMeta](https://wiki.alliedmods.net/Advanced_Scripting_\(AMX_Mod_X\)#FakeMeta)


# Tasks
Tasks are timers that let you run code at an interval, either once or repeated. They are useful for things like waiting a few seconds, setting objects to destroy themselves, or just repeating a task over and over. 
A task can be set in a number of different ways. The actual function is set_task(): 
```
set_task(Float:time,const function[],id = 0,parameter[]="",len = 0,flags[]="", repeat = 0)
```

The parameters break down as such: 
  * Float:time - Interval of timer in seconds (minimum 0.1 seconds)
  * function[] - A string that contains the public function to run on the timer
  * id - A unique id to assign to the task
  * parameter - An array contain data to send to the timer function
  * len - Size of the array to send to the timer function
  * flags - One of the following: 
    * "a" - Repeat task a specified number of times
    * "b" - Loop task infinitely
    * "c" - do task on time after a map timeleft
    * "d" - do task on time before a map timeleft
  * repeat - If flags is "a", specifies the number of times to repeat the task


An example of a task is below. It will slap a specified player 5 times, once per second. 
```
//the timed function receives the parameter array and its task id
public slapTask(params[], id)
{
   new player = params[0]
   user_slap(player, 5)
}
 
public start_slapping(id)
{
   new params[1]
   params[0] = id
   //we don't need a specific id
   set_task(1.0, "slapTask", 0, params, 1, "a", 5)
}
```

Note that if you specify 0 for task id, then the task function should look like: 
```
public slapTask()
```

  

# Menus
Menus are HUD messages that give a player a choice of options to select. They are quite messy to deal with but can be very useful for things like voting and command selection. 
Menus must be registered by two things - a set of "keys" that tells how many options to register and a string which identifies the menu as unique. This string must appear in the beginning of every menu you want to trigger your function. When you display a menu, you can show it to one or more players. Once they hit a key, the result of their key press will be sent to the function you registered the menu to. 
For our example, we'll make a menu that displays a list of guns: AK47, M4A1, or AWP, to a player. Whichever he selects, he will be given. 
```
#include <amxmodx>
#include <amxmisc>
#include <fun>
public plugin_init()
{
    register_plugin("Menu Demo", "1.0", "BAILOPAN")
    new keys = MENU_KEY_0|MENU_KEY_1|MENU_KEY_2
    register_menucmd(register_menuid("Which Weapon?"), keys, "giveWeapon")
}
```

Two commands are apparent here - register_menuid and register_menucmd. register_menuid registers a short phrase that will appear at the beginning of the menu, then returns an id. This id is the first parameter to register_menucmd. The second parameter to register_menucmd is the key configuration. Our menu will have three options, so we've added three menu keys in. In actuality, these are bitwise flags totalling "7", but that's not important. The last parameter is the public function that will handle the menu results. 
Next, how do we show the menu? Let's make a quick console command: "giveme". 
```
public plugin_init()
{
    register_plugin("Menu Demo", "1.0", "BAILOPAN")
    new keys = MENU_KEY_0|MENU_KEY_1|MENU_KEY_2
    register_menucmd(register_menuid("Which Weapon?"), keys, "giveWeapon")
    register_clcmd("giveme", "showWeaponMenu")
}
```

register_clcmd is similar to register_concmd, except it only takes two parameters. It's used to register any command a client can use (except for special ones, like +attack). 
```
//The clcmd function will just give us the player id
public showWeaponMenu(id)
{
    new menu[192]
    new keys = MENU_KEY_0|MENU_KEY_1|MENU_KEY_2
 
    format(menu, 191, "Which Weapon?^n^n1. AK47^n2. M4A1^n3. AWP")
    show_menu(id, keys, menu)
    return PLUGIN_HANDLED
}
 
//Our menu function will get the player id and the key they pressed
public giveWeapon(id, key)
{
    //key will start at zero
    if (key == 0)
    {
         give_item(id, "weapon_ak47")
    } else if (key == 1) {
         give_item(id, "weapon_m4a1")
    } else if (key == 2) {
         give_item(id, "weapon_awp")
    }
}
```

And we're done! The format line may be a little confusing. The "^n" means "new line", so the menu looks nicely formatted. You can use other modifiers in VGUI2 mods, such as "\w" for white text, "\r" for red text, and "\y" for yellow text. When a player types the command, he will see the menu. When he hits a key, the giveWeapon function will receive his id and the key number he pressed. Then he will get a gun corresponding to what he chose. 
# Events/Messages
For this demonstration, we're going to extend the above example. Every time a player respawns, he will be shown the menu to choose a weapon (note - we're ignoring other things like blocking buying and removing buyzones, this is just a demonstration). 
Messages are a way for Half-Life clients to talk to servers, and vice versa. They are specially formatted lists of parameters. For example, the message "DeathMsg" (message id 83) has three parameters: Attacker (byte), Victim (byte), and Weapon (string). You can either capture messages or send them. Here, we'll do a simple demonstration of both. First let's make it so a user gets their gun menu when they spawn. 
```
public plugin_init()
{
    register_plugin("Menu Demo", "1.0", "BAILOPAN")
    new keys = MENU_KEY_0|MENU_KEY_1|MENU_KEY_2
    register_menucmd(register_menuid("Which Weapon?"), keys, "giveWeapon")
    //flags - b means "sent to one target", e means "target is alive"
    //this event is sent when a player spawns
    register_event("ResetHUD", "hook_hud", "be")
}
 
public hook_hud(id)
{
    //since we specify no parameters to the task,
    //the task id will be given to the function
    //this is useful because we can reuse our old
    //show menu function which takes an id
    set_task(0.2, "showWeaponMenu", id)
}
```

Note that we've set a small delay when we receive the message - this is to make sure that the user has had time to respawn. register_event can take more parameters in order to help restrict the event you catch - for example only matching certain parameters. You can read more about this in the function reference. 
Now, let's say we want to figure out when a player has died... 
```
public plugin_init()
{
    register_plugin("Message Demo", "1.0", "BAILOPAN")
    //this message informs everyone of a death, so we use
    // flag "a" - global event
    register_event("DeathMsg", "hook_death", "a")
}
 
public hook_death()
{
    new Killer = read_data(1) //get the first message parameter
    new Victim = read_data(2) //get the second message parameter
    new headshot = read_data(3) //was this a headshot?
    new weapon[32]
    read_data(4, weapon, 31)  //get the weapon name
}
```

Or, let's say we want to make a simple function for generating a death message: 
```
stock make_deathMsg(Killer, Victim, const weapon[])
{
    //message_begin starts a message.  NEVER start two messages at once.
    //MSG_ALL means send the message to everyone
    //get_user_msgid returns the id of a message name
    //{0,0,0} is the origin vector - not used here
    //0 is the target - no specific target here
    message_begin(MSG_ALL, get_user_msgid("DeathMsg"), {0,0,0}, 0) 
    write_byte(Killer)
    write_byte(Victim)
    write_string(weapon)
    message_end()
}
```

To find more about messages, consult the HLSDK, AMX Mod X forums, HL-related programming sites, or other plugins. To list the messages a mod has, type "meta game" in the server console (with metamod loaded). You can also use register_message, the more advanced message disection method found in the Engine module. 
# Catching Log Messages
Catching log messages is not used heavily any more, but it's still good to know how to do it. As log messages are sent by the mod, AMX Mod X will be able to catch them and let you hook them. For our example, let's give everyone $16,000 on round start. 
The log messages for rounds are sent like this: World triggered "Round_Start". AMX Mod X will consider "World_triggered" as the first parameter and "Round_Start" as the second parameter. So: 
```
#include <amxmodx>
 
public plugin_init()
{
    register_plugin("Log Demo", "1.0", "BAILOPAN")
    //this will filter for two parameters
    //roundstart is the public function
    register_logevent("roundstart", 2, "0=World triggered", "1=Round_Start")
}
 
public roundstart()
{
    //set a small delay to make sure everyone spawns
    set_task(1.0, "roundDelay")
}
 
public roundDelay(taskId)
{
    new players[32], num
    get_players(players, num)
 
    for (new i=0; i<num; i++)
    {
         cs_set_user_money(players[i], 16000)
    }
}
```

You can also read specific log parameters with read_logdata(), which can only be used inside the "plugin_log()" forward: 
```
//receives all log messages
public plugin_log()
{
    new data[32]
    read_logdata(data, 31)
}
```

  

# Multi-Lingual Support
Adding multi-lingual support to a plugin can be difficult, but it's usually worth it if you have clients who are willing to translate your strings into their native language. 
The first step is to identify what needs to be translated. Say you have a call like this: 
```
new score = get_score()
client_print(id, print_chat, "[AMXX] Your score is %d", score)
```

This is a good candidate for being multi-lingual. First, create a .txt file (preferrably named after your plugin) and store it in addons\amxmodx\data\lang\\. Let's use "myplugin.txt" for the example. For each language, add an entry to the file. Entries are set up as 'keys', which are matched to 'translation strings'. Observe: 
```
(addons\amxmodx\data\lang\myplugin.txt)

[en]
SCORE_MSG = Your score is %d

[de]
SCORE_MSG = Ihr Spielergebnis ist %d

[es]
SCORE_MSG = Su cuenta es %d

[fr]
SCORE_MSG = Votre score est %d

```

Then, in plugin_init(), you must register the language keys: 
```
public plugin_init()
{
    ...
    //assumes placed in amxmodx\data\lang
    register_dictionary("myplugin.txt")
}
```

Now, here comes the hard part. AMX Mod X's Multi-Lingual API is built into the format() style routines. For anything that looks like or uses format()-style strings, you can use the ML API. 
```
    client_print(id, print_chat, "[AMXX] %L", id, "SCORE_MSG", get_score())
```

Let's break this down. For each %L that appears, we need at least two parameters. The first parameter is the TARGET. This must be a player id, LANG_SERVER (meaning show in the server's native language), or LANG_PLAYER. LANG_PLAYER is a special modifier that should only be used when sending a message to all players - it means "show in every player's native language". The second parameter is the key string that identifies the language phrase to translate. Lastly, if the translated string requires any parameters itself (ours needs %d, one integer), that must be added as well. 
You can get very complicated designs with this, but it's recommended that you keep things simple for clarity. Here is a final example using a global message to all players, assuming the key HELLO is properly translated in all the languages available: 
```
    client_print(0, print_chat, "[AMXX] %L", LANG_PLAYER, "HELLO")
```

# SQL Support
SQL support has greatly improved in AMX Mod X. There is a common set of natives that work with a single driver, so as long as one (and only one) SQL module is loaded, the SQL (or DBI) natives will work. Here is a short primer on how to use the DBI natives: 
```
//Create a connection
	new Sql:mysql = dbi_connect("localhost", "dvander", "pass", "dbase")
 
//If the connection is less than 1, it is bad	
	if (mysql < SQL_OK) {
		new err[255]
		new errNum = dbi_error(mysql, err, 254)
		server_print("error1: %s|%d", err, errNum)
		return 1
	}
 
	server_print("Connection handle: %d", mysql)
//Run a query
	new Result:ret = dbi_query(mysql, "INSERT INTO config (keyname, val) VALUES ('amx', 'yes')")
 
//If the query is less than RESULT_NONE, it failed	
	if (ret < RESULT_NONE) {
		new err[255]
		new errNum = dbi_error(mysql, err, 254)
		server_print("error2: %s|%d", err, errNum)
		return 1
	}
 
//Do a select query	
	new Result:res = dbi_query(mysql, "SELECT * FROM config")
 
//If the query is less than or equal to RESULT_FAILED, you got an invalid result and can't do anything with it.
	if (res <= RESULT_FAILED) {
		new err[255]
		new errNum = dbi_error(mysql, err, 254)
		server_print("error3: %s|%d", err, errNum)
		return 1
	}
 
	server_print("Result handle: %d", res)
 
//Loop through the result set	
	while (res && dbi_nextrow(res)>0) {
		new qry[32]
//Get the column/field called "keyname" from the result set
		dbi_result(res, "keyname", qry, 32)
		server_print("result: %s", qry)
	}
 
//Free the result set	
	dbi_free_result(res)
 
//Close the connection	
	dbi_close(mysql)
```

# Regular Expressions
Regular Expressions let you describe ways in which to break down strings. They are extremely powerful. AMX Mod X uses the Perl Compatible RE library, you can read the specifics at their site. AMX Mod X offers regular expressions with the regex_amxx module. Here is a short example: 
```
#include <amxmodx>
#include <regex>
 
public plugin_init()
{
    register_plugin("Regex", "1.0", "BAILOPAN")
    register_srvcmd("amx_regex", "cmdtest")
}
 
public cmdtest()
{
    new str[] = "It's Walky!"
    //this pattern will match any string which contains
    // two groupings of characters separated by a space
    // the two groupings are substrings 1 and 2
    new pattern[] = "(.+) (.+)"
 
    new num, error[128]
    //str = string
    //pattern = pattern to use
    //num = special return case code
    //error = if there's an error, it will go here
    //127 - error's max length
    new Regex:re = regex_match(str, pattern, num, error, 127)
 
    server_print("Result=%d, num=%d, error=%s", re, num, error)    
 
    //REGEX_OK means there was a match
    if (re >= REGEX_OK)
    {
        new str2[64]
        //since it returned REGEX_OK, num has
        // the number of substrings matched by the pattern.
        //the first substring (0) seems to match the whole string.
        for (new i=0; i<num; i++)
        {
            regex_substr(re, i, str2, 63)
            server_print("Substring %d: %s", i, str2)
        }
        //the regular expression matcher uses memory.
        //you must free it if you get REGEX_OK
        //This will also set re to 0.
        regex_free(re)
    }
 
    //note the invalid regular expression pattern
    //this will return REGEX_PATTERN_FAIL, -1
    re = regex_match("Bruno the Bandit", ".+(]", num, error, 127)
 
    server_print("Result=%d, num=%d, error=%s", re, num, error)
}
```

If you compile and run this script (amx_regex in server console) you will see the following output: 
```
Result=1, num=3, error=
Substring 0: It's Walky!
Substring 1: It's
Substring 2: Walky!
Result=-1, num=4, error=missing ) 

```

Note that the third parameter to "regex_match()" is special. It's either the number of substrings, a match error code, or a pattern error position (depending on the return value). 
# Entities
Entities are basically any dynamic structure in Half-Life. Players, weapons, grenades, and other little objects laying around are entities. They have a unique "entity id" which you can use to change their values. 
I won't go into this too deeply as it's a complicated subject, but the Engine module features natives that let you modify the properties of entities, or search for entities in game by their class/owner (class is the type of entity, such as "player"). 
For this example, we'll make an entity that looks like a fake player holding a gun. 
```
	//create a basic entity
	new entid = create_entity("info_target")
	//set its classname
	entity_set_string(entid, EV_SZ_classname, "some_guy")
	//set its model
	entity_set_model(entid, "models/w_suit.mdl")
	new Float:Vec[3] = {0.0,0.0,0.0}
	//set its origin 
	entity_set_origin(entid, Vec)
	//set some basic properties
	entity_set_int(entid, EV_INT_solid, 1)
	entity_set_int(entid, EV_INT_movetype, 6)
	//create the weapon - thanks to pimp_daddy!
	entWeapon = create_entity("info_target")
	entity_set_string(entWeapon, EV_SZ_classname, weapString)
	//set to follow
	entity_set_int(entWeapon, EV_INT_movetype, MOVETYPE_FOLLOW)
	entity_set_int(entWeapon, EV_INT_solid, SOLID_NOT)
	entity_set_edict(entWeapon, EV_ENT_aiment, entid)
	entity_set_model(entWeapon, "models/p_m4a1.mdl")
```

You can also change other basic things, such as: 
```
//how set_user_armor() works in the fun module
stock set_armor(player, Float:value)
{
    entity_set_int(player, EV_FL_armorvalue, value)
}
```

  

# FakeMeta
FakeMeta is the next generation of Half-Life scripting. It essentially lets you write MetaMod plugins in Pawn. It is extremely powerful, and for this reason, it won't really be covered here. This is just to tell you what it is capable of. 
  * Engine/DLL Calls 
    * There are two types of functions in the HL namespace - Engine functions and DLL functions (DLL functions are ones the game/mod library must export). Both of these can be called using the FakeMeta module using the dllfunc() and engfunc() natives. The parameters are directly passed on to MetaMod, so be careful! You could easily crash a server doing the wrong thing.
  * Engine/DLL Hooks 
    * As stated above, HL provides Engine and DLL functions. You can also hook/supercede these calls using register_forward. You can supercede these calls using fm_return() and return PLUGIN_HANDLED. Again, make sure you know what you are doing. Malformed hooks will cause crashes.
  * Easy entity manipulation 
    * FakeMeta replaces Engine's entity__() function with a natives called "pev()" and "set_pev()". They are a bit easier to use. For more information see the fakemeta includes.
  * Private Offset Hacking 
    * Private offsets are offsets into a block of memory called "pvPrivateData". The right offsets can often modify game-specific features, such as money in Counter-Strike, or resources in Natural-Selection. However, the wrong offsets can cause game crashes.


