;STL FILE: parrot.stl

;Layer height: 0.2mm

;Nozzle diameter: 0.4mm

;Filament diameter: 1.75mm

;Extrusion multiplier: 1

G21 ; set units to millimeters

G90 ; use absolute coordinates

M82 ; use absolute distances for extrusion

M106 S0 ; turn off fan

M107 ; turn off laser

G28 ; home all axes

G1 F1500 ; set nozzle opening / feed rate

G92 E0 ; zero the extruded length

G1 Z0.4 ; raise nozzle

G1 X0 Y0 F5000 ; move to front left corner

M109 S200 ; set temperature and wait for it to be reached

; load filament

G1 E10 F600 ; extrude 10mm of filament

G92 E0 ; zero the extruded length

G1 F1500 ; set feed rate

; start printing

; perimeters

G1 X38.651 Y10.355 E0.118 F2100 ; outer perimeter

G1 E0.471 F1080 ; inner perimeter

G1 X38.978 Y9.321 E0.589 F2100 ; outer perimeter

G1 E0.942 F1080 ; inner perimeter

G1 X38.978 Y8.287 E1.060 F2100 ; outer perimeter

G1 E1.413 F1080 ; inner perimeter

G1 X38.651 Y7.254 E1.531 F2100 ; outer perimeter

G1 E1.884 F1080 ; inner perimeter

G1 X37.617 Y7.254 E1.977 F2100 ; outer perimeter

G1 E2.329 F1080 ; inner perimeter

G1 X37.291 Y8.287 E2.425 F2100 ; outer perimeter

G1 E2.773 F1080 ; inner perimeter

G1 X37.291 Y9.321 E2.871 F2100 ; outer perimeter

G1 E3.217 F1080 ; inner perimeter

G1 X37.617 Y10.355 E3.319 F2100 ; outer perimeter

G1 E3.662 F1080 ; inner perimeter

G92 E0 ; zero the extruded length

; infill

G1 X21.348 Y10.355 E0.118 F2100 ; outer perimeter

G1 E0.177 F1080 ; inner perimeter

G1 X22.022 Y9.52 E0.295 F2100 ; outer perimeter

G1 E0.353 F1080 ; inner perimeter

G1 X22.724 Y8.526 E0.462 F2100 ; outer perimeter

G1 E0.529 F1080 ; inner perimeter

G1 X23.326 Y7.988 E0.62 F2100 ; outer perimeter

G1 E0.705 F1080 ; inner perimeter

G1 X23.928 Y7.454 E0.778 F2100 ; outer perimeter

G1 E0.881 F1080 ; inner perimeter

G1 X24.53 Y7.254 E0.936 F2100 ; outer perimeter

G1 E1.012 F1080 ; inner perimeter

G1 X25.132 Y7.454 E1.092 F2100 ; outer perimeter

G1 E1.244 F1080 ; inner perimeter

G1 X25.734 Y7.988 E1.25 F2100 ; outer perimeter

G1 E1.426 F1080 ; inner perimeter

G1 X26.336 Y8.526 E1.408 F2100 ; outer perimeter

G1 E1.608 F1080 ; inner perimeter

G1 X27.038 Y9.52 E1.575 F2100 ; outer perimeter

G1 E1.784 F1080 ; inner perimeter

G1 X27.712 Y10.355 E1.752 F2100 ; outer perimeter

G1 E1.93 F1080 ; inner perimeter

G1 X28.387 Y9.52 E1.909 F2100 ; outer perimeter

G1 E2.085 F1080 ; inner perimeter

G1 X29.089 Y8.526 E2.076 F2100 ; outer perimeter

G1 E2.257 F1080 ; inner perimeter

G1 X29.691 Y7.988 E2.234 F2100 ; outer perimeter

G1 E2.429 F1080 ; inner perimeter

G1 X30.293 Y7.454 E2.392 F2100 ; outer perimeter

G1 E2.601 F1080 ; inner perimeter

G1 X30.895 Y7.254 E2.548 F2100 ; outer perimeter

G1 E2.773 F1080 ; inner perimeter

G1 X31.497 Y7.454 E2.704 F2100 ; outer perimeter

G1 E2.949 F1080 ; inner perimeter

G1 X32.099 Y7.988 E2.862 F2100 ; outer perimeter

G1 E3.125 F1080 ; inner perimeter

G1 X32.701 Y8.526 E3.02 F2100 ; outer perimeter

G1 E3.297 F1080 ; inner perimeter

G1 X33.403 Y9.52 E3.187 F2100 ; outer perimeter

G1 E3.473 F1080 ; inner perimeter

G1 X34.105 Y10.355 E3.354 F2100 ; outer perimeter

G1 E3.649 F1080 ; inner perimeter

G1 X34.78 Y9.52 E3.511 F2100 ; outer perimeter

G1 E3.837 F1080 ; inner perimeter

G1 X35.482 Y8.526 E3.678 F2100 ; outer perimeter

