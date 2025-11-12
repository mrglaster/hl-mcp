s_set_user_team
[Cstrike](http://127.0.0.1:8000/content/index.htm) (cstrike.inc) 
Description
cs_set_user_team - Sets a CS player's team without killing the player. 
Syntax
cs_set_user_team ( index, CsTeams:team, [ CsInternalModel: model = CS_DONTCHANGE ] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
Team values are CS_TEAM_T, CS_TEAM_CT, or CS_TEAM_SPECTATOR.   
  
You can optionally set a model:   
CS_DONTCHANGE   
CS_CT_URBAN   
CS_T_TERROR   
CS_T_LEET   
CS_T_ARCTIC   
CS_CT_GSG9   
CS_CT_GIGN   
CS_CT_SAS   
CS_T_GUERILLA   
CS_CT_VIP
