import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
path='weighted_karate.gml';
def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem);
        except ValueError:
            continue
        return row
    return -1
def weight_inC(path, C):
    G=nx.read_gml(path);
    w=0;             
    for i in C:
        for j in C:
            if i<j:
                if j in G.neighbors(i):
                   w=w+G[i][j][1]['value'];
    return w 
def weight_i_C(path, C,i):
    G=nx.read_gml(path);
    w=0;             
    for j in C:
        if j in G.neighbors(i):
           w=w+G[i][j][1]['value'];
    return w  
def weight_tot_C(path, C):
    G=nx.read_gml(path);
    w=0;             
    for i in C:
        for j in G.neighbors(i):
            if(i<j):
               w=w+G[i][j][1]['value'];
    return w           
G=nx.read_gml(path);
N=G.nodes();
noc=len(N);         
communities=[];     
for i in N:
    communities.append([i]);
        
k=[];
m=0;
for i in N:
     E=G.neighbors(i); 
     z=0; 
     for j in E:
         if(i<j):
             z=z+G[i][j][1]['value'];
     k.append(z)
     m=m+k[i-1];
temp=0;
temp1=0;
temp2=0;
change_noc=34;
while(change_noc>0):
   noc=len(communities); 
   for i in range(0,noc):
        for j in communities[i]:
            Nbr=G.neighbors(j);
            delQ=[];                
            for count in Nbr:
                ind=find(communities,count);
                if(ind!=i):        
                   sigma_in=weight_inC(path,communities[ind]);
                   sigma_k_in=weight_i_C(path,communities[ind],j);  
                   sigma_tot=weight_tot_C(path,communities[ind]) 
                   temp1= (sigma_in+sigma_k_in)/(2*m)-((sigma_tot+k[j-1])/(2*m))**2;
                   temp2= (sigma_in)/(2*m)-((sigma_tot)/(2*m))**2-(k[j-1]/(2*m))**2;
                   temp=temp1-temp2; 
                   delQ.append(temp);
            if delQ!=[]:
                    t=np.argmax(delQ);
                    q=find(communities,Nbr[t]);         
                    communities[q].append(j)            
                    communities[i].remove(j)  
   communities = [x for x in communities if x != []];
   change_noc=noc-len(communities);
                 
            
                 
    