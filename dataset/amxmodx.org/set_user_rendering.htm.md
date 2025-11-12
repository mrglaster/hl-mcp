et_user_rendering
[Fun](http://127.0.0.1:8000/content/index.htm) (fun.inc) 
Description
set_user_rendering - Sets player rendering mode. 
Syntax
set_user_rendering ( index, [ fx = kRenderFxNone, r = 255, g = 255, b = 255, render = kRenderNormal, amount = 16 ] ) 
Type
Native 
Notes
Example: ( Make a player Glow red )   
`    
set_user_rendering(index,kRenderFxGlowShell,255,0,0,kRenderNormal,25)   
  `   
  
Example: ( Remove the glow)   
`    
set_user_rendering(index,kRenderFxGlowShell,0,0,0,kRenderNormal,25)   
  `   
  
A list of different render modes:   
kRenderNormal = 0, /* src */   
kRenderTransColor, /* c*a+dest*(1-a) */   
kRenderTransTexture, /* src*a+dest*(1-a) */   
kRenderGlow, /* src*a+dest -- No Z buffer checks */   
kRenderTransAlpha, /* src*srca+dest*(1-srca) */   
kRenderTransAdd, /* src*a+dest */   
  
A list of different render effects:   
kRenderFxNone = 0,   
kRenderFxPulseSlow,   
kRenderFxPulseFast,   
kRenderFxPulseSlowWide,   
kRenderFxPulseFastWide,   
kRenderFxFadeSlow,   
kRenderFxFadeFast,   
kRenderFxSolidSlow,   
kRenderFxSolidFast,   
kRenderFxStrobeSlow,   
kRenderFxStrobeFast,   
kRenderFxStrobeFaster,   
kRenderFxFlickerSlow,   
kRenderFxFlickerFast,   
kRenderFxNoDissipation,   
kRenderFxDistort, /* Distort/scale/translate flicker */   
kRenderFxHologram, /* kRenderFxDistort + distance fade */   
kRenderFxDeadPlayer, /* kRenderAmt is the player index */   
kRenderFxExplode, /* Scale up really big! */   
kRenderFxGlowShell, /* Glowing Shell */   
kRenderFxClampMinScale, /* Keep this sprite from getting very small (SPRITES only!) */ 
User Contributed Notes
root at Neo-Vortex dot Ath dot Cx | Jul-23-04 16:16:58  
---|---  
well, render types, whatever, but yeah, its the second last param, *mutters about them not being listed making me look them up...*   
  
root at Neo-Vortex dot Ath dot Cx | Jul-23-04 15:50:01  
---|---  
Some other, non-listed rendering modes (from amxconst.inc): kRenderNormal = 0, // src kRenderTransColor, // c*a+dest*(1-a) kRenderTransTexture, // src*a+dest*(1-a) kRenderGlow, // src*a+dest -- No Z buffer checks kRenderTransAlpha, // src*srca+dest*(1-srca) kRenderTransAdd, // src*a+dest   
  

