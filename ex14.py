from sys import argv
script, user_name=argv
p = "hello"
print(f"hi {user_name}, i'm the {script} script.")
print("i 'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(p)
print(f"where do you live {user_name}?")
lives = input(p)
print("what kind of computer do you have?")
computer = input(p)
print(f"""
alright so you say {likes} about liking me.
you live in {lives}. not sure where that is .
and you have a {computer} computer. Nice.
""" )
