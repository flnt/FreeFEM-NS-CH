set xlabel 'x
set ylabel 'y_{CL}'

set xr [0:20]
set yr [0:5]
set size ratio 1
#set yr [0:0.266]

plot 'test6/stats.txt' u 1:($2-3.5) w l lw 2 t 'Ca = 0.10 slip = 0.05 Pe = 100 muf = 2.0',\
    'test7/stats.txt' u 1:($2-3.5) w l lw 2 t 'Ca = 0.10 slip = 0.05 Pe = 10 muf = 2.0',\
    'test8/stats.txt' u 1:($2-3.5) w l lw 2 t 'Ca = 0.10 slip = 0.05 Pe = 1 muf = 2.0',\
    '/home/tf/Downloads/PLOTS_FINALE_corrected_GNBC0_SLIP1/PLOTS_FINALE_corrected_GNBC0_SLIP1/GNBC0_SLIP1_Ca0.1_LEVEL10_eps0.05_angle90' u 1:2 w l lw 2 dt 2

pause -1

#    '~/Downloads/to_Yash_PhaseField/test4/stats.txt' u 1:($2-1.75) w l lw 2 dt 2 t 'Ca = 0.3 L = 3, Pe = 1 (Old sim)',\
#    '~/Downloads/to_Yash_PhaseField/test1/stats.txt' u 1:($2-1.75) w l lw 2 dt 2 t 'Ca = 0.1 L = 3, Pe = 1 (Old sim)'

#'test1/stats.txt' u 1:($2-3.5) w l lw 2 t 'Ca = 0.14 slip = 0.05 Pe = 10',\
#'test2/stats.txt' u 1:($2-3.5) w l lw 2 t 'Ca = 0.14 slip = 0.05 Pe = 100',\
#'test3/stats.txt' u 1:($2-3.5) w l lw 2 t 'Ca = 0.14 slip = 0.05 Pe = 1000',\
#'test4/stats.txt' u 1:($2-3.5) w l lw 2 t 'Ca = 0.10 slip = 0.05 Pe = 10',\
#'test5/stats.txt' u 1:($2-3.5) w l lw 2 t 'Ca = 0.04 slip = 0.05 Pe = 10',\

#'/home/tf/Downloads/PLOTS_FINALE_corrected_GNBC0_SLIP1/PLOTS_FINALE_corrected_GNBC0_SLIP1/GNBC0_SLIP1_Ca0.14_LEVEL10_eps0.05_angle90' u 1:2 w l lw 2 dt 2,\
#'/home/tf/Downloads/PLOTS_FINALE_corrected_GNBC0_SLIP1/PLOTS_FINALE_corrected_GNBC0_SLIP1/GNBC0_SLIP1_Ca0.04_LEVEL10_eps0.05_angle90' u 1:2 w l lw 2 dt 2,\
,\
#    'test5/stats.txt' u 1:($2-3.5) w l lw 2 dt 2 t 'Ca = 0.05 dt*10',\
#    'test6/stats.txt' u 1:($2-3.5) w l lw 2 dt 2 t 'Ca = 0.10 dt*10',\
#    'test7/stats.txt' u 1:($2-3.5) w l lw 2 dt 2 t 'Ca = 0.15 dt*10',\
#    'test8/stats.txt' u 1:($2-3.5) w l lw 2 dt 2 t 'Ca = 0.20 dt*10'


