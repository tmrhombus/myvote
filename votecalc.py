#!/bin/python

from states import states
from pops import pops
from evotes import evotes

totpop    = sum(pops)
totevotes = sum(evotes)

# thanks john
# http://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input
import readline
def complete(text, state):
    for cmd in states:
        if cmd.startswith(text):
            if not state:
                return cmd 
            else:
                state -= 1

readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

thestate = raw_input('Enter state name: (use tab complete to find it, or type "all" for all states) \n')
print("\n\n")

for state,pop,evote in zip(states,pops,evotes):
 if(state==thestate or thestate=="all"):
  print(state)
  print("Population: {} is {:.2f}% of total US population: {}".format(pop,pop*100/float(totpop),totpop))
  print("Electoral votes: {} of {}".format(evote,totevotes))

  frac_opov = 1./float(totpop)
  frac_person_state = 1./float(pop)
  frac_state_usa = evote/float(totevotes)
  frac_person_usa = frac_person_state * frac_state_usa
  frac_myvote = frac_person_usa/frac_opov

  #print("frac_opov          {:.4f}".format(frac_opov        ))  
  #print("frac_person_state  {:.4f}".format(frac_person_state))  
  #print("frac_state_usa     {:.4f}".format(frac_state_usa   ))  
  #print("frac_person_usa    {:.4f}".format(frac_person_usa  ))  
  #print("frac_myvote        {:.4f}".format(frac_myvote      ))  

  if(frac_myvote>1):
   vote="votes"
  elif(frac_myvote==1):
   vote="vote"
  elif(frac_myvote<1):
   vote="of a vote"

  print("One vote counts as {:.2f} {}\n\n".format(frac_myvote,vote))
