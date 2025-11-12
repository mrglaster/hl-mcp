# get_tr2
#### Syntax
```
native get_tr2(tr_handle, any:tr_member, any:...);
```

#### Description

Allows to get fraction parameter. Usage example:

```
stock is_wall_between_points(Float: start[3], Float: end[3], ignore_ent) {
    // Create the trace handle! It is best to create it!
    new ptr = create_tr2()

    // The main traceline function!
    // This function ignores GLASS, MISSILE and MONSTERS!
    // Here is an example of how you should combine all the flags!
    engfunc(EngFunc_TraceLine, start, end, IGNORE_GLASS | IGNORE_MONSTERS | IGNORE_MISSILE, ignore_ent, ptr)

    // We are interested in the fraction parameter
    new fraction
    get_tr2(ptr, TR_flFraction, fraction)

    // Free the trace handle (don't forget to do this!)
    free_tr2(ptr)

    // If = 1.0 then it didn't hit anything!
    return (fraction != 1.0)
}
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

