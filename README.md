# Encryption-and-Decryption-in-Python-Project

## Create the Constructor
In this project, you are tasked to implement a Python class (call it TranspositionCipher) that can encrypt and decrypt a message using the transposition cipher—a simple yet effective way of encrypting a text in a way that becomes unreadable to anyone who doesn’t possess the key to decryption. It relies on scrambling the words in plaintext by rearranging its characters according to a specific algorithm.

The project requires you to implement a TranspositionCipher class incorporating the following elements:

A constructor function that accepts the cipher's key as an argument
A method designated for encrypting a message requiring a single parameter—the plaintext message to be encrypted
A method dedicated to decrypting a message that calls for one argument—the previously encrypted message in ciphertext format
Optional: As an additional challenge—not required for completing the project—you can implement a function outside the TranspositionCipher class, which hacks the columnar transposition cipher, i.e., it decrypts a ciphertext without knowing the key. The function should return the decrypted message and the key.
Consider the following code skeleton included in the downloadable Transposition Cipher.ipynb file:
```
class TranspositionCipher(object): 
        
    def __init__(self, key):
        pass
        
    def encrypt_message(self, message):
        pass
    
    def decrypt_message(self, message):
        pass
```
You might’ve noticed the pass keyword. pass is a unique statement in Python that does nothing. It can be used as a placeholder for future code. Nothing happens when the pass statement is executed, but you avoid getting an error when empty code is not allowed. In the context of this project, it's used in the class skeleton to indicate where you need to add your method implementations.

Your first task is implementing the constructor for the TranspositionCipher class in Python. The constructor will be responsible for initializing new class instances and should take a single argument: the cipher key. The keyword self refers to the instance that is being manipulated.

## Encrypt a Message
Now that your constructor is implemented and the key is known, it’s time to implement the functionality to encrypt a message within the encrypt_message() method. The method should take self and message as parameters, with message being the plaintext message to be encrypted in string format. The method should return the encrypted message as a string.

Encryption using the columnar transposition cipher is done as follows:

1. Select a Message: Start the encryption by determining the message you intend to encrypt.
   
   Example: Let our secret message be

   Learning Python is fun

2. Select a Key: Select a key, which can be any positive integer value.

   Example: Let’s choose six.

3. Construct the Grid: Start creating the grid by forming a row of cells equal in number to your selected key.

   Example: Create a row with six cells.

- / -- / -- / -- / -- / -- / -- /
 	 	 	 	 	 
4. Populate Initial Characters: Fill in the initial characters of your message into the grid, ensuring each cell contains a single character.

   Example: We can fit the first six characters in the grid.
- L	e	a	r	n	i


5. Complete the Grid: Continually add rows having the same length as the original one. Populate them with the subsequent characters from your message until you have exhausted all characters. Remember that space also      counts as a character. 	 

   Example: The grid that would fit all characters in the text has four rows and six columns.

6. Mark Unused Cells: Disregard any remaining unpopulated cells within the grid.

   Example: We need to ignore the final two cells of the last row because no characters are placed inside.

8. Encrypt the Message: Perform the encryption by reading the populated grid column by column, beginning from the top-left corner. Ensure you exclude the unused cells.

   Example: The resulting encrypted message reads

   Lnh egofa nurP nnyiits

## Decrypt a Message
Great job so far! You’ve successfully encrypted your secret message.

Now, to share a secret communication with your friends, they need to be able to decrypt the message you’ve sent them. Therefore, your final task is to construct a decryption method that takes only the encrypted message as a parameter, which should return the decrypted message as a string.

A message’s decryption works like the encryption process but inverted.

1. Select a message to decrypt: Select an encrypted message for which you are given the key.

   Example: Let’s use the following encrypted message:

   Lnh egofa nurP nnyiits

   We know the key for decrypting it is 6.
   
2. Construct the grid: Start creating the decryption grid by forming a row of cells equal in number to the ceiling of the ratio between the length of the message and the key.

   Example: Create a row with ceil(22/6) = 4 cells.

3. Populate initial characters: Fill in the initial characters of your encrypted message into the grid, ensuring each cell contains a single character.

   Example: We can fit the first four characters in the grid.
4. Complete the grid: Continually add rows having the same length as the original one. Populate them with the subsequent characters from your message until you have exhausted all characters. Remember that space also
 counts as a character. And this time, the two unused cells are the final ones from the last column rather than the last row.

   Example: The grid that would fit all characters in the text has six rows and four columns.

5. Encrypt the message: Perform the decryption by reading the populated grid column by column, beginning from the top-left corner. Ensure you exclude the unused cells.

   Example: The resulting encrypted message reads:

   Learning Python is fun
