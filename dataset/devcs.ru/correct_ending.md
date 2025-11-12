#  Правильное окончание слов после числительных (например 1 час 21 минута):

```
enum _:

{
    Plural,        // минут
    Singular,    // минуты
    Nominative    // минута

};


stock get_numerical_noun_form(iNum)

{
    if (iNum > 10 && ((iNum % 100) / 10) == 1)
        return Plural;                   

    switch (iNum % 10)

    {
        case 1: return Nominative;       
        case 2, 3, 4: return Singular;   
    }
    return Plural;                       

}
```
