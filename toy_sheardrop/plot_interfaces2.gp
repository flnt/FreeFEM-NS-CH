set key bottom right
set xlabel 'x'
set ylabel 'y'

plot 'interface_Pe30_Cn0.02.txt' u 1:2 w lp lt 1 pt 6 ps 2 title 'Pe = 30, Cn = 0.02',\
    'interface_Pe30_Cn0.04.txt' u 1:2 w lp lt 1 pt 8 ps 2 title 'Pe = 30, Cn = 0.04',\
    'interface_Pe100_Cn0.01.txt' u 1:2 w lp lt 2 pt 4 ps 2 title 'Pe = 100, Cn = 0.01',\
    'interface_Pe100_Cn0.02.txt' u 1:2 w lp lt 2 pt 6 ps 2 title 'Pe = 100, Cn = 0.02',\
    'interface_Pe160_Cn0.02.txt' u 1:2 w lp lt 3 pt 6 ps 2 title 'Pe = 160, Cn = 0.02',\
    'interface_Pe160_Cn0.04.txt' u 1:2 w lp lt 3 pt 8 ps 2 title 'Pe = 160, Cn = 0.04',\
    'interface_Pe300_Cn0.01.txt' u 1:2 w lp lt 4 pt 4 ps 2 title 'Pe = 300, Cn = 0.01',\
    'interface_Pe300_Cn0.02.txt' u 1:2 w lp lt 4 pt 6 ps 2 title 'Pe = 300, Cn = 0.02',\
    'interface_Pe300_Cn0.04.txt' u 1:2 w lp lt 4 pt 8 ps 2 title 'Pe = 300, Cn = 0.04'

pause -1

set key top center
set xlabel 'y'
set ylabel 'curvature'

plot 'interface_Pe30_Cn0.02.txt' u 2:3 w lp lt 1 pt 6 ps 2 title 'Pe = 30, Cn = 0.02',\
    'interface_Pe30_Cn0.04.txt' u 2:3 w lp lt 1 pt 8 ps 2 title 'Pe = 30, Cn = 0.04',\
    'interface_Pe100_Cn0.01.txt' u 2:3 w lp lt 2 pt 4 ps 2 title 'Pe = 100, Cn = 0.01',\
    'interface_Pe100_Cn0.02.txt' u 2:3 w lp lt 2 pt 6 ps 2 title 'Pe = 100, Cn = 0.02',\
    'interface_Pe160_Cn0.02.txt' u 2:3 w lp lt 3 pt 6 ps 2 title 'Pe = 160, Cn = 0.02',\
    'interface_Pe160_Cn0.04.txt' u 2:3 w lp lt 3 pt 8 ps 2 title 'Pe = 160, Cn = 0.04',\
    'interface_Pe300_Cn0.01.txt' u 2:3 w lp lt 4 pt 4 ps 2 title 'Pe = 300, Cn = 0.01',\
    'interface_Pe300_Cn0.02.txt' u 2:3 w lp lt 4 pt 6 ps 2 title 'Pe = 300, Cn = 0.02',\
    'interface_Pe300_Cn0.04.txt' u 2:3 w lp lt 4 pt 8 ps 2 title 'Pe = 300, Cn = 0.04'

pause -1