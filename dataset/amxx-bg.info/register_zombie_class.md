# register_zombie_class
#### Syntax
```
native register_zombie_class(const classname[], const classinfo[], const classmdl[], const classclawmdl[], health, Float:gravity, Float:speed, access)
```

#### Usage
classname | ```Името на зомби класа (пример: "Test Zombie")```
---|---
classinfo | ```Кратка информация относно зомби класа (пример: "g+ s-")```
classmdl | ```Модел на зомби класа (пример: "zombie" , трябва да се намира в models/player/име/име.mdl)```
classclawmdl | ```Модел на ръцете на зомби класа (пример: "claw" , трябва да се намира в models/име.mdl)```
health | ```Кръв на зомби класа (пример: 2000)```
gravity | ```Гравитация на зомби класа (пример: 0.5) (1.0 = 800 гравитаця , 0.5 = 400 гравитация ...)```
speed | ```Скорост на зомби класа (пример: 400.0) (0.0 = нормална скорост)```
access | ```Админ достъп нужен за избиране на класа (ADMIN_ALL - за всички)```
#### Description
```
Регистрира нов зомби клас
```

#### Return
```
Връща индекса на класа. (int)
```


This code is a part of vzbb_mod.inc. To use this code you should include vzbb_mod.inc as ```#include <vzbb_mod>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.