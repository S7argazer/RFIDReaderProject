#Code by Josh Reed. Modified by Jeremiah O'Neal on Aug 11, 2023
#Visit this link if you would like to help or feel free to fork this project.
#https://replit.com/join/hvgwgarcpd-jeremiah9407one
#code mirrored at http://tinyurl.com/joneal811b

#from PiicoDev_RFID import PiicoDev_RFID
#from PiicoDev_Unified import sleep_ms

#rfid = PiicoDev_RFID()   # Initialise the RFID module

#Simulate RFID data
import time
import _thread
import random
import array
#Static variables

#This code is here just to simulate the RFID hardware since I'm only coding the project. No need to modify.
class rfid:
  isTagPresent = False
  varReadID = "Undefined"
  varReadIDDetail = "Undefined"
  IDs = ['12345', '23456', '34567', '45678']
  detailedList = ['12345 JCorp', '23456 Sams Comp', '34567 ABC inc', '45678 A Company name']


  def tagPresent():
    return rfid.isTagPresent
  def readID(detail = False):
    if detail == False:
      return rfid.varReadID
    else:
      return rfid.varReadIDDetail
    
def simulate_RFID_read():
   i = 0
   j = 0
   while i <= 9999:
      time.sleep(1)
      if random.random() > .5:
        rfid.isTagPresent = True
        rfid.varReadID = rfid.IDs[j]
        rfid.varReadIDDetail = rfid.detailedList[j]
      else:
        rfid.isTagPresent = False
        rfid.varReadID = "Undefined"
        rfid.varReadIDDetail = "Undefined"
        j = j + 1
        if j > 3:
          j = 0
      i = i + 1

def sleep_ms(i):
  time.sleep(i/1000)
if __name__ == "__main__":
  _thread.start_new_thread(simulate_RFID_read, ())
#end simulation

#This is the actual code that works with the RFID module. Feel free to modify the code below this line.
#The finalized code portion below will go into the capstone project for CYB699A. 8/11/2023
#Ideas are welcome but not guaranteed to be included. This is mostly just for fun.
#and to see if I could emulate the card reader without actually having the hardware in my possession.

print('Place tag near the PiicoDev RFID Module')

while True:    
    if rfid.tagPresent():    # if an RFID tag is present
        id = rfid.readID()   # get the id
        print(id)
      
        id = rfid.readID(detail=True) # gets more details eg. tag type

        print(id)            # print the id

    sleep_ms(100)
