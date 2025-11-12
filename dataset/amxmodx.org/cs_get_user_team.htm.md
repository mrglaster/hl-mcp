s_get_user_team
[Cstrike](http://127.0.0.1:8000/content/index.htm) (cstrike.inc) 
Description
cs_get_user_team - Gets a user's CS team. 
Syntax
cs_get_user_team ( index ) 
Type
Native 
Notes
Return type is CsTeams, which means you have to declare your variable as CsTeams:name, just as you declare a float as Float:name.   
  
index is a player index from 1 to 32.   
  
Return values are CS_TEAM_T, CS_TEAM_CT, or CS_TEAM_SPECTATOR. 
User Contributed Notes
XxAvalanchexX at hotmail dot com | Oct-23-04 06:14:19  
---|---  
This function returns constants that are interpreted as 1 being Terrorist, 2 being Counter-Terrorist, and 3 being Spectator.   
  
jim_nicebutdim at hotmail dot com | Jul-08-04 19:05:38  
---|---  
How does this work? Specifically I'm trying to defferentiate between teams in CS Maps, so for example I could make a teleporter that works for CT's only. I know this comment isn't helpful, but the *answer* might provide some useful insight for CS mappers, like me, who have so far been unable to put team-specific triggers/event in their maps!   
  

