set term pngcairo fontscale 2.25 size 1080, 1080

set xlabel "y"
set ylabel "Angle (degrees)"
set yr [80:92]
set size ratio 1

set output 'angles_Pe30_Cn0.02.png'

plot 'angles_Pe30_Cn0.02.txt' u 1:2 w p ps 2 pt 3 lt rgb 'black' notitle,\
    'angles_Pe30_Cn0.02_VOF' u 1:2 w l lw 3 lt rgb 'red' notitle

unset ylabel
set output 'angles_Pe30_Cn0.04.png'

plot 'angles_Pe30_Cn0.04.txt' u 1:2 w p ps 2 pt 3 lt rgb 'black' notitle,\
    'angles_Pe30_Cn0.04_VOF' u 1:2 w l lw 3 lt rgb 'red' notitle


set output 'angles_Pe100_Cn0.02.png'

plot 'angles_Pe100_Cn0.02.txt' u 1:2 w p ps 2 pt 3 lt rgb 'black' notitle,\
    'angles_Pe100_Cn0.02_VOF' u 1:2 w l lw 3 lt rgb 'red' notitle


set ylabel "Angle (degrees)"
set output 'angles_Pe160_Cn0.04.png'

plot 'angles_Pe160_Cn0.04.txt' u 1:2 w p ps 2 pt 3 lt rgb 'black' notitle,\
    'angles_Pe160_Cn0.04_VOF' u 1:2 w l lw 3 lt rgb 'red' notitle

unset ylabel
set output 'angles_Pe300_Cn0.02.png'

plot 'angles_Pe300_Cn0.02.txt' u 1:2 w p ps 2 pt 3 lt rgb 'black' notitle,\
    'angles_Pe300_Cn0.02_VOF' u 1:2 w l lw 3 lt rgb 'red' notitle


set output 'angles_Pe300_Cn0.04.png'

plot 'angles_Pe300_Cn0.04.txt' u 1:2 w p ps 2 pt 3 lt rgb 'black' notitle,\
    'angles_Pe300_Cn0.04_VOF' u 1:2 w l lw 3 lt rgb 'red' notitle
