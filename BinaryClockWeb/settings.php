<?php

/* 
 *  
 * Settings ui for pybinaryclock:
 * 
 * Select and write these things to a setting-file: 
 * Brightness, color '1', color '0', timezone,  enable/disable background ligth measure,
 * CPU temp warning, 
 * 
 */

//Input form BRG values for 1 and 0
// Selectbox for timezone


$file = fopen("pybinaryclock.py","w");

echo fwrite($file,"GeneralSettings = {'HW-version': 1, 'DefaultBrightness': 50, 'TempMax': 60, }");
fclose($file);

