# Код позволяет "использовать" разные энтити объекты (где нет возм. по умолчанию)

```
public plugin_init()

{

    RegisterHam(Ham_ObjectCaps,  "weaponbox", "ObjectCaps", .Post = false)

    RegisterHam(Ham_Use, "weaponbox", "Weaponbox_Use", .Post = true)  

}



public ObjectCaps(pWeaponBox)

{

    SetHamReturnInteger(FCAP_ONOFF_USE)    // see FCAP_ cons hlsdk_const.inc
    return HAM_OVERRIDE

}



public Weaponbox_Use(pWeaponBox, pOther)

{
    if(is_user_connected(pOther)) // is player

    {
        client_print(pOther, print_center, "%i", pWeaponBox)

    }

}

```
