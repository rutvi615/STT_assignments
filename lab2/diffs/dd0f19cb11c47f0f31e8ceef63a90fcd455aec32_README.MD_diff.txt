@@ -1,5 +1,5 @@
 <p align="center">
-  <img src="logo.png" alt="Ciphey">
+  <img src="Pictures_for_README/binoculars.png" alt="Ciphey">
 </p>
 
 
@@ -8,81 +8,68 @@
   <img src="https://github.com/brandonskerritt/Ciphey/workflows/Python%20application/badge.svg?branch=master" alt="Ciphey">
 </p>
 
-
+# Ciphey (centered)
+Automated Decryption Tool
 
 # What is this?
-Ciphey is an automated decryption tool.
-You put in encrypted text, and it outputs the decrypted text.
-
-> "What type of encryption?"
-
-That's the point. You don't know. Ciphey will find out and do it for you.
-
-# How does it work?
-You input a string (via a file, or via a terminal)
-
-Ciphey uses a Deep Neural Network to create a probability distribution (softmax). 
-
-This distribution gives how likely it is to be a hash, a basic encoding (hex, binary) or encryption (such as caeser, aes etc)
-Ciphey will then work through each cipher to try and decode it.
-
-Ciphey uses the language module (app/languageChecker) to determine both the language something is written in, and whether or not that string is valid in that language. So Ciphey would say "hello my name is whiteboard" is English. But it wouldn't say "iaid i2iv ria9i" is a language.
-
-Using the probability distribution, Ciphey calls each object on a new thread. Yes, Ciphey is **multi-threaded**.
-
-Ciphey is designed from the groundup to be as fast as physically possible. The second it sees the answer, it will stop and return that answer.
-
-# What encryptions can Ciphey deal with?
-Not just encryptions, but hashes and encodings too.
-
-* Vigenère cipher
-* Affine cipher
-* Transposition Cipher
-* Pig Latin
-* Morse Code
-* Ascii
-* Binary
-* Base64
-* Hexadecimal
-* Caesar Cipher
-* Reverse (palindrome)
-* Sha512
-* MD5
-* Sha1
-* Sha384
-* Sha256
-* Base32
-* Base85
-* Base16
-
-# How to install
-```
-pip3 install ciphey
-```
-
-# How to use
-
-In Terminal:
-
-```
-ciphey -t "encrypted text here"
-```
-
-# How to import Ciphey
-```
-import ciphey.__main__
-x = ciphey.__main__.Ciphey("Encrypted text", grep=True)
-print(x.decrypt())
-```
-
-The grep argument is to make the output greppable, meaning the output is a single string. Without the flag, the output would involve the progress bar.
-
-The `__main__` part is so you can call the package anywhere on your OS like a normal program. ciphey is the name of the folder, `__main__` is the name of the file, Ciphey is the name of the class in that file.
-
-It is possible  to import language checker, the neural network, or any of the decryptor modules by themselves and use them.
-# The internal data packet
-This is the data packet specification Ciphey uses. To pass data around the different modules and to language checker, it is neccesary to use an internal data packet.
-```python
-{"lc": self.lc, "IsPlaintext?": True, "Plaintext": translated, "Cipher": "Caesar", "Extra Information": "The rotation used is {counter}"}
-```
+Ciphey is an automated decryption tool. Input encrypted text, get the decrypted text back.
+> "What time of encryption?"
+That's the point. You don't know, you just know it's possibly encrypted. Ciphey will figure it out for you.
+
+Ciphey uses a deep neural network to guess what something is encrypted with, and then a custom built natural language processing module to determine the output.
+
+Ciphey can solve most things in under 3 seconds.
+[![asciicast](https://asciinema.org/a/FBBM0tgBW86svZmjJzct73oln.svg)](https://asciinema.org/a/FBBM0tgBW86svZmjJzct73oln)
+
+# Features
+
+- **20+ encryptions supported** such as hashes, encodings (binary, base64) and normal encryptions like Caesar cipher, Transposition and more.
+- **Deep neural network for targetting the right decryption** resulting in decryptions taking less than 3 seconds. If Ciphey cannot decrypt the text, Ciphey will use the neural network analysis to give you information on how to decrypt it yourself.
+- **Custom built natural language processing module** Ciphey can determine whether something is plaintext or not. It has an incredibly high accuracy, along with being fast.
+- **Multi Language Support** at present, only English.
+- **Supports hashes & encryptions** Which the alternatives such as CyberChef do not. 
+
+# Getting Started
+## Installation
+### Pip
+```pip3 install ciphey```
+
+```ciphey -t "encrypted text here"```
+To run ciphey.
+
+### Cloning from GitHub
+```git clone https://github.com/brandonskerritt/ciphey```
+cd ciphey && python3 ciphey -t "encrypted text here"```
+To run ciphey
+### Running Ciphey
+To get rid of the progress bars, probability table, and all the noise use the grep mode.
+```ciphey -t "encrypted text here" -g```
+For a full list of arguments, run `ciphey -h`.
+
+It is also possible to pipe data into Ciphey, or to use Ciphey like `ciphey 'encrypted text here'`
+### Importing Ciphey
+You can import Ciphey\'s __main__ and use it in your own programs and code.
+This is feature is expected to expand in the next version.
+# FAQ
+
+<details>
+  <summary>Click to expand!</summary>
+  
+## Curious about the neural network or language checker? 
+* The documentation is your friend at /docs
+## The Internal Data packet
+* Passed around in the program, it is `{"lc": self.lc, "IsPlaintext?": True, "Plaintext": translated, "Cipher": "Caesar", "Extra Information": "The rotation used is {counter}"}`
+## What new features were added?
+* Read the [changelog.md](changelog.md)
+</details>
+
+
+# Contributors
+## Contributing
+Please read the contributing file.
+## Code Contributors
+[Cyclic3](https://github.com/Cyclic3)
+## Financial Contributors
+
+<a target="_blank" href="https://icons8.com/icons/set/binoculars">iOS</a>, <a target="_blank" href="https://icons8.com/icons/set/binoculars">iOS Filled</a> and other icons by <a target="_blank" href="https://icons8.com">Icons8</a>
 
