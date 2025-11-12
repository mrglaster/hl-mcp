# Module Writing (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#p-search)
AMX Mod X Modules are written in C or C++ (the API is C compatible). 
## Contents
  * [1 Introduction](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Introduction)
  * [2 Necessary Files](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Necessary_Files)
    * [2.1 Metamod](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Metamod)
      * [2.1.1 HL-SDK](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#HL-SDK)
      * [2.1.2 Metamod SDK](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Metamod_SDK)
      * [2.1.3 Amxmodx SDK](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Amxmodx_SDK)
      * [2.1.4 Unix2Dos the Files](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Unix2Dos_the_Files)
  * [3 Setup](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Setup)
  * [4 Compiler GUI](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Compiler_GUI)
    * [4.1 Visual C++ 2005 Express Edition](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Visual_C.2B.2B_2005_Express_Edition)
    * [4.2 Platform SDK](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Platform_SDK)
    * [4.3 .NET SDK](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#.NET_SDK)
  * [5 Message Module ( Demo )](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Message_Module_.28_Demo_.29)
    * [5.1 Editing Module Information](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Editing_Module_Information)
    * [5.2 Exposing Functions](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Exposing_Functions)
      * [5.2.1 Amxmodx](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Amxmodx)
      * [5.2.2 HL API](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#HL_API)
    * [5.3 Developing Module](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Developing_Module)
      * [5.3.1 CPP File](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#CPP_File)
      * [5.3.2 Amxmodx Functions Created](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Amxmodx_Functions_Created)
      * [5.3.3 Metamod HL API Functions Created](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#Metamod_HL_API_Functions_Created)
  * [6 In Conclusion](https://wiki.alliedmods.net/Module_Writing_\(AMX_Mod_X\)#In_Conclusion)


## Introduction
So you want to be a module developer for Amxmodx! Well its not too hard. I will be doing this in Windows as I dont have a Linux box to frick around with at the moment. So, windows only at this point, a Linux version will be forthcoming! 
## Necessary Files
Well first we need to gather up the neccessary files for your computer. The first thing you need to know, its NOT complicated. If you can script in pawn, you can program in C/C++! 
### Metamod
As we all know metamod is the backbone of the whole thing, without this all mods for and HL game would not be possible unless we programmed it ourselves! So many thanks to willday for the development of Metamod, and for BAILOPAN and his crew helping to maintain and update it! Hats off to all! Ok so now onto the file gathering! First thing is first we need to goto Metamod: [metamod.org](http://metamod.org/) from there we need to gather up 2 SDK's. 
#### HL-SDK
The Half Life SDK is the first thing in the list to gather up! We can get this at the same spot that we will be gathering up metamod! So we click on the SDK Link or goto: [Here](http://metamod.sourceforge.net/files/sdk/). From here we need to grab the HLSDK, preferably the one that has been tweeked out for Metamod. So we are looking for this: 
```
hlsdk-2.3-p3.zip                - The Standard SDK v2.3 with various fixes and
                                  updates, that Metamod is compiled against.
                                  Files are in DOS format.

```

So lets grab the [hlsdk-2.3-p3.zip](http://metamod.sourceforge.net/files/sdk/hlsdk-2.3-p3.zip) first! Once this is done you will need to extract this to your Hard Drive. What we will be doing is extracting these files to the following directory, these will be arbitray directories for ease of the document so dont sweat it once you proficient you can move them around :-) Ok so extract the files to the following directory: c:\sdk_files\ 
#### Metamod SDK
Ok, so we have the HL-SDK we now need to Metamod SDK. So we need to go back to the root of Metamod [here](http://metamod.org/) and then click on the v1.xx Sourcecode zip to get the latest SDK from Sourceforge, you can get that file from the best location for you or for a quick link click [metamod-1.xx-win.src.zip](http://prdownloads.sourceforge.net/metamod/metamod-1.19-win.src.zip?download) to get the files. 
#### Amxmodx SDK
Now we need to grab the last of the SDK's so we can go carry on. First we need to goto the Amxmodx Website so that we can get to the SDK via the Downloads area and SVN! [Amxmodx SDK](http://hg.alliedmods.net/amxmodx-central/). 
#### Unix2Dos the Files
So, once you have all the files we need to fix them up a bit. One of the things that will become bothersome later is the Unix File Format that HLSDK / Metamod has, its suppose to be Windows, but its not, so we need to convert the files, soooo...we will use the following tutorial to fix this [GnuWin32](https://wiki.alliedmods.net/index.php?title=GnuWin32&action=edit&redlink=1 "GnuWin32 \(page does not exist\)") Once you have that setup you can use the following to repair all files easily [Repair.bat](http://wiki.dodplugins.net/images/6/61/Repair.rar). 
## Setup
On Windows, a particular directory layout is not required. Instead, environment variables are used. The directions below apply to Windows XP, and are assumed to be similar for other versions of Windows. 
  * Open the Control Panel (for example, via Start -> Settings).
  * Open the System control. If you don't see it, you may need to switch to "Classic view" (either via the left-hand pane or by going to Tools -> Folder Options).
  * Click the Advanced tab.
  * Click the Environment Variables button.


You can add your environment variables to either your User settings or your System settings. Create a new variable for each item in the list below. The item names are in `fixed-width font` and their value descriptions follow. 
  * `METAMOD` - Path to Metamod headers (where metamod.h resides)
  * `HLSDK` - Path to Half-Life SDK


## Compiler GUI
Now that we have all the SDK files we will need to get the Compiler. The one that we will be using will be the Microsoft Visual 2005 Express Edition. 
### Visual C++ 2005 Express Edition
First thing you need to do is grab the web install files: [Visual C++ 2005 Express Edition](http://go.microsoft.com/fwlink/?LinkId=51410&clcid=0x409) if you want to grab the network install you should grab the following: [Network Install Files](http://msdn.microsoft.com/vstudio/express/support/install/), for network install either grab the [Image File](http://go.microsoft.com/fwlink/?linkid=54766) or the [ISO File](http://go.microsoft.com/fwlink/?linkid=57034) your choice. Ok so now your have the iso/img file you need to either burn it or use a Virtual CD/DVD to install it. I wont go into detail on this as its pretty simple, but make sure that you only install the Graphical IDE, if you want to you can install the Microsoft MSDN 2005 Express Edition, these are the help files that you can access by hitting F1 once in the GUI, if you haven't downloaded them, thats fine it will connect you to the Online version of them instead. 
### Platform SDK
The platform SDK is a needed piece of kit, without it we wont be able to compile. You will need to grab it from this site: [Platform SDK Site](http://msdn.microsoft.com/vstudio/express/visualc/usingpsdk/). Specifically you need to grab proper file for your architecture, goto the above page and scroll down to the Files in This Download section. Download the file that you need and install it. Make sure to do a custom install unless you dont mind a bunch of crap on your computer. You want to have only the following items installed: 
```
Microsoft Windows Core SDK
Microsoft Direct Show SDK
Microsoft Media Services SDK

```

### .NET SDK
Next we need to grab the Dot Net install and the Dot Net SDK. You can grab the [dotnet.1.1.exe](http://www.microsoft.com/downloads/info.aspx?na=90&p=&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=262d25e3-f589-4842-8157-034d1e7cf3a3&u=http%3a%2f%2fdownload.microsoft.com%2fdownload%2fa%2fa%2fc%2faac39226-8825-44ce-90e3-bf8203e74006%2fdotnetfx.exe) and install it. Next you will need the .NET SDK, you can grapple [dotnet.1.1.sdk.exe](http://www.microsoft.com/downloads/info.aspx?na=90&p=&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=9B3A2CA6-3647-4070-9F41-A333C6B9181D&u=http%3a%2f%2fdownload.microsoft.com%2fdownload%2f5%2f2%2f0%2f5202f918-306e-426d-9637-d7ee26fbe507%2fsetup.exe) Once these are installed your good to start up the GUI. 
## Message Module ( Demo )
Right, now that we have the base all good and done, we need to get going with the module. First thing we need to do is create a new module, for ease of use I have for the moment made up a demo module called [dod_mm](http://www.dodplugins.net/files/dod_mm.zip), DoD Message Module. Grab this and extract it to the c:\sdk_files directory. 
### Editing Module Information
First things first you need to open up the dod_mm.vcproj this will open up Visual C++. Once its open you will see on the left a dod_mm under the solutions area. Open moduleconfig.h. In here we will look for the following: 
```
#define MODULE_NAME "--ENTER NAME HERE--"
#define MODULE_VERSION "--ENTER VERSION HERE--"
#define MODULE_AUTHOR "--ENTER AUTHOR HERE--"
#define MODULE_URL "--ENTER URL HERE--"
#define MODULE_LOGTAG "--ENTER LOGTAG HERE--"
#define MODULE_LIBRARY "--ENTER LIBRARY HERE--"
#define MODULE_LIBCLASS "" 

```

This is the infor that will be displayed about the module when you have it running on your server. Lets say you type in amxx modules in the command line, you will get information about all the modules running on your server, including this one, once its done. So now we need to edit it to reflect our new module: 
```
#define MODULE_NAME "DoD Message Module"
#define MODULE_VERSION "0.1"
#define MODULE_AUTHOR "DoD Plugins Community"
#define MODULE_URL "http://www.dodplugins.net[](http://www.dodplugins.net)"
#define MODULE_LOGTAG "DoDMM"
#define MODULE_LIBRARY "dod_mm"
#define MODULE_LIBCLASS "" 

```

### Exposing Functions
So now that this is done we need to tell the module to use Metamod Natives, this is done by finding the followin: 
```
// metamod plugin?
// #define USE_METAMOD

```

And changing it to: 
```
// metamod plugin?
#define USE_METAMOD

```

Or in other words uncommenting it. :-) So now that this is done we have access to loads of stuff that metamod has to offer us as well as Amxmodx stuff. Once this is done we now need to expose the functions from metamod that we will be using for this message module. 
#### Amxmodx
If you scroll down you will find the following two functions from amxmodx that we will be using: 
```
/** AMXX attach
 * Do native functions init here (MF_AddNatives)
 */
// #define FN_AMXX_ATTACH OnAmxxAttach

/** AMXX Detach (unload) */
// #define FN_AMXX_DETACH OnAmxxDetach

```

We will expose these by uncommenting them. Later on in this document I will explain where the function itself goes and what goes in them. 
#### HL API
Next we will expose some of the functions that come from the HL Server Engine that Metamod has exposed for us. The functions that we are exposing are ones that we will need specific to messages: 
```
#define FN_MessageBegin_Post					MessageBegin_Post
#define FN_MessageEnd_Post					MessageEnd_Post
#define FN_WriteByte_Post					WriteByte_Post
#define FN_WriteChar_Post					WriteChar_Post
#define FN_WriteShort_Post					WriteShort_Post
#define FN_WriteLong_Post					WriteLong_Post
#define FN_WriteAngle_Post					WriteAngle_Post
#define FN_WriteCoord_Post					WriteCoord_Post
#define FN_WriteString_Post					WriteString_Post
#define FN_WriteEntity_Post					WriteEntity_Post

```

These are the actual messages that will be caught. Finally we need to catch the registering of those messages we can see in [Meta Game](http://wiki.dodplugins.net/index.php/Meta_Game). This is the function we are going to expose next: 
```
#define FN_RegUserMsg_Post					RegUserMsg_Post

```

Now that all the functions that we will be using have been exposed we are good to carry on with the meat of the module. 
### Developing Module
Right on, now we have the basics down. We are ready to start programming. So we need a main file now. So now we need to right click on the dod_mm and goto Add->New Item as shown in the picture below: 
[![Adding item.jpg](https://wiki.alliedmods.net/images/Adding_item.jpg)](https://wiki.alliedmods.net/File:Adding_item.jpg)
Once thats done a new window comes up, we need to click on code, then Header File (.h) giving it the name main.h 
[![Main header.jpg](https://wiki.alliedmods.net/images/Main_header.jpg)](https://wiki.alliedmods.net/File:Main_header.jpg)
Now we have a file to work with. So, we need to first set it up as a standard Header file so that it is only included once into memory. So we add the following: 
```
#ifndef DOD_MM_H
     #define DOD_MM_H
     // Code will go between here

     // And Here!
#endif

```

So this will ensure that all the code we put between those two comments are only loaded once into the compilation process. Now that we have this part complete we will start coding. As we are making a module to catch all the Messages that occur on a HL DoD Server the first thing we need to do is create a structure to keep all the data that we will use. This structure will be called StructUserMsg and will contain two members the id of the message which can be anything from 0 - 256 messages and the name of the message. We can get these names from [Meta Game](http://wiki.dodplugins.net/index.php/Meta_Game). These will be the messages that will pop up. Now that we have this done the file should look like so: 
```
#ifndef DOD_MM_H
     #define DOD_MM_H
     // Code will go between here

     #include <stdio.h>
     #include "sdk/amxxmodule.h"

     struct StructUserMsg 
     {
           int id;
           char name[256];
     };

     // And Here!
#endif

```

#### CPP File
So now that we have the structure done the first thing we have to do is make a CPP file the same as we did the Header file except with a CPP. We will name this file the same as the Header that we created as this cpp will call the header to get its information. Once we have created the file the first thing we need to do is call the header file by adding this to the top: 
```
#include "main.h"

```

That will ensure to grab our structure so the rest of the program knows what it is. Once this is done we need to create a few global variables to use. The first one we will use is one that will allow us to output to a file all the data that we are gathering: 
```
FILE *stream;

```

Next we need a global state variable so that we know what call we are on within the message. This will count all the calls to each specific message: 
```
int g_state;

```

Now finally we need to create the global variable for the structure we created: 
```
StructUserMsg g_user_msg[MAX_REG_MSGS];

```

#### Amxmodx Functions Created
So this is most important. We created a StructUserMsg array of MAX_REG_MSGS in length, this is 256. Ok we are good now on the globals. Pretty simple. Now remember those functions we exposed, well we need to create those functions so that Amxmodx will call them. First we will look at the Amxmodx functions: 
```
void OnAmxxAttach()
{
     fopen_s(&stream, "messages.txt", "w");
}

void OnAmxxDetach()
{
     fclose(stream);
}

```

So now that these are created lets understand them. When amxmodx starts up and calls the module we are creating the OnAmxxAttach is the first thing that is called, in our case we are opening up a file called messages.txt that will be in the base HL directory. This will contain all the output from our module. 
```
***** NOTE *** This will take up alot of room, so be carefull**

```

Ok, the second function is just the opposite, when amxmodx closes this is the last function called, so we want to close the file. 
#### Metamod HL API Functions Created
Now onward. The Amxmodx functions are complete now we need to create the functions for the Metamod / HL API. First we will create the most important function the registration function, in order to understand the funtions we first need to know what we are looking for. So we exposed the following: 
```
#define FN_RegUserMsg_Post					RegUserMsg_Post

```

Ok so what the hell is this??? Well if you highlight and copy FN_RegUserMsg_Post then open up amxxmodule.h and do a search for **FN_RegUserMsg_Post** you will find the following: 
```
#ifdef FN_RegUserMsg_Post
int FN_RegUserMsg_Post(const char *pszName, int iSize);
#endif // FN_RegUserMsg_Post

```

This is where we get the function declaration from. So we copy the following: 
```
int FN_RegUserMsg_Post(const char *pszName, int iSize);

```

And make a function out of it as such: 
```
int RegUserMsg_Post(const char *pszName, int iSize)
{
     RETURN_META_VALUE(MRES_IGNORED, 0);
}

```

Now this is the start of our function. You notice the RETURN_META_VALUE, this is a metamod return, because the function is returning an int we need to tell metamod to ignore what we have done with this function and return an integer. This is what this means. One of the others we will be returning alot is as follows: 
```
RETURN_META(MRES_IGNORED);

```

This is what we use when a function returns a void or nothing. This function is pretty basic. First thing we are going to do is grab the original return value that we would have gotten if we wanted to do stuff with this function. In this case it is the message id: 
```
int msgid = META_RESULT_ORIG_RET(int);

```

Next we are going to assign the message id to our message structure at the location of the message id...bit confusing but important: 
```
g_user_msg[msgid].id = msgid;

```

Finally we are going to assign the message name to the message structure using a string copy: 
```
strcpy(g_user_msg[msgid].name, pszName);

```

Ok now we have the register function done it will look like so when done: 
```
// First thing when all the messages are sent out to a client we grab them and take a look at them
int RegUserMsg_Post(const char *pszName, int iSize)
{
     int msgid = META_RESULT_ORIG_RET(int);
     g_user_msg[msgid].id = msgid;
     strcpy(g_user_msg[msgid].name, pszName);

     RETURN_META_VALUE(MRES_IGNORED, 0);
}

```

  
Now we need to worry about the next important function, the message begins function. This is called when a message is initialized on the server to be sent out to someone somewhere. It looks like this: 
```
// When a MESSAGE_BEGIN is sent we catch it After it gets to the player
void MessageBegin_Post(int msg_dest, int msg_type, const float *pOrigin, edict_t *player) 
{
     RETURN_META(MRES_IGNORED);
}

```

Voila...now this is very important part because this is where and when the message begins...remember we can **NEVER** call another message_begin while we are in a message...so we have to wait until after when we hit message_end. Now we are going to add some stuff to this to make it work. First we want to make sure that its not a bogus or bad message: 
```
if(msg_type < 0 || msg_type >= MAX_REG_MSGS)
{
     g_state = -1;
     RETURN_META(MRES_IGNORED); // Bad Message
}

```

If it is we bounce out of this message. If not then its a good message and we want to carry on. Next thing we do is print out that we are in the message beginning to both the console and the file: 
```
// Log the message Name
printf("[Message ID]\t%d\n[Message Name]\t%s\n[Message Dest]\t", g_user_msg[msg_type].id, g_user_msg[msg_type].name);
fprintf(stream, "[Message ID]\t%d\n[Message Name]\t%s\n[Message Dest]\t", g_user_msg[msg_type].id, g_user_msg[msg_type].name);

```

As you can see we are printing out the message id the message name that we stored in our structure earlier. Once this is done we will check the message destination and print that out as well. There are 3 places a message could be going 0 = all, 1 - 32 is Individually to a player, and 33 - MAX_REG_MSGS is all others. So we will tell which it is with the following: 
```
// Is it too all, or to an individual
if(msg_dest == 0)
{
      printf("All\n");
      fprintf(stream, "All\n");
}

else if(msg_dest > 0 && msg_dest < 33)
{
      printf("Individual\n");
      fprintf(stream, "Individual\n");

      if(player)
      {
             int id = ENTINDEX(player);
             const char* name = STRING(player->v.netname);
             const char* auth = (*g_engfuncs.pfnGetPlayerAuthId)(player);
             printf("[Player]\t<%s><%d><%s>\n", name, id, auth);
             fprintf(stream, "[Player]\t<%s><%d><%s>\n", name, id, auth);
      }
}

else
{
      printf("Other\n");
      fprintf(stream, "Other\n");
}

```

Self explanatory, finally we need to set the global variable g_state to zero: 
```
g_state = 0;

```

So this funtion is done. Here is the end result: 
```
// When a MESSAGE_BEGIN is sent we catch it After it gets to the player
void MessageBegin_Post(int msg_dest, int msg_type, const float *pOrigin, edict_t *player) 
{
     if(msg_type < 0 || msg_type >= MAX_REG_MSGS)
     {
           g_state = -1;
           RETURN_META(MRES_IGNORED); // Bad Message
     }

     // Log the message Name
     printf("[Message ID]\t%d\n[Message Name]\t%s\n[Message Dest]\t", g_user_msg[msg_type].id, g_user_msg[msg_type].name);
     fprintf(stream, "[Message ID]\t%d\n[Message Name]\t%s\n[Message Dest]\t", g_user_msg[msg_type].id, g_user_msg[msg_type].name);

     // Is it too all, or to an individual
     if(msg_dest == 0)
     {
           printf("All\n");
           fprintf(stream, "All\n");
     }

     else if(msg_dest > 0 && msg_dest < 33)
     {
           printf("Individual\n");
           fprintf(stream, "Individual\n");

           if(player)
           {
                 int id = ENTINDEX(player);
                 const char* name = STRING(player->v.netname);
                 const char* auth = (*g_engfuncs.pfnGetPlayerAuthId)(player);
                 printf("[Player]\t<%s><%d><%s>\n", name, id, auth);
                 fprintf(stream, "[Player]\t<%s><%d><%s>\n", name, id, auth);
           }
     }

     else
     {
           printf("Other\n");
           fprintf(stream, "Other\n");
     }

     g_state = 0;

     RETURN_META(MRES_IGNORED);
}

```

Ok from here on out it will be a bit repetitive so I will just show them too you: 
```
void WriteByte_Post(int iValue) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     printf("%d [Byte]\t%d\n", g_state++, iValue);
     fprintf(stream, "%d [Byte]\t%d\n", g_state++, iValue);

     RETURN_META(MRES_IGNORED);
}

void WriteChar_Post(int iValue) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     char buffer[10];
     _itoa_s(iValue, buffer, 10);
     printf("%d [Char]\t%s\n", g_state++, buffer);
     fprintf(stream, "%d [Char]\t%s\n", g_state++, buffer);

     RETURN_META(MRES_IGNORED);
}

void WriteShort_Post(int iValue) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     printf("%d [Short]\t%d\n", g_state++, (short)iValue);
     fprintf(stream, "%d [Short]\t%d\n", g_state++, (short)iValue);

     RETURN_META(MRES_IGNORED);
}

void WriteLong_Post(int iValue) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     printf("%d [Long]\t%d\n", g_state++, (long)iValue);
     fprintf(stream, "%d [Long]\t%d\n", g_state++, (long)iValue);

     RETURN_META(MRES_IGNORED);
}

void WriteAngle_Post(float flValue) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     printf("%d [Angle]\t%d\n", g_state++, (int)flValue);
     fprintf(stream, "%d [Angle]\t%d\n", g_state++, (int)flValue);

     RETURN_META(MRES_IGNORED);
}

void WriteCoord_Post(float flValue) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     printf("%d [Coord]\t%d\n", g_state++, (int)flValue);
     fprintf(stream, "%d [Coord]\t%d\n", g_state++, (int)flValue);

     RETURN_META(MRES_IGNORED);
}

void WriteString_Post(const char *sz) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     printf("%d [String]\t%s\n", g_state++, sz);
     fprintf(stream, "%d [String]\t%s\n", g_state++, sz);

     RETURN_META(MRES_IGNORED);
}

void WriteEntity_Post(int iValue) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     printf("%d [Entity]\t%d\n", g_state++, iValue);
     fprintf(stream, "%d [Entity]\t%d\n", g_state++, iValue);

     RETURN_META(MRES_IGNORED);
}

```

The last but not least function is the message end function. It too is simple to understand: 
```
void MessageEnd_Post(void) 
{
     if(g_state == -1)
           RETURN_META(MRES_IGNORED);

     printf("[End Message]\n\n");
     fprintf(stream, "[End Message]\n\n");

     fflush(stream);

     RETURN_META(MRES_IGNORED);
}

```

The only thing weird about this one is the flush...this just ensures the data we just collected gets sent to the file. Well thats it...we're done...all thats left is the compile and moving the module to the addons/amxmodx/modules/ directory then adding it to the addons/amxmodx/configs/modules.ini file at the bottom. Remember to name it dod_mm not dod_mm_amxx.dll just the first part. 
## In Conclusion
Ok we are setup to start compiling, you can grab the source code to any of the modules at amxmodx and compile them now...or just play about. I suggest you try the easy one that you can grab here: [ESF Model Changing Module](http://forums.alliedmods.net/showthread.php?t=18763) just to look at it. Here is the direct download: [esf_model_changer](http://forums.alliedmods.net/attachment.php?attachmentid=4104&d=1128187905)
The files for this project can be found [DoD Message Module Tutorial / Module](http://www.dodplugins.net/forums/showthread.php?p=2471)
I have made great use of this in helping in developing dodx and dodfun. 
Cheers! Zor 
For more information, look in: [/svn.tcwonline.org/viewvc.cgi/trunk/amxmodx/sdk/?root=amxmodx](http://svn.tcwonline.org/viewvc.cgi/trunk/amxmodx/sdk/?root=amxmodx) or [click here](http://svn.tcwonline.org/viewvc.cgi/trunk/amxmodx/sdk.tar.gz?root=amxmodx&view=tar) to download a tarball of that directory. 
Copy these files into a new folder. The amxxmodule.h/cpp files are the Module SDK backend. You only need to edit the moduleconfig.h file to customize your module. 