G1 E4.024 F1080 ; inner perimeter

G1 X36.184 Y7.988 E3.836 F2100 ; outer perimeter

G1 E4.211 F1080 ; inner perimeter

G1 X36.786 Y7.454 E3.994 F2100 ; outer perimeter

G1 E4.398 F1080 ; inner perimeter

G1 X37.388 Y7.254 E4.15 F2100 ; outer perimeter

G1 E4.585 F1080 ; inner perimeter

G1 X37.99 Y7.454 E4.306 F2100 ; outer perimeter

G1 E4.772 F1080 ; inner perimeter

G1 X38.592 Y7.988 E4.464 F2100 ; outer perimeter

G1 E4.949 F1080 ; inner perimeter

G1 X39.194 Y8.526 E4.622 F2100 ; outer perimeter

G1 E5.136 F1080 ; inner perimeter

G1 X39.896 Y9.52 E4.789 F2100 ; outer perimeter

G1 E5.323 F1080 ; inner perimeter

G1 X40.598 Y10.355 E4.956 F2100 ; outer perimeter

G1 E5.51 F1080 ; inner perimeter

G1 X41.273 Y9.52 E5.113 F2100 ; outer perimeter

G1 E5.707 F1080 ; inner perimeter

G1 X41.975 Y8.526 E5.28 F2100 ; outer perimeter

G1 E5.894 F1080 ; inner perimeter

G1 X42.677 Y7.988 E5.438 F2100 ; outer perimeter

G1 E6.081 F1080 ; inner perimeter

G1 X43.279 Y7.454 E5.596 F2100 ; outer perimeter

G1 E6.268 F1080 ; inner perimeter

G1 X43.881 Y7.254 E5.752 F2100 ; outer perimeter

G1 E6.455 F1080 ; inner perimeter

G1 X44.483 Y7.454 E5.908 F2100 ; outer perimeter

G1 E6.642 F1080 ; inner perimeter

G1 X45.085 Y7.988 E6.066 F2100 ; outer perimeter

G1 E6.829 F1080 ; inner perimeter

G1 X45.687 Y8.526 E6.224 F2100 ; outer perimeter

G1 E7.016 F1080 ; inner perimeter

G1 X46.389 Y9.52 E6.391 F2100 ; outer perimeter

G1 E7.203 F1080 ; inner perimeter

G1 X47.091 Y10.355 E6.558 F2100 ; outer perimeter

G1 E7.39 F1080 ; inner perimeter

G1 X47.766 Y9.52 E6.715 F2100 ; outer perimeter

G1 E7.587 F1080 ; inner perimeter

G1 X48.468 Y8.526 E6.882 F2100 ; outer perimeter

G1 E7.774 F1080 ; inner perimeter

G1 X49.17 Y7.988 E7.04 F2100 ; outer perimeter

G1 E7.961 F1080 ; inner perimeter

G1 X49.772 Y7.454 E7.198 F2100 ; outer perimeter

G1 E8.148 F1080 ; inner perimeter

G1 X50.374 Y7.254 E7.354 F2100 ; outer perimeter

G1 E8.335 F1080 ; inner perimeter

G1 X50.976 Y7.454 E7.51 F2100 ; outer perimeter

G1 E8.522 F1080 ; inner perimeter

G1 X51.578 Y7.988 E7.668 F2100 ; outer perimeter

G1 E8.709 F1080 ; inner perimeter

G1 X52.18 Y8.526 E7.826 F2100 ; outer perimeter

G1 E8.896 F1080 ; inner perimeter

G1 X52.882 Y9.52 E7.993 F2100 ; outer perimeter

G1 E9.083 F1080 ; inner perimeter

G1 X53.584 Y10.355 E8.16 F2100 ; outer perimeter

G1 E9.27 F1080 ; inner perimeter

G1 X54.259 Y9.52 E8.317 F2100 ; outer perimeter

G1 E9.457 F1080 ; inner perimeter

G1 X54.961 Y8.526 E8.484 F2100 ; outer perimeter

G1 E9.644 F1080 ; inner perimeter

G1 X55.663 Y7.988 E8.642 F2100 ; outer perimeter

G1 E9.831 F1080 ; inner perimeter

G1 X56.265 Y7.454 E8.8 F2100 ; outer perimeter

G1 E10.018 F1080 ; inner perimeter

G1 X56.867 Y7.254 E8.956 F2100 ; outer perimeter

G1 E10.205 F1080 ; inner perimeter

G1 X57.469 Y7.454 E9.112 F2100 ; outer perimeter

G1 E10.392 F1080 ; inner perimeter

G1 X58.071 Y7.988 E9.27 F2100 ; outer perimeter

G1 E10.579 F1080 ; inner perimeter

G1 X58.673 Y8.526 E9.428 F2100 ; outer perimeter

G1 E10.766 F1080 ; inner perimeter

G1 X59.375 Y9.52 E9.595 F2100 ; outer perimeter

