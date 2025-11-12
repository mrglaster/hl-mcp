eplace
[Core](http://127.0.0.1:8000/content/index.htm) (string.inc) 
Description
replace - Replaces a contained string 
Syntax
replace ( text[], len, const what[], const with[] ) 
Type
Native 
Notes
Replaces string what inside string text, with given string "with", for a maximum length of len. 
User Contributed Notes
amxmodx at dagy dot sk | Jan-11-05 16:46:14  
---|---  
Sorry but in replace statements in previous post should ofcourse be ">", "&gt;" ) and < to &lt; respectively. This was a mistake.   
  
amxmodx at dagy dot sk | Jan-11-05 16:42:29  
---|---  
```
I've looked for statsx.amxx fix to properly handle html tags in user names for top15 list, but nothing found.
So I decided to fix this myself.
I've modified statsx.sma in function format_top15
to replace special html chars  from < to &lt; and > to &gt;. 
like this:  

    get_stats( i, izStats, izBody, t_sName, MAX_NAME_LENGTH )
    // properly handle html tags in name
    while( contain ( t_sName, "<" ) != -1 )
    	replace( t_sName, MAX_NAME_LENGTH, "<", "<" )
    while( contain ( t_sName, ">" ) != -1 )
    	replace( t_sName, MAX_NAME_LENGTH, ">", ">" )
    iLen += format( sBuffer[iLen], MAX_BUFFER_LENGTH - iLen,
                    "%2d %-22.22s %6d %6d %6d %6d %4d %3.0f%% %3.0f%%^n", i+1, t_sName,
                    izStats[STATS_KILLS], izStats[STATS_DEATHS], izStats[STATS_HITS], 
                    izStats[STATS_SHOTS], izStats[STATS_HS],
                    effec( izStats ), accuracy( izStats ) )

the question is what happened if replace[](http://127.0.0.1:8000/content/funcwiki.php?go=func&id=47) function did not replace character in case of maximal name length ? then this is an endless loop isn't it ?
Can be return value of replace used in any case ?

```
  
  

