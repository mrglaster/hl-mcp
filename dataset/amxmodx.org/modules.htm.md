. Commands
  

Content:
  * [Installing Modules](http://127.0.0.1:8000/content/modules.htm#install)
  * [Removing Modules](http://127.0.0.1:8000/content/modules.htm#remove)
  * [Default Modules](http://127.0.0.1:8000/content/modules.htm#default)
  * [Troubleshooting](http://127.0.0.1:8000/content/modules.htm#help)

  
**Installing Modules**
  1. Figure out what operating system your server is: Windows, Linux, or Linux using AMD64 (64bit).
  2. Download the module corresponding to your OS, normally modules follow the following naming scheme:  
module_amxx.dll - Windows  
module_amxx_i386.so - Linux  
module_amxx_amd64.so - Linux, AMD64.
  3. Place the file in addons\amxmodx\modules\
  4. Add the module's name to addons\amxmodx\configs\modules.ini. You should use the full file name, although AMX Mod X supports notation like this for multiple server configurations: ```
;auto-detct OS
module_amxx

```

  5. Follow any additional instructions the module author has. Then restart the server.
  6. To see if the module is working, you can type in your server console: ```
amxx modules
```


  
**Removing Modules**
  * Remove or comment the entry from addons\amxmodx\configs\modules.ini (commenting is prepending a semi-colon).
  * Delete any associated files.

  
**Default Modules** Module Name | Purpose  
---|---  
fun_amxx | General functions for changing game values.  
engine_amxx | More advanced functions for getting and setting values in the HL engine.  
fakemeta_amxx | Expert/advanced functions for manipulating, hooking, and calling functions in the HL engine.  
mysql_amxx, pgsql_amxx, mssql_amxx | MySQL (all platforms), PgSQL (all platforms except AMD64), and MS-SQL (Windows only) scripting functions.  
geoip_amxx | Functions for finding countries by IP address.  
array_amxx | Functions for somewhat-dynamic arrays.  
sockets_amxx | Functions for socket (TCP/UDP) control and manipulation.  
regex_amxx | Functions for regular expression support.  
  
**Troubleshooting**   
  
If a module does not load, you are pretty much stuck for options. The most you can do is contact the module author or attempt to modify/compile the source code on your own system.  
  
To troubleshoot why a module might not load on Linux, you can use the supplied "dlsym" or "dlsym64" (for AMD64) program.  
  
Log into your linux server using SSH and use something like: ```
cd  hlds_l/cstrike/addons/amxmodx/scripting
chmod +x dlsym
./dlsym ../modules/module_amxx_i386.so

```
  
If you get a successful load/handle, the module should be loading correctly. To be safest, post on the AMX Mod X forums or contact the module author.
