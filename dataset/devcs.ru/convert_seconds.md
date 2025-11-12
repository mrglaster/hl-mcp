# Конвертация секунд (get_systime()) в дни\часы\минуты:

```
stock seconds_to_time(iSec, &iDays, &iHours, &iMinutes)

{
    iDays = iSec / 60 / 60 / 24;
    iHours = (iSec / 60 / 60) % 24;
    iMinutes = (iSec / 60) % 60;
}
```
