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
  
