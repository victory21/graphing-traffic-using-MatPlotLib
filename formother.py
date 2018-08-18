from easygui import *
import matplotlib.pyplot as plt
filename=input("file name: ")+'.txt'
f=open(filename, 'r')
array=f.readlines()
c=68
err={}
firster=0
line_n=2
#flow_ex=internal=no_flow=port_de=rst_from=tcp_3whs=tcp_rst=handshake=0
while firster<70:
    if array[firster][0:10]=='RST Cause:':
        while array[firster+line_n]!='\n':
            err[array[firster+line_n][0:35]]=int(array[firster+line_n][35:len(array[firster+line_n])-1])
            line_n=line_n+1
    firster=firster+1

err_list=list(err.keys()) #puts all the dicts into a list

for x in range(0,len(err_list)): #makes a string for each item in the list  
    temp=err_list[x]             #using the second to last word without first letter and add _ to end
    sec_to_last =temp.split()[len(temp.split())-2]
    exec(sec_to_last[1:len(sec_to_last)]+'_=[]') 

while c<len(array):
    if array[c][0:10]=='RST Cause:':
        line_n=2
        while array[c+line_n]!='\n':
            temp=array[c+line_n][0:35]
            sec_to_last =temp.split()[len(temp.split())-2]
            
            eval(sec_to_last[1:len(sec_to_last)]+'_').append(str(abs(err[array[c+line_n][0:35]]-int(array[c+line_n][35:len(array[c+line_n])-1]))))
            err[array[c+line_n][0:35]]=int(array[c+line_n][35:len(array[c+line_n])-1])
            line_n=line_n+1
    c=c+1

var = multchoicebox ('message', 'title',err_list) #var is the chosen ones

#len_x=range(0,len(var[0]))

#print(var) 
for x in range(0,len(var)):
    temp=var[x].split()[len(var[x].split())-2]+'_'
    temp=temp[1:len(temp)]
    #print(len(eval(temp)))
    len_x=range(0,len(eval(temp)))
    plt.plot(len_x,eval(temp), linewidth=1.0)

plt.show()
