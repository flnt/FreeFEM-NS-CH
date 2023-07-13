
plot 'interfaces_0.tsv' u 2:3 w p lt 1 pt 4 ps 2 title 'Pe = 30, Cn = 0.01',\
    'interfaces_1.tsv' u 2:3 w p lt 1 pt 6 ps 2 title 'Pe = 30, Cn = 0.02',\
    'interfaces_2.tsv' u 2:3 w p lt 1 pt 8 ps 2 title 'Pe = 30, Cn = 0.04',\
    'interfaces_3.tsv' u 2:3 w p lt 2 pt 4 ps 2 title 'Pe = 100, Cn = 0.01',\
    'interfaces_4.tsv' u 2:3 w p lt 2 pt 6 ps 2 title 'Pe = 100, Cn = 0.02',\
    'interfaces_5.tsv' u 2:3 w p lt 2 pt 8 ps 2 title 'Pe = 100, Cn = 0.04',\
    'interfaces_6.tsv' u 2:3 w p lt 3 pt 6 ps 2 title 'Pe = 160, Cn = 0.02',\
    'interfaces_7.tsv' u 2:3 w p lt 3 pt 8 ps 2 title 'Pe = 160, Cn = 0.04',\
    'interfaces_8.tsv' u 2:3 w p lt 4 pt 4 ps 2 title 'Pe = 300, Cn = 0.01',\
    'interfaces_9.tsv' u 2:3 w p lt 4 pt 6 ps 2 title 'Pe = 300, Cn = 0.02',\
    'interfaces_10.tsv' u 2:3 w p lt 4 pt 8 ps 2 title 'Pe = 300, Cn = 0.04'

pause -1


set yr [-0.5:0.0]
set xr [-0.8:-0.3]

replot

pause -1

