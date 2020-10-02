#! /usr/bin/python
import random,argparse,sys,subprocess,os
parser = argparse.ArgumentParser()
import numpy as np
random.seed(0)

input_flies_ls = ["data/maze/grid10.txt","data/maze/grid20.txt","data/maze/grid30.txt","data/maze/grid40.txt","data/maze/grid50.txt","data/maze/grid60.txt","data/maze/grid70.txt","data/maze/grid80.txt","data/maze/grid90.txt","data/maze/grid100.txt"]
#input_flies_ls = ["data/maze/grid30.txt"]

class MazeVerifyOutput:
    def __init__(self,algo):
        
        counter = 1
        for in_file in input_flies_ls:
            print("test instance",counter,"-"*100)
            counter+=1
            cmd_encode = "python","encoder.py","--grid",in_file
            cmd_planner = "python","encoder.py","--mdp","mdpFile","--algorithm",algo
            cmd_decode = "python","decoder.py","--grid","gridFile","value_policy","value_and_policy_file"
            
            print("Executing..."," ".join(cmd_encode))
            mdpFile = subprocess.check_output(cmd_encode,universal_newlines=True)
            fw = open("mdpFile",'w');fw.wrtie(mdpFile);fw.close()
            
            print("Executing..."," ".join(cmd_planner))
            value_and_policy_file = subprocess.check_output(cmd_encode,universal_newlines=True)
            fw = open("value_and_policy_file",'w');fw.wrtie(value_and_policy_file);fw.close()
            
            print("Executing..."," ".join(cmd_decode))
            shortestPath = subprocess.check_output(cmd_encode,universal_newlines=True)
            
            
            #fr = open(in_file.replace("grid","solution"),'r')
            #shortestPath = fr.read()
            #fr.close()
            
            mistakeFlag = self.traversePath(shortestPath,in_file)
            if not mistakeFlag:
                self.verifyOutput(shortestPath,in_file)
                
            
            
    def traversePath(self,path,in_file):
        mistakeFlag = False
        gridData = np.loadtxt(in_file,delimiter=" ",dtype=int)
        #print(gridData)
        path_ls = path.split()
        #print(path_ls)
        
        startIndex = np.where(gridData==2)
        x = startIndex[0][0]
        y = startIndex[1][0]
        
        direction_dict = {'N':[-1,0], 'E':[0,1],'W':[0,-1],'S':[1,0]}
        for i in path_ls:
            x+=direction_dict[i][0]
            y+=direction_dict[i][1]
            #print(i,x,y)
            
            if gridData[x][y]==1:
                print("\n","*"*10,"Mistake:Wall ahead. Unable to traverse your path","*"*10)
                mistakeFlag = True
                break
        
        endIndex = np.where(gridData==3)
        x = endIndex[0][0]
        y = endIndex[1][0]
        
        if not gridData[x][y]==3:
            print("\n","*"*10,"Mistake: Wrong path","*"*10)
            mistakeFlag = True
        
        
        return mistakeFlag
        
    
    def verifyOutput(self,shortestPath,in_file):
        
        sol_file = in_file.replace("grid","solution")
        fr = open(in_file.replace("grid","solution"),'r')
        base = fr.read()
        fr.close()
        base = base.split() 
        est = shortestPath.split()
        
        direction_ls = ['N','E','W','S']
        mistakeFlag = False
        for item in est:
            if not item in direction_ls:
                mistakeFlag = True
                print("\n","*"*10,"Mistake:Invalid direction printed","*"*10)
                print("your path:",est)
                break
                
        if not mistakeFlag:
            if len(base)<len(est):
                print("Your path is not shortestPath")
            elif len(base)==len(est):
                print("OK. You have printed the correct shortest path")
            else:
                print("You your path is shorter than shortest paht! This should not happen")
                print("base path: ",base)
                print("your path:",est)
            
            

            
        
if __name__ == "__main__":
    parser.add_argument("--algorithm",type=str,default="hpi")
    args = parser.parse_args()
    algo = MazeVerifyOutput(args.algorithm)




        
        