set term cairolatex size 3in,3in standalone header '\usepackage{amsmath} \usepackage{nicefrac}'

set xlabel "y"
set ylabel "Angle (degrees)"
set yr [79:91]
set xr [-0.5:0.5]

set xtics -0.5,0.5,0.5
set ytics 80,2,90

set size ratio 1

set output '512angles_Pe30_Cn0.02.tex'

plot 'angles_Pe30_Cn0.02.txt' u 1:2 w p ps 0.4 pt 3 lt rgb 'black' notitle,\
    'angles_Pe30_Cn0.02_VOF512' u 1:2 w l lw 2 lt rgb 'red' notitle

set output 'angles_Pe30_Cn0.02.tex'

plot 'angles_Pe30_Cn0.02.txt' u 1:2 w p ps 0.4 pt 3 lt rgb 'black' notitle,\
    'angles_Pe30_Cn0.02_VOF' u 1:2 w l lw 2 lt rgb 'red' notitle


set output 'angles_Pe30_Cn0.04.tex'

plot 'angles_Pe30_Cn0.04.txt' u 1:2 w p ps 0.4 pt 3 lt rgb 'black' notitle,\
    'angles_Pe30_Cn0.04_VOF' u 1:2 w l lw 2 lt rgb 'red' notitle


set output 'angles_Pe100_Cn0.02.tex'

plot 'angles_Pe100_Cn0.02.txt' u 1:2 w p ps 0.4 pt 3 lt rgb 'black' notitle,\
    'angles_Pe100_Cn0.02_VOF' u 1:2 w l lw 2 lt rgb 'red' notitle


set ylabel "Angle (degrees)"
set output 'angles_Pe160_Cn0.04.tex'

plot 'angles_Pe160_Cn0.04.txt' u 1:2 w p ps 0.4 pt 3 lt rgb 'black' notitle,\
    'angles_Pe160_Cn0.04_VOF' u 1:2 w l lw 2 lt rgb 'red' notitle


set output 'angles_Pe300_Cn0.02.tex'

plot 'angles_Pe300_Cn0.02.txt' u 1:2 w p ps 0.4 pt 3 lt rgb 'black' notitle,\
    'angles_Pe300_Cn0.02_VOF' u 1:2 w p ps 0.4 pt 3 lt rgb 'red' notitle


set output 'angles_Pe300_Cn0.04.tex'

plot 'angles_Pe300_Cn0.04.txt' u 1:2 w p ps 0.4 pt 3 lt rgb 'black' notitle,\
    'angles_Pe300_Cn0.04_VOF' u 1:2 w l lw 2 lt rgb 'red' notitle
