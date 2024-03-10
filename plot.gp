set xlabel "angle"
set ylabel "intensity"
set datafile separator tab
plot "data.csv" using 1:2 w l 