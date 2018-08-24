from sys import argv
from os.path import exists
script , from_file , to_file , too_file = argv


print(f"copying from {from_file} , {to_file} to {too_file}")
in_file=open(from_file)
indata=in_file.read()
inn_file=open(to_file)
inndata1=inn_file.read()
print(f"the input file is {len(indata)} bytes long")
print(f"the input file is {len(inndata1)} bytes long")
print(f"does the output file exist? {exists(to_file)}")
print(f"does the output file exist? {exists(too_file)}")
print("ready,hit RETURN to continue, CTRL-C to abort.")
input()
out_file=open(too_file,'w+')
out_file.write(indata)
out_file.write(inndata1)
print("alright,all done")
out_file.close()
in_file.close() 
inn_file.close()