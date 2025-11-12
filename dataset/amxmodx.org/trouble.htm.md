. Troubleshooting
  

Questions:
  * [AMX Mod X doesn't load (bad load)](http://127.0.0.1:8000/content/trouble.htm#q1)
  * [A module doesn't load](http://127.0.0.1:8000/content/trouble.htm#q2)
  * [Modules or plugins don't load](http://127.0.0.1:8000/content/trouble.htm#q3)
  * [A plugin doesn't load (badload)](http://127.0.0.1:8000/content/trouble.htm#q4)
  * [How do I add admins?](http://127.0.0.1:8000/content/trouble.htm#q5)
  * [My admin doesn't work!](http://127.0.0.1:8000/content/trouble.htm#q6)
  * [I get "ML_LNOTFOUND"!](http://127.0.0.1:8000/content/trouble.htm#q7)
  * [I get "ML_NOTFOUND"!](http://127.0.0.1:8000/content/trouble.htm#q8)
  * [I get "Run time error 10!"](http://127.0.0.1:8000/content/trouble.htm#q9)
  * [I get "Run time error <x>!"](http://127.0.0.1:8000/content/trouble.htm#q10)

  
  
**Q: AMX Mod X doesn't load (bad load)**   
A: This could be caused by a number of things. On windows, it's almost always caused by the file being named incorrectly, being in the wrong place, or having the \addons\metamod\plugins.ini entry incorrect. On linux, it could be the above or a dependency failure. To see the error, type this at your server console: (make sure logging is on with "log on") ```
meta refresh

```
This will show you where AMX Mod X failed to load. If the file could not be found, make sure all locations above are correct. If you get an error about "_gxx_personality" or "lstdc++", it's possible your binary was compiled incorrectly. Contact the development team. If you get another error, your binary could be corrupt or for the wrong system.   
  
**Q: A module doesn't load**   
A: Read the above information on the AMX Mod X Core binary. Contact the developer of the module for more information.   
  
**Q: Modules or plugins don't load**   
A: Make sure your core.ini is correct - if you used AMX Mod X 0.16 before, it may be pointing toward the old path (addons/amxx).   
  
**Q: A plugin doesn't load (badload)**   
A: This could be caused by a number of things. First, make sure the plugin was downloaded correctly. If the file size is 0KB, the compile failed. If you compiled the plugin and/or used it with AMX Mod X 0.20-TP2, you should recompile it with the new compiler as the file format and compression changed. For other errors, see the Plugin Troubleshooting section.   
  
**Q: How do I add admins?**   
A: Please read the documentation for adding administrators.   
  
**Q: My admin doesn't work!**   
A: This is a loaded question as just about anything could be causing it. For general purposes, it's recommended that you authenticate by SteamID because then there's no need to set a password. Make sure your users.ini looks like this: ```
"STEAM_ID:0:1:1234" "" "abcdefghijklmnopqrstu" "ce"

```
Make sure your Steam ID is set correctly, that the second parameter "" is empty (two quotes), that you aren't using access flags "y" or "z", and that the last parameter is "ce" (c=steamid, e=no password).   
  
**Q: I get "ML_LNOTFOUND"!**   
A: This means that a plugin is attempting to translate a multi-lingual phrase which could not be found in any of the dictionaries. You should check to see what language key it is attempting to translate and ask the plugin author if it's incorrect, or check to make sure you have the latest dictionary files for the plugin.   
  
**Q: I get "ML_NOTFOUND"!**   
A: This means that a plugin is attempting to translate a multi-lingual phrase which was found in the dictionary files, but couldn't be translated to the language selected. You should check to make sure you have the latest dictionary files for the plugin or ask the author (or provide one yourself) with an acceptable translation for the key phrase.   
  
**Q: I get "Run time error 10!"**   
A: This an error that is extremely vague. It usually means a function failed to operate the way it should, or that there is a logic error in a plugin. For example, if a plugin tries to access a MySQL connection that does not exist, you will get a run time error 10. You should contact the plugin author to let him know what's failing.   
  
**Q: I get "Run time error <x>!"**   
A: Most run-time errors are harmless, but they can point out a serious logic error. If they occur once in a while they're probably safe to ignore, but repeated and frequent RTEs on similar lines of code in a plugin usually point to a flaw. You should contact the plugin author about the error.
