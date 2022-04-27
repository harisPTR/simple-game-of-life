from tkinter import *
import tkinter as tk
import pygame
import time
import random
#------------------------------------------------------------------------------logic
def calculation(x,y,prev):
 next=[[0] * y for i in range(x)]
 for i in range(x):
  for j in range(y):
   nnum=0
   for r in range(i-1,i+2):
    for c in range(j-1,j+2):
     if r >= 0 and c >= 0 and r < len(prev) and c < len(prev[0]):
      nnum+=prev[r][c]
   nnum-=prev[i][j]
   next[i][j]=life(nnum,prev[i][j])
 return next

def life(num,l):
 if l==1:
  if num<2 or num>3:
   return 0
  return 1
 else:
  if num==3:
   return 1
  return 0
#------------------------------------------------------------------------------game of life simulation
def sim():
 try:
  temp=((entry.get()).lower().split("x"))
  x = int(temp[0])
  y = int(temp[1])
  r = int(entry2.get())
  main1=[[0] * y for i in range(x)]
  round=0
  for i in range(x):
   for j in range(y):
    temp=random.randrange(1,100)
    if temp<=r:
     main1[i][j]=1
    else:
     main1[i][j]=0
   main2=main1.copy()
   flag=0
#start pygame
  pygame.init()
  s1=(5 + 20) * y + 5
  s2=(5 + 20) * x + 5
  screen = pygame.display.set_mode((s1,s2))
  pygame.display.set_caption("Game of life")
  run=True
  while run:
   for event in pygame.event.get():
    if event.type==pygame.QUIT:
     run=False
    if event.type==pygame.KEYUP:
     if event.key==pygame.K_ESCAPE:
      run=False
     elif event.key==pygame.K_RIGHT:
      flag=1
     elif event.key==pygame.K_UP:
      flag=2
     elif event.key==pygame.K_DOWN:
      flag=0
     elif event.key==pygame.K_LEFT:
      flag=3

   if flag>0 and flag<3:
    if flag==2:
     time.sleep(0.5)
    round+=1
    main2=calculation(x,y,main2)
    if flag==1:
     flag=0
   elif flag==3:
    main2=main1.copy()
    if round>0:
     round-=1
     for k in range(round):
      main2=calculation(x,y,main2)
    flag=0

   for row in range(x):
    for column in range(y):
     color = (255, 255, 255)
     if main2[row][column] == 1:
      color = (0, 255, 0)
     pygame.draw.rect(screen,color,[(5 + 20) * column + 5,(5 + 20) * row + 5,20,20])
   pygame.display.flip()
  pygame.quit()
  return 0
 except ValueError:
  result = "Something went wrong"
  return 0
#---------------------------------------------------------------------------------------------------first window
root = Tk()
#windgets
prompt = tk.Label(root, text="διαστάσεις πλέγματος:  (π.χ:10x10)", anchor="w")
entry = tk.Entry(root)
prompt2 = tk.Label(root, text="πιθανότητα ενεργοποίησης κάθε κελιού στο αρχικό πλέγμα:   (π.χ: 47)", anchor="w")
entry2 = tk.Entry(root)
btn = Button(root, text="Start", command = sim)
# widget layout 
prompt.pack(side="top", fill="x")
entry.pack(side="top", fill="x", padx=20)
prompt2.pack(side="top", fill="x")
entry2.pack(side="top", fill="x", padx=20)
btn.pack(side="right")
mainloop()