# dod_get_map_info
#### Syntax
```
native dod_get_map_info( info );
```

#### Description

The function checks if some information is valid for the map. 


```
// Function changes your skin for ITEM_MOLE and Chameleon
public SHARED_ChangeSkin( id, iFlag )
{
    
      // For Day of Defeat
      else if ( g_MOD == GAME_DOD )
      {
         new iModelNum = random_num( 0, 1 );
 
         if ( iTeam == ALLIES )
         {
            add( szSkin, 31, SKIN_AXIS[iModelNum] );
         }
         else
         {
             
            // Then we should use a British model
            if ( dod_get_map_info( MI_ALLIES_TEAM ) == 1 )
            {
               add( szSkin, 31, SKIN_BRIT[0] );
            }
             
            // Otherwise use American model
            else
            {
               add( szSkin, 31, SKIN_ALLIES[iModelNum] );
            }
         }
          
         dod_set_model( id, szSkin );
      }
 
      p_data_b[id][PB_SKINSWITCHED] = true;
   }
 
   return;
}
```


This code is a part of dodx.inc. To use this code you should include dodx.inc as ```#include <dodx>```

Warning: This include is compatible only with Day of Defeat and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).
