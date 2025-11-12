# Functions in orpheu_advanced.inc
Function | Description  
---|---  
[OrpheuGetBytesAtAddress](https://amxx-bg.info/api/orpheu_advanced/OrpheuGetBytesAtAddress) | ```
Gets the bytes found at an address
```
  
[OrpheuGetFunctionAddress](https://amxx-bg.info/api/orpheu_advanced/OrpheuGetFunctionAddress) | ```
Gets the address in memory of a function given a handler to it
```
  
[OrpheuGetStructFromAddress](https://amxx-bg.info/api/orpheu_advanced/OrpheuGetStructFromAddress) | ```
Gets a handle to a struct given an address in memory
```
  
[OrpheuCreateFunction](https://amxx-bg.info/api/orpheu_advanced/OrpheuCreateFunction) | ```
Gets the handler to a function given its address and the name that you give it in the file where you define the function
```
  
[OrpheuGetFunctionOffset](https://amxx-bg.info/api/orpheu_advanced/OrpheuGetFunctionOffset) | ```
Gets the offset of the adress where the function is located to the base address of its library
```
  
[OrpheuGetLibraryAddress](https://amxx-bg.info/api/orpheu_advanced/OrpheuGetLibraryAddress) | ```
Gets the adress of a library
```
  
[OrpheuGetNextCallAtAddress](https://amxx-bg.info/api/orpheu_advanced/OrpheuGetNextCallAtAddress) | ```
This native should retrieve the address of functions called from an address
 For example by passing the address of the function X, and 1 as n, it should retrieve the address of the first
function called in X. It isn't confirmed to work on every condition and it should be use for experiments only
to help retrieving functions on Windows
```
  

This code is a part of orpheu_advanced.inc. To use this code you should include orpheu_advanced.inc as ```#include <orpheu_advanced>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk. 