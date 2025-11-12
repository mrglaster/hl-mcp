# Макросы для работы с битсуммами

```
#define get_bit(%1,%2)        (%1 &    (1 << (%2 & 31)))
#define set_bit(%1,%2)        (%1 |=    (1 << (%2 & 31)))
#define reset_bit(%1,%2)    (%1 &= ~(1 << (%2 & 31)))
#define invert_bit(%1,%2)    (%1 ^=    (1 << (%2 & 31)))
```

Пример использования: 

```
enum { FIRST_BIT, TWO_BIT }
new bitsummData;

...

if(get_bit(bitsummData, FIRST_BIT)){
    ...
}
```
