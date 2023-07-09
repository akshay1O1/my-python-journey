std=["peter","steve","mj","gwen","miles"]
a=input("enter your choice: ")
if a=="break":
    for i in std:
      '''print(std)
      if i=="gwen":
          break    in this case gwen will also be included in the final output'''
      if  i=="gwen":
          break
      print(i)
else:
   for i in std:
      if  i=="gwen":
          continue
      print(i)

   

    

    






