set datafile separator ","

unset key
set grid

set xlabel "Time (s)" font "Helvetica,14"
set ylabel "Voltage (V)" font "Helvetica,14"
set xtics font "Helvetica,14"
set ytics font "Helvetica,14"

plot \
"sine_100_Hz.csv" u 1:2 w l lw 1 lc rgb 'blue',\
"sine_100_Hz.csv" u 1:3 w l lw 1 lc rgb 'red',\
"< cat sine_100_Hz.csv | tail -n +3 | awk '{if ((NR%40) == 0) print}'" u 1:3 w p pt 7 lc rgb 'black'

pause -1

delay = 0.0006
plot \
"sine_100_Hz.csv" u 1:2 w l lw 1 lc rgb 'blue',\
"sine_100_Hz.csv" u 1:3 w l lw 1 lc rgb 'red',\
"< cat sine_100_Hz.csv | tail -n +3 | awk '{if ((NR%40) == 0) print}'" u ($1-delay):3 w p pt 7 lc rgb 'black'

pause -1


T = 0.001

# Generate r(t) function via shell command (function is written to file "r_of_t.gp")
`cat sine_100_Hz.csv | tail -n +3 |
awk '
BEGIN
{firstDone=0;
print "r(t) = \\"} 
{if ((NR%40) == 0) 
	{if(firstDone) 
		print " + \\";
		split($0,a,",");
		printf("%f * k(t%s%f)", a[3], ((a[1]<0)? "+" : "") ,-a[1]);	
		firstDone=1
	}
} 
END{printf("\n")}' > r_of_t.gp`
load("r_of_t.gp")


# Linear kernel
tAbs(t) = (t < 0)? -t : t
k(t) = (tAbs(t) < T)? (1 - tAbs(t)/T) : 0

plot \
"sine_100_Hz.csv" u ($1 + delay):2 w l lc rgb 'blue',\
r(x) w l lc rgb 'red'

pause -1


# Sinc kernel
sinc(x) = (x == 0)? 1 : sin(x) / x
k(t) = sinc(pi*t/T)

plot \
"sine_100_Hz.csv" u ($1 + delay):2 w l lc rgb 'blue',\
r(x) w l lc rgb 'red'

pause -1
