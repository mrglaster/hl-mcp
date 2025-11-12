# Functions in timer_controller.inc
Function | Description  
---|---  
[RoundTimerPause](https://amxx-bg.info/api/timer_controller/RoundTimerPause) | ```
@brief Pauses / Unpauses the round timer.

@note  The countdown timer will be paused and will also put any time objective 
   check on hold.

@noreturn
```
  
[IsRoundTimerPaused](https://amxx-bg.info/api/timer_controller/IsRoundTimerPaused) | ```
@brief Returns whether the round timer is paused or not.

@return type  boolean
```
  
[RoundTimerSet](https://amxx-bg.info/api/timer_controller/RoundTimerSet) | ```
@brief Sets the round timer to the given time.

@param int    Minutes 
@param int    Seconds

@noreturn
```
  
[RoundTimerGet](https://amxx-bg.info/api/timer_controller/RoundTimerGet) | ```
@brief Returns round timer in seconds.

@return time
```
  

This code is a part of timer_controller.inc. To use this code you should include timer_controller.inc as ```#include <timer_controller>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.