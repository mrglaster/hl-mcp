. Debugging
AMX Mod X features a greatly enhanced plugin debugger over AMX Mod. If your plugin is giving runtime errors, you should enable the debugger by opening amxmodx\configs\plugins.ini and appending " debug" to your plugin's entry, like so:  
  
```
myplugin.amxx debug

```
  
When you get a runtime error, it will show a full trace of the problem:  
  
```
L 09/15/2004 - 17:38:17: [AMXX] Run time error 4 (index out of bounds) on line 46 (file "debug.sma").
L 09/15/2004 - 17:38:17: [AMXX] Debug Trace =>
L 09/15/2004 - 17:38:17: [AMXX]       [0] Line 40, File "debug.sma"
L 09/15/2004 - 17:38:17: [AMXX]       [1] Line 25, File "debug.sma" 

```
This type of error is called an AMX run time error - one that occured directly in the plugin interpreter. From this output, we know that this order of events happened: 
  * Line 25 was called in debug.sma
  * Line 25 jumped to line 40 in debug.sma
  * Line 40 jumped to line 46 in debug.sma, where an error occured

This specific error is one of the three common errors. It means that an array was improperly indexed, for example:  
  
```
new array[5]
new x = 500
array[x] = x

```
  
Will generate this message. Another common message is AMX_ERR_STACKERR, which means your plugin ran out of memory. The fix for this is to increase the default size from 16KB:  
  
```
#pragma dynamic 32768 

```
  
This will increase the memory allocated to 128KB. The dynamic size is measured in cells, which are four bytes each (eight bytes on AMD64). AMX_ERR_STACKLOW and AMX_ERR_HEAPLOW are similar. The most common error by far is AMX_ERR_NATIVE, which means a native function in the AMX Mod X core signaled an error message.  
  
Native errors are usually caused by some error checking failure on the part of the script programmer. For example, supplying an invalid connection id to an SQL function, or trying to modify the data on a player that doesn't exist. These errors will usually give a more helpful error message along with the call trace, as well as the actual name of the native that failed.  
  
For more information on debugging, it is recommended you post on the AMX Mod X forums at [http://www.amxmodx.org](http://www.amxmodx.org/). Often times people will have solved similar problems before and can help you easily.
