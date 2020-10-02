#! /usr/bin/python
import random,argparse,sys,subprocess,os
parser = argparse.ArgumentParser()
import numpy as np
random.seed(0)

input_flies_ls = ['data/mdp/continuing-mdp-10-5.txt','data/mdp/continuing-mdp-2-2.txt','data/mdp/continuing-mdp-50-20.txt','data/mdp/episodic-mdp-10-5.txt','data/mdp/episodic-mdp-2-2.txt','data/mdp/episodic-mdp-50-20.txt']


class VerifyOutputPlanner:
    def __init__(self,algorithm):
        algorithm_ls = list()
        if algorithm=='all':
            algorithm_ls+=['hpi','vi','lp']
        else:
            algorithm_ls.append(algorithm)
            
        for algo in algorithm_ls:
            print('verify output',algo)
            counter = 1    
        
            for in_file in input_flies_ls:
                print("-"*100)
                cmd_planner = "python","planner.py","--mdp",in_file,"--algorithm",algo
                print('test case',str(counter)+algo,":\t"," ".join(cmd_planner))
                counter+=1
                cmd_output = subprocess.check_output(cmd_planner,universal_newlines=True)
                mistakeFlag = self.verifyOutput(cmd_planner,cmd_output,in_file)
                #if not mistakeFlag:
                #    self.calculateError(cmd_output,in_file)
                    
            
            

    def verifyOutput(self,cmd_planner,cmd_output,in_file):
        
        sol_file = in_file.replace("continuing","sol-continuing").replace("episodic","sol-episodic")
        base = np.loadtxt(sol_file,delimiter=" ",dtype=float)
        output = cmd_output.split("\n")
        nstates = base.shape[0]
        
        est = [i.split() for i in output if i!='']
        
        
        mistakeFlag = False
        if '' in output:
            output.remove('')
        if not len(output)==nstates:
            mistakeFlag = True
            print("\n","*"*10,"Mistake:Exact number of line in standard output should be",nstates,"but have",len(output),"*"*10)
            #print(output[0:5])
        est = [i.split() for i in output if i!='']
        if not mistakeFlag:
            print("You have printed in correct format. \nCalculating error of your value function")
        else:
            print("You haven't printed output in correct format. \nExiting without calculating error of your value function")
            sys.exit(0)
        for i in range(len(est)):
            if not len(est[i])==2:
                mistakeFlag = True
                print("\n","*"*10,"Mistake: On each line you should print only value,policy for a state","*"*10)
                #print(line)
                sys.exit(0)
            est_V = float(est[i][0]);base_V = float(base[i][0])
            print("%10.6f"%est_V,"%10.6f"%base_V,"%10.6f"%abs(est_V-base_V),end="\t")
            if (est_V-base_V) <= (10**-4):
                print("OK")
            else:
                print("\t\t\tNot OK")
            
        
if __name__ == "__main__":
    parser.add_argument("--algorithm",type=str,default="all")
    args = parser.parse_args()
    algo = VerifyOutputPlanner(args.algorithm)




        
        