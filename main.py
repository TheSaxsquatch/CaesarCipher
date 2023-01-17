from art import logo

# Alphabet list for the cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar Function as one:
def caesar(direction, t, s):
  
  # Encrypt function
  def encrypt(text, shift):
    result = ""
  
    for i in text:
      if i in alphabet:
        position = alphabet.index(i)
        code_position = position + shift
        result += alphabet[code_position]
      else:
        result += i
    print(f"The encoded message is: {result}")
  
  # Decrypt function
  def decrypt(text, shift):
    result = ""
  
    for i in text:
      if i in alphabet:
        position = alphabet.index(i)
        message_position = position - shift
        result += alphabet[message_position]
      else:
        result += i
    print(f"The decoded message is: {result}")
  
  # Call to functions to run program
  if direction == 'encode':
    encrypt(text=t, shift=s)
  
  elif direction == 'decode':
    decrypt(text=t, shift=s)

# Print logo on function start:
print(logo)

# Loop program:
use_cipher = True

while use_cipher:
# Gathering variables from user input
  user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  user_input = input("Type your message:\n").lower()
  shift_value = int(input("Type the shift number:\n"))
  
  # Valid shift:
  shift_value = shift_value % 26

  
  # Call to ceasar function:
  caesar(direction = user_choice, t = user_input, s = shift_value)

  user_continue = input("Would you like to try another message? Type 'yes' or 'no'.\n")
  user_continue = user_continue.lower()

  if user_continue == 'yes':
    use_cipher = True
  else:
    use_cipher = False
    print("Good-Bye")