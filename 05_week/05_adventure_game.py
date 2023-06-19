print('Welcome to an adventure game!')
print()
#STORY BEGIN
print('You are in an amazing expedition in the Amazonas jungle. Is around midday')
print('and you lost the track of your group. So, you are all alone. Just you and the jungle')
path = input('Now you see two paths to choose the LEFT or RIGHT one. Which one you choose? 1')
print()

while True:
      #If the value typed by the user is different to any of the options the program prompts the following.
      while True:
         if path.lower() != 'left' and path.lower() != 'right':
            print(f'-{path}- is not available.')
            print('-----------------------------------------------------------------------------')
            print('You are in an amazing expedition in the Amazonas jungle. Is around midday')
            print('and you lost the track of your group. So, you are all alone. Just you and the jungle')
            path = input('Now you see two paths to choose the LEFT or RIGHT one. Which one you choose? 2')
            print()

         if path.lower() == 'left':
            #-LEFT OPTION 
            print('Interesting but dangerous option. While you keep going by this path')
            print('you see a very deep and wide river. You can CROSS the river or SEARCH other way.')
            river = input('Or you can CLIMB a tree to see where is your group. What do you choose to do? ')
            print()
            break


      while True:
               if river.lower() != 'cross' and river.lower() != 'search' and river.lower() != 'climb':
                  print(f'-{river}- is not available.')
                  print('-----------------------------------------------------------------------------')
                  print('Interesting but dangerous option. While you keep going by this path')
                  print('you see a very deep and wide river. You can CROSS the river or SEARCH other way.')
                  river = input('Or you can CLIMB a tree to see where is your group. What do you choose to do? ')
                  print()

               if river.lower() == 'cross':
                  #--CROSS
                  print('You decided to cross the river swimming. You get to the other side')
                  print('and you see your group in the forest. Well done you are safe now!')
                  print()
                  break

               if river.lower() == 'search':
                  #--SEARCH
                  print('You start looking for others paths for hours. It is getting dark.')
                  print('You fall asleep but you never wake up. You passed away. Game Over! ')
                  print()
                  break

               if river.lower() == 'climb':
                  #--CLIMB
                  print('You start to climb the tallest tree around you. But halfway up,')
                  print("your foot slips off. You try to grab a branch, but you can't. Falling from that height ends your life.")
                  print('Game over!')
                  print()
                  break
      

      if path.lower() == 'right':
         #-RIGHT OPTION
         print('Good choice. While you walk in this path you come to a dead end valley.')
         print('Then you see a CAVE you can enter. And you remember you could CALL your leader group.')
         dead_end = input('Or you can CLIMB the mountain in front of you. What do you choose in this situation? ')
         print()

         while True:
               if dead_end.lower() != 'cave' and dead_end.lower() != 'call' and dead_end.lower() != 'climb':
                  print(f'-{dead_end}- is not available.')
                  print('-----------------------------------------------------------------------------')
                  print('Good choice. While you walk in this path you come to a dead end valley.')
                  print('Then you see a CAVE you can enter. And you remember you could CALL your leader group.')
                  dead_end = input('Or you can CLIMB the mountain in front of you. What do you choose in this situation? ')
                  print()
                  break

               if dead_end.lower() == 'cave':
                  #--CAVE 
                  print('When you enter the cave you realize there is no light. While trying to grab your cell phone to use the flashlight,')
                  print('your foot slips off and your head hits a rock on the ground. You never wake up.')
                  print('Game over!')    
                  break

               if dead_end.lower() == 'call':
                  #--CALL
                  print('Very smart choice! You start calling your leader group and he pick up the call.') 
                  print('He says they are just a few meters away and they will wait for you.')
                  print('You find the group. You are safe now!')
                  print()
                  break

               if dead_end.lower() == 'climb':
                  #--CLIMB
                  print('A brave decision! You start climbing but you did not realize it was a huge mountain.')
                  print('So you try to go down. Your foot slips off and you fall 40 meters to the ground.')
                  print('Game Over!')  
                  print()
                  break
      break