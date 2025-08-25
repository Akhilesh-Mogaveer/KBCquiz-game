print("\n\033[1mWELCOME TO THE GAME!\n\033[0m")

questions = [
    "Which is the smallest state in India by area? \nA) Goa \nB) Sikkim \nC) Tripura \nD) Nagaland",
    "Who invented the telephone? \nA) Alexander Graham Bell \nB) Thomas Edison \nC) Nikola Tesla \nD) James Watt",
    "Who was the first person to step on the moon? \nA) Neil Armstrong \nB) Yuri Gagarin \nC) Buzz Aldrin \nD) Rakesh Sharma",
    "Which sport is associated with the term Duckworth-Lewis method? \nA) Hockey \nB) Football \nC) Cricket \nD) Tennis",
    "Which of these books was written by R. K. Narayan? \nA) The Guide \nB) Train to Pakistan \nC) God of Small Things \nD) Discovery of India",
    "Who was the first Indian woman to go into space? \nA) Kalpana Chawla \nB) Sunita Williams \nC) Tessy Thomas \nD) Indira Gandhi",
    "Who was the first Indian to win an individual Olympic gold medal? \nA) Abhinav Bindra \nB) Milkha Singh \nC) P. T. Usha \nD) Leander Paes",
    "Which Indian city hosted the first session of the Indian National Congress in 1885? \nA) Kolkata \nB) Mumbai \nC) Chennai \nD) Delhi",
    "Who was the first recipient of the Bharat Ratna Award in 1954? \nA) C. Rajagopalachari \nB) Dr. Sarvepalli Radhakrishnan \nC) Dr. C. V. Raman \nD) Jawaharlal Nehru",
    "The first battle of Panipat (1526) was fought between whom? \nA) Babur and Ibrahim Lodi \nB) Akbar and Rana Sanga \nC) Humayun and Sher Shah Suri \nD) Aurangzeb and Shivaji",
    "Which Indian scientist won the Nobel Prize in Physics in 1930? \nA) Homi J. Bhabha \nB) C. V. Raman \nC) S. Chandrasekhar \nD) Jagadish Chandra Bose",
    "The term 'Operation Flood' in India is related to which sector? \nA) Agriculture \nB) Dairy production \nC) Green revolution \nD) Irrigation",
    "The Harappan Civilization was discovered in which year? \nA) 1911 \nB) 1921 \nC) 1935 \nD) 1947",
    "In which year was the Battle of Plassey fought? \nA) 1757 \nB) 1764 \nC) 1857 \nD) 1707",
    "Which is the only country that is also a continent? \nA) Greenland \nB) Australia \nC) Antarctica \nD) South America"
]

answers = ["A", "A", "A", "C", "A", "A", "A", "B", "A", "A", "B", "B", "B", "A", "B"]

prizes = [1000, 2000, 3000, 5000, 10000,
          20000, 40000, 80000, 160000, 320000,
          640000, 1250000, 2500000, 5000000, 7000000]

safe_levels = {4: 10000, 9: 320000, 14: 5000000}  

amount = 0

for i in range(len(questions)):
    print(f"\nQ{i+1}) {questions[i]}")
    quit_choice = input("Do you want to quit? (yes/no): ").strip().lower()
    
    if quit_choice == "yes":
        print(f"\nYou quit the game with ₹{amount} 🎉")
        break
    
    ans = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    if ans == answers[i]:
        amount = prizes[i]
        print(f" Correct! You won ₹{amount}")
    else:
        print(" Wrong answer!")
        
        safe_amount = 0
        for level, money in safe_levels.items():
            if i >= level:
                safe_amount = money
        print(f"\nYou take home ₹{safe_amount}")
        break
else:
    print(f"\n Congratulations! You won the jackpot of ₹{amount} ")


