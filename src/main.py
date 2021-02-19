from lexer import Lexer
import datetime

melons = "\U0001f348"
happy = "\U0001f600" 

print(f"Logged in: {datetime.datetime.now()} ==> {happy} Welcome to the {melons} Interpretor")


if __name__ == "__main__":
   while True:
      lexed_input = input(">>> ")
      if lexed_input == "gtfo()":
         exit(f"Logged out: {datetime.datetime.now()} ==> Goodbye!")
      else:
         lexer_sen = Lexer(lexed_input)
         lexer_sen.main()