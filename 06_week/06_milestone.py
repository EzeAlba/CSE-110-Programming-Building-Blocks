print('Welcome to an adventure game!')
print()
#STORY BEGIN
print('You are in an amazing expedition in the Amazonas jungle. Is around midday')
print('and you lost the track of your group. So, you are all alone. Just you and the jungle')
path = input('Now you see two paths to choose the LEFT or RIGHT one. Which one you choose? ')
print()

while True:
    if path.lower() == 'left':
        #-LEFT OPTION 
        print('1.Interesting but dangerous option. While you keep going by this path')
        print('you see a very deep and wide river. You can CROSS the river or SEARCH other way.')
        river = input('Or you can CLIMB a tree to see where is your group. What do you choose to do? ')
        print()

        while river.lower() != 'cross' and river.lower() != 'search' and river.lower() != 'climb':
                print(f'-{river}- is not available. Try again!')
                print('-----------------------------------------------------------------------------')
                print('2.Interesting but dangerous option. While you keep going by this path')
                print('you see a very deep and wide river. You can CROSS the river or SEARCH other way.')
                river = input('Or you can CLIMB a tree to see where is your group. What do you choose to do? ')
                print()        

        if river.lower() == 'cross':
            #--CROSS
                print('You decided to cross the river swimming. You get to the other side')
                print('and you see your group in the forest. You RUN to them or you SCREAM')
                cross = input('What do you choose to do? ')
                print()
                
        
                while cross.lower()!= 'run' and cross.lower()!= 'scream':
                    print(f'-{cross}- is not available. Try again!')
                    print('-----------------------------------------------------------------------------')
                    print('You decided to cross the river swimming. You get to the other side')
                    print('and you see your group in the forest. You RUN to them or you SCREAM')
                    cross = input('What do you choose to do? ')
                    print()

                #last scenario
                if cross.lower() == 'run':
                    print('You start running very fast. But the road ends and you fall into a precipice.')
                    print('Game Over!')
                    break

                elif cross.lower() == 'scream':
                    print('You start to scream and your group hears you. They show you the way')
                    print('to get to them. Well done you are safe now!')
                    break

        elif river.lower() == 'search':
                #--SEARCH
                print('You start looking for others paths for hours. It is getting dark.')
                print('You fall asleep and when you wake up you see you see shoe prints on the road')
                search=input('You choose to FOLLOW the footprints or SEARCH other paths? ')
                print()
                        
                while search.lower()!= 'follow' and search.lower()!= 'search':
                    print(f'-{search}- is not available. Try again!')
                    print('-----------------------------------------------------------------------------')
                    print('You start looking for others paths for hours. It is getting dark.')
                    print('You fall asleep and when you wake up you see you see shoe prints on the road')
                    search=input('You choose to FOLLOW the footprints or SEARCH other paths? ')
                    print()

                #last scenario
                if search.lower() == 'follow':
                    print('You follow the prints but in the way you found cocodriles')
                    print('eating some human parts. You are next. Game Over!')
                    break

                elif search == 'search':
                    print('While looking for other paths you see your group. And you join them.')
                    print('You are safe now!')
                    break

        elif river.lower() == 'climb':
                #--CLIMB
                print('You start to climb the tallest tree around you. But halfway up,')
                print("your foot slips off. While you are fallin you can GRAB a branch or LET yourself go and see what happens.")
                climb= input('What do you choose to do? ')
                print()
                        
                while climb.lower()!= 'grab' and climb.lower()!= 'let':
                    print(f'-{climb}- is not available. Try again!')
                    print('-----------------------------------------------------------------------------')
                    print('You start to climb the tallest tree around you. But halfway up,')
                    print("your foot slips off. While you are fallin you can GRAB a branch or LET yourself go and see what happens.")
                    climb = input('What do you choose to do? ')
                    print() 


                #last scenario
                if climb == 'grab':
                    print('You grab a branch. But after a few seconds the branch brakes.')
                    print('You fall down to the ground and die. Game Over!')
                    break

                elif climb == 'let':
                    print('You fall down to the ground and die. Game Over!')
                    break

    elif path.lower() == 'right':
    #-RIGHT OPTION
        print('Good choice. While you walk in this path you come to a dead end valley.')
        print('Then you see a CAVE you can enter. And you remember you could CALL your leader group.')
        dead_end = input('Or you can CLIMB the mountain in front of you. What do you choose in this situation? ')
        print()

        while dead_end.lower() != 'cave' and dead_end.lower() != 'call' and dead_end.lower() != 'climb':
            print(f'-{dead_end}- is not available. Try again!')
            print('-----------------------------------------------------------------------------')
            print('Good choice. While you walk in this path you come to a dead end valley.')
            print('Then you see a CAVE you can enter. And you remember you could CALL your leader group.')
            dead_end = input('Or you can CLIMB the mountain in front of you. What do you choose in this situation? ')
            print()

        if dead_end.lower() == 'cave':
            #--CAVE 
            print('When you enter the cave you realize there is no light. You can use your PHONE to turn on the light,')
            print('or you can WALK without light.')
            cave=input('What do you choose? ')  

            while cave.lower()!= 'phone' and cave.lower()!= 'walk':
                print(f'-{cave}- is not available. Try again!')
                print('-----------------------------------------------------------------------------')
                print('When you enter the cave you realize there is no light. You can use your PHONE to turn on the light,')
                print('or you can WALK without light.')
                cave=input('What do you choose? ')                  

                #last scenario
            if cave.lower() == 'phone':
                print('While you are taking your phone out of your pocket,')
                print('your foot slips off and your head hits a rock on the ground. You never wake up. Game Over!')
                break

            elif cave.lower() == 'walk':
                print('While you walk you see a few lights, is your group a few meters ahead of you')
                print('You scream to them and you join them. Well done you are safe now!')
                break        

        if dead_end.lower() == 'call':
            #--CALL
            print('Very smart choice! You start calling your leader group and he pick up the call.') 
            print('He says they are just a few meters away and they will wait for you.')
            call = input('You see two paths the MUDDY one or the CLEAN one. Which one do you choose? ')
            print() 

            while call.lower()!= 'muddy' and call.lower()!= 'clean':
                print(f'-{call}- is not available. Try again!')
                print('-----------------------------------------------------------------------------')
                print('Very smart choice! You start calling your leader group and he pick up the call.') 
                print('He says they are just a few meters away and they will wait for you.')
                call = input('You see two paths the MUDDY one or the CLEAN one. Which one do you choose? ')
                print() 


                #last scenario
            if call.lower() == 'muddy':
                print('This path looks bad but is the right one. You meet your group. Well done!')
                break

            elif call == 'clean':
                print('This one looks good but is not the right one. You get lost. Game over!')
                break 

        if dead_end.lower() == 'climb':
            #--CLIMB
            print('A brave decision! You start climbing but you did not realize it was a huge mountain.')
            print('So you came up with two choices go DOWN or go UP.')
            climb=input('What do you choose? ')  
            print()

            while climb.lower()!= 'down' and climb.lower()!= 'up':
                print(f'-{climb}- is not available. Try again!')
                print('-----------------------------------------------------------------------------')
                print('A brave decision! You start climbing but you did not realize it was a huge mountain.')
                print('So you came up with two choices go DOWN or go UP.')
                climb=input('What do you choose? ')  
                print()

                #last scenario
            if climb.lower() == 'down':
                    print('You try to go down. But your foot slips off and you fall 40 meters to the ground. Game Over!')
                    break

            elif climb.lower() == 'up ':
                print('You try to go up but your foot slips off and you fall 40 meters to the ground. Game Over!' )
                break             

    while path.lower() != 'left' and path.lower() != 'right':
        print(f'-{path}- is not available. Try again!')
        print('-----------------------------------------------------------------------------')
        print('You are in an amazing expedition in the Amazonas jungle. Is around midday')
        print('and you lost the track of your group. So, you are all alone. Just you and the jungle')
        path = input('Now you see two paths to choose the LEFT or RIGHT one. Which one you choose? ')
        print()