G1 E10.953 F1080 ; inner perimeter

G1 X60.077 Y10.355 E9.762 F2100 ; outer perimeter

G1 E11.14 F1080 ; inner perimeter

G1 X60.752 Y9.52 E9.919 F2100 ; outer perimeter

G1 E11.337 F1080 ; inner perimeter

G1 X61.454 Y8.526 E10.086 F2100 ; outer perimeter

G1 E11.524 F1080 ; inner perimeter

G1 X62.156 Y7.988 E10.244 F2100 ; outer perimeter

G1 E11.711 F1080 ; inner perimeter

G1 X62.758 Y7.454 E10.402 F2100 ; outer perimeter

G1 E11.898 F1080 ; inner perimeter

G1 X63.36 Y7.254 E10.558 F2100 ; outer perimeter

G1 E12.085 F1080 ; inner perimeter

G1 X63.962 Y7.454 E10.714 F2100 ; outer perimeter

G1 E12.272 F1080 ; inner perimeter

G1 X64.564 Y7.988 E10.872 F2100 ; outer perimeter

G1 E12.459 F1080 ; inner perimeter

G1 X65.166 Y8.526 E11.03 F2100 ; outer perimeter

G1 E12.646 F1080 ; inner perimeter

G1 X65.868 Y9.52 E11.197 F2100 ; outer perimeter

G1 E12.833 F1080 ; inner perimeter

G1 X66.57 Y10.355 E11.364 F2100 ; outer perimeter

G1 E13.02 F1080 ; inner perimeter

G1 X67.245 Y9.52 E11.521 F2100 ; outer perimeter

G1 E13.217 F1080 ; inner perimeter

G1 X67.947 Y8.526 E11.688 F2100 ; outer perimeter

G1 E13.404 F1080 ; inner perimeter

G1 X68.649 Y7.988 E11.846 F2100 ; outer perimeter

G1 E13.591 F1080 ; inner perimeter

G1 X69.251 Y7.454 E12.004 F2100 ; outer perimeter

G1 E13.778 F1080 ; inner perimeter

G1 X69.853 Y7.254 E12.16 F2100 ; outer perimeter

G1 E13.965 F1080 ; inner perimeter

G1 X70.455 Y7.454 E12.316 F2100 ; outer perimeter

G1 E14.152 F1080 ; inner perimeter

G1 X71.057 Y7.988 E12.474 F2100 ; outer perimeter

G1 E14.339 F1080 ; inner perimeter

G1 X71.659 Y8.526 E12.632 F2100 ; outer perimeter

G1 E14.526 F1080 ; inner perimeter

G1 X72.361 Y9.52 E12.799 F2100 ; outer perimeter

G1 E14.713 F1080 ; inner perimeter

G1 X73.063 Y10.355 E12.966 F2100 ; outer perimeter

G1 E14.9 F1080 ; inner perimeter

G1 X73.738 Y9.52 E13.123 F2100 ; outer perimeter

G1 E15.097 F1080 ; inner perimeter

G1 X74.44 Y8.526 E13.29 F2100 ; outer perimeter

G1 E15.284 F1080 ; inner perimeter

G1 X75.142 Y7.988 E13.448 F2100 ; outer perimeter

G1 E15.471 F1080 ; inner perimeter

G1 X75.744 Y7.454 E13.606 F2100 ; outer perimeter

G1 E15.658 F1080 ; inner perimeter

G1 X76.346 Y7.254 E13.762 F2100 ; outer perimeter

G1 E15.845 F1080 ; inner perimeter

G1 X76.948 Y7.454 E13.918 F2100 ; outer perimeter

G1 E16.032 F1080 ; inner perimeter

G1 X77.55 Y7.988 E14.076 F2100 ; outer perimeter

G1 E16.219 F1080 ; inner perimeter

G1 X78.152 Y8.526 E14.234 F2100 ; outer perimeter

G1 E16.406 F1080 ; inner perimeter

G1 X78.854 Y9.52 E14.401 F2100 ; outer perimeter

G1 E16.593 F1080 ; inner perimeter

G1 X79.556 Y10.355 E14.568 F2100 ; outer perimeter

G1 E16.78 F1080 ; inner perimeter

G1 X80.231 Y9.52 E14.725 F2100 ; outer perimeter

G1 E16.977 F1080 ; inner perimeter

G1 X80.933 Y8.526 E14.892 F2100 ; outer perimeter

G1 E17.164 F1080 ; inner perimeter

G1 X81.635 Y7.988 E15.048 F2100 ; outer perimeter

G1 E17.351 F1080 ; inner perimeter

G1 X82.237 Y7.454 E15.206 F2100 ; outer perimeter

G1 E17.538 F1080 ; inner perimeter

G1 X82.839 Y7.254 E15.362 F2100 ; outer perimeter

G1 E17.725 F1080 ; inner perimeter

G1 X83.441 Y7.454 E15.518 F2100 ; outer perimeter
