"""
Automation
Student Project
Project Title: Triangles Oh my!
"""

import math as hugebrain

print("88888888888 8888888b.  8888888        d8888 888b    888  .d8888b.  888      8888888888 .d8888b.  ")
print("    888     888   Y88b   888         d88888 8888b   888 d88P  Y88b 888      888       d88P  Y88b ")
print("    888     888    888   888        d88P888 88888b  888 888    888 888      888       Y88b.      ")
print("    888     888   d88P   888       d88P 888 888Y88b 888 888        888      8888888    'Y888b.   ")
print("    888     8888888P'    888      d88P  888 888 Y88b888 888  88888 888      888           'Y88b. ")
print("    888     888 T88b     888     d88P   888 888  Y88888 888    888 888      888             '888 ")
print("    888     888  T88b    888    d8888888888 888   Y8888 Y88b  d88P 888      888       Y88b  d88P ")
print("    888     888   T88b 8888888 d88P     888 888    Y888  'Y8888P88 88888888 8888888888 'Y8888P'  ")

"""
        WHAT CAN THIS PROGRAM DO?

        This program helps solve the problem of triangles taking over your life! Such a problem

        You can solve these triangles with this program! No more life consuming triangles eating your time
"""

print("\n\n\nWelcome to triangles!")

running = True

# Main loop
while running:
    # Ask user for more general what they want with triangles
    choice1 = input("What type of computation would you like? Pythagorean Theorem: (1), Trig: (2), Exit: (3)\n")
    if choice1 == str(1):
        # What do you want with Pythagorean!?
        choice2 = input("Cool cool. Would you like to find a side (1) or check if a triangle is a right triangle (2)\n")

        if choice2 == str(1):
            choice3 = input("Are you finding the hypotenuse (1) or a leg? (2)")
            if choice3 == str(1):
                # Asks for legs
                leg1 = float(input("What is the first leg value\n"))
                leg2 = float(input("What is the second leg value\n"))

                # Pythagorean theorem
                answer = hugebrain.sqrt(hugebrain.pow(leg1, 2) + hugebrain.pow(leg2, 2))
                print("The hypotenuse is " + answer)
            if choice3 == str(2):
                # Asks for sides
                hypotenuse = float(input("What is the Hypotenuse value\n"))
                leg1 = float(input("What is the leg value\n"))

                # Pythagorean theorem
                answer = hugebrain.sqrt(hugebrain.pow(hypotenuse, 2) - hugebrain.pow(leg1, 2))
                print("The leg is " + str(answer))

        if choice2 == str(2):
            leg1 = float(input("What is the first leg value\n"))
            leg2 = float(input("What is the second leg value\n"))
            hyp = float(input("What is the Hypostenuse value\n"))

            isRight = hugebrain.pow(leg1, 2) + hugebrain.pow(leg2, 2) == hugebrain.pow(hyp, 2)
            print("The triangle is a right triangle: " + str(isRight))

    if choice1 == str(2):

        choice2 = input("Would you like to find an angle (1) or side (2) ")

        # User is trying to find the angle
        if choice2 == str(1):
            print('''          
                               
                              /|
                             / |A
                           C/  |
                           /   |
                          ────── 	 	 	
                             B
                           ''')
            strr = ""
            A = 0
            B = 0
            C = 0

            # This lets the user assign the values of the sides
            while strr != "exit":
                strr = input("What are these values CASE SENSITIVE? ex (B=57) or (A=12) to exit type (exit) ")
                if strr == "exit":
                    continue
                value = int(strr[2:])
                if strr.startswith("A"):
                    A = value
                if strr.startswith("B"):
                    B = value
                if strr.startswith("C"):
                    C = value

            print('''          
                               b
                              /|
                             / |
                            /  |
                           /   |
                         a────── 	 	 	
                             
                           ''')
            choice3 = input("Great! Which angle are you trying to find? (a) (b)")

            # This does the correct trig function based on where the angle is and what the user has input
            if choice3 == "b":
                if A != 0 and B != 0:
                    result = hugebrain.degrees(hugebrain.atan(B / A))
                    print(result)
                if A != 0 and C != 0:
                    result = hugebrain.degrees(hugebrain.acos(A / C))
                    print(result)
                if B != 0 and C != 0:
                    result = hugebrain.degrees(hugebrain.asin(B / C))
                    print(result)
            if choice3 == "a":
                if A != 0 and B != 0:
                    result = hugebrain.degrees(hugebrain.atan(A / B))
                    print(result)
                if A != 0 and C != 0:
                    result = hugebrain.degrees(hugebrain.asin(A / C))
                    print(result)
                if B != 0 and C != 0:
                    result = hugebrain.degrees(hugebrain.acos(B / C))
                    print(result)

        if choice2 == str(2):
            print("This feature is a WIP!")

    if choice1 == str(3):
        break

print("-" * 60 + "\n\nThank you for using triangles and fixing your horrible life!\n\n" + "-" * 60)
