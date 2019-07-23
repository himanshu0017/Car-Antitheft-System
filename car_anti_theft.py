from Tkinter import *
from SimpleCV import *
import winsound
import smtplib
import time

root = Tk()
root.geometry("850x500")
root.title('Car Anti theft')
i=0
j=0
x = True
after_id=None
per=0
def simplecvo():
    global after_id     
    global i
    global j
    idx = 0
    #cam = JpegStreamCamera('http://192.168.43.1:8080/videofeed')
    car = Image("C:\Users\himan\Desktop\parking-car-only.png")
    car_not_in_lot = Image("C:\Users\himan\Desktop\parking-car-only.png")
   # car=cam.getImage()
   # time.sleep(10)
    #car_not_in_lot=cam.getImage()
    
    if x:
        idx+=1
       
        #car_in_lot = car.crop(470,200,200,200)
        
       # car_not_in_lo
       t = car.getImage().scale(320,240)
        
         
        #c =JpegStreamCamera('http://192.168.43.1:8080/videofeed')
        
        yellow_car = car.colorDistance(Color.YELLOW)
        result2=yellow_car
        only_car = car - yellow_car
        arr1=only_car.meanColor()
        result=car.sideBySide(result2,side='bottom',scale=False)
        result=result.sideBySide(only_car,side='right')
        #result=result2.sideBySide(only_car,side='left')
        result.show()
        
        #car_not_in_lot=cam.getImage()
        yellow_car_no = car_not_in_lot.colorDistance(Color.YELLOW)
        #yellow_car_no.show()
        only_car_no = car_not_in_lot - yellow_car_no
       # only_car_no.show()
        arr2=only_car_no.meanColor()
        print arr1[0]
        print arr1[1]
        print arr1[2]

        print arr2[0]
        print arr2[1]
        print arr2[2]
        
        one=(arr1[2]+arr2[2])/2
        two=(arr1[1]+arr2[1])/2
        print one
        print two
        if arr2[2] >= one and arr2[1] >= two:
                  sec = "Car is Safe"
                  timeLabel.configure(text=sec)
        else:
                  sec = "Car Stolen"
                  timeLabel.configure(text=sec)
                  stop()
               
    after_id=root.after(3000,simplecvo)    



def mail():
         fromaddr = 'himanshuraj38@gmail.com'
         toaddrs  = 'himanshuraj38@gmail.com'
         sub = 'Subject:Testing \n'
         msg = 'car stolen'
         result=sub+msg


         # Credentials (if needed)
         username = 'himanshuraj38@gmail.com'
         password = ''

         # The actual mail send
         server = smtplib.SMTP('smtp.gmail.com',587)
         server.ehlo()
         server.starttls()
         server.login(username,password)
         server.sendmail(fromaddr,toaddrs,result)
         server.quit()



def start():
        global x
        x==True
        simplecvo()
         
         
def des(root):
        root.destroy()

def stop():
         global after_id
         if after_id:
                  root.after_cancel(after_id)
                  after_id=None
                  #mail()



timeLabel = Label(root, fg='green', width=10,font=('Helvetica',50))
timeLabel.pack()

startButton = Button(root, text='Start', width=20, command=start)
startButton.pack()

stopButton = Button(root, text='Stop', width=20, command=stop)
stopButton.pack()

button_2 = Button(root, text='Quit', width=20, command=lambda root=root:des(root))
button_2.pack()
root.mainloop()
