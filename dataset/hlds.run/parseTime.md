# parseTime - сток для получения времени в секундах из строки

```pawn


/**
 * Парсинг строки для получения времени в секундах
 *
 * @param szTime    Строка для парсинга
 *
 * @return          Время в секундах
 */
stock parseTime(const szTime[])
{
    const SecondsInMinute = 60;
    const SecondsInHour = 3600;
    const SecondsInDay = 86400;
    const SecondsInWeek = 604800;
    const SecondsInMonth = 25920000;
    const SecondsInYear = 31536000;

    new k, t, h, bool:check_chars;

    for (new i; szTime[i] != EOS; i++)
    {
        if (isspace(szTime[i]))
        {
            check_chars = true;
            continue;
        }

        switch(szTime[i])
        {
            case '0'..'9':
            {
                if (check_chars)
                {
                    check_chars = false;
                    k += t;
                }

                t = (t * 10) + (szTime[i] - '0');
            }

            case 's', 'S':
            {
                k += t;
                t = 0;
            }

            case 'i','I':
            {
                k += t * SecondsInMinute;
                t = 0;
            }

            case 'h','H':
            {
                k += t * SecondsInHour;
                t = 0;
            }

            case 'd','D':
            {
                k += t * SecondsInDay;
                t = 0;
            }

            case 'w','W':
            {
                k += t * SecondsInWeek;
                t = 0;
            }

            case 'm','M':
            {
                k += t * SecondsInMonth;
                t = 0;
            }

            case 'y','Y':
            {
                k += t * SecondsInYear;
                t = 0;
            }

            default:
            {
                break;
            }
        }
    }

    return k + t;
}

/**
 * Замена для SQL запроса
 *
 * @param szDest   Строка
 * @param iLen     Длина строки
 *
 * @noreturn
 */
stock UTIL_SqlEscapeString(szDest, const iLen)
{
    replace_all(szDest, iLen, "\\", "\\\\");
    replace_all(szDest, iLen, "\0", "\\0");
    replace_all(szDest, iLen, "\n", "\\n");
    replace_all(szDest, iLen, "\r", "\\r");
    replace_all(szDest, iLen, "\x1a", "\Z");
    replace_all(szDest, iLen, "'", "\'");
    replace_all(szDest, iLen, "^"", "\^"");
}


```
