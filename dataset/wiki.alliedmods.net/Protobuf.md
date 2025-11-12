# Protobuf
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Protobuf#mw-head), [search](https://wiki.alliedmods.net/Protobuf#p-search)
## Contents
  * [1 Intro](https://wiki.alliedmods.net/Protobuf#Intro)
  * [2 Differences](https://wiki.alliedmods.net/Protobuf#Differences)
  * [3 Protobuf natives](https://wiki.alliedmods.net/Protobuf#Protobuf_natives)
  * [4 Multi-game usermessages example](https://wiki.alliedmods.net/Protobuf#Multi-game_usermessages_example)
  * [5 Embedded message example](https://wiki.alliedmods.net/Protobuf#Embedded_message_example)


## Intro
Unlike the serial bitbuffer-backed usermessages in older games, newer games such as CS:GO (and DOTA 2) now use Google's [Protocol Buffers](https://code.google.com/p/protobuf/) or "protobuf" to back net messages and usermessages. 
## Differences
Instead of having to be read or written in order, the protobuf usermessages use defined fields, accessible by name, in any order. 
Starting, ending, and hooking usermessages remains unchanged. Reading and writing values to/from them is done using the Pb* set of natives in protobuf.inc instead of the Bf* natives in bitbuffer.inc. 
You can tell which usermessage system is in use for the current game by checking GetUserMessageType(). Possible returns are UM_BitBuf and UM_Protobuf. 
  
Basic fields ("optional" or "required") are single values and use the PbRead*/PbSet* natives. 
Repeated fields are arrays of values, accessible by their 0-based index with the PbReadRepeated* natives or added with the PbAdd* natives. You can get the count of values in a repeated field with PbGetRepeatedFieldCount. 
  
For message and field names, see the [CS:GO Usermessages](https://github.com/alliedmodders/hl2sdk/blob/csgo/public/game/shared/csgo/protobuf/cstrike15_usermessages.proto#L68) as defined in protobuf's proto format, the [Counter-Strike: Global Offensive UserMessages](https://wiki.alliedmods.net/Counter-Strike:_Global_Offensive_UserMessages "Counter-Strike: Global Offensive UserMessages") page, or the [DOTA 2 UserMessages](https://wiki.alliedmods.net/DOTA_2_UserMessages "DOTA 2 UserMessages") page. 
## Protobuf natives
See [protobuf.inc](https://github.com/alliedmodders/sourcemod/blob/master/plugins/include/protobuf.inc)
## Multi-game usermessages example
From funcommands' drug.sp, using the [Fade](http://hg.alliedmods.net/hl2sdks/hl2sdk-csgo/file/9a3c7f5049b6/public/game/shared/csgo/protobuf/cstrike15_usermessages.proto#l204) usermessage: 
```
    int clients[2];
    clients[0] = client;    
 
    int duration = 255;
    int holdtime = 255;
    int flags = 0x0002;
    int color[4] = { 0, 0, 0, 128 };
    color[0] = GetRandomInt(0,255);
    color[1] = GetRandomInt(0,255);
    color[2] = GetRandomInt(0,255);
 
    Handle msg = StartMessageEx(g_FadeUserMsgId, clients, 1);
 
    if (GetUserMessageType() == UM_Protobuf)
    {
        Protobuf pb = UserMessageToProtobuf(msg);
 
        pb.SetInt("duration", duration);
        pb.SetInt("hold_time", holdtime);
        pb.SetInt("flags", flags);
        pb.SetColor("clr", color);
    }
    else
    {
        BrWrite bf = UserMessageToBfWrite(msg);
 
        bf.WriteShort(duration);
        bf.WriteShort(holdtime);
        bf.WriteShort(flags);
        bf.WriteByte(color[0]);
        bf.WriteByte(color[1]);
        bf.WriteByte(color[2]);
        bf.WriteByte(color[3]);
    }
 
    EndMessage();
```

## Embedded message example
This example sends a VGUIMenu usermessage, adding values to a repeated field "subkeys" that uses the [Subkey message type](http://hg.alliedmods.net/hl2sdks/hl2sdk-csgo/file/tip/public/game/shared/csgo/protobuf/cstrike15_usermessages.proto#l137) defined in the [VGUIMenu message](http://hg.alliedmods.net/hl2sdks/hl2sdk-csgo/file/tip/public/game/shared/csgo/protobuf/cstrike15_usermessages.proto#l132). 
Once an embedded message handle is retrieved with ReadMessage, you can read or write to its fields with the normal PbRead/Set natives. GetRepeatedMessage or AddMessage will retrieve the handle for reading or writing respectively if it is a repeated field. 
```
void SendSourceModMOTD(int client)
{
    Protobuf pb = UserMessageToProtobuf(StartMessageOne("VGUIMenu", client));
 
    pb.SetString("name", "info");
    pb.SetBool("show", true);
 
    Protobuf subkey = PbAddMessage(pb, "subkeys");
    subkey.SetString("name", "type");
    subkey.SetString("str", "2"); // MOTDPANEL_TYPE_URL
 
    subkey = pb.AddMessage("subkeys");
    subkey.SetString("name", "title");
    subkey.SetString("str", "TESTING");
 
    subkey = pb.AddMessage("subkeys");
    subkey.SetString("name", "msg");
    subkey.SetString("str", "http://www.sourcemod.net");
 
    EndMessage();
}
```

