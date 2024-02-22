from collections import OrderedDict
from operator import getitem
import numpy as np
import math


spins = [10, 1, 5, 35, 22, "0", "00", 10, 35, 22, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,1, 2, 21, 22, 23, 24,  26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,"0"]

def sinceRolled(num):
    i = 0
    spinsSinceLastRolled = i
    while i <= len(spins):
        if spins[i] == num:
            spinsSinceLastRolled = i + 1
            break
        elif spins[i] == str(num):
            spinsSinceLastRolled = i + 1
            break
        elif num not in spins:
            spinsSinceLastRolled = len(spins)
            break
        else: i += 1
    return spinsSinceLastRolled


numbers = {
  "1": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 1,
      "row": 1,
      "align": "left",
      "counter": spins.count(1),
      "spinsSinceLastRolled": sinceRolled(1)
  },
  "2": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 1,
      "row": 2,
      "align": "right",
      "counter": spins.count(2),
      "spinsSinceLastRolled": sinceRolled(2)
  },
  "3": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 1,
      "row": 3,
      "align": "left",
      "counter": spins.count(3),
      "spinsSinceLastRolled": sinceRolled(3)
  }, 
  "4": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 1,
      "row": 1,
      "align": "right",
      "counter": spins.count(4),
      "spinsSinceLastRolled": sinceRolled(4)

  },
  "5": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 1,
      "row": 2,
      "align": "left",
      "counter": spins.count(5),
      "spinsSinceLastRolled": sinceRolled(5)
      },
  "6": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 1,
      "row": 3,
      "align": "right",
      "counter": spins.count(6),
      "spinsSinceLastRolled": sinceRolled(6)
  },
  "7": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 1,
      "row": 1,
      "align": "left",
      "counter": spins.count(7),
      "spinsSinceLastRolled": sinceRolled(7)
  },
  "8": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 1,
      "row": 2,
      "align": "right",
      "counter": spins.count(8),
      "spinsSinceLastRolled": sinceRolled(8)
  },
  "9": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 1,
      "row": 3,
      "align": "left",
      "counter": spins.count(9),
      "spinsSinceLastRolled": sinceRolled(9)
  }, 
  "10": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 1,
      "row": 1,
      "align": "right",
      "counter": spins.count(10),
      "spinsSinceLastRolled": sinceRolled(10)
  },
  "11": {
      "color": "black",
      "evenOdd": "odd",
      "twelve": 1,
      "row": 2,
      "align": "right",
      "counter": spins.count(11),
      "spinsSinceLastRolled": sinceRolled(11)
  },
  "12": {
      "color": "red",
      "evenOdd": "even",
      "twelve": 1,
      "row": 3,
      "align": "left",
      "counter": spins.count(12),
      "spinsSinceLastRolled": sinceRolled(12)
          },
  "13": {
      "color": "black",
      "evenOdd": "odd",
      "twelve": 2,
      "row": 1,
      "align": "right",
      "counter": spins.count(13),
      "spinsSinceLastRolled": sinceRolled(13)
  },
  "14": {
      "color": "red",
      "evenOdd": "even",
      "twelve": 2,
      "row": 2,
      "align": "left",
      "counter": spins.count(14),
      "spinsSinceLastRolled": sinceRolled(14)
  }, 
  "15": {
      "color": "black",
      "evenOdd": "odd",
      "twelve": 2,
      "row": 3,
      "align": "right",
      "counter": spins.count(15),
      "spinsSinceLastRolled": sinceRolled(15)
  },
  "16": {
      "color": "red",
      "evenOdd": "even",
      "twelve": 2,
      "row": 1,
      "align": "left",
      "counter": spins.count(16),
      "spinsSinceLastRolled": sinceRolled(16)
  },
  "17": {
      "color": "black",
      "evenOdd": "odd",
      "twelve": 2,
      "row": 2,
      "align": "right",
      "counter": spins.count(17),
      "spinsSinceLastRolled": sinceRolled(17)
  },
  "18": {
      "color": "red",
      "evenOdd": "even",
      "twelve": 2,
      "row": 3,
      "align": "left",
      "counter": spins.count(18),
      "spinsSinceLastRolled": sinceRolled(18)
  }, 
  "19": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 2,
      "row": 1,
      "align": "left",
      "counter": spins.count(19),
      "spinsSinceLastRolled": sinceRolled(19)
  },
  "20": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 2,
      "row": 2,
      "align": "right",
      "counter": spins.count(20),
      "spinsSinceLastRolled": sinceRolled(20)
  },
  "21": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 2,
      "row": 3,
      "align": "left",
      "counter": spins.count(21),
      "spinsSinceLastRolled": sinceRolled(21)
  }, 
  "22": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 2,
      "row": 1,
      "align": "left",
      "counter": spins.count(22),
      "spinsSinceLastRolled": sinceRolled(22)
  }, 
  "23": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 2,
      "row": 2,
      "align": "left",
      "counter": spins.count(23),
      "spinsSinceLastRolled": sinceRolled(23)
  },
  "24": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 2,
      "row": 3,
      "align": "right",
      "counter": spins.count(24),
      "spinsSinceLastRolled": sinceRolled(24)
  },
  "25": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 3,
      "row": 1,
      "align": "left",
      "counter": spins.count(25),
      "spinsSinceLastRolled": sinceRolled(25)
  }, 
  "26": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 3,
      "row": 2,
      "align": "left",
      "counter": spins.count(26),
      "spinsSinceLastRolled": sinceRolled(26)
  }, 
  "27": {
      "color": "red",
      "evenOdd": "odd",
      "twelve": 3,
      "row": 3,
      "align": "left",
      "counter": spins.count(27),
      "spinsSinceLastRolled": sinceRolled(27)
  },
  "28": {
      "color": "black",
      "evenOdd": "even",
      "twelve": 3,
      "row": 1,
      "align": "right",
      "counter": spins.count(28),
      "spinsSinceLastRolled": sinceRolled(28)
  },
  "29": {
      "color": "black",
      "evenOdd": "odd",
      "twelve": 3,
      "row": 2,
      "align": "right",
      "counter": spins.count(29),
      "spinsSinceLastRolled": sinceRolled(29)
  },
  "30": {
      "color": "red",
      "evenOdd": "even",
      "twelve": 3,
      "row": 3,
      "align": "left",
      "counter": spins.count(30),
      "spinsSinceLastRolled": sinceRolled(30)

  },
  "31": {
      "color": "black",
      "evenOdd": "odd",
      "twelve": 2,
      "row": 1,
      "align": "left",
      "counter": spins.count(31),
      "spinsSinceLastRolled": sinceRolled(31)

  },
  "32": {
      "color": "red",
      "evenOdd": "even",
      "twelve": 2,
      "row": 2,
      "align": "right",
      "counter": spins.count(32),
      "spinsSinceLastRolled": sinceRolled(32)

  },
  "33": {
      "color": "black",
      "evenOdd": "odd",
      "twelve": 3,
      "row": 3,
      "align": "left",
      "counter": spins.count(33),
      "spinsSinceLastRolled": sinceRolled(33)

  }, 
  "34": {
      "color": "red",
      "evenOdd": "even",
      "twelve": 3,
      "row": 1,
      "align": "left",
      "counter": spins.count(34),
      "spinsSinceLastRolled": sinceRolled(34)

  }, 
  "35": {
      "color": "black",
      "evenOdd": "odd",
      "twelve": 3,
      "row": 2,
      "align": "left",
      "counter": spins.count(35),
      "spinsSinceLastRolled": sinceRolled(35)

  },
  "36": {
      "color": "red",
      "evenOdd": "even",
      "twelve": 3,
      "row": 3,
      "align": "right",
      "counter": spins.count(36),
      "spinsSinceLastRolled": sinceRolled(36)

      },

  "0": {
      "color": "green",
      "evenOdd": "zero",
      "twelve": 0,
      "row": 0,
      "align": "center",
      
"counter": spins.count("0"),
      "spinsSinceLastRolled": sinceRolled("0")
      },
  "00": {
      "color": "green",
      "evenOdd": "zero",
      "twelve": 0,
      "row": 0,
      "align": "center",
      "counter": spins.count("00"),
      "spinsSinceLastRolled": sinceRolled("00")

  }

}


