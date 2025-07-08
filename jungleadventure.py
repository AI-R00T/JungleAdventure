import time

def get_validated_input(prompt, valid_options):
    valid_options_lower = [opt.lower() for opt in valid_options]
    while True:
        user_input = input(f"{prompt} ({'/'.join(valid_options)}): ").strip().lower()
        if user_input in valid_options_lower:
            return user_input
        else:
            print(f"Invalid choice. Please enter one of the following: {', '.join(valid_options)}")
            time.sleep(1)

def jungle_adventure():
    print("Welcome to the Jungle - here, you never know what to expect...")
    time.sleep(2)
    print("You feel the humid air and hear the distant calls of exotic birds.")
    time.sleep(2)
    print("You see a shadow in the bushes.")
    time.sleep(2)
    print("You see a vibrant bird in the sky.")
    time.sleep(2)
    print("You see the ancient trees sway with the wind.")
    time.sleep(2)

    # --- First Decision: Path Choice ---
    path = get_validated_input("You find two paths: one goes to a river, the other to a mountain. Where do you go?", ["river", "mountain"])
    time.sleep(1)

    if path == "river":
        print("You head towards the sound of flowing water.")
        time.sleep(2)
        print("You arrive at a wide, shimmering river.")
        time.sleep(2)
        
        # --- River Path Decision ---
        river_choice = get_validated_input("Do you want to 'swim' across the river or 'follow bank' along its edge?", ["swim", "follow bank"])
        time.sleep(1)

        if river_choice == "swim":
            print("You plunge into the cool water, feeling refreshed.")
            time.sleep(2)
            print("Suddenly, you see movement in the water near you!")
            time.sleep(2)
            swim_encounter = get_validated_input("Is it 'friendly dolphins' or 'hungry piranhas'?", ["dolphins", "piranhas"])
            time.sleep(1)

            if swim_encounter == "dolphins":
                print("A pod of playful dolphins surrounds you and guides you to a hidden lagoon!")
                time.sleep(2)
                print("In the lagoon, you find a chest filled with ancient gold! You're rich!")
            elif swim_encounter == "piranhas":
                print("Sharp teeth flash in the water! You quickly swim back to shore, narrowly escaping!")
                time.sleep(2)
                print("You're safe, but covered in scratches and a little shaken.")
            else: # Fallback - should be caught by get_validated_input, but good for safety
                print("The river holds unexpected dangers, and you decide to retreat.")

        elif river_choice == "follow bank":
            print("You decide to stick to dry land, navigating along the river's edge.")
            time.sleep(2)
            print("The dense foliage starts to clear, revealing something intriguing.")
            time.sleep(2)
            bank_encounter = get_validated_input("You stumble upon 'ancient ruins' or a 'sleeping jaguar'. What do you do?", ["ruins", "jaguar"])
            time.sleep(1)

            if bank_encounter == "ruins":
                print("You discover the overgrown remains of an ancient civilization.")
                time.sleep(2)
                print("Inside, you find a mysterious glowing artifact that hums with energy!")
            elif bank_encounter == "jaguar":
                print("A majestic jaguar is sleeping peacefully on a sun-drenched rock.")
                time.sleep(2)
                jaguar_action = get_validated_input("Do you try to 'sneak past' or 'try to scare' it?", ["sneak past", "scare"])
                time.sleep(1)
                if jaguar_action == "sneak past":
                    print("You carefully tiptoe past the sleeping beast. Success! You continue your journey undisturbed.")
                elif jaguar_action == "scare":
                    print("You let out a loud yell! The jaguar wakes with a roar and chases you for miles! You barely escape!")
                else:
                    print("Hesitation leads to danger. The jaguar stirs, and you quickly back away.")
            else: # Fallback
                print("You decide the river bank is too unpredictable and turn back.")

    elif path == "mountain":
        print("You begin the arduous climb up the winding mountain path.")
        time.sleep(2)
        print("The air grows cooler as you ascend, and the jungle canopy stretches below.")
        time.sleep(2)

        # --- Mountain Path Decision ---
        mountain_choice = get_validated_input("Do you want to 'explore temple' you spot higher up or 'climb higher' to the summit?", ["explore temple", "climb higher"])
        time.sleep(1)

        if mountain_choice == "explore temple":
            print("You carefully approach the ancient temple carved into the mountainside.")
            time.sleep(2)
            print("The entrance is dark and foreboding.")
            time.sleep(2)
            temple_encounter = get_validated_input("Do you encounter a 'hidden trap' or a 'wise old guardian'?", ["trap", "guardian"])
            time.sleep(1)

            if temple_encounter == "trap":
                print("You step on a pressure plate! A hidden dart shoots out, but you narrowly dodge it!")
                time.sleep(2)
                print("That was close! You proceed with extreme caution.")
            elif temple_encounter == "guardian":
                print("An ancient, robed figure appears from the shadows.")
                time.sleep(2)
                print("The guardian offers you a riddle: 'What has an eye, but cannot see?'")
                time.sleep(2)
                riddle_answer = get_validated_input("What is your answer?", ["needle", "storm", "potato"]) # Example answers
                if riddle_answer == "needle":
                    print("The guardian smiles. 'Correct! You are wise beyond your years.' They grant you passage to a secret chamber!")
                else:
                    print("The guardian shakes their head. 'Incorrect. You must seek true wisdom.' You are politely, but firmly, shown the exit.")
            else: # Fallback
                print("The temple's mysteries remain unsolved as you decide not to enter.")

        elif mountain_choice == "climb higher":
            print("You push yourself, climbing higher and higher, the view expanding with every step.")
            time.sleep(2)
            print("The wind whips around you, revealing the majestic landscape.")
            time.sleep(2)
            climb_encounter = get_validated_input("Do you find a 'stunning vista' or a 'treacherous cliff'?", ["vista", "cliff"])
            time.sleep(1)

            if climb_encounter == "vista":
                print("You reach the peak and are greeted by a breathtaking panoramic vista!")
                time.sleep(2)
                print("You feel invigorated, seeing distant lands stretching to the horizon. The journey was worth it!")
            elif climb_encounter == "cliff":
                print("The path narrows, leading to a perilous, crumbling cliff edge.")
                time.sleep(2)
                cliff_action = get_validated_input("Do you try to find a 'hidden cave' on the cliff face or 'turn back'?", ["cave", "turn back"])
                time.sleep(1)
                if cliff_action == "cave":
                    print("You carefully rappel down, finding a small, hidden cave filled with rare crystals!")
                elif cliff_action == "turn back":
                    print("Wisely, you decide to turn back. Safety is paramount in the jungle.")
                else:
                    print("Hesitation on the cliff leads to a stumble. You manage to regain your footing, shaken but safe.")
            else: # Fallback
                print("The climb becomes too dangerous, and you decide to descend.")
    
    # --- End of Adventure ---
    print("\nYour jungle adventure concludes for today. What an experience!")
    time.sleep(2)


# Start the jungle adventure by calling the function
if __name__ == "__main__":
    jungle_adventure()
    
    # Optional: Allow playing again
    while True:
        play_again = get_validated_input("Do you want to embark on another jungle adventure? (yes/no)", ["yes", "no"])
        if play_again == "yes":
            jungle_adventure()
        else:
            print("Thanks for exploring the jungle! Farewell!")
            break