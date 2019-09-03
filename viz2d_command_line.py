#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

warnings.filterwarnings('ignore')

__tool_name__='STREAM'
print('''
   _____ _______ _____  ______          __  __ 
  / ____|__   __|  __ \|  ____|   /\   |  \/  |
 | (___    | |  | |__) | |__     /  \  | \  / |
  \___ \   | |  |  _  /|  __|   / /\ \ | |\/| |
  ____) |  | |  | | \ \| |____ / ____ \| |  | |
 |_____/   |_|  |_|  \_\______/_/    \_\_|  |_|
... Validation                                               
''',flush=True)

import stream as st
import argparse
import multiprocessing
import os
from slugify import slugify
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import sys

mpl.use('Agg')
mpl.rc('pdf', fonttype=42)

os.environ['KMP_DUPLICATE_LIB_OK']='True'


print('- STREAM Single-cell Trajectory Reconstruction And Mapping -',flush=True)
print('Version %s\n' % st.__version__,flush=True)
    

def main():
    sns.set_style('white')
    sns.set_context('poster')
    parser = argparse.ArgumentParser(description='%s Parameters' % __tool_name__ ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--data-file", dest="input_filename",default = None, help="input file name, pkl format from Stream preprocessing module", metavar="FILE")
    parser.add_argument("-of","--of",dest="output_filename_prefix", default="StreamiFSOutput",  help="output file name prefix")

    parser.add_argument("-fig_name",dest="fig_name",  default=None, help="")
    parser.add_argument("--flag_useprecomputed",dest="flag_useprecomputed", action="store_true", help="Save the figure")

    parser.add_argument("-nb_pct","--percent_neighbor_cells",dest="nb_pct", type=float, default=None, help="")
    parser.add_argument("-n_comp_k",dest="n_comp_k", type = int, default=None,  help="")
    parser.add_argument("-perplexity",dest="perplexity", default=None,   help="feature")

    parser.add_argument("-method",dest="method",  default=None,  help="")
    parser.add_argument("-color_by",dest="color_by",  default='label',  help="")
    parser.add_argument("-fig_width",dest="fig_width", type=int, default=8, help="")        
    parser.add_argument("-fig_height",dest="fig_height", type=int, default=8, help="")

    parser.add_argument("-fig_legend_ncol",dest="fig_legend_ncol", type=int, default=None, help="")                                   


    args = parser.parse_args()
    
    print('Starting validation procedure...')
    workdir = "./"

    adata = st.read(file_name=args.input_filename, file_format='pkl', experiment='rna-seq', workdir=workdir)

    st.plot_visualization_2D(adata, method=args.method, nb_pct=args.nb_pct, perplexity=args.perplexity, color_by=args.color_by,use_precomputed=args.flag_useprecomputed, save_fig=True, fig_path='./', fig_name=args.fig_name, fig_size=(args.fig_width,args.fig_height ),fig_legend_ncol=args.fig_legend_ncol)

    st.write(adata,file_name=(args.output_filename_prefix + '_stream_result.pkl'),file_path='./',file_format='pkl') 

    print('Finished computation.')

if __name__ == "__main__":
    main()
