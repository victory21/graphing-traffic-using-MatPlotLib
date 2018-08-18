filename= input("file name: ")+'.txt'
import matplotlib.pyplot as plt
f=open(filename, 'r')
array=f.readlines()
c=68
firster=0
sum_array_y=[]
put_in_y=[]
while firster<70:
    if array[firster][0:16]=='Throughput(bits)':
        first_time=array[firster][59:76]
    elif array[firster][0:10]=='shaper_tid':
        fiver=int(array[firster+2][46:60])    
        seven=int(array[firster+3][46:60])
        six=int(array[firster+4][46:60])
        two=int(array[firster+5][46:60])
        one=int(array[firster+6][46:60])
        tree=int(array[firster+7][46:60])
        four=int(array[firster+8][46:60])
        zero=int(array[firster+9][46:60])

    firster=firster+1

while c<len(array):
    if array[c][0:16]=='Throughput(bits)':
        multi=1.0
       # print array[c+2][46]
        if array[c+2][46]=='K':
            multi=.001
            #print "dab"
        elif array[c+2][46]=='G':
            multi=1000.0
        put_in_y.append(float(array[c+2][38:46])*multi)


    elif array[c][0:10]=='shaper_tid':
        summer=2 #counter for adding
        the_sum=0 #sum of the array[c+summer]

        while summer<10:
            the_sum=the_sum+int(array[c+summer][46:60])
            summer=summer+1

        the_sum=the_sum-fiver-seven-six-two-one-tree-four-zero
            
        sum_array_y.append(the_sum)
        
        fiver=int(array[c+2][46:60])    
        seven=int(array[c+3][46:60])
        six=int(array[c+4][46:60])
        two=int(array[c+5][46:60])
        one=int(array[c+6][46:60])
        tree=int(array[c+7][46:60])
        four=int(array[c+8][46:60])
        zero=int(array[c+9][46:60])

    c=c+1

len_x=range(0,len(sum_array_y))
#print len(sum_array_y)
#plt.plot(len_x, sum_array_y, linewidth=1.0)
plt.plot(len_x, sum_array_y, linewidth=1.0)
plt.plot(put_in_y,  linewidth=1.0)
plt.ylabel('Sum of all TMM Packet Drops / Avg. Throughput Mbits')
plt.xlabel('time instances')

plt.show()

