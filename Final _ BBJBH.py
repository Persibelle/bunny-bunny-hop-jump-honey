import time

# ASCII Art Covers
bunny_ascii = r"""
         (\(\ 
         (-.-) 
        o_(")(")
     Bunny Bunny Hop Jump Honey
  A Rhyming Bunny Adventure Awaits! 🐰✨
"""

carrot_ascii = r"""
     \ | /
     - 🥕 -
     / | \
   ~*~ Golden Carrot ~*~
  You're brave and wise and WON!
"""

strawberry_ascii = r"""
     🍓🍓🍓
    ~*~ Strawberry ~*~
 Silly fun! A berry good run!
"""

lettuce_ascii = r"""
     ______
    /      \
   |  🥬     |
    \______/
  ~*~ Smart Lettuce ~*~
 Wise bunny wins the leafy prize!
"""

potato_ascii = r"""
     (🥔)
  ~*~ Tough Potato ~*~
 Brave and bold, but not too old!
"""

watermelon_ascii = r"""
   🍉🍉🍉
 ~*~ Juicy Watermelon ~*~
 A balance of hop, smarts, and fun!
"""

# Choice Art
bee_ascii = r"""
    \\     //
     \\   //
      \\_//
     (•_•)
     <)   )╯
     /   \   🐝
 A buzzing bee salutes you!
"""

rainbow_ascii = r"""
     🌈🌈🌈
    ~*~ Rainbow Slide ~*~
Down you go, in loops and pride!
"""

squirrel_ascii = r"""
     (\_/)  
    ( •_•)  
    / >🌰  
Friendly squirrel offers a treat!
"""

boogie_ascii = r"""
     (\(\
     ( -.-) 
    o_(")(") ♪ ♫ ♩
  Boogie bunny busts a move!
"""

trail_ascii = r"""
     ~~~~🌀~~~~
 A mystical trail of dancing air
 Whispers guide you with gentle care
"""

# Intro
print(bunny_ascii)
time.sleep(1)
bunny_name = input("\nWhat's your bunny’s name? ")

print(f"\nWelcome, {bunny_name} the bunny of legend! 🐇")
print("You're hopping along, full of honey and hope...")
print("Will your path be silly? brave? or wise?")
print("Your prize awaits beyond the skies! 🌤️")
time.sleep(2)

# Track bunny's personality
brave = 0
wise = 0
silly = 0

# 🐾 Choice 1
print("\n🍯 1. A buzzing bee blocks the trail ahead...")
print("Do you 'wave with glee' or 'hop in dread'?")
choice1 = input("Type 'wave' or 'hop': ").lower()
if choice1 == "wave":
    brave += 1
    print("You're fearless! The bee salutes you. 🐝")
    print(bee_ascii)
else:
    silly += 1
    print("You bounce away in a zig-zaggy loop!")
    print(r"""
      (\_/)
     ( •_•)
    / >🎈 Zig-zag hop away!
    """)

# 🐾 Choice 2
print("\n🌈 2. A rainbow glows — a bridge or a slide?")
print("Will you 'analyze' or 'glide and ride'?")
choice2 = input("Type 'analyze' or 'glide': ").lower()
if choice2 == "analyze":
    wise += 1
    print("You study the angle, then cross like a pro. 🧠")
    print(rainbow_ascii)
else:
    silly += 1
    print("You slip down squealing, giggling with glee!")
    print(rainbow_ascii)

# 🐾 Choice 3
print("\n🌰 3. A squirrel gives you a nut with pride...")
print("Do you 'thank him kindly' or 'snatch and hide'?")
choice3 = input("Type 'thank' or 'snatch': ").lower()
if choice3 == "thank":
    wise += 1
    print("A polite bunny is a wise bunny. 🍂")
    print(squirrel_ascii)
else:
    brave += 1
    print("Bold move! The squirrel is shocked but impressed.")
    print(r"""
     (\_/)  
    ( •_•)  😲
    (___)> 💨  He lets you keep it anyway.
    """)

# 🐾 Choice 4
print("\n🎶 4. A bunny band starts to jam nearby...")
print("Do you 'boogie down' or just 'pass by'?")
choice4 = input("Type 'boogie' or 'pass': ").lower()
if choice4 == "boogie":
    silly += 1
    print("You bust a move! You're the life of the meadow 💃")
    print(boogie_ascii)
else:
    wise += 1
    print("You nod in respect and hop with focus.")
    print(r"""
    (\_/)
   ( •_•) ~♪
   />📚  Keepin' it classy.
    """)

# 🐾 Choice 5
print("\n🌀 5. A whispering breeze pulls you down a trail...")
print("Do you 'follow your gut' or 'wait for detail'?")
choice5 = input("Type 'follow' or 'wait': ").lower()
if choice5 == "follow":
    brave += 1
    print("Your bold hop lands you on an enchanted leaf!")
    print(trail_ascii)
else:
    wise += 1
    print("Patience, young hopper. Smart choice.")
    print(trail_ascii)

# 🏁 Ending
print("\n🌟 Your journey is complete!\n")
time.sleep(1)
print(f"{bunny_name} the bunny made their way through rhyme and risk...")
time.sleep(1)
print(f"Brave: {brave}  |  Wise: {wise}  |  Silly: {silly}")
time.sleep(2)

# Determine Ending
if brave >= 2 and wise >= 2:
    print(carrot_ascii)
    print(f"\nCONGRATS, {bunny_name}! You earned the legendary GOLDEN CARROT! 🥇")
elif silly > brave and silly > wise:
    print(strawberry_ascii)
    print(f"\n{bunny_name}'s silly style brought joy — here's a strawberry for your smile! 🍓")
elif wise > brave and wise > silly:
    print(lettuce_ascii)
    print(f"\n{bunny_name}, the clever hopper, earns a leafy crown of LETTUCE! 🥬")
elif brave > wise and brave > silly:
    print(potato_ascii)
    print(f"\n{bunny_name} was bold and wild — here's a POTATO, tough and mild! 🥔")
else:
    print(watermelon_ascii)
    print(f"\nBalanced and bright, {bunny_name} wins a juicy WATERMELON delight! 🍉")

print("\nThanks for playing Bunny Bunny Hop Jump Honey! 🐇💛")
