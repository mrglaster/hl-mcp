egister_event
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
register_event - Registers an event on which a given function will be called 
Syntax
register_event ( const event[], const function[], const flags[], [ cond=[], ... ] ) 
Type
Native 
Notes
event is a message, such as "DeathMsg", "Damage", et cetera.   
  
function is the name of a public function which will be called on this event.   
  
flags is a combination of flags that determine if this event is forwarded:   
"a" - Global Event   
"b" - Event sent to a single target   
"c" - Send only once when repeated to other players   
"d" - Only if sent to a dead player   
"e" - Only if sent to an alive player   
  
You can optionally set a list of restrictions/conditions on the event. For example:   
"2=c4" - 2nd parameter of message must be sting "c4".   
"3>10" - 3rd parameter must be greater then 10.   
"3!4" - 3rd must not be 4.   
"2&Buy" - 2nd parameter of message must contain "Buy" substring.   
"2!Buy" - 2nd parameter of message can't contain "Buy" substring.   
  
Example:   
`    
public plugin_init()   
  
   //Only called if killer is not worldspawn    
   register_event("DeathMsg", "hook_death", "a", "1>0")   
}   
   
public hook_death()   
  
   new Killer = read_data(1)   
   new Victim = read_data(2)   
}   
  `   

User Contributed Notes
wchristian at gmx dot ch | Dec-26-04 21:15:52  
---|---  
Hi, Correction ;) You need to type "meta game" (it's key sensitive ;))   
  
burnincoldblue at comcast dot net | Oct-20-04 04:24:18  
---|---  
If you have a server running you can type "meta Game" into the console showing you all the messages that you can use with this function.   
  

