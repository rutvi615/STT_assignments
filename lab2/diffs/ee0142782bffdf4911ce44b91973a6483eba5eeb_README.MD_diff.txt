@@ -9,7 +9,7 @@ That's the point. You don't know. Ciphey will find out and do it for you.
 # How does it work?
 You input a string (via a file, or via a terminal)
 
-Ciphey uses a Convulutional Neural Network to create a probability distribution (softmax). 
+Ciphey uses a Deep Neural Network to create a probability distribution (softmax). 
 
 This distribution gives how likely it is to be a hash, a basic encoding (hex, binary) or encryption (such as caeser, aes etc)
 Ciphey will then work through each cipher to try and decode it.
@@ -56,6 +56,7 @@ python main.py
 ```
 
 # The internal data packet
+This is the data packet specification Ciphey uses.
 ```python
 {"lc": self.lc, "IsPlaintext?": True, "Plaintext": translated, "Cipher": "Caesar", "Extra Information": "The rotation used is {counter}"}
 ```
