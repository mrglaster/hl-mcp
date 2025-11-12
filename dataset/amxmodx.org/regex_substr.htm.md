egex_substr
[Regex](http://127.0.0.1:8000/content/index.htm) (regex.inc) 
Description
regex_substr - Retrieves a matched substring 
Syntax
regex_substr ( Regex:id, str_id, buffer[], maxLen ) 
Type
Native 
Notes
Returns a matched substring from a regex handle. Substring ids start at 0 and end at Num-1, where Num is the return value from the third parameter of [regex_match](http://127.0.0.1:8000/content/regex_match.htm).
