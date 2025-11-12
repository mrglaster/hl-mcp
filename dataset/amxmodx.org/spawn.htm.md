pawn
[Fun](http://127.0.0.1:8000/content/index.htm) (fun.inc) 
Description
spawn - Spawns entity. 
Syntax
spawn ( index ) 
Type
Native 
User Contributed Notes
XxAvalanchexX at hotmail dot com | Feb-05-05 22:40:28  
---|---  
People have had trouble getting this to work, the below seems to be the "correct" way to do it without any bugs: ` public soandso(id)   
{   
   spawn(id);   
   set_task(0.5,"spawnagain",id);   
}   
   
public spawnagain(id) {   
   spawn(id);   
}  ` You can play around with the 0.5 time.   
  
sniperbeamer at amxmodx dot org | Jul-07-04 19:41:54  
---|---  
You might have to use spawn() two times for players.   
  

