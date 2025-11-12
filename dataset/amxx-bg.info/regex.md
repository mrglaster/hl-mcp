# Functions in regex.inc
Function | Description  
---|---  
[regex_compile](https://amxx-bg.info/api/regex/regex_compile) | ```
Precompile a regular expression.
```
  
[regex_match_c](https://amxx-bg.info/api/regex/regex_match_c) | ```
Matches a string against a pre-compiled regular expression pattern.
```
  
[regex_match](https://amxx-bg.info/api/regex/regex_match) | ```
Matches a string against a regular expression pattern.
```
  
[regex_substr](https://amxx-bg.info/api/regex/regex_substr) | ```
Returns a matched substring from a regex handle.
```
  
[regex_free](https://amxx-bg.info/api/regex/regex_free) | ```
Frees the memory associated with a regex result, and sets the handle to 0.
```
  
[regex_compile_ex](https://amxx-bg.info/api/regex/regex_compile_ex) | ```
Precompile a regular expression.
```
  
[regex_match_all_c](https://amxx-bg.info/api/regex/regex_match_all_c) | ```
Matches a string against a pre-compiled regular expression pattern, matching all
occurrences of the pattern inside the string. This is similar to using the "g" flag
in perl regex.
```
  
[regex_match_all](https://amxx-bg.info/api/regex/regex_match_all) | ```
Matches a string against a regular expression pattern, matching all occurrences of the
pattern inside the string. This is similar to using the "g" flag in perl regex.
```
  
[regex_match_simple](https://amxx-bg.info/api/regex/regex_match_simple) | ```
Matches a string against a regular expression pattern.
```
  
[regex_replace](https://amxx-bg.info/api/regex/regex_replace) | ```
Perform a regular expression search and replace.

An optional parameter, flags, allows you to specify options on how the replacement is performed.
Supported format specifiers for replace parameter:
  $number  : Substitutes the substring matched by group number.
             n must be an integer value designating a valid backreference, greater than 0, and of two digits at most.
  ${name}  : Substitutes the substring matched by the named group name (a maximum of 32 characters).
  $&       : Substitutes a copy of the whole match.
  $`       : Substitutes all the text of the input string before the match.
  $'       : Substitutes all the text of the input string after the match.
  $+       : Substitutes the last group that was captured.
  $_       : Substitutes the entire input string.
  $$       : Substitutes a literal "$".
As note, the character \ can be also used with format specifier, this is same hehavior as $.
```
  

This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

