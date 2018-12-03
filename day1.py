print( 'Please input frequencies:')
lines=[]
while True :
  line = input()
  if line:
    lines.append(line)
  else:
    break
currentFrequency =0
for i in range (0, len(lines)):
  currentFrequency+= int(lines[i])
  print (currentFrequency)

print("finalFrequency is:", currentFrequency )
  
currentFrequency=0
frequencies=[]
for line in lines:
        currentFrequency+=int(line)
        if currentFrequency in frequencies:
                print("The first frequency reached twice is:", currentFrequency)
        frequencies.append(currentFrequency)
