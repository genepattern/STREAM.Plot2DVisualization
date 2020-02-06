# python /stream/viz2d_command_line.py -m <data.file> -of <output.filename> <percent.neighbor.cells> <perplexity> <color.by>  <method> <use.precomputed> <figure.width> <figure.height> <figure.legend.num.columns> 

docker run  -v ${PWD}:$PWD -w $PWD/job_1 genepattern/plot2dvisualization python /stream/viz2d_command_line.py -m $PWD/test/data/stream_epg_result.pkl -of val_ -nb_pct 0.1 -color_by 'branch' -perplexity 30   -fig_width 10 -fig_height 7 -fig_legend_ncol 3
