import random #შემოგვაქვს შემთხვევითი რიცხვი

def guess_number():
    secret_number = random.randint(1, 1000) ## ბოტი ირჩევს რიცხვს 1-დან 100-ის ჩათვლით.
    attempts = 9 #მცდელობები
    
    print("Welcome to the Guessing Game! You have 9 attempts to guess the secret number.")
     #მოგესალმებით გამოცნობის თამაშში, თქვენ გაქვთ 5 მცდელობა იმისათვის, რომ გამოიცნოთ საიდუმლო რიცხვი.

    while attempts > 0: #უზრუნველყოფს, რომ თამაში გაგრძელდება მანამ, სანამ მოთამაშე არ გამოიცნობს სწორ რიცხვს
        try:
            guess = int(input("Enter your guessing number (between 1 and 1000.): ")) #დაწერეთ თქვენი რიცხვი, 1-დან 100-ის ჩათვლით.
            
            if guess < 1 or guess > 1000:
                print("Error: Please enter a number between 1 and 1000.") #თუ რიცხვი არის 1-ზე ნაკლები ან 100-ზე მეტი, მაშინ შეცდომა იქნება.
                continue

            if guess < secret_number: #თუ რიცხვი ნაკლებია საიდუმლო რიცხვზე, მაშინ დაიწერება, რომ საიდუმლო რიცხვი მეტია.
                print("Higher!")
            elif guess > secret_number: #თუ რიცხვი მეტია საიდუმლო რიცხვზე, მაშინ დაიწერება, რომ საიდუმლო რიცხვი ნაკლებია.
                print("Lower!")
            else:
                print("Congratulations! You guessed the secret number:", secret_number) #გილოცავთ თქვენ გამოიცანით საიდუმლო რიცხვი!
                break
            
            attempts -= 1 #ყოველ მცდელობაზე, გვაკლდება ერთი მცდელობა.
            print("Attempts left:", attempts) #დაგრჩათ ამდენი რაოდენობის მცდელობები
        
        except ValueError: #არ შეიძლება რაიმე ასოსი ან სიმბოლოსი გამოყენება.
            print("Error: Please enter a valid number.") #შეცდომა, გთხოვთ ჩაწეროთ სწორი რიცხვი.
    
    if attempts == 0:
        print("Game Over! The secret number was:", secret_number) #თამაში დასრულდა, საიდუმლო რიცხვი იყო (საიდუმლო რიცხვი)

guess_number()