bi_result
[SQL](http://127.0.0.1:8000/content/index.htm) (dbi.inc) 
Description
dbi_result - Gets a field result by name instead of number. 
Syntax
dbi_result ( Result:result, field[], [ ... ] ) 
Type
Native 
Notes
With one extra parameter, this returns a float by reference. With two extra parameters, this stores into string with length.   
  
Examples of how to get SQL rows:   
` ret = dbi_query(sql, query)   
new Float:fResult   
new string[32]   
new iResult   
   
dbi_nextrow(ret)   
   
iResult = dbi_result(ret, "id")   
dbi_result(ret, "score", fResult)   
dbi_result(ret, "name", string, 31)   
dbi_free_result(ret)  `   

