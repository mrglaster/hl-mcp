# jbshop_const.inc
```
#if defined _jbshop_const_included
    #endinput
#endif

#define _jbshop_const_included

const MAX_COMMANDS_BUFFER_LEN = 128
const MAX_ITEM_NAME_LEN       = 64
const MAX_COMMAND_LEN         = 32

const JBSHOP_INVALID_VALUE    = -1

enum JBShop_PriceTypes
{
	JBSHOP_PT_OBEY_SHOP,
	JBSHOP_PT_MONEY,
	JBSHOP_PT_ALIEN_CELLS
}

enum JBShop_ExpireTypes
{
	JBSHOP_ET_INSTANT,
	JBSHOP_ET_RESPAWN,
	JBSHOP_ET_MANUAL
}

enum JBShop_SortTypes
{
	JBSHOP_ST_DONT_SORT,
	JBSHOP_ST_PRICE_ASC,
	JBSHOP_ST_PRICE_DESC
}

enum JBShop_WhenBuy
{
	JBSHOP_WB_ONLY_ALIVE,
	JBSHOP_WB_ONLY_DEAD,
	JBSHOP_WB_DEAD_ALIVE
}
```


This code is a part of jbshop_const.inc. To use this code you should include jbshop_const.inc as ```#include <jbshop_const>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.