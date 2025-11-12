# Optimizing Plugins (AMX Mod X Scripting)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#mw-head), [search](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#p-search)
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/Ru:Optimizing_Plugins_\(AMX_Mod_X_Scripting\) "Ru:Optimizing Plugins \(AMX Mod X Scripting\)") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/index.php?title=Zh_cn:Optimizing_Plugins_\(AMX_Mod_X_Scripting\)&action=edit&redlink=1 "Zh cn:Optimizing Plugins \(AMX Mod X Scripting\) \(page does not exist\)") |   
## Contents
[hide] 
  * [1 Introduction](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Introduction)
    * [1.1 Terms](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Terms)
  * [2 Compiler Optimizations](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Compiler_Optimizations)
    * [2.1 Always Save Results](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Always_Save_Results)
    * [2.2 Switch instead of If](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Switch_instead_of_If)
    * [2.3 Don't Re-index Arrays](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Don.27t_Re-index_Arrays)
    * [2.4 Global vs Local and Variables in Loops](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Global_vs_Local_and_Variables_in_Loops)
    * [2.5 Static vs Global](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Static_vs_Global)
    * [2.6 Constant variables](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Constant_variables)
    * [2.7 For Loop Comparisons](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#For_Loop_Comparisons)
  * [3 Tips and Tricks](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Tips_and_Tricks)
    * [3.1 Lookup Tables](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Lookup_Tables)
    * [3.2 Perfect Hashing](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Perfect_Hashing)
    * [3.3 Local Strings](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Local_Strings)
  * [4 Faster Natives](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Faster_Natives)
    * [4.1 Cvar Pointers](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#Cvar_Pointers)
    * [4.2 FormatEX](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#FormatEX)
    * [4.3 File Writing](https://wiki.alliedmods.net/Optimizing_Plugins_\(AMX_Mod_X_Scripting\)#File_Writing)


## Introduction
[Admin-Mod](https://wiki.alliedmods.net/Admin-Mod "Admin-Mod") and [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X") became very popular because of their easy to use scripting language. However, the words "scripting language" come with a lot of loaded preconceptions. Most people assume that because it's scripted: 
  * You can't possibly make it any faster
  * It's pre-compiled, so it's already quite fast
  * Details don't matter, as it's only "scripting" anyway


Especially, with [Pawn](https://wiki.alliedmods.net/Pawn "Pawn") (formerly Small), none of these are true. The compiler, in fact, is very poor at optimizing, and you can **greatly** increase the speed and efficiency of your plugins by keeping a few rules in mind. Remember - it's more important to minimize instructions than it is to minimize lines of code. 
### Terms
To read this document, you will need to understand a few concepts beforehand: 
  * `BRANCHING` - When the processor takes a different path of code. For example, to call a function or to use an if statement, the processor will "branch". Modern processors attempt to predict pathways with "branch prediction", but it's best to avoid branching a lot if possible.
  * `STACK ALLOCATION` - In Pawn, all local data is stored on the stack, a big chunk of continuous memory. Whenever you create a variable on the stack, it is automatically written with zeroes.
  * `HEAP ALLOCATION` - In Pawn, temporary data that needs to be referenced by a native is stored on the heap, another area of contiguous, but less restrictive memory.
  * `DATA SECTION` - This is an area of memory built into your .amxx file. In fact, it "becomes" the heap at load time. All your strings and arrays are hardcoded into this area.
  * `EXPENSIVENESS` - To be "expensive" in computer science means an operation requires a lot of CPU processing. It usually does not refer to memory size, only to processing cycles and time. Addition is inexpensive, floating power operations are expensive. However, both are inexpensive in comparison to writing a file. An inexpensive operation can also be called "cheap".
  * `BIG-OH NOTATION` - O(*) notation refers to the expensiveness of an algorithm. If something is O(n), it occurs in linear time -- meaning that for N items, it will complete relative to N. O(N^2) means with N items, it will complete relative to N^2. O(1) means "constant time" - no matter what N is, it will run in the same amount of time.


## Compiler Optimizations
These optimizations have to do with changing how your code is compiled. While the syntax may remain the same, you are not only increasing compile time, but increasing your plugin's efficiency and speed at run time. 
### Always Save Results
Observe the example code snippet below: 
```
if (get_user_team(player) == TEAM_T)
{
    //...code
} else if (get_user_team(player) == TEAM_CT) {
    //...code
} else if (get_user_team(player) == TEAM_SPECTATOR) {
    //...code
}
```

This is a mild example of "cache your results". When the compiler generates assembly for this code, it will (in pseudo code) generate: 
```
  CALL get_user_team
  COMPARE+BRANCH
  CALL get_user_team
  COMPARE+BRANCH
  CALL get_user_team
  COMPARE+BRANCH

```

Notice the problem? We have called `get_user_team` an extra two times than necessary. The result doesn't change, so we can save it. Observe: 
```
new team = get_user_team(player)
if (team == TEAM_T)
{
    //...code
} else if (team == TEAM_CT) {
    //...code
} else if (team == TEAM_SPECTATOR) {
    //...code
}
```

Now, the compiler will only generate this: 
```
  CALL get_user_team
  COMPARE+BRANCH
  COMPARE+BRANCH
  COMPARE+BRANCH

```

If `get_user_team` were an expensive operation (it's relatively cheap), we would have recalculated the entire result each branch of the `if` case. 
### Switch instead of If
If you can, you should use `switch` cases instead of `if`. This is because for an if statement, the compiler must branch to each consecutive `if` case. Using the example from above, observe the switch version: 
```
new team = get_user_team(player)
switch (team)
{
  case TEAM_T:
     //code...
  case TEAM_CT:
     //code...
  case TEAM_SPECTATOR:
     //code...
}
```

This will generate what's called a "case table". Rather than worm through displaced `if` tests, the compiler generates a table of possible values, which the virtual machine knows to browse through: 
```
  CALL get_user_team
  COMPARE
  COMPARE
  COMPARE

```

  

### Don't Re-index Arrays
A common practice in Small is to "save space" by re-indexing arrays. There are a few myths behind this, such as saving memory, assuming the compiler does it for you, or readability. Fact: none of these are true. Observe the code below: 
```
new players[32], num, team
get_players(players, num, "h")
for (new i=0; i<num; i++)
{
   team = get_user_team(players[i])
   set_user_frags(players[i], 0)
}
```

For this, the compiler generates code similar to: 
```
:LOOP_BEGIN
   LOAD i
   LOAD players
   CALC
   LOAD players[i]
   CALL get_user_team
   LOAD i
   LOAD players
   CALC
   LOAD players[i]
   CALL set_user_frags

```

See what happened? The compiler does not cache array indexing. Because we've used `players[i]` each time, every instance generates 4-6 (or more) instructions which load `i`, the address of `players`, computes the final location, and then grabs the data out of memory. It is much faster to do: 
```
new player
for (new i=0; i<num; i++)
{
   player = players[i]
   team = get_user_team(player)
   set_user_frags(player, 0)
}
```

Not only is this more readable, but look at how much cruft we've shaved off the compiler's generated code: 
```
:LOOP_BEGIN
   LOAD i
   LOAD players
   CALC
   LOAD players[i]
   STORE player
   CALL get_user_team
   LOAD player
   CALL set_user_frags

```

In a large loop you can drastically reduce codesize in this manner. 
### Global vs Local and Variables in Loops
It is important to realize that every variable in [Pawn](https://wiki.alliedmods.net/Pawn "Pawn") is automatically zeroed. For global variables, they are static and permanent, thus they are zeroed when your plugin is loaded. Variables in functions, however, must be zeroed dynamically. This is a slow and tedious operation, and you should not only avoid relying on it when necessary, but you should keep that fact in mind when using arrays. 
[Arrays](https://wiki.alliedmods.net/index.php?title=Arrays&action=edit&redlink=1 "Arrays \(page does not exist\)") in [Pawn](https://wiki.alliedmods.net/Pawn "Pawn") are "cells" of data. Each cell is four or eight bytes, depending on whether your processor is 32bit or 64bit. To create an array of 4096 cells, for example: 
```
new array[4096]
```

The compiler generates code to manually zero every single one of the 16,384 bytes in that location. Normally, this isn't too bad -- but it can be absolutely deadly in a function which is called quite often. For example, `server_frame` is called on every [server tick](https://wiki.alliedmods.net/index.php?title=Server_tick&action=edit&redlink=1 "Server tick \(page does not exist\)") in [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X"). To declare an array of that size in `server_frame` is highly unnecessary. Instead, you can take advantage of the fact that not only are globals free of charge, but `server_frame` does not need to be re-entrant. That is, you will never call `server_frame` inside of `server_frame`, so making the variable global will not bring up the problem of one instance of the function overwriting data from another instance of the same function. Observe: 
```
new g_serverframe_array[4096]
public server_frame()
{
  //...code that uses g_serverframe_array
}
```

This will execute conseridably faster. You can do this with smaller arrays too. 
Likewise, it is equally important to avoid declaring arrays inside of loops. Consider the following block of code: 
```
for (new i=0; i<num; i++)
{
   new message[255], name[32], player
   player = players[i]
   get_user_name(player, name, 31)
   format(message, 254, "Hello, %s", name)
}
```

If there are 32 players, this loop will actually resize and zero out over 1K of memory thirty two times in a row. Not good! However, on the other hand, it's nice that the message is zeroed out for us each time. `Tip:` you often only need to zero out the first character of a string. This will make the entire string empty. The code below is much more efficient: 
```
new message[255], name[32], player
for (new i=0; i<num; i++)
{
   player = players[i]
   name[0] = '^0'
   message[0] = '^0'
   get_user_name(player, name, 31)
   format(message, 254, "Hello, %s", name)
}
```

This has the effect of safely making the string empty beforehand, as well as largely reducing a lot of run-time overhead. 
### Static vs Global
An alternative to global variables is static variables, which are internally the same but easier to work with for programming. 
A variable declared with the keyword "static" instead of "new" operates in the same way a global does (it is created only once) but the variable is local to the function; this means the code is much easier to read, while drastically improving speed just like a global variable. Example: 
```
stock SomeBigFunction()
{
   static gaben[255];
   format(gaben, "%L", LANG_SERVER, "STUFF");
}
```

This has the same effect as declaring `gaben` as global, except only `SomeBigFunction` can use it. 
`**Note:** Be careful of re-entrancy!`When a variable is static, it has the same re-entrancy problems of a global variable. That means, if your function might be called recursively, or twice in the same stack frame, you should not use static variables. This is most often the case for API provided to other plugins or helper functions. Triggered events are usually never called twice on the same execution chain.
### Constant variables
You can declare a variable "constant" by adding the "const" keyword before the variable name: 
```
new const AMX_GABEN[] = "amx_gaben"
```

What this does is prevents the variable from being changed; essentially, you've locked the variable to a certain value. In this way, a constant can offer a type safe method of simplifying code, unlike a define, which is not type safe. 
In addition, constant variables are often optimized out, resulting in quicker and smaller code. 
### For Loop Comparisons
A common mistake is to write code like this: 
```
new string[256] = "something long"
for (new i=0; i<strlen(string); i++)
   //...code
```

This plays off a similar principle from before: cache results. The compiler will actually recompute your string length on each iteration of the loop. This will have even worse effects if your string changes mid-loop. A more sensible method is: 
```
new string[256] = "something long"
new len = strlen(string)
for (new i=0; i<len; i++)
   //...code
```

  

## Tips and Tricks
### Lookup Tables
Precompute what can be precomputed. For example, say you have a mapping of weapon indices to names: 
```
if (weapon == CSW_AK47)
   copy(name, len, "weapon_ak47")
```

Ignoring the fact that we have `get_weapon_name` in [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X"), this is inefficient. We could precompute this result in a table: 
```
new g_WeaponNamesTable[TOTAL_WEAPONS][] = {
   //..0 to CSW_AK47-1
   "weapon_ak47",
   //..CSW_AK47+1 to TOTAL_WEAPONS-1
};
```

### Perfect Hashing     TODO: explain this
  

### Local Strings
The [Pawn](https://wiki.alliedmods.net/Pawn "Pawn") compiler does not optimize the DATA section, which stores all hardcoded strings and global arrays. If you reference the same hardcoded string 500 times in your plugin, it will appear 500 different times. If this seems bad enough, it actually does this with all strings. For example, the empty string ("") appears everywhere in the include files, usually used as a default parameter to many natives. This too is copied into the data section for each unique reference. 
For example: 
```
set_cvar_num("amx_gaben", get_cvar_num("amx_gaben") + 1)
```

This will create two copies of "amx_gaben" in the DATA section. While this doesn't really hurt, it does increase the size of your plugin. 
Similarly, this has the same problem: 
```
#define AMX_GABEN "amx_gaben"
set_cvar_num(AMX_GABEN, get_cvar_num(AMX_GABEN) + 1)
```

The only way to avoid this mess is to use global variables. As stated earlier, they're basically free storage. 
```
new AMX_GABEN[] = "amx_gaben"
set_cvar_num(AMX_GABEN, get_cvar_num(AMX_GABEN) + 1)
```

Again, while not necessary, this will reduce your plugin's size in memory and on disk. If you're already using defines, you can make this switch easily. 
In order to prevent this from changing, you may want to declare it constant: 
```
new const AMX_GABEN[] = "amx_gaben"
set_cvar_num(AMX_GABEN, get_cvar_num(AMX_GABEN) + 1)
```

Now it is a perfectly safe method of storage. 
## Faster Natives
AMX Mod X replaces many of the old AMX Mod natives with faster versions. Read below to discover them. 
### Cvar Pointers
As of AMX Mod X 1.70, you can cache "cvar pointers". These are direct accesses to cvars, rather than named access. This is a critical optimization which is dozens of times faster. For example: 
```
new g_enabled = register_cvar("csdm_enabled", "1")
//OR
new g_enabled = get_cvar_pointer("csdm_enabled")
 
stock SetCSDM(num)
   set_pcvar_num(g_enabled, num)
 
stock GetCSDM()
   return get_pcvar_num(g_enabled)
```

All of the cvar* functions (except for set_cvar_string) are mapped to [get|set]_pcvar_*. You can get a cached cvar pointer with get_cvar_pointer() or register_cvar(). 
### FormatEX
As of AMX Mod X 1.70, there is an ultra high-speed version of format() called formatex(). It skips copy-back checking, unlike format(). formatex() cannot be used if a source input is the same as the output buffer. For example, these are invalid: 
```
new buffer[255]
formatex(buffer, charsmax(buffer), "%s", buffer);
formatex(buffer, charsmax(buffer), buffer);
formatex(buffer, charsmax(buffer), "%d %s", buffer[2]);
```

It should be noted that format() will behave the same as formatex() if it detects that there will be no copy-back needed. However, formatex() does not check this, and thus is slightly faster for situations where the coder is sure of its usage. 
### File Writing
As of AMX Mod X 1.70, there are new natives for file writing. Read_file and write_file are O(n^2) functions for consecutive read/writes. fopen(), fgets(), fputs(), and fclose() are O(n) (or better) depending on how you use them. 
