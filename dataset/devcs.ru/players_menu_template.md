
# Шаблон меню игроков

Простой шаблон игроков от Subb98, основным отличием которого является построения меню игроков с использованием уникального идентификатора UserID, который позволяет избежать недочет с неверным выбором игрока (случай носит исключающий характер, но тем не менее довольно встречающийся. При открытии меню игроков администратор может не надолго задержать его открытым или затратить некое время на поиск нужного игрока, тем временем данный игрок может выйти из сервера и на место его ID встать другой ID игрока, таким образом мы выбираем одного игрока для удаления, а удаляется другой игрок. По-своему опыту 1-3 случая за неделю точно).

И небольшая модификация от меня, которая требовалась под свои нужды.

    - Главный администратор (ADMIN_RCON) имеет право выбрать любого игрока, включая самого себя.
    - Простой администратор (ADMIN_BAN) имеет право выбрать любого игрока (включая иммунитированного), кроме главного администратора, самого себя и администраторов себе подобных (ADMIN_BAN).
    - Все иммунитированные игроки отмечаются с желтой звездочкой возле никнейма
    - Самого себя видно с красной звездочкой возле никнейма
    - Те игроки, которых выбрать невозможно выделяются серым цветом и желтой звездочкой возле никнейма, дабы тоже имеют своего рода "иммунитет" от выбора.


```
#include <amxmodx>

const PLAYERS_PER_PAGE = 8;

new g_MenuPosition[MAX_PLAYERS + 1];
new g_Players[MAX_PLAYERS + 1][MAX_PLAYERS];
new g_UserID[MAX_PLAYERS + 1][MAX_PLAYERS + 1];

public plugin_init() {
    register_clcmd("players_menu", "CmdPlayersMenu");
    register_menucmd(register_menuid("_players_menu"), 1023, "HandleMenu");
}

public CmdPlayersMenu(const id) {
    if(get_user_flags(id) & ADMIN_BAN) {
        return ShowMenu(id, g_MenuPosition[id] = 0);
    }
    console_print(id, "У вас недостаточно прав для использования этой команды");
    return PLUGIN_HANDLED;
}

ShowMenu(const id, Pos) {
    if(Pos < 0) return PLUGIN_CONTINUE;
  
    new PlayersNum, Start, End, PagesNum, Len, Menu[512], i, Name[32], b, Keys = MENU_KEY_0;
    new PlayerFlags, AdminFlags = get_user_flags(id);
  
    get_players(g_Players[id], PlayersNum, "ch");
  
    if((Start = Pos * PLAYERS_PER_PAGE) >= PlayersNum)
        Start = Pos = g_MenuPosition[id] = 0;
  
    if((End = Start + PLAYERS_PER_PAGE) > PlayersNum)
        End = PlayersNum;
  
    if((PagesNum = PlayersNum / PLAYERS_PER_PAGE + (PlayersNum % PLAYERS_PER_PAGE ? 1 : 0)) == 1)
        Len = copy(Menu, charsmax(Menu), "\yВыберите игрока^n^n");
    else
        Len = formatex(Menu, charsmax(Menu), "\yВыберите игрока \d(%d/%d)^n^n", Pos + 1, PagesNum);
  
    while(Start < End) {
        i = g_Players[id][Start++];
        g_UserID[id] = get_user_userid(i);
        get_user_name(i, Name, charsmax(Name));
        PlayerFlags = get_user_flags(i);
       
        if(AdminFlags & ADMIN_RCON) {
            Keys |= (1<<b);
            if(i != id)
                Len += formatex(Menu[Len], charsmax(Menu) - Len, "\y%d. \w%s%s^n", ++b, Name, (PlayerFlags & ADMIN_IMMUNITY) || (PlayerFlags & ADMIN_BAN) ? " \y*" : "");
            else {
                Len += formatex(Menu[Len], charsmax(Menu) - Len, "\y%d. \w%s \r*^n", ++b, Name);
            }
        } else if(AdminFlags & ADMIN_BAN) {
            if(i == id || PlayerFlags & ADMIN_BAN || PlayerFlags & ADMIN_RCON)
                Len += formatex(Menu[Len], charsmax(Menu) - Len, "\d%d. %s%s^n", ++b, Name, i == id ? " \r*" : " \y*");
            else {
                Keys |= (1<<b);
                Len += formatex(Menu[Len], charsmax(Menu) - Len, "\y%d. \w%s%s^n", ++b, Name, (PlayerFlags & ADMIN_IMMUNITY) ? " \y*" : "");
            }
        }
    }
   
    if(End < PlayersNum) {
        Keys |= MENU_KEY_9;
        formatex(Menu[Len], charsmax(Menu) - Len, "^n\y9. \wДалее^n\y0. \w%s", Pos ? "Назад" : "Выход");
    } else
        formatex(Menu[Len], charsmax(Menu) - Len, "^n\y0. \w%s", Pos ? "Назад" : "Выход");
   
    return show_menu(id, Keys, Menu, -1, "_players_menu");
}

public HandleMenu(const id, const Key) {
    switch(Key) {
        case 8: ShowMenu(id, ++g_MenuPosition[id]);
        case 9: ShowMenu(id, --g_MenuPosition[id]);
        default: {
            new Target = g_Players[id][g_MenuPosition[id] * PLAYERS_PER_PAGE + Key];
            if(get_user_userid(Target) == g_UserID[id][Target]) {
                new Name[32];
                get_user_name(Target, Name, charsmax(Name));
                client_print(id, print_chat, "Вы выбрали игрока: %s", Name);
            } else
                client_print(id, print_chat, "Выбранный Вами игрок отключился от сервера");
        }
    }
}
```
