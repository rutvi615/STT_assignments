@@ -10,17 +10,21 @@ That's the point. You don't know, you just know it's possibly encrypted. Ciphey
 Ciphey uses a deep neural network to guess what something is encrypted with, and then a custom built natural language processing module to determine the output.
 
 Ciphey can solve most things in under 3 seconds.
+[![asciicast](https://asciinema.org/a/XTy9UvvXYTd5tOeSi4jK9KdVh.svg)](https://asciinema.org/a/XTy9UvvXYTd5tOeSi4jK9KdVh)
+
 # Features
-* Ciphey supports over 20 kinds of encryptions, such as hashes, encodings (binary, base64) and normal encryptions like Caesar cipher, Transposition and more. For the full list, check this out (LINK HERE)
-* Ciphey's deep neural network helps it target the right encryption method the first time around, resulting in decryptions taking less than 3 seconds. If Ciphey cannot decrypt the text, Ciphey will use the neural network analysis to give you information on how to decrypt it yourself.
-* The custom built natural language processing module is designed to be fast and accurcate. Ciphey can determine whether something likely isn't Engllish in a fraction of second, and it can determine for sure if something is English in < 0.5 seconds.
-* Ciphey can support multiple languages (at present, only English.)
-* Supports hashes & encryption methods, which the alternatives such as CyberChef do not. Also, it is physically quicker to pipe in data to Ciphey than it is to copy and paste it into a website with bloated JavaScript.
-MAYBE TOO MANY FEATURES???
+
+- **20+ encryptions supported** such as hashes, encodings (binary, base64) and normal encryptions like Caesar cipher, Transposition and more.
+- **Deep neural network for targetting the right decryption** resulting in decryptions taking less than 3 seconds. If Ciphey cannot decrypt the text, Ciphey will use the neural network analysis to give you information on how to decrypt it yourself.
+- **Custom built natural language processing module** Ciphey can determine whether something is plaintext or not. It has an incredibly high accuracy, along with being fast.
+- **Multi Language Support** at present, only English.
+- **Supports hashes & encryptions** Which the alternatives such as CyberChef do not. 
+- 
 # Getting Started
 ## Installation
 ### Pip
 ```pip3 install ciphey```
+
 ```ciphey -t "encrypted text here"```
 To run ciphey.
 
@@ -32,23 +36,33 @@ To run ciphey
 To get rid of the progress bars, probability table, and all the noise use the grep mode.
 ```ciphey -t "encrypted text here" -g```
 For a full list of arguments, run `ciphey -h`.
+
+It is also possible to pipe data into Ciphey, or to use Ciphey like `ciphey 'encrypted text here'`
 ### Importing Ciphey
 You can import Ciphey\'s __main__ and use it in your own programs and code.
 This is feature is expected to expand in the next version.
 ### FAQ
+
+<details>
+  <summary>Click to expand!</summary>
+  
+  ## Curious about the neural network or language checker? 
+	* The documentation is your friend
+  ## The Internal Data packet
+  * Passed around in the program, it is `{"lc": self.lc, "IsPlaintext?": True, "Plaintext": translated, "Cipher": "Caesar", "Extra Information": "The rotation used is {counter}"}
+`
+	## What new features were added?
+	* Read the changelog.md
+</details>
+
+
 MAKE THIS COLLAPSABLE
 
-Curious about the neural network or language checker? Read /docs
-The Internal Data Packet
-Changelog.md
 # Contributors
 ## Contributing
 Please read the contributing file.
 ## Code Contributors
-Harlan ****
-None
+Cyclic3
 ## Financial Contributors
 
 <a target="_blank" href="https://icons8.com/icons/set/binoculars">iOS</a>, <a target="_blank" href="https://icons8.com/icons/set/binoculars">iOS Filled</a> and other icons by <a target="_blank" href="https://icons8.com">Icons8</a>
-
-
