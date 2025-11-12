# Получение из строки вида "123 -123 1234" массива с координатами iOrigin[3]

```
get_coords(string[], iOrigin[3], const delimiter[] = " ")

{
    new i;
    new ePos, stPos, rawPoint[32];
    do {
        ePos = strfind(string[stPos],delimiter);
        formatex(rawPoint, ePos, string[stPos]);
        stPos += ePos + 1;
        trim(rawPoint);
        if(rawPoint[0]) {
            iOrigin = str_to_num(rawPoint);
        }
    }

    while(ePos != -1)
}
```
