# Functions in vzbb_mod.inc
Function | Description  
---|---  
[register_zombie_class](https://amxx-bg.info/api/vzbb_mod/register_zombie_class) | ```
Регистрира нов зомби клас
```
  
[register_shop_item](https://amxx-bg.info/api/vzbb_mod/register_shop_item) | ```
Регистрира нов итем в shop менюто
```
  
[get_user_zombie_class](https://amxx-bg.info/api/vzbb_mod/get_user_zombie_class) | ```
Връща индекса на зомби класа на играча. (int)
```
  
[set_user_zombie_class](https://amxx-bg.info/api/vzbb_mod/set_user_zombie_class) | ```
Задава индекса на зомби класа на играча
```
  
[is_user_zombie](https://amxx-bg.info/api/vzbb_mod/is_user_zombie) | ```
Връща съответна стойност, ако играчът е зомби
```
  
[is_user_human](https://amxx-bg.info/api/vzbb_mod/is_user_human) | ```
Връща съответна стойност, ако играчът е човек
```
  
[get_user_credits](https://amxx-bg.info/api/vzbb_mod/get_user_credits) | ```
Връща стойността на кредитите на играч
```
  
[set_user_credits](https://amxx-bg.info/api/vzbb_mod/set_user_credits) | ```
Задава стойността на кредитите на играч
```
  
[get_total_zombie_classes](https://amxx-bg.info/api/vzbb_mod/get_total_zombie_classes) | ```
Връща общия брой зомби класове, заредени в момента
```
  
[get_total_shop_items](https://amxx-bg.info/api/vzbb_mod/get_total_shop_items) | ```
Връща общия брой shop итеми, заредени в момента
```
  
[get_user_can_build_battle](https://amxx-bg.info/api/vzbb_mod/get_user_can_build_battle) | ```
Връща съответна стойност, ако играчът може да строи в бойната фаза
```
  
[set_user_can_build_battle](https://amxx-bg.info/api/vzbb_mod/set_user_can_build_battle) | ```
Задава стойността на играч, за да може да мести блокове и в бойната фаза (действа до стартирането на следващата бойна фаза)
```
  
[get_user_block_ent](https://amxx-bg.info/api/vzbb_mod/get_user_block_ent) | ```
Връща индекс на ентитито на блока, който играчът мести в момента
```
  
[set_user_block_ent](https://amxx-bg.info/api/vzbb_mod/set_user_block_ent) | ```
Задава индекс на ентитито на блока, който играчът мести в момента
```
  
[is_freezetime](https://amxx-bg.info/api/vzbb_mod/is_freezetime) | ```
Връща съответна стойност, ако е freezetime в момента
```
  
[get_build_phase_remaining_time](https://amxx-bg.info/api/vzbb_mod/get_build_phase_remaining_time) | ```
Връща оставащото време на строителната фаза
```
  
[user_can_build](https://amxx-bg.info/api/vzbb_mod/user_can_build) | ```
Връща съответна стойност, ако играчите могат да строят (ако в момента е строителната фаза)
```
  
[set_user_can_build](https://amxx-bg.info/api/vzbb_mod/set_user_can_build) | ```
Задава дали играчите могат да строят (дали в момента е строителна фаза)
```
  
[get_roundmode](https://amxx-bg.info/api/vzbb_mod/get_roundmode) | ```
Връща съответна стойност на режима на игра в момента
```
  
[was_user_zombie](https://amxx-bg.info/api/vzbb_mod/was_user_zombie) | ```
Връща съответна стойност, ако играчът е бил зомби при раждането си
```
  
[set_user_was_zombie](https://amxx-bg.info/api/vzbb_mod/set_user_was_zombie) | ```
Задава стойност дали играчът е бил зомби при раждането си (ако е бил накрая на рунда ще бъде човек, използва се при инфекции)
```
  
[is_user_banned](https://amxx-bg.info/api/vzbb_mod/is_user_banned) | ```
Връща съответна стойност, ако играчът е баннат (местенето на блоковете)
```
  
[get_user_fire_duration](https://amxx-bg.info/api/vzbb_mod/get_user_fire_duration) | ```
Връща стойността на оставащата кръв за взимане при горене
```
  
[set_user_fire_duration](https://amxx-bg.info/api/vzbb_mod/set_user_fire_duration) | ```
Задава стойността на oставащата кръв за взимане при горене
```
  
[is_user_frozen](https://amxx-bg.info/api/vzbb_mod/is_user_frozen) | ```
Връща съответна стойност, ако играчът е заледен
```
  
[is_user_frozen_cool](https://amxx-bg.info/api/vzbb_mod/is_user_frozen_cool) | ```
Връща съответна стойност, ако играчът е заледен (започва да се топи)
```
  
[user_burn](https://amxx-bg.info/api/vzbb_mod/user_burn) | ```
Запалва играч
```
  
[user_freeze](https://amxx-bg.info/api/vzbb_mod/user_freeze) | ```
Заледява играч
```
  
[user_freeze_cool](https://amxx-bg.info/api/vzbb_mod/user_freeze_cool) | ```
Заледява играч (играчът веднага започва да се топи)
```
  
[user_unfreeze](https://amxx-bg.info/api/vzbb_mod/user_unfreeze) | ```
Премахва заледяването на играч
```
  
[user_unfreeze_cool](https://amxx-bg.info/api/vzbb_mod/user_unfreeze_cool) | ```
Премахва топенето на играч
```
  
[user_infect](https://amxx-bg.info/api/vzbb_mod/user_infect) | ```
Инфектира играч
```
  
[user_uninfect](https://amxx-bg.info/api/vzbb_mod/user_uninfect) | ```
Деинфектира играч
```
  
[get_block_fun_type](https://amxx-bg.info/api/vzbb_mod/get_block_fun_type) | ```
Връща забавния тип на блок
```
  
[set_block_fun_type](https://amxx-bg.info/api/vzbb_mod/set_block_fun_type) | ```
Задава забавен тип на блок
```
  
[reset_block_fun_type](https://amxx-bg.info/api/vzbb_mod/reset_block_fun_type) | ```
Премахва забавния тип на блок
```
  
[get_deal_discount](https://amxx-bg.info/api/vzbb_mod/get_deal_discount) | ```
Връща стойността на намалението на "Round Deal" в съответния рунд
```
  
[is_deal_offer](https://amxx-bg.info/api/vzbb_mod/is_deal_offer) | ```
Връща съответна стойност дали итемът е в офертите на "Round Deal" в съответния рунд
```
  
[hide_barrierent](https://amxx-bg.info/api/vzbb_mod/hide_barrierent) | ```
Премахва бариерата (ако има такава)
```
  
[reset_barrierent](https://amxx-bg.info/api/vzbb_mod/reset_barrierent) | ```
Рестартира местоположението на бариерата (ако има такава)
```
  
[set_hud_cache_text](https://amxx-bg.info/api/vzbb_mod/set_hud_cache_text) | ```
Задава текст за HUD-a на играчите, на мястото на HUD-a за режима (използвайте при update_user_hud_data forward-a)
```
  
[set_hud_cache_colors](https://amxx-bg.info/api/vzbb_mod/set_hud_cache_colors) | ```
Задава цвят (в RGB формат) за HUD-a на играчите, на мястото на HUD-a за режима (използвайте при update_user_hud_data forward-a)
```
  
[set_hud_cache_condition](https://amxx-bg.info/api/vzbb_mod/set_hud_cache_condition) | ```
Задава условие за показване на HUD-a на играчите, на мястото на HUD-a за режима (използвайте при update_user_hud_data forward-a)
```
  
[force_user_hud_data](https://amxx-bg.info/api/vzbb_mod/force_user_hud_data) | ```
Извиква фунцкията за показване на HUD-a на играчите
```
  
[force_weapon_menu](https://amxx-bg.info/api/vzbb_mod/force_weapon_menu) | ```
Извиква функцията за менюто за оръжия
```
  
[restore_user_rendering](https://amxx-bg.info/api/vzbb_mod/restore_user_rendering) | ```
Възвръща rendering-а на играча (полезно за премахване на glow и възвръщане на невидимостта на играча)
```
  
[zombie_class_selected](https://amxx-bg.info/api/vzbb_mod/zombie_class_selected) | ```
Извиква се при избиране на зомби клас
```
  
[shop_item_selected](https://amxx-bg.info/api/vzbb_mod/shop_item_selected) | ```
Извиква се при избиране на итем от shop менюто
```
  
[block_pull_push](https://amxx-bg.info/api/vzbb_mod/block_pull_push) | ```
Извиква се при теглене или бутане на блок
```
  
[battle_phase_begin](https://amxx-bg.info/api/vzbb_mod/battle_phase_begin) | ```
Извиква се след започването на бойната фаза
```
  
[battle_phase_begin_admin](https://amxx-bg.info/api/vzbb_mod/battle_phase_begin_admin) | ```
Извиква се след принудителното започване на бойната фаза от админ (с командата /start)
```
  
[nade_throw_pre](https://amxx-bg.info/api/vzbb_mod/nade_throw_pre) | ```
Извиква се преди хвърляне на граната
```
  
[nade_throw_post](https://amxx-bg.info/api/vzbb_mod/nade_throw_post) | ```
Извиква се след хвърляне на граната
```
  
[user_burn_pre](https://amxx-bg.info/api/vzbb_mod/user_burn_pre) | ```
Извиква се преди всяко взимане на кръв при запалване на играч
```
  
[user_burn_post](https://amxx-bg.info/api/vzbb_mod/user_burn_post) | ```
Извиква се след всяко взимане на кръв при запалване на играч
```
  
[user_remove_burn](https://amxx-bg.info/api/vzbb_mod/user_remove_burn) | ```
Извиква се при премахването на горенето на играч
```
  
[user_freeze_pre](https://amxx-bg.info/api/vzbb_mod/user_freeze_pre) | ```
Извиква се преди замразяване на играч
```
  
[user_freeze_post](https://amxx-bg.info/api/vzbb_mod/user_freeze_post) | ```
Извиква се след замразяване на играч
```
  
[user_unfreeze_pre](https://amxx-bg.info/api/vzbb_mod/user_unfreeze_pre) | ```
Извиква се преди премахването на замразяването на играч
```
  
[user_unfreeze_post](https://amxx-bg.info/api/vzbb_mod/user_unfreeze_post) | ```
Извиква се след премахването на замразяването на играч
```
  
[user_freeze_cool_pre](https://amxx-bg.info/api/vzbb_mod/user_freeze_cool_pre) | ```
Извиква се преди играч да започне да се топи
```
  
[user_freeze_cool_post](https://amxx-bg.info/api/vzbb_mod/user_freeze_cool_post) | ```
Извиква се след като играч започне да се топи
```
  
[user_unfreeze_cool_pre](https://amxx-bg.info/api/vzbb_mod/user_unfreeze_cool_pre) | ```
Извиква се преди играч да спре да се топи
```
  
[user_unfreeze_cool_post](https://amxx-bg.info/api/vzbb_mod/user_unfreeze_cool_post) | ```
Извиква се след като играч спре да се топи
```
  
[user_infect_pre](https://amxx-bg.info/api/vzbb_mod/user_infect_pre) | ```
Извиква се преди инфектиране на играч
```
  
[user_infect_post](https://amxx-bg.info/api/vzbb_mod/user_infect_post) | ```
Извиква се след инфектиране на играч
```
  
[user_uninfect_pre](https://amxx-bg.info/api/vzbb_mod/user_uninfect_pre) | ```
Извиква се преди деинфектиране на играч
```
  
[user_uninfect_post](https://amxx-bg.info/api/vzbb_mod/user_uninfect_post) | ```
Извиква се след деинфектиране на играч
```
  
[grab_block_pre](https://amxx-bg.info/api/vzbb_mod/grab_block_pre) | ```
Извиква се преди взимане на блок
```
  
[grab_block_post](https://amxx-bg.info/api/vzbb_mod/grab_block_post) | ```
Извиква се след взимане на блок
```
  
[release_block_pre](https://amxx-bg.info/api/vzbb_mod/release_block_pre) | ```
Извиква се преди пускането на блок
```
  
[release_block_post](https://amxx-bg.info/api/vzbb_mod/release_block_post) | ```
Извиква се след пускането на блок
```
  
[update_user_hud_data](https://amxx-bg.info/api/vzbb_mod/update_user_hud_data) | ```
Извиква се при всяко обновяване на HUD-а на играчите
```
  
[fun_block_touch_pre](https://amxx-bg.info/api/vzbb_mod/fun_block_touch_pre) | ```
Извиква се преди докосване на играч със забавен блок
```
  
[fun_block_touch_post](https://amxx-bg.info/api/vzbb_mod/fun_block_touch_post) | ```
Извиква се след докосване на играч със забавен блок
```
  

This code is a part of vzbb_mod.inc. To use this code you should include vzbb_mod.inc as ```#include <vzbb_mod>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.