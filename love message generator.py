def main():
    while True:
        print('Welcome!!!')
        print('Do you want a to generate a love or friendly message? ')
        user_input_AB = input('Enter "A" for a love message and "B" for a Friendly message: ')
        if user_input_AB in ('a','b'):
            break
        print("\nInvalid Input. Please enter A or B\n")
        
    mssg = mssg_gen(user_input_AB)
    print(mssg)

def mssg_gen(valuex):
    if valuex.lower() == "a":
            
        user_input_name=input('Enter your lover\'s name: ')
        user_input_your_name=input('Enter your name: ')
        user_input_gender=input('Is your lover a female or male or others (F,M,O)?: ')
        print("")
        if  user_input_gender.lower()=='f':
            print("My Dearest "+ user_input_name +",")
            print("In the quiet moments of the day, when the world fades away, my heart whispers your name.")
            print("You are the melody that plays in my soul,the warmth that wraps around me, and the reason I believe in magic.")
            print("Your laughter is my favorite song, and your smile is the sunrise that paints my days with hues of joy.")
            print("When I hold your hand, I feel like I’m holding the universe itself.")
            print("In this chaotic world, you are my calm harbor, my safe haven.")
            print("Your love is the compass that guides me home, no matter how far I wander.")
            print("So here’s to us—two imperfect souls dancing through life, creating our own symphony.")
            print("Thank you for being my partner, my confidante, and my forever love.")
            print("")
            print("With all my heart ")
            print(user_input_your_name + " 🌟💖")
            print("")
            print("Feel free to personalize it further with memories or specific details that resonate with your love story ! 😊")
                      
        elif  user_input_gender.lower()=='m':
            print("My Dearest "+ user_input_name +",")
            print("From the moment our eyes met, I knew there was something extraordinary about you. You are my compass, guiding me through life’s twists and turns.")
            print("Your laughter is my favorite melody, and your smile is the sun breaking through the clouds after a storm. When I’m with you, time slows down, and the world fades away.")
            print("In your arms, I’ve found my home—the place where my heart feels safe and cherished. Your love is the rhythm that beats in sync with mine, creating a beautiful symphony of emotions.")
            print("Thank you for being my confidant, my partner in adventure, and my best friend. With you, every day is an enchanting journey, and I can’t wait to see where our love takes us next.")
            print("")
            print("Forever and always, ")
            print(user_input_your_name + " 🌟💖")
            print("")
            print("Feel free to personalize it further with memories or specific details that resonate with your love story ! 😊")

        else:
            print("My Dearest "+ user_input_name +",")
            print("From the moment our eyes met, I knew there was something extraordinary about you. You are my compass, guiding me through life’s twists and turns.")
            print("Your laughter is my favorite melody, and your smile is the sun breaking through the clouds after a storm. When I’m with you, time slows down, and the world fades away.")
            print("In your arms, I’ve found my home—the place where my heart feels safe and cherished. Your love is the rhythm that beats in sync with mine, creating a beautiful symphony of emotions.")
            print("Thank you for being my confidant, my partner in adventure, and my best friend. With you, every day is an enchanting journey, and I can’t wait to see where our love takes us next.")
            print("")
            print("Forever and always, ")
            print(user_input_your_name + " 🌟💖")
            print("")
            print("Feel free to personalize it further with memories or specific details that resonate with your love story ! 😊 ")
                  
                    
                    
    elif valuex.lower() == "b":
            
        user_input_name=input('Enter your Friend\'s name: ')
        user_input_your_name=input('Enter your name: ')
        print ("")
        print("Dear "+ user_input_name +",")
        print("As the sun rises and sets, our friendship remains steadfast. Through laughter and tears, shared secrets and inside jokes, you’ve become an irreplaceable part of my life.")
        print("Thank you for the late-night chats, the spontaneous adventures, and the unwavering support.You’re the one I turn to when life feels like a tangled web, and your wisdom is my compass when I’m lost. ")
        print("In your arms, I’ve found my home—the place where my heart feels safe and cherished. Your love is the rhythm that beats in sync with mine, creating a beautiful symphony of emotions.")
        print("Here’s to countless more memories, inside our secret language of glances and nods. May our bond continue to grow stronger, like roots intertwining beneath the surface.")
        print("")
        print("With gratitude,")
        print(user_input_your_name + " 🌟🤗")
        print("")
        print("Feel free to personalize it further with memories or specific details that resonate with your friendship! 😊 ")

main()


    #else:
        #print("")
        #print("Invalid input try again!!!")
        #print("")
        #print('Do you want a to generate a love or friendly message? ')
