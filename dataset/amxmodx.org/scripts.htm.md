. Basic AMX Mod X Plugins
Sections:
  * [Overview](http://127.0.0.1:8000/content/scripts.htm#over)
  * [Beginning](http://127.0.0.1:8000/content/scripts.htm#begin)
  * [Building Admin Commands](http://127.0.0.1:8000/content/scripts.htm#cmds)
  * [CVARs](http://127.0.0.1:8000/content/scripts.htm#cvars)
  * [Finding More](http://127.0.0.1:8000/content/scripts.htm#inc)

**1. Overview**   
  
So you want to create a plugin? You should have a good understand of how Pawn works, so make sure Sections 0 and 1 of this manual make perfect sense to you. You should be reading this portion of the document, sitting at a computer, with a text editor and small compiler at hand. Doing this interactively helps learning. You won't be writing plugins like WC3, Matrix Mod, and CSDM right away, but this is meant to give you a kick start to the modding world of AMX Mod X. For a good text editor that is AMX Pawn enabled, try Crimson Editor (it's free as in beer): <http://www.crimsoneditor.com/>   
  
You should get familiar with compiling plugins. Refer to the "Compiling Plugins" section of the AMX Mod X Documentation, as it will not be provided here. You should also be familiar with adding new plugins, so you can test your plugins out.   
  
**2. The structure of an AMX Mod X plugin.**   
  
An AMX Mod X plugin can have four main types of functions. The first is a "public" function. This means it is publically viewable to the AMX Mod X engine. The second is a "native" function, which is declared in a module or the AMX Mod X Core. The third is a regular user function, which is declared without any special attributes. The fourth is a "forward" function, which is called whenever a special event occurs (a forward is also public). An AMX Mod X plugin must begin with a function initializing the plugin:  
  
```
//This makes it so you can use the core AMX Mod X functions
//It "includes" the native definitions from includes\amxmodx.inc
#include <amxmodx>

//Declare three string variables
new PLUGIN[]="AMXX Demo"
new AUTHOR[]="BAILOPAN"
new VERSION[]="1.00"

//This is a public function.  
//It is necessary to initialize your script under AMX Mod X.
//It takes no parameters, and is called right after map load.
public plugin_init()
{
     //This is a function that takes three strings.
     //It registers your function in AMX Mod X, and assigns some basic information.
     register_plugin(PLUGIN, VERSION, AUTHOR)
} 

```
  
Try compiling the script above. It will be very small - as it does nothing so far. However, if you load this script, and type "amxx plugins", you should see the new entry on the list.   
  
**3. Building Admin Commands**   
  
AMX Mod X provides a way to easily add console admin commands. Each command is "registered" as a console command. When you register a command, you must define four properties: The console command that is typed in, the function you are making that interprets the command, the access level required to use it, and a short description of the command.  
  
For this demonstration, let's build a plugin that lets you change the health of players on the server with the command "amx_hp".  
  
We'll need to do two things to start off - first, we need to register the command in the console. As we are binding a command to a public function, we must then make sure that function exists.  
  
```
#include <amxmodx>
#include <amxmisc> //This contains some useful functions
#include <fun>     //This contains the function to change health

new PLUGIN[]="Change Health"
new AUTHOR[]="BAILOPAN"
new VERSION[]="1.00"

public plugin_init()
{
     register_plugin(PLUGIN, VERSION, AUTHOR)
     register_concmd("amx_hp", "cmd_hp", ADMIN_SLAY, "<target> ")
}

public cmd_hp(id, level, cid)
{
     return PLUGIN_HANDLED
}

```
  
The first new function is "register_concmd", which takes four parameters. The first is the command that a player must type into their console. The second is the public function that will handle the command. The third is the access level your command needs. Lastly, you can pass a string that describes how to use your command (for amx_help).   
  
Next, we have created a public function to handle the amx_hp command. Note that we are giving it three parameters. These parameters will hold special data when the command is used - id will hold the player's id who started the command, level will hold the access level of the command (you must do access checking yourself), and cid will hold the command's internal id.  
  
Also, note PLUGIN_HANDLED. There are two main return values you should concern yourself with. PLUGIN_CONTINUE generally means "continue with normal operation", and PLUGIN_HANDLED means "block further operation". The differences are subtle but important. For example, when binding a command, you should never return PLUGIN_CONTINUE. But if you return PLUGIN_HANDLED while binding to the "say" command, it will block the player's text from ever appearing. You must be careful with which you choose in certain situations. However, most things are unaffected (such as tasks, events, and other things you will run into later on).  
  
So, first things first. How do we make sure this user is an admin who has ADMIN_SLAY access? ```
public cmd_hp(id, level, cid)
{
     if (!cmd_access(id, level, cid, 3))
        return PLUGIN_HANDLED
     return PLUGIN_HANDLED
}

```
  
The cmd_access() function will check a command's information (user, access level, and id) and makes sure of two things: that the user has access to it, and that it was given a minimum number of parameters. Here we passed three, because the command will look like this: amx_hp <target> <amount>, and the actual command itself counts as a parameter. If cmd_access fails, we have the command immediately end.  
  
The next portion to solve is: we need to take the two parameters and decode them. The "amount" parameter is easy, as we just convert it from a string to a number. The second parameter will be trickier, as we want to be able to target three different types of people:  
  

  * @CT or @T - CTs or Ts 
  * @ALL - Everyone 
  * <target> - Partial name of a player 

```
public cmd_hp(id, level, cid)
{
     if (!cmd_access(id, level, cid, 3))
        return PLUGIN_HANDLED

     new Arg1[24]
     new Arg2[4]

     //Get the command arguments from the console
     read_argv(1, Arg1, 23)
     read_argv(2, Arg2, 3)

     //Convert the health from a string to a number
     new Health = str_to_num(Arg2)

     //Is the first character the @ symbol?
     if (Arg1[0] == '@')
     {
          new Team = 0
          //Check which team was specified.
          //Note that we start from [1], this is okay
          // it just means the @ isn't included
          if (equali(Arg1[1], "CT"))
          {
               Team = 2
          } else if (equali(Arg1[1], "T")) {
               Team = 1
          }
          new players[32], num
          //This function will fill the players[32] variable
          // with valid player ids.  num will contain the number
          // of players that are valid.
          get_players(players, num)
          new i
          for (i=0; i<num; i++)
          {
               if (!Team)
               {
                    //Set this player's health
                    set_user_health(players[i], Health)
               } else {
                    if (get_user_team(players[i]) == Team)
                    {
                         set_user_health(players[i], Health)
                    }
               }
          }
     } else {
          //finds a player id that matches the partial name given
          //the 1 means that it will not target the player if he
          // has immunity access
          new player = cmd_target(id, Arg1, 1)
          if (!player)
          {
               //this will print a message to the user who tried the command
               //The format for this command is called "format()" style,
               // where the first string formats the message according
               // to any number of following parameters.
               //  %s means a string
               //  %d or %i means an integer
               //  %f means a float
               // so "Hello %s, I am %d years old" will 
               //  require a string and integer to follow
               console_print(id, "Sorry, player %s could not be found or targetted!", Arg1)
               return PLUGIN_HANDLED
          } else {
               set_user_health(player, Health)
          }
     }

     return PLUGIN_HANDLED
}

```
  
So, our final stripped amx_hp plugin will look like:  
  
```
#include <amxmodx>
#include <fun>

new PLUGIN[]="Change Health"
new AUTHOR[]="BAILOPAN"
new VERSION[]="1.00"

public plugin_init()
{
     register_plugin(PLUGIN, VERSION, AUTHOR)
     register_concmd("amx_hp", "cmd_hp", ADMIN_SLAY, "<target> <hp>")
}

public cmd_hp(id, level, cid)
{
     if (!cmd_access(id, level, cid, 3))
        return PLUGIN_HANDLED

     new Arg1[24]
     new Arg2[4]

     //Get the command arguments from the console
     read_argv(1, Arg1, 23)
     read_argv(2, Arg2, 3)

     //Convert the health from a string to a number
     new Health = str_to_num(Arg2)

     //Is the first character the @ symbol?
     if (Arg1[0] == '@')
     {
          new Team = 0
          if (equali(Arg1[1], "CT"))
          {
               Team = 2
          } else if (equali(Arg1[1], "T")) {
               Team = 1
          }
          new players[32], num
          get_players(players, num)
          new i
          for (i=0; i<num; i++)
          {
               if (!Team)
               {
                    set_user_health(players[i], Health)
               } else {
                    if (get_user_team(players[i]) == Team)
                    {
                         set_user_health(players[i], Health)
                    }
               }
          }
     } else {
          new player = cmd_target(id, Arg1, 1)
          if (!player)
          {
               console_print(id, "Sorry, player %s could not be found or targetted!", Arg1)
               return PLUGIN_HANDLED
          } else {
               set_user_health(player, Health)
          }
     }

     return PLUGIN_HANDLED
}

```
  
  
**4. CVARs**   
  
CVARs are server-side storage keys. For example, "mp_startmoney" is the Counter-Strike CVAR to hold how much money people get when they join the game. You can make your own CVARs by registering them in plugin_init(). Let's replicate mp_startmoney.  
  
```
#include <amxmodx>

public plugin_init()
{
     register_plugin("CVAR Test", "1.0", "BAILOPAN")
     //set default value to 500
     register_cvar("amx_startmoney", "500")
}

//this occurs when a client is put in game
public client_putinserver(id)
{
     if (get_cvar_num("amx_startmoney") > 0)
     {
          cs_set_user_money(id, get_cvar_num("amx_startmoney"))
     } else {
	    cs_set_user_money(id, get_cvar_num("mp_startmoney"))
     }
}

```
  
(this plugin probably won't work, it's just a demonstration). You can set CVARs as floats, numbers, or strings, and you can modify just about any valid CVAR from the HL engine or mod.  
  
**5. Finding More**   
  
To learn more about scripting for AMX Mod X, you should look through the natives in the function reference or the include files. Include files generally follow two formats. They are named after a module or specific purpose. _const is appended if they contain pre-defined numbers or lists. _stocks is appended if they contain helper or useful wrapping functions. Remember, stocks are only compiled if you use them, so it is safe to include an include file with many stocks.  
  
You can also visit the forums at http://www.amxmodx.org/ and ask questions, or read how other people achieved certain goals to learn and innovate.   
  

