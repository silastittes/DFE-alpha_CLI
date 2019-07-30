#!/usr/bin/env python3

#A complete cli to interact with all three programs of dfe-alpha

import argparse
import os
import sys 
parser = argparse.ArgumentParser(prog='PROG')
subparsers = parser.add_subparsers()

#############!!!!!!!!!!!!!
## est_dfe ##!!!!!!!!!!!!!
#############!!!!!!!!!!!!!

parser_est_dfe = subparsers.add_parser('est_dfe', help='wrapper for est_dfe command.')

parser_est_dfe.set_defaults(mode='est_dfe')

parser_est_dfe.add_argument('--data_path_1', type=str, help='Name of directory containing the data files for the 1 and 2 epoch models. If absent, default directory specified in directory_config.dat is used.')

parser_est_dfe.add_argument('--data_path_2', type=str, help = "Name of directory containing the data files for the 3 epoch model. Must be different from data_path_1. If absent, default directory specified in directory_config_three_epoch.dat is used.")

parser_est_dfe.add_argument('--sfs_input_file', type = str, help = "File containing the site frequency spectra read by the program for analysis. DEFAULT = sfs.txt")

parser_est_dfe.add_argument('--est_dfe_results_dir', type = str, help = "Name of directory to which est_dfe results files are written. If absent, current directory is written to.")

parser_est_dfe.add_argument('--est_dfe_demography_results_file', type = str, help = "File containing results of previous run of est_dfe. The demographic parameters are read in from this file by the program, and assumed as fixed. Applies only to the case of site_class = 1. REQUIRED if site_class = 1.")

parser_est_dfe.add_argument('--fold', type = str, help = "Fold the SFS [1] or not [0].", required=True)

parser_est_dfe.add_argument('--epochs', type = str, help = "Number of population size changes +1. (1, 2, 3)", required=True)

parser_est_dfe.add_argument('--site_class', type = str, help = "0 = analyse neutral SFS only, 1 = analyse selected SFS only, 2 = analyse neutral and selected SFSs simultaneously. Option 2 is not allowed if fold = 0 or epochs = 3.", required=True)

parser_est_dfe.add_argument('--search_n2', type = str, help = "Search for the best-fitting population size n2 in 2-epoch model (0,1).")

parser_est_dfe.add_argument('--n2', type = str, help = "Population size after first change in population size. REQUIRED if epochs = 2 and search_n2 = 0.")

parser_est_dfe.add_argument('--t2_variable', type = str, help = "t2 is variable [1] or not [0] in likelihood maximization. REQUIRED if epochs = 2 or 3.")

parser_est_dfe.add_argument('--t2', type = str, help = "Duration of epoch after first population size change (an initial or fixed value). REQUIRED if epochs = 2 or 3.")

parser_est_dfe.add_argument('--mean_s_variable', type = str, help = "Mean effect of a deleterious mutation is variable [1] or not [0] in likelihood maximization. REQUIRED if site_class = 1 or 2.")

parser_est_dfe.add_argument('--mean_s', type = float, help = "Mean effect of a deleterious mutation (an initial or fixed value). (< 0). REQUIRED if site_class = 1 or 2.")

parser_est_dfe.add_argument('--beta_variable', type = str, help = "hape parameter of gamma distribution is variable [1] or not [0] in likelihood maximization. REQUIRED if site_class = 1 or 2.")

parser_est_dfe.add_argument('--beta', type = str, help = "Shape parameter of gamma distribution (an initial or fixed value); The value -99 specified the equal effects model (a fixed value). REQUIRED if site_class = 1 or 2.")

parser_est_dfe.add_argument('--p_additional', type = str, help = "Proportion of mutations in fixed class 1. Only applies if fold = 0. REQUIRED if site_class = 1 and fold = 0.")

parser_est_dfe.add_argument('--s_additional', type = str, help = "Proportion of mutations in fixed class 1. Only applies if fold = 0. REQUIRED if site_class = 1 and fold = 0.")

parser_est_dfe.add_argument("est_dfe_config_file", type = str, help = "The name of the config file to pass to est_dfe command.")



#####################!!!!!!!!!!!!!!!!
## est_alpha_omega ##!!!!!!!!!!!!!!!!
#####################!!!!!!!!!!!!!!!!

