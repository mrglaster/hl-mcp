bi_field
[SQL](http://127.0.0.1:8000/content/index.htm) (dbi.inc) 
Description
dbi_field - Returns a field from an SQL result row. 
Syntax
dbi_field ( Result:result, fieldnum, [ ... ] ) 
Type
Native 
Notes
Returns 0 on failure. Although internally fields always start from 0, this function takes fieldnum starting from 1.   
  
Examples of how to get SQL rows:   
` ret = dbi_query(sql, query)   
new Float:fResult   
new string[32]   
new iResult   
   
dbi_nextrow(ret)   
   
iResult = dbi_field(ret, 1)   
dbi_field(ret, 2, fResult)   
dbi_field(ret, 3, string, 31)  `
