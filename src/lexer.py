import re as regex
from words import words


class Lexer:
   def __init__(self, sen):
        self.sen = sen
        self.sen_lexed = list(self.sen)
        self.ints = words['ints']
        self.ops = words['ops']
        self.seps = words['seps']
        self.token_list = []

   #CHECK METHODS
   def remove_whitespace(self):
      for l in self.sen_lexed: 
         if l == " ":
            self.sen_lexed.remove(" ")
         else: 
            pass
   
   def empty(self):
      if self.sen == "":
         return True
      else:
         False
   
   #TOKEN MANIPULATION
   def update_token_list(self, token):
      self.token_list.append(token)
   
   def check_tokens(self): 
      len_sen_lexed = len(self.sen_lexed)

      for i in range(0, len_sen_lexed):
         #CHECKS FOR INTS
         if self.sen_lexed[i] in self.ints:
            temp_token = self.sen_lexed[i]
            self.update_token_list(f"INT: {temp_token}")
         
         #CHECKS FOR SEPERATORS
         elif self.sen_lexed[i] in self.seps[0][0:2]:
            seps_index = self.seps[0].index(self.sen_lexed[i])
            temp_token = self.seps[1][seps_index]
            self.update_token_list(f"SEP: {temp_token}")
         
         elif self.sen_lexed[i] in self.seps[0][2][0] and self.sen_lexed[i:3] == self.seps[0][2]:
               self.update_token_list(self.seps[1][2])

         #CHECKS FOR OPERATIONS
         elif self.sen_lexed[i] in self.ops[0]: 
            op_symbol = self.ops[0].index(self.sen_lexed[i])
            temp_token = self.ops[1][op_symbol]
            self.update_token_list(f"OP: {temp_token}")
      
   def main(self):
      if self.empty():
         pass
      else:
         self.remove_whitespace()
         self.check_tokens()
         return self.token_list