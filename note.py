print(" ") or print(' ')=>to print any message or to show output
"#"=>this use to give comment
print(a>b or a>=b or b<a or b<=a)=>output will be true or false
print(f"hello{}world")=>this will print hello ,content inside {string} ,world
a.format(b)=>this is basicaly calling of b by a
print(string1 + string2)=>it prints adding two string
print(" anything" *n)=>it prints anything n times
a=" " or a=' '=>this joins the two print part by putting this in the end of printing part
print(""" a """)=>this print the exactly  part  written  on the editor screen 
 \n=>to go to next line
 \t=>to give space like a  horizontal tab
 print("a\\b\\c")=>this will print a\b\c
 \a=>ascii bell
 \b=>>ascii backspace
 \f=>ascii form skip(go to next form)
 a=input()=>this is the input prototype
 a=input("message")=>by this we can show message and take input as well at the same time
 from sys import argv=>another input method 
 from os.path import exists=>this returns true if file exists and false if does not exist 
 txt=open(filename)=>to open filename
 txt.read()=>to read a file
 print(txt.read()=>to print that content which is present on that file
 txt.write()=>to write anything in the file
 txt.close()=>to close  any file
 txt.truncate()=>to empties the file or clear the file
 len( name of where reading part is stored)=>how long is the input file in bytes
 exists(file name)=>it tells the file exists or not ::true or false
def function_name(argument): =>function prototype
def function_name(*argument): =>this asterisk before argument is used because this argument contain two more argument . and they take input just like script
function_name("argument 1","argument 2")=>function definition
f.seek(position)=>it move to that position 
f.readline()=>to read each line individually
.format(string_name)=>another method to format string
.format(*list_name)=>this is an easy way to apply a list to a format string
words= stuff.split(' ')=>this function will break words for Us
word=sorted(words)=>sorts the words
word=words.pop(0)=>print the first word after popping it off
word=words.pop(-1)=>print the last word after popping it off
if a > b: => this is the syntax of if condition
elif b>a: => this is the syntax of elif ,,which we write after if
else: => it is the either condition of one of them (if or else)
count=['z',2,'rt',5]=>list declaration and initialization  
for a in count=>for loop 
b.append()=>  it simply append to the end of lists and it is the function that list understand;; where b is list
while condition:=> while loop
dictionary style=> mystuff['apples']
module style=> mystuff.apples()
                print(mystuff.tangerine)
class style=> thing=mystuff():
              thing.apples()
              print(thing.tangerine)
is-a=>   You	use	the	phrase is-a	when	you	talk	about	objects	
        and	classes	being	related	to	each	other	by	a
        class	relationship.:
has-a=> You	use	has-a	when	you	talk	about	objects	and	
        classes	that	are related	only	because	they 
        reference 	each	other. 
            
class	=>Tell	Python	to	make	a	new	type	of	thing. 
object=>	Two	meanings:	the	most	basic	type	of	thing,	and	any	instance	of some	thing. 
instance=>	What	you	get	when	you	tell	Python	to	create	a	class. 
def=>	How	you	define	a	function	inside	a	class. 
self=>	Inside	the	functions	in	a	class,	self	is	a	variable	for	the instance/object	being	accessed.
 inheritance=>	The	concept	that	one	class	can	inherit	traits	from	another class,	much	like	you	and	your	parents. 
 composition=>	The	concept	that	a	class	can	be	composed	of	other	classes as	parts,	much	like	how	a	car	has	wheels.
 attribute=>	A	property	classes	have	that	are	from	composition
	and	are usually	variables. 
 is-a=>	A	phrase	to	say	that	something	inherits	from	another,
	as	in	a “salmon”	is-a	”fish.“ 
 has-a	=> A	phrase	to	say	that	something	is	composed	of	other	things
	or	has a	trait,	as	in	“a	salmon	has-a	mouth.”