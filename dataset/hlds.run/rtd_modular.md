# Roll the Dice Modular: Core​ - Плагин для управления случайными эффектами

## Описание 

Roll the Dice Modular: Core - это гибкая и расширяемая система "Roll the Dice" (брось кубик), построенная по модульному принципу. Вместо жёстко прописанных эффектов, плагин позволяет реализовывать их в сторонних плагинах и просто регистрировать их. Плагин совместим со всеми играми, поддерживающими AMX MOD X.

Игроки могут использовать команду rtd (или /rtd, rollthedice) в чате, чтобы получить случайный эффект с учётом трёх уровней редкости:

    - Normal (обычный)
    - Rare (редкий)
    - Ultra Rare (очень редкий)

Шансы выпадения каждого типа эффекта настраиваются автоматически в зависимости от того, какие типы эффектов зарегистрированы. Например, если в сервере есть только Ultra Rare эффекты — они будут выпадать с 100% вероятностью.

Для администраторов доступно меню тестирования эффектов, для его открытия необходимо ввести команду /rtdtest
В этом меню можно выбрать категорию тестируемого эффекта, сам эффект, а также игрока, на которого он будет применен.

## Создаем собственный случайный эффект

0. Скачайте плагин [Roll The Dice Modular: Core](https://hlds.run/resources/267/) и установите его
1. Импортируйте модуль как ```#include <rtd_core>```
2. Задайте имя и вашему эффекту
```
#define EFFECT_NAME "Free Battery"
```

3. Зарегистрируйте эфект в plugin_init при помощи метода rtdc_register_effect. Метод принимает в себя следующие параметры:

    - Функция, которая будет выполнена при выпадении эффекта
    - Название эффекта
    - Редкость эффекта. Доступны следующие опции: EFFECT_NORMAL (обычный эффект), EFFECT_RARE (редкий эффект) и EFFECT_ULTRA_RARE (Ультра редкий эффект)

В одном плагине можно зарегистрировать сразу несколько эффектов, но для демонстрации ограничемся одним.

```
public plugin_init(){
    register_plugin(PLUGIN_NAME, PLUGIN_VERSION, PLUGIN_AUTHOR);
    rtdc_register_effect("giveUserArmor", EFFECT_NAME, EFFECT_NORMAL);
}
```

4. Реализуйте заданную ранее функцию эффекта

```
public giveUserArmor(id){
    set_hudmessage(0, 255, 255, -1.0, 0.6, 1, 1.0, 1.0, 0.1, 0.1, -1);
    show_hudmessage(id, EFFECT_NAME);
    emit_sound(id, 0, "items/suitchargeok1.wav", 1.0, ATTN_NORM, 0, PITCH_NORM);
    hl_set_user_armor(id, hl_get_user_armor(id) + batteryValue);
}
```

5. Соберите и установите плагин как обычно.

## Содержимое rtd_core.inc

```
#define EFFECT_NORMAL 0
#define EFFECT_RARE 1
#define EFFECT_ULTRA_RARE 2
#define is_user_valid(%1) (1 <= %1 <= get_maxplayers() && is_user_alive(%1) && is_user_connected(%1))

// The rarity os valculated the following way:
// value <= EFFECT_NORMAL_PERCENT  -  Normal Effect
// EFFECT_NORMAL_PERCENT+1 <= value <= EFFECT_RARE_PERCENT - Rare Effect
// value >= EFFECT_RARE_PERCENT + 1 - Ultra Rare Effect

#define EFFECT_NORMAL_PERCENT 80
#define EFFECT_RARE_PERCENT 95
#define EFFECT_ULTRA_RARE_PERCENT 100

native rtdc_register_effect(const szEffectMethod[128], const szEffectName[128], const effectRarity)
```




