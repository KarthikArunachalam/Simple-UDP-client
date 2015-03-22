from socket import *
import datetime
import time
from decimal import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

message = 'Ping'
i=1
low=1
high=0
sum_time=0
time_final=0.0
j=1
getcontext().prec = 6
while i<=10:
    start=datetime.datetime.now().time()
    #print str(start)
    clientSocket.sendto(message+' '+str(i)+' '+str(datetime.datetime.now().time()),(serverName,serverPort))
    try :
        clientSocket.settimeout(1.0)
        modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
        end=datetime.datetime.now().time()
        #print str(end)
        #print end.microsecond
        #print start.microsecond
        time_final =(end.second-start.second)+Decimal(end.microsecond-start.microsecond)/Decimal(1000000)
        #time_final =(end.second-start.second)*1000000+(end.microsecond-start.microsecond)
        if time_final>high:
            high=time_final
            

        if time_final<low:
            low=time_final
        sum_time=sum_time+time_final
        j=j+1
        
        print modifiedMessage+' RTT='+str(time_final)+' '+'seconds'
    except timeout:
        #end=time.time() 
        print "REQUEST TIMED OUT" #+str(end-start)
    
    i=i+1
clientSocket.close()
avg=sum_time/j
packet_loss=(i-j)*10
print '         Min RTT='+str(low)
print '         max RTT='+str(high)
print '         avg RTT='+str(avg)
print '         packet loss rate='+str(packet_loss)+'%'
raw_input()
