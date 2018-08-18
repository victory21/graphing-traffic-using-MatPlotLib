filename= raw_input("file name: ")+'.txt'
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
f=open(filename, 'r')
array=f.readlines()
c=68
err={}
firster=0
flow=[]
no=[]
RST=[]
TCP=[]
time=[]

while firster<70:
    if array[firster][0:35]=='Flow expired (sweeper)             ':
        flow_nub=int(array[firster][35:len(array[firster])-1])
        #print flow_nub
    elif array[firster][0:35]=='RST from BIG-IP internal Linux host':
        rst_nub=int(array[firster][35:len(array[firster])-1])
        #print rst_nub
    elif array[firster][0:35]=='TCP 3WHS rejected                  ':
        tcp_nub=int(array[firster][35:len(array[firster])-1])
    elif array[firster][0:35]=='No flow found for ACK              ':
        no_nub=int(array[firster][35:len(array[firster])-1])
    elif array[firster][0:35]=='handshake timeout                  ':
        time_nub=int(array[firster][35:len(array[firster])-1])

    firster=firster+1
x=0
while c<len(array):

    if array[c][0:35]=='Flow expired (sweeper)             ':
        flow.append(abs(flow_nub-int(array[c][35:len(array[c])-1])))
        #flow.append(abs(flow_nub-int(array[c][35:len(array[c])-1])))
        #x=x+1
        #print x
        #print len(flow)
        #print "dab"
        flow_nub=int(array[c][35:len(array[c])-1])
    elif array[c][0:35]=='RST from BIG-IP internal Linux host':
        RST.append(abs(rst_nub-int(array[c][35:len(array[c])-1])))
        #print 2
        rst_nub=int(array[c][35:len(array[c])-1])        
    elif array[c][0:35]=='TCP 3WHS rejected                  ':
        TCP.append(abs(tcp_nub-int(array[c][35:len(array[c])-1])))
        tcp_nub=int(array[c][35:len(array[c])-1])
    elif array[c][0:35]=='No flow found for ACK              ':
        no.append(abs(no_nub-int(array[c][35:len(array[c])-1])))
        no_nub=int(array[c][35:len(array[c])-1])
    elif array[c][0:35]=='handshake timeout                  ':
        time.append(abs(time_nub-int(array[c][35:len(array[c])-1])))
        time_nub=int(array[c][35:len(array[c])-1])

    c=c+1
len_x=range(0,len(flow))
#print len(flow)
plt.plot(flow, 'black',linewidth=1.0)
plt.plot(RST,  'blue',linewidth=1.0)
plt.plot(TCP,  'red', linewidth=1.0)
plt.plot(no,  'green',linewidth=1.0)
#plt.plot(time, 'purple', linewidth=1.0)


red_patch = mpatches.Patch(color='black', label='Flow expired')
blue_patch = mpatches.Patch(color='blue', label='RST from Big IP')
black_patch = mpatches.Patch(color='red', label='TCP 3WHS rejected')
green_patch = mpatches.Patch(color='green', label='No flow found for ACK')
#purple_patch = mpatches.Patch(color='purple', label='handshake timeout')
#plt.legend(handles=[red_patch,blue_patch,black_patch,green_patch,purple_patch])
plt.legend(handles=[red_patch,blue_patch,black_patch,green_patch])


plt.ylabel('y')
plt.xlabel('x')

plt.show()
