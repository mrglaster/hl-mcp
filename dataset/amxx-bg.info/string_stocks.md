# Functions in string_stocks.inc
Function | Description  
---|---  
[is_str_num](https://amxx-bg.info/api/string_stocks/is_str_num) | ```
Returns whether a given string contains only digits.
This returns false for zero-length strings.
```
  
[char_to_upper](https://amxx-bg.info/api/string_stocks/char_to_upper) | ```
Returns an uppercase character to a lowercase character.
```
  
[char_to_lower](https://amxx-bg.info/api/string_stocks/char_to_lower) | ```
Returns a lowercase character to an uppercase character.
```
  
[strbreak](https://amxx-bg.info/api/string_stocks/strbreak) | ```
Backwards compatibility stock - use argbreak or argparse.
```
  
[argbreak](https://amxx-bg.info/api/string_stocks/argbreak) | ```
Emulates strbreak() using argparse().
```
  
[split](https://amxx-bg.info/api/string_stocks/split) | ```
It is basically strbreak but you have a delimiter that is more than one character in length. By Suicid3.
```
  
[remove_filepath](https://amxx-bg.info/api/string_stocks/remove_filepath) | ```
Removes a path from szFilePath leaving the name of the file in szFile for a pMax length.
```
  
[replace_all](https://amxx-bg.info/api/string_stocks/replace_all) | ```
Replaces a contained string iteratively.
```
  
[explode_string](https://amxx-bg.info/api/string_stocks/explode_string) | ```
Breaks a string into pieces and stores each piece into an array of buffers.
```
  
[implode_strings](https://amxx-bg.info/api/string_stocks/implode_strings) | ```
Joins an array of strings into one string, with a "join" string inserted in
between each given string.  This function complements ExplodeString.
```
  

This code is a part of string_stocks.inc. To use this code you should include string_stocks.inc as ```#include <string_stocks>```


  
  

