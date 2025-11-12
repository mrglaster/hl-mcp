et_user_info
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_info - Gets an info string from a player 
Syntax
get_user_info ( index, const info[], output[], len ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
The result is stored in output for a maximum length of len characters.   
  
Example:   
` new name[32]   
get_user_info(id, "name", name, 31)   
  `   
  
A list that contains some of the information you can retrive:   
get_user_info(index,"cl_updaterate",MyString,8)   
get_user_info(index,"rate",MyString,8)   
get_user_info(index,"name",MyString,8)   
get_user_info(index,"model",MyString,8)   
get_user_info(index,"_vgui_menus",MyString,8);   
get_user_info(index,"team",MyString,8); 
User Contributed Notes
djschwartz at adelphia dot net | Aug-22-04 03:59:08  
---|---  
A good way to look at this **get_user_info(who, command, variable, howmany)** new name[32] - declaring variable name with a buffer of 32 id - This is the id of the client you would like to get the name of.. This could also be a number! "name" - This is basicly in short the command you would like info back on. name - Assigns the clients username to the variable name. _So how do you use this:_ `    
   
public client_connect(id)   
{   
     new name[32]   
     get_user_info(id, "name", name, 31)   
     set_hudmessage(200, 0, 0, 0.05, 0.65, 2, 0.02, 30.0, 0.03, 0.3, 2)   
     show_hudmessage(0, "%s has Entered",name)   
}   
   
   
When the Client connects it will send a hud message "{clan}playername has Entered"   
   
Other uses might be to get a user's rates.  A couple commands for that would be.   
   
   
new rate[32]   
get_user_info(id, "rate", rate, 31)   
      OR   
get_user_info(id, "cl_rate", rate, 31)   
      OR   
get_user_info(id, "cl_cmdrate", rate, 31)   
   
//One more example   
new getfps[32]   
get_user_info(id, "fps_max", getfps, 31)   
   
  ` If I made any typos sorry you guys BillyTheKid   
  

