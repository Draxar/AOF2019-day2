# we need to get 19690720
# OBSERVATIONS:
# verb is impactiong only 2 last digits
# probably circularly 0=76, 1=77 ... 98=74, 99=75
# so verb should be probably 44
# I could probably bruteforce 100*100 combinations
# output seems to be bigget when  bigger when the noun is bigger
# manual divide and conquer should easly apply

#input from stdin
#program = list(map(int,input().split(",")))

#hardcoded input
program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,2,155,1,9,155,0,99,2,0,14,0]
noun = 84
verb = 44

#prep program
itr = 0
process = True
program[1] = noun 
program[2] = verb

#process program
while process:
  if program[itr] == 99:
    process = False
  elif program[itr] == 1:
    program[program[itr+3]] = program[program[itr+1]] + program[program[itr+2]]
  elif program[itr] == 2:
    program[program[itr+3]] = program[program[itr+1]] * program[program[itr+2]]
  itr += 4
print("---RESAULT---")
print(program[0])
print("-------------")