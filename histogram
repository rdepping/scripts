#!/bin/sh
# -----------------------------------------------------------------------
#
# histogram --- Create ASCII histogram from log data.
# Jim Lawton, S3, April 25 2006.
#
# Requires: a sh-compatible shell and GNU Awk.
#
# Syntax: histogram logfile
#
# Assumes that the data you're analysing is integral. 
# It should be easy to support floating as well. 
#
# -----------------------------------------------------------------------

# Modify this line to change the regex used to extract the data.
SEARCH="([0-9]+)"

# The -g command-line option generates gnuplot command files to 
# make nice plots of the data.
gnuplot=0
if [ "$1" = "-g" ]; then
    gnuplot=1
    shift
fi

if [ "$1" = "" ]; then
    echo "Please supply a log file name." 1>&2
    exit 1
fi

if [ ! -f "$1" ]; then
        echo "File \"$1\" does not exist." 1>&2
    exit 1
fi

filename="$1"

cat $filename | \
    gawk 'match($0,"'$SEARCH'") {print substr($0,RSTART,RLENGTH)}' | \
    gawk -F= '{print $1}' | sort -n | \
    gawk '

function round(x) {
    intval = int(x);
    
    if (intval == x)
        return x;
    
    if (x < 0) {
        absval = -x;
        intval = int(absval);
        frac = absval - intval;
        if (frac >= .5)
            return int(x) - 1;   # -2.5 --> -3
        else
            return int(x);       # -2.3 --> -2
    } else {
        frac = x - intval;
        if (frac >= .5)
            return intval + 1;
        else
            return intval;
    }
}

BEGIN {
    columns = 60;
    num_bins = 10;
    sum = 0;
    mean = 0.0;
    mode = 0.0;
    stdev = 0.0;
    gnuplot = '"$gnuplot"';
}

{
    data[NR] = $1;
    sum += $1;
}

END {
    minval = data[1];
    maxval = data[NR];
    mean = sum / NR;
    
    printf("Count:     %11d\n", NR);
    printf("Min value: %11d\n", minval);
    printf("Max value: %11d\n", maxval);

    bin_width = (maxval - minval) / (num_bins - 1);
    bin_top  = minval + bin_width;
    bin_index = 0;

    printf("Bin width: %11.2f\n", bin_width);
        
    for (i=0; i<num_bins; i++) {
        bins[i] = 0;
    }

    for (i=1; i<=NR; i++) {
        while (data[i] >= bin_top) { 
            bin_index++;
            bin_top = minval + bin_width * (1 + bin_index);
        }
        bins[bin_index]++;
    }

    max_count = 0;
    for (i=0; i<num_bins; i++) {
        if (bins[i] > max_count) {
            max_count = bins[i];
            mode = minval + (bin_width * i);
        }
    }

    printf("Mean:      %11.2f\n", mean);
    printf("Mode:      %11.2f\n", mode);

    printf("Bin size:  %11.2f\n\n", bin_width);

    if (max_count <= columns) 
        scale = 1.0; 
    else 
        scale = columns / max_count;

    bin_label = minval;
    for (i=0; i<num_bins; i++) {
        printf("%11.2f %6d ", bin_label, bins[i]);
        num_stars = round(scale * bins[i]);
        for (j=0; j<num_stars; j++) 
            printf("*"); 
        printf("\n"); 
        bin_label += bin_width;
    }

    if (gnuplot == 1) {
        printf("Generating GNUplot command file...\n");
    }
}
'
