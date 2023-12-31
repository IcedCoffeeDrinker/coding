; add_to_cart.gcode

; generated by Slic3r 1.3.0 on 2017-02-02 at 16:48:57

; external perimeters extrusion width = 0.45mm (2.20mm ^ 2)

; first layer extrusion width = 0.45mm (2.20mm ^ 2)

; perimeters extrusion width = 0.45mm (2.20mm ^ 2)

; infill extrusion width = 0.45mm (2.20mm ^ 2)

; solid infill extrusion width = 0.45mm (2.20mm ^ 2)

; top infill extrusion width = 0.45mm (2.20mm ^ 2)

; support material extrusion width = 0.45mm (2.20mm ^ 2)

; nozzle diameter = 0.4mm

; filament diameter = 2.85mm

; __GENERATED__

M190 S60
M104 S200
M109 S200
G21        ;metric values
G90        ;absolute positioning
M82        ;set extruder to absolute mode
M107       ;start with the fan off
G28 X0 Y0  ;move X/Y to min endstops
G28 Z0     ;move Z to min endstops
G1 Z15.0 F9000 ;move the platform down 15mm
G92 E0                  ;zero the extruded length
G1 F200 E3              ;extrude 3mm of feed stock
G92 E0                  ;zero the extruded length again
G1 F9000
M117 Building...
; Stranger Things
; layer 1, Z = 0.28
; perimeters for 15 loops
G1 X80.66Y68.77 F9000
G1 X80.24Y68.79 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X79.54Y68.53 E0.1887 F9000
; inner perimeter
G1 X74.57Y67.28 E0.2833 F9000
; infill for 15 loops
G1 X66.06Y63.25 E0.4051 F9000
G1 X65.64Y63.27 E0.4138 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X48.73Y63.13 E0.5562 F9000
; inner perimeter
G1 X73.20Y64.31 E0.6166 F9000
; infill for 5 loops
G1 X80.91Y66.23 E0.6526 F9000
G1 X81.33Y66.21 E0.6555 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X73.53Y53.43 E0.7602 F9000
; inner perimeter
G1 X48.13Y54.38 E0.8078 F9000
; infill for 3 loops
G1 X73.07Y55.91 E0.8360 F9000
G1 X73.49Y55.89 E0.8400 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X83.67Y50.57 E0.8610 F9000
; inner perimeter
G1 X97.34Y61.10 E0.9099 F9000
; infill for 1 loops
G1 X 98.21Y61.50 E0.9147 F9000
G1 X 98.63Y61.48 E0.9172 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X83.97Y37.39 E0.9377 F9000
; inner perimeter
G1 X67.17Y46.57 E0.9811 F9000
; infill for 2 loops
G1 X76.95Y48.88 E1.0057 F9000
G1 X77.37Y48.86 E1.0079 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X110.17Y63.34 E1.0284 F9000
; inner perimeter
G1 X128.89Y51.86 E1.0794 F9000
; infill for 1 loops
G1 X 129.76Y52.26 E1.0844 F9000
G1 X 130.18Y52.24 E1.0867 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X110.47Y50.12 E1.0942 F9000
; inner perimeter
G1 X129.19Y38.76 E1.1460 F9000
; infill for 15 loops
G1 X132.56Y36.39 E1.1651 F9000
G1 X133.10Y36.37 E1.1678 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X111.77Y37.01 E1.2242 F9000
; inner perimeter
G1 X136.55Y38.59 E1.2727 F9000
; infill for 5 loops
G1 X143.03Y40.92 E1.3046 F9000
G1 X143.53Y40.90 E1.3073 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X103.09Y29.84 E1.358 F9000
; inner perimeter
G1 X140.59Y34.67 E1.4130 F9000
; infill for 3 loops
G1 X146.85Y37.16 E1.4345 F9000
G1 X147.37Y37.14 E1.4372 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X173.31Y51.88 E1.4480 F9000
; inner perimeter
G1 X155.75Y40.60 E1.4955 F9000
; infill for 1 loops
G1 X 156.64Y41.02 E1.5007 F9000
G1 X 157.08Y41.00 E1.5031 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X190.60Y36.49 E1.5105 F9000
; inner perimeter
G1 X172.07Y25.27 E1.5585 F9000
; infill for 2 loops
G1 X181.83Y23.04 E1.5804 F9000
G1 X182.38Y23.02 E1.5832 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X161.60Y81.64 E1.5911 F9000
; inner perimeter
G1 X183.24Y93.45 E1.6417 F9000
; infill for 1 loops
G1 X 184.14Y93.89 E1.6470 F9000
G1 X 184.61Y93.88 E1.6498 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X165.31Y64.44 E1.6546 F9000
; inner perimeter
G1 X188.34Y81.17 E1.7062 F9000
; infill for 15 loops
G1 X193.98Y84.41 E1.7270 F9000
G1 X194.70Y84.37 E1.7297 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X166.61Y51.26 E1.7853 F9000
; inner perimeter
G1 X192.85Y67.40 E1.8361 F9000
; infill for 5 loops
G1 X200.21Y71.41 E1.8704 F9000
G1 X200.91Y71.37 E1.8735 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X157.37Y44.39 E1.9157 F9000
; inner perimeter
G1 X196.56Y60.72 E1.9711 F9000
; infill for 3 loops
G1 X204.50Y65.98 E1.9957 F9000
G1 X205.21Y65.95 E2.0000 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X213.60Y41.04 E2.005 F9000
; inner perimeter
G1 X196.05Y29.44 E2.0554 F9000
; infill for 1 loops
G1 X 196.97Y29.85 E2.0608 F9000
G1 X 197.50Y29.84 E2.0636 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X213.87Y18.23 E2.0697 F9000
; inner perimeter
G1 X196.36Y6.76 E2.1191 F9000
; infill for 2 loops
G1 X206.10Y4.65 E2.1419 F9000
G1 X206.68Y4.63 E2.1449 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X92.55Y52.98 E2.1463 F9000
; inner perimeter
G1 X74.16Y64.66 E2.1964 F9000
; infill for 1 loops
G1 X 74.97Y65.10 E2.2019 F9000
G1 X 75.41Y65.11 E2.2044 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X58.03Y36.70 E2.2111 F9000
; inner perimeter
G1 X74.96Y20.91 E2.2613 F9000
; infill for 15 loops
G1 X86.23Y16.21 E2.2968 F9000
G1 X87.39Y16.17 E2.3007 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X60.41Y23.58 E2.3596 F9000
; inner perimeter
G1 X74.94Y38.23 E2.4106 F9000
; infill for 5 loops
G1 X83.22Y45.46 E2.4485 F9000
G1 X84.12Y45.41 E2.4532 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X82.90Y85.03 E2.4590 F9000
; inner perimeter
G1 X66.14Y98.12 E2.5102 F9000
; infill for 3 loops
G1 X76.50Y103.82 E2.5352 F9000
G1 X77.44Y103.78 E2.5401 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X152.33Y42.56 E2.5480 F9000
; inner perimeter
G1 X134.77Y56.06 E2.6014 F9000
; infill for 1 loops
G1 X 135.71Y56.53 E2.6070 F9000
G1 X136.28Y56.52 E2.6101 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X152.64Y29.36 E2.6158 F9000
; inner perimeter
G1 X135.16Y15.02 E2.6661 F9000
; infill for 2 loops
G1 X145.81Y12.00 E2.6890 F9000
G1 X146.46Y11.99 E2.6923 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X171.06Y24.88 E2.6933 F9000
; inner perimeter
G1 X152.40Y40.36 E2.7428 F9000
; infill for 1 loops
G1 X 153.34Y40.86 E2.7484 F9000
G1 X 153.85Y40.85 E2.7516 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X170.79Y10.46 E2.7554 F9000
; inner perimeter
G1 X152.20Y-2.25 E2.8048 F9000
; infill for 1 loops
G1 X 152.98Y-1.81 E2.8102 F9000
G1 X 153.40Y-1.82 E2.8125 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X189.38Y35.61 E2.815 F9000
; inner perimeter
G1 X170.77Y50.86 E2.8662 F9000
; infill for 15 loops
G1 X178.42Y56.70 E2.8929 F9000
G1 X179.46Y56.67 E2.8970 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X171.10Y37.66 E2.9524 F9000
; inner perimeter
G1 X195.44Y54.23 E3.0046 F9000
; infill for 5 loops
G1 X203.75Y58.42 E3.0406 F9000
G1 X204.71Y58.40 E3.0457 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X114.14Y-31.28 E3.0493 F9000
; inner perimeter
G1 X194.07Y-17.40 E3.1019 F9000
; infill for 3 loops
G1 X204.96Y-11.43 E3.1292 F9000
G1 X205.85Y-11.39 E3.1345 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X236.77Y17.69 E3.1362 F9000
; inner perimeter
G1 X217.16Y33.13 E3.1867 F9000
; infill for 1 loops
G1 X 218.10Y33.64 E3.1924 F9000
G1 X 218.65Y33.64 E3.1954 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X236.50Y4.57 E3.1988 F9000
; inner perimeter
G1 X217.18Y-10.89 E3.2484 F9000
; infill for 2 loops
G1 X227.93Y-13.72 E3.2727 F9000
G1 X228.56Y-13.72 E3.2764 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X180.94Y-61.60 E3.2772 F9000
; inner perimeter
G1 X165.48Y-76.29 E3.3288 F9000
; infill for 1 loops
G1 X 166.42Y-76.76 E3.3345 F9000
G1 X 166.98Y-76.77 E3.3377 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X63.71Y-42.46 E3.3399 F9000
; inner perimeter
G1 X44.0E-1Y-31.75 E3.3904 F9000
; infill for 1 loops
G1 X 44.98Y-31.40 E3.3959 F9000
G1 X 45.51Y-31.40 E3.3986 F9000
G1 E0.0000 F2400.0000
G92 E0
G1 F900
G1 X7.63Y-0.17E-5 E3.3986 F9000
; inner perimeter
G1 X26.23Y-11.59 E3.4492 F9000
