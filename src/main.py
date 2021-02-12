from lexer import Lexer

if __name__ == "__main__":
   while True:
      lexed_input = input(">>> ")
      if lexed_input == "gtfo()":
         exit()
      else:
         lexer_sen = Lexer(lexed_input)
         print(lexer_sen.main())