parser_est_alpha_omega = subparsers.add_parser('est_alpha_omega', help='Wrapper for est_alpha_omega command.')

parser_est_alpha_omega.set_defaults(mode='est_alpha_omega')

parser_est_alpha_omega.add_argument('--data_path_1', type=str, help='Name of directory containing the data files for the 1 and 2 epoch models. If absent, default directory specified in directory_config.dat is used.')

parser_est_alpha_omega.add_argument("--divergence_file", type = str, help = "Input file containing numbers of nucleotide differences and sites. If absent default file is used. DEFAULT = divergence.txt.")

parser_est_alpha_omega.add_argument("--est_alpha_omega_results_file", type = str, help = "Output file from the program. If absent default file is used. DEFAULT = est_alpha_omega.out")

parser_est_alpha_omega.add_argument("--est_dfe_results_file", type = str, help = "Results file produced by est_dfe, which is read by est_alpha_omega. If absent, default file is used. DEFAULT = est_dfe.out")

parser_est_alpha_omega.add_argument("--neut_egf_file", type = str, help = "File containing the neutral gene frequency vector produced by est_dfe, which is read by est_alpha_omega. If absent, default file is used. DEFAULT = neut_egf.out")

parser_est_alpha_omega.add_argument("--sel_egf_file", type = str, help = "File containing the selected gene frequency vector produced by est_dfe, which is read by est_alpha_omega. If absent, default file is used. DEFAULT = sel_egf.out")

parser_est_alpha_omega.add_argument("--do_jukes_cantor", type = int, help = "Carry out Jukes-Cantor correction [1] or not [0] when calculating nucleotide divergence.", required = True)

parser_est_alpha_omega.add_argument("--remove_poly", type = int, help = "Remove polymorphism contributing to divergence [1] or not [0] when estimating alpha and omega_a.", required = True)

parser_est_alpha_omega.add_argument("est_alpha_omega_config_file", type = str, help = "The name of the config file to pass to est_alpha_omega command.")


###########################!!!!!!!!!!!!!!!!!!
## prop_muts_in_s_ranges ##!!!!!!!!!!!!!!!!!!
###########################!!!!!!!!!!!!!!!!!!

parser_prop_muts_in_s_ranges = subparsers.add_parser('prop_muts_in_s_ranges', help='Wrapper for prop_muts_in_s_ranges command.')

parser_prop_muts_in_s_ranges.set_defaults(mode='prop_muts_in_s_ranges')

parser_prop_muts_in_s_ranges.add_argument('--est_dfe_output_file', type = str, help = "Main results file produced by est_dfe. DEFAULT = est_dfe.out.", default = "est_dfe.out")

parser_prop_muts_in_s_ranges.add_argument('--output_file', type = str, help = "Name fo file to write output to. DEFAULT = prop_muts_in_s_ranges.out", default = "prop_muts_in_s_ranges.out")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
argsDict = vars(args)

#############!!!!!!!!!!!!!
## est_dfe ##!!!!!!!!!!!!!
#############!!!!!!!!!!!!!

if argsDict['mode'] == "est_dfe":
    with open(args.est_dfe_config_file, "a") as config:
        for arg in vars(args):
            if getattr(args, arg) and arg != "est_dfe_config_file":
                print(arg, getattr(args, arg), file = config)

    os.system("est_dfe -c {}".format(args.est_dfe_config_file))


#####################!!!!!!!!!!!!!!!!
## est_alpha_omega ##!!!!!!!!!!!!!!!!
#####################!!!!!!!!!!!!!!!!

if argsDict['mode'] == "est_alpha_omega":
    with open(args.est_alpha_omega_config_file, "a") as config:
        for arg in vars(args):
            if getattr(args, arg) and arg != "est_alpha_omega_config_file":
                print(arg, getattr(args, arg), file = config)
    
    os.system("est_alpha_omega -c {}".format(args.est_alpha_omega_config_file))

###########################!!!!!!!!!!!!!!!!!!
## prop_muts_in_s_ranges ##!!!!!!!!!!!!!!!!!!
###########################!!!!!!!!!!!!!!!!!!

if argsDict['mode'] == "prop_muts_in_s_ranges":
    os.system("prop_muts_in_s_ranges -c {0} -o {1}".format(args.est_dfe_output_file, args.output_file))


