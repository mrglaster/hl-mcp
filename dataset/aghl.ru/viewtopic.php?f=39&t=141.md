# Half-Life и Adrenaline Gamer форум
Всё об игре в Халф-Лайф и АГ  


## [[TUT] Меняем емкость настенных аптечек и HEV в HLDM](https://aghlru.ds-servers.com/forum/viewtopic.php?f=39&t=141)
Категории: [Туториал](https://aghlru.ds-servers.com/forum/search.php?keywords=%2B%D0%A2%D1%83%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB&terms=all&fid\[\]=19&sc=1&sf=catonly&sr=topics)
Модератор: [KORD_12.7](https://aghlru.ds-servers.com/forum/memberlist.php?mode=viewprofile&u=67)
  
Количество ХП в аптечке можно поменять через CVAR sk_suitcharger1  
Он прописан в skill.cfg, по дефолту его значение 50.  
А вот с HEV чарджерами несколько сложнее. Дело в том что их максимальное значение для HLDM жестко прописано в коде и через skill.cfg его не изменить.  
  
Вот кусок кода из HLSDK  
  
**Код:**
```
void CHalfLifeMultiplay::RefreshSkillData( void )  
{  
// load all default values  
 CGameRules::RefreshSkillData();  
  
// override some values for multiplay.  
  
 // suitcharger  
 gSkillData.suitchargerCapacity = 30;  
```
  
Средствами амхх я решил вопрос так:  
  
**Код:** 
```
#include <amxmodx>  
#include <fakemeta>  
#include <hamsandwich>  
  
#define PLUGIN "HEV Chargers"  
#define VERSION "0.01"  
#define AUTHOR "AfaLINK"  
  
#define M_IJUICE_OFFSET 62  
  
new pArmorCharger  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    pArmorCharger = register_cvar("armor_charger", "50")  
    RegisterHam(Ham_Use, "func_recharge", "UseCharger_Pre")  
    RegisterHam(Ham_Use, "func_recharge", "UseCharger_Post", 1)  
}  
  
  
public UseCharger_Pre(entid, player)  
{  
    if(!pev(entid, pev_iuser1) && get_pdata_int(entid, M_IJUICE_OFFSET))  
    {  
        set_pev(entid, pev_iuser1, 1)  
        set_pdata_int(entid, M_IJUICE_OFFSET, get_pcvar_num(pArmorCharger))  
    }  
}  
  
  
public UseCharger_Post(entid, player)  
{  
    if(!get_pdata_int(entid, M_IJUICE_OFFSET))  
        set_pev(entid, pev_iuser1, 0)  
}
```
  
Аналогичным способом, если нужно, можно менять аптечки.  
Только вместо func_recharge в RegisterHam нужно поставить func_healthcharger.  
  
  
А если сделать так, то аптечки и броня будут бесконечными:  
  
**Код:**
```
#include <amxmodx>  
#include <fakemeta>  
#include <hamsandwich>  
  
#define PLUGIN "Infinit Chargers"  
#define VERSION "0.01"  
#define AUTHOR "AfaLINK"  
  
#define M_IJUICE_OFFSET 62  
  
  
public plugin_init() {  
    register_plugin(PLUGIN, VERSION, AUTHOR)  
    RegisterHam(Ham_Use, "func_recharge", "UseCharger_Post", 1)  
    RegisterHam(Ham_Use, "func_healthcharger", "UseCharger_Post", 1)  
}  
  
  
public UseCharger_Post(entid, player)  
    set_pdata_int(entid, M_IJUICE_OFFSET, 100)
```
