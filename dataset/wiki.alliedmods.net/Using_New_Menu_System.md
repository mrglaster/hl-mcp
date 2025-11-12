# Using New Menu System
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Using_New_Menu_System#mw-head), [search](https://wiki.alliedmods.net/Using_New_Menu_System#p-search)
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/Ru:Using_New_Menu_System "Ru:Using New Menu System") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/index.php?title=Zh_cn:Using_New_Menu_System&action=edit&redlink=1 "Zh cn:Using New Menu System \(page does not exist\)") |   
  

## Contents
  * [1 Introduction](https://wiki.alliedmods.net/Using_New_Menu_System#Introduction)
    * [1.1 Beginners Menu Tutorial](https://wiki.alliedmods.net/Using_New_Menu_System#Beginners_Menu_Tutorial)
      * [1.1.1 Includes](https://wiki.alliedmods.net/Using_New_Menu_System#Includes)
      * [1.1.2 Global Variables](https://wiki.alliedmods.net/Using_New_Menu_System#Global_Variables)
      * [1.1.3 Registering Plugin and Menu](https://wiki.alliedmods.net/Using_New_Menu_System#Registering_Plugin_and_Menu)
      * [1.1.4 Constructing Menu](https://wiki.alliedmods.net/Using_New_Menu_System#Constructing_Menu)
      * [1.1.5 Displaying the Vote Menu](https://wiki.alliedmods.net/Using_New_Menu_System#Displaying_the_Vote_Menu)
      * [1.1.6 Handling Menu Choices](https://wiki.alliedmods.net/Using_New_Menu_System#Handling_Menu_Choices)
      * [1.1.7 Fenito](https://wiki.alliedmods.net/Using_New_Menu_System#Fenito)


# Introduction
Write some intro here 
## Beginners Menu Tutorial
Now lets discuss how to use the new menu system. We will go through the basics in this tutorial and make a simple Change Level vote. 
### Includes
As always we will start out by adding the required includes 
```
#include <amxmodx>
```

### Global Variables
```
new g_Menu;	// Main Menu handler
new g_Votes[3];	// Store Yes votes at 1, No at 2
new g_maxplayers; // Store maxplayers
```

In here we created 2 global var's. One to hold our menu handle, and the other to store our menu votes. The 'Yes' votes will be stored in g_Votes[1] and the 'No' votes will be stored in g_Votes[2]. 
### Registering Plugin and Menu
```
public plugin_init()
{
	// Register Our Plugin
	register_plugin("Vote Menu","1.0","Freecode");
 
        // Cache maxplayers so we don't have to loop 32 times
        g_maxplayers = get_maxplayers()
 
	// Register our Change Level vote menu
	g_Menu = menu_create("Change Level?","menu_handle");
 
	register_clcmd("amx_startvote","startvote",ADMIN_CFG,"Gaben");
 
	// Now we need to build our menu
	build_menu();
}
```

Lets break this down. 
  * Registers our plugin

```
register_plugin("Vote Menu","1.0","Freecode");
```

  * g_Menu - Our menu handle. It will be set after menu_create gets called.

```
g_Menu = menu_create("Change Level?","menu_handle");
 
//menu_create ( title[], handler[], ml=0 )
//title[] - Menu title
//handler[] - This is a function which will get called once someone presses a key on your menu.
```

  * We made this client command so we can start our vote.

```
register_clcmd("amx_startvote","startvote",ADMIN_CFG,"Gaben");
```

  * This is a function call. build_menu() function will construct our vote menu.

```
build_menu();
```

### Constructing Menu
Constructing the menu is just adding needed items to your menu. Before we go ahead with adding items we must look at menu_additem native. 
```
menu_additem ( menu, const name[], const command[], paccess=0, callback=-1 )
```

  * menu - menu handle. This tells menu_additem the menu to which we are adding our item.
  * const name[] - the item name. This is what gets displayed into the menu.
  * const command[] - item info.


Now lets get into constructing our menu. As said, this is a simple vote for a Change of Level. So we will only need 2 items. A "Yes" and a "No". 
```
build_menu()
{
	menu_additem(g_Menu, "Yes", "1");
	menu_additem(g_Menu, "No", "2");
 
	menu_setprop(g_Menu, MPROP_PERPAGE, 0);
}
```

  * `Notes`
    * As you can see i set the const command[] to numbers. This is for us to identify the item easier.
    * I have also added menu_setprop. This sets our menu to have no pages. For additional properties look into newmenus.inc


### Displaying the Vote Menu
To display our menu we must simply use menu_display. 
```
menu_display ( id, menu, page )
```

  * id - id of the user your displaying menu to.
  * menu - which menu are you showing the user.
  * page - what page (of the menu) to start on. Page of the menu starts at 0.


Ok lets proceed to our code. 
```
public startvote(id)
{
	for(new i = 1; i <= g_maxplayers; i++)
	{
		if( is_user_alive(i) )
		{
			menu_display(i, g_Menu, 0);
		}
	}
 
	return PLUGIN_HANDLED;
}
```

  * `Notes:`
    * The for loop is used to cycle through players and display the menu to players that are alive. We are looping from 1 to Max Players. Note that if you don't use the get_maxplayers() native and server slot is lower than the one you specified it will throw an error.


### Handling Menu Choices
Last step is actualy handling the menu choices. This happens through the menu handler function. It will get called once someone chooses an item off the menu. There are **3** variables that are passed to the function. 
  * id - the users id
  * menu - the menu user had open
  * item - and the item user chose


Now there are a few of special items like the Exit item. 
```
#define MENU_EXIT	-3
#define	MENU_BACK	-2
#define MENU_MORE	-1
```

So we must check at first if the item chosen was not one of the special ones. Note that the only special item that may cause your handler to be called is MENU_EXIT, because MENU_BACK and MENU_MORE items are entirely handled in AMXX core (you can't hook them). 
```
if( item < 0 ) return PLUGIN_CONTINUE;
```

Next we must retrieve the item information. What we are looking for is the number we gave the item (Yes = 1, No = 2). And to do this we use menu_item_getinfo. 
```
menu_item_getinfo ( menu, item, &access, command[], cmdlen, name[]="", namelen=0, &callback )
```

  * menu - the menu where the item exists.
  * item - the item itself
  * &access - (edit)
  * command[] - (edit)(this is where we stored our item identification numbers)
  * cmdlen - length of the command[]
  * name[] - items name
  * namelen - length of the name
  * &callback - (edit)


After we get our items info we will convert the command[] to a number (will either be a 1 or 2) and update the g_Votes array with the appropriate vote chosen. Here is our finished handle function: 
```
public menu_handle(id, menu, item)
{
	if( item < 0 ) return PLUGIN_CONTINUE;
 
	// Get item info
	new cmd[3];
	new access, callback;
 
	menu_item_getinfo(menu, item, access, cmd,2,_,_, callback);
 
	new iChoice = str_to_num(cmd);
 
	g_Votes[iChoice]++;
 
	return PLUGIN_HANDLED;
}
```

### Fenito
The end. You have completed the Beginner's Menu Tutorial. Using the new menu system we have more control over the menu. In the next tutorial you will see how powerfull the new menu system is. The use of callbacks and destroying and creating menus. Here is the completed code after the menu. 
```
#include <amxmodx>
 
new g_Menu;	// Main Menu handler
new g_Votes[3];	// Store Yes votes at 1, No at 2
 
public plugin_init()
{
	// Register Our Plugin
	register_plugin("Vote Menu","1.0","Freecode");
 
	// Register our Change Level vote menu
	g_Menu = menu_create("Change Level?","menu_handle");
 
	register_clcmd("amx_startvote","startvote",ADMIN_CFG,"Gaben");
 
	// Now we need to build our menu
	build_menu();
}
 
build_menu()
{
	menu_additem(g_Menu, "Yes", "1");
	menu_additem(g_Menu, "No", "2");
 
	menu_setprop(g_Menu, MPROP_PERPAGE, 0);
}
 
public startvote(id)
{
	for(new i = 1; i <= g_maxplayers; i++)
	{
		if( is_user_alive(i) )
		{
			menu_display(i, g_Menu, 0);
		}
	}
 
	return PLUGIN_HANDLED;
}
 
public menu_handle(id, menu, item)
{
	if( item < 0 ) return PLUGIN_CONTINUE;
 
	// Get item info
	new cmd[3];
	new access, callback;
 
	menu_item_getinfo(menu, item, access, cmd,2,_,_, callback);
 
	new iChoice = str_to_num(cmd);
 
	g_Votes[iChoice]++;
 
	return PLUGIN_HANDLED;
}
```

