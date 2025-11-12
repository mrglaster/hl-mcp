egex_match
[Regex](http://127.0.0.1:8000/content/index.htm) (regex.inc) 
Description
regex_match - Initiates a regular expression match 
Syntax
regex_match ( const string[], const pattern[], &ret, error[], maxLen ) 
Type
Native 
Notes
Return values:   
-2 = Matching error (error code stored in ret)   
-1 = Error in pattern (error message and offset # in error[] and ret)   
0 = No match   
>1 = Id for getting more info (you must call regex_free() later on, or have a memory leak.).   
  
The return value is a Regex tag, so you must declare a variable like this:   
new Regex:re   
  
Note that the third parameter to [regex_match](http://127.0.0.1:8000/content/regex_match.htm) is special. It's either the number of substrings, a match error code, or a pattern error position (depending on the return value).   
  
The return codes above are aliased:   
`   
enum Regex   
{   
	REGEX_MATCH_FAIL = -2,   
	REGEX_PATTERN_FAIL,   
	REGEX_NO_MATCH,   
	REGEX_OK   
};   
`   
  
  