currentSpin = 0


totalCount = len(spins)

#print(numbers[numStg]["color" ])

def clearSpins():
  spins = []
  return spins



def redAverage():
  redCount = 0
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["color"]== "red":
         redCount += 1
        
       
  redAvg = 100*(redCount / totalCount)
  redPercent = str(redAvg) + "%"
  print(redPercent) 
  return redPercent
    
  

def blackAverage():
  blackCount = 0
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["color"]== "black":
         blackCount += 1
         
       
  blackAvg =  100*(blackCount / totalCount)
  blackPercent = str(blackAvg) + "%"
  print(blackPercent) 
  return blackPercent

def greenAverage():
  greenCount = 0
  
  for num in spins:
      numStg = str(num)
      
      if numbers[numStg]["color"]== "green":
         greenCount += 1
         
       
  greendAvg =  100*(greenCount / totalCount)
  greenPercent = str(greendAvg) + "%"
  print(greenPercent) 
  return greenPercent

def evenAverages():
  evenCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["evenOdd"]== "even":
         evenCount += 1
    
         
        
       
  evenAvg = 100*(evenCount / totalCount)
  evenPercent = str(evenAvg) + "%"
  print(evenPercent) 
  return evenPercent

def oddAverages():
  oddCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["evenOdd"]== "odd":
         oddCount += 1
    
         
        
       
  oddAvg = 100*(oddCount / totalCount)
  oddPercent = str(oddAvg) + "%"
  print(oddPercent) 
  return oddPercent

