# Caesar Cipher

![ceaserCipher](https://user-images.githubusercontent.com/57579907/211664824-bb4d4eea-89fb-40d7-a2fb-eaf70d61b4d5.png)


### What is a Caesar Cipher?

A Caesar Cipher is an encryption technique. It is a type of substitution cipher where each letter of your message is replaced by a letter with a fixed number of
positions down the alphabet. For example with a shift of 1, A would be replaced by B, B by C, C by D, and so on. In this cipher, we are going to need a string value
as well as a number value to be stored as a shift key for encoding. The arithmetic for the cipher can start by transferring the leters into numbers 0 - 25. 

For this code, the following formulas will be assumed:

![quicklatex com-dca1f01b6a20a73c189d48228c230009_l3](https://user-images.githubusercontent.com/57579907/211665151-0883ed21-85b8-4635-aa84-b5b71abb5e13.svg)
(Encryption Phase with shift n)

![quicklatex com-c467600170f4b71b5d82f39f79b82a67_l3](https://user-images.githubusercontent.com/57579907/211665183-be60fb25-0f07-4e65-9fd8-e0fd0fc94363.svg)
(Decryption Phase with shift n)


### Algorithm for Caesar Cipher: 
#### Input: 
* A String of lower case letters, called Text.
* An Integer between 0-25 denoting the required shift.

#### Procedure: 
* Traverse the given text one character at a time .
* For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text.
* Return the new string generated.
