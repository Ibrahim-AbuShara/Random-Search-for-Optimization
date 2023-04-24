import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import os

data=pd.read_excel("15-Points.xlsx")
nodes_l=list(data.to_records()) 


def calc_destans(node1,node2):
    return math.sqrt((node2[1] - node1[1])**2 + (node2[2] - node1[2])**2)



def TSP(nodes):
    start_node=nodes[0]
    nodes[start_node[0]][-1]=True
    current_node=start_node.copy()
    nodes_list=[start_node[0]]
    total=0
    while len(nodes)!=len(nodes_list):
        des=np.inf
        index=-1
        for node in nodes:
            if node[-1]!= True:
                temp_des=calc_destans(current_node,node)
                temp_index=node[0]
                if temp_des<des:
                    des=temp_des
                    index=temp_index
        total=total+des
        nodes_list.append(index)
        current_node=nodes[index]
        nodes[index][-1]=True    
    final_des=total+calc_destans(nodes[nodes_list[-1]],start_node)
    nodes_list.append(start_node[0])
    return final_des,nodes_list

def plot_map(nodes_list):
    for i in range(len(nodes_list)):
        plt.plot(data.values[nodes_list][:,0],data.values[nodes_list][:,1],'*',color='green')
        df=np.array(data.values[nodes_list[:i+1]])
        ax=plt.plot(df[:,0],df[:,1],lw=5,color="blue")
        plt.plot(data.values[nodes_list[i]][0],data.values[nodes_list[i]][1],'o',lw=10,color="red")
        plt.xlim(-90,30)
        plt.ylim(-50,30)
        plt.title(f"Traveling Salesman Problem N-N\nCity:{int(data.values[nodes_list[i]][-1])}")
        plt.savefig(f"/home/ibrahim/projects/Random-Search-for-Optimization/NN_imgs/{i:003}",dpi=100,facecolor="white")
        plt.close()
    os.system("convert -delay 50 /home/ibrahim/projects/Random-Search-for-Optimization/NN_imgs/*.png tsp_N_N.gif")
    os.system("gifview -a tsp_N_N.gif")
        
    
             

final_des,nodes_list=TSP(nodes_l)
print(f"Best road found: {nodes_list}\nTotl Destans: {final_des}")

plot_map(nodes_list)




