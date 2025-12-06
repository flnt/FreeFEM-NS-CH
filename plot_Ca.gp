set yr [0:5]
set xr [0:20]
set size ratio 1

plot 'test1/stats.txt' u 1:($2-1.75) w l lw 2 t 'Ca = 0.15',\
    'test2/stats.txt' u 1:($2-1.75) w l lw 2 t 'Ca = 0.20',\
    'test3/stats.txt' u 1:($2-1.75) w l lw 2 t 'Ca = 0.25',\
    'test4/stats.txt' u 1:($2-1.75) w l lw 2 t 'Ca = 0.30',\
    'test5/stats.txt' u 1:($2-1.75) w l lw 2 t 'Ca = 0.35',\
    'test6/stats.txt' u 1:($2-1.75) w l lw 2 t 'Ca = 0.40',\
    'test7/stats.txt' u 1:($2-1.75) w l lw 2 t 'Ca = 0.45',\
    'test8/stats.txt' u 1:($2-1.75) w l lw 2 t 'Ca = 0.50'
    
pause -1