def zeroAverages():
  zeroCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["evenOdd"]== "zero":
         zeroCount += 1
    
         
        
       
  zeroAvg = 100*(zeroCount / totalCount)
  zeroPercent = str(zeroAvg) + "%"
  print(zeroPercent) 
  return zeroPercent

def firstTwelve():
  firstTwelveCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["twelve"]== 1:
         firstTwelveCount += 1
    
         
        
       
  firstTwelveAvg = 100*(firstTwelveCount / totalCount)
  firstTwelvePercent = str(firstTwelveAvg) + "%"
  print(firstTwelvePercent) 
  return firstTwelvePercent

def secondTwelve():
  secondTwelveCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["twelve"]== 2:
         secondTwelveCount += 1
    
         
        
       
  secondTwelveAvg = 100*(secondTwelveCount / totalCount)
  secondTwelvePercent = str(secondTwelveAvg) + "%"
  print(secondTwelvePercent) 
  return secondTwelvePercent

def thirdTwelve():
  thirdTwelveCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["twelve"]== 2:
         thirdTwelveCount += 1
    
         
        
       
  thirdTwelveAvg = 100*(thirdTwelveCount / totalCount)
  thirdTwelvePercent = str(thirdTwelveAvg) + "%"
  print(thirdTwelvePercent) 
  return thirdTwelvePercent

def firstRow():
  firstRowCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["row"]== 1:
         firstRowCount += 1
    
         
        
       
  firstRowAvg = 100*(firstRowCount / totalCount)
  firstRowPercent = str(firstRowAvg) + "%"
  print(firstRowPercent) 
  return firstRowPercent

def secondRow():
  secondRowCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["row"]== 2:
         secondRowCount += 1
    
         
        
       
  secondRowAvg = 100*(secondRowCount / totalCount)
  secondRowPercent = str(secondRowAvg) + "%"
  print(secondRowPercent) 
  return secondRowPercent

def thirdRow():
  thirdRowCount = 0
  
  
  for num in spins:
      numStg = str(num)
      #print(numStg)
      if numbers[numStg]["row"]== 3:
         thirdRowCount += 1
    
         
        
       
  thirdRowAvg = 100*(thirdRowCount / totalCount)
  thirdRowPercent = str(thirdRowAvg) + "%"
  print(thirdRowPercent) 
  return thirdRowPercent

   

def hotCold():
    uniqueSpins = []
    for num in spins:
      if num not in uniqueSpins:
         uniqueSpins.append(num)

    print(uniqueSpins)
    

    average = len(spins)/len(uniqueSpins)
    print("average: " + str(average))
    print("math floor: "+ str(math.floor(average)))
    print("math ceiling: "+ str(math.ceil(average)))
    hotNumbers = []
       
    for k,v in numbers.items():
        numStg = str(k)
        if numbers[numStg]["counter"] >= math.ceil(average):
            hotNumbers.append(k)
        else: pass
        
    
    print("Hot Numbers: " +str(hotNumbers))


   

#spins = [10, 1, 5, 35, 22, 0, 00, 10, 35, 22, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


#redAverage()
#blackAverage()
#greenAverage()
#evenAverages()
#oddAverages()
#zeroAverages()
#firstTwelve()
#secondTwelve()
#thirdTwelve()
#firstRow()
#secondRow()
#thirdRow()

#print(numbers["00"]["counter"])
#print(totalCount)
#hotCold()
x = sinceRolled("00")
print(x)




