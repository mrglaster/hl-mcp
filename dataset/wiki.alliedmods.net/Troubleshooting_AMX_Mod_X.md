# Troubleshooting AMX Mod X
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Troubleshooting_AMX_Mod_X#mw-head), [search](https://wiki.alliedmods.net/Troubleshooting_AMX_Mod_X#p-search)
If something goes wrong with your AMX Mod X installation, it's usually a problem someone else before has had. This FAQ shows some of the more common problems with steps to solving them. 
# Plugin Problems
## Loading Errors
`**Q:** What does "function not found" mean?`  
**A:** This means a function the plugin uses could not be found. Most likely you forgot to enable a module that the plugin uses. Check the plugin's documentation, then see [Configuring Modules](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Modules "Configuring AMX Mod X"). 
`**Q:** What does "module required for plugin" mean?`  
**A:** See above question. If you get this error, it should also tell you exactly which module you need to enable. 
`**Q:** What does "Run time error ... debug not enabled" mean?`  
**A:** This means an internal error occured in the plugin. To enable debug mode, and report the problem to the author, add the word "debug" after the plugin's entry in amxmodx/plugins/plugins.ini. For example: 
```
myplugin.amxx debug
```

For more information, see [Debugging Plugins](https://wiki.alliedmods.net/Debugging_Plugins_\(AMX_Mod_X\) "Debugging Plugins \(AMX Mod X\)"). 
`**Q:** I have debug enabled and I still get run time errors!`  
**A:** Copy and paste the runtime errors and give them to the plugin author. If the errors occur in official AMX Mod X plugins, make a bug report. 
