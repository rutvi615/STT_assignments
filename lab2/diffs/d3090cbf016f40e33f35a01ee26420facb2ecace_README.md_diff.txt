@@ -106,7 +106,7 @@ Ciphey旨在成为一种工具，用于自动执行许多解密和解码，例
 <sub><b>魔术笔记 </b>CyberChef与Ciphey最相似的功能是Magic。魔术在此输入上立即失败并崩溃。我们迫使CyberChef竞争的唯一方法是手动定义它。</sub>
 
 
-我们还使用** 6gb文件**测试了CyberChef和Ciphey。 Ciphey在** 5分钟54秒内破解了它。 CyberChef在开始之前就系统崩溃了。
+我们还使用**6gb文件**测试了CyberChef和Ciphey。 Ciphey在5分钟54秒内破解了它。 CyberChef在开始之前就系统崩溃了。
 
 
 
@@ -132,44 +132,44 @@ Ciphey旨在成为一种工具，用于自动执行许多解密和解码，例
 | ------------------ | ------------- | ------- | ------- | 
 | 📖 [安装指南](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [文献资料](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) | 🐋 [Docker 文献资料](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey)
 
-## 🏃‍♀️Running Ciphey
-There are 3 ways to run Ciphey.
-1. File Input `ciphey -f encrypted.txt`
-2. Unqualified input `ciphey -- "Encrypted input"`
-3. Normal way `ciphey -t "Encrypted input"`
+## 🏃‍♀️运行 Ciphey
+有3种方式可以运行Ciphey。
+1. 文件输入 `ciphey -f encrypted.txt`
+2.不合格输入 `ciphey -- "Encrypted input"`
+3. 正常方式 `ciphey -t "Encrypted input"`
 
-![Gif showing 3 ways to run Ciphey](Pictures_for_README/3ways.gif)
+![Gif显示3种运行Ciphey的方法](Pictures_for_README/3ways.gif)
 
-To get rid of the progress bars, probability table, and all the noise use the quiet mode.
+要消除进度条，概率表和所有杂音，请使用安静模式。
 
 ```ciphey -t "encrypted text here" -q```
 
-For a full list of arguments, run `ciphey --help`.
+有关命令的完整列表，请运行 `ciphey --help`.
 
-### ⚗️ Importing Ciphey
-You can import Ciphey\'s main and use it in your own programs and code. `from Ciphey.__main__ import main`
+### ⚗️ 导入Ciphey
+您可以导入Ciphey\'s main，并在您自己的程序和代码中使用它。 `from Ciphey.__main__ import main`
 
-# 🎪 Contributors
-Ciphey was invented by [Brandon](https://github.com/bee-san) in 2008, and revived in 2019. Ciphey wouldn't be where it was today without [Cyclic3](https://github.com/Cyclic3) - president of UoL's Cyber Security Society.
+# 🎪 制作者
+Ciphey是由[Brandon]制作的(https://github.com/bee-san) 在2008年，并在2019年复活。如果没有[Cyclic3](https://github.com/Cyclic3) - UoL网络安全协会主席。，Ciphey将不会是今天的样子 
 
-Ciphey was revived & recreated by the [Cyber Security Society](https://www.cybersoc.cf/) for use in CTFs. If you're ever in Liverpool, consider giving a talk or sponsoring our events. Email us at `cybersecurity@society.liverpoolguild.org` to find out more 🤠
+Ciphey由[网络安全协会](https://www.cybersoc.cf/)进行了复兴和重建以用于CTF。如果您曾经在利物浦，请考虑发表演讲或赞助我们的活动。 给我们发电子邮件`cybersecurity@society.liverpoolguild.org` 以了解更多🤠
 
-**Major Credit** to George H for working out how we could use proper algorithms to speed up the search process.
-**Special thanks** to [varghalladesign](https://www.facebook.com/varghalladesign) for designing the logo. Check out their other design work!
+**主要信用** 感谢George H找出如何使用适当的算法来加快搜索过程。
+**特别感谢** 至 [varghalladesign](https://www.facebook.com/varghalladesign) 用于设计徽标。查看他们的其他设计工作！
 
-## 🐕‍🦺 [Contributing](https://github.com/Ciphey/Ciphey/wiki/Contributing)
-Don't be afraid to contribute! We have many, many things you can do to help out. Each of them labelled and easily explained with examples. If you're trying to contribute but stuck, tag @bee-san or @cyclic3 in the GitHub issue ✨
+## 🐕‍🦺 [参与制作](https://github.com/Ciphey/Ciphey/wiki/Contributing)
+不要害怕参与！您可以做很多事情来帮助我们。它们每个都带有标签，并通过示例轻松解释。如果您想贡献但被停止，请在GitHub问题中标记 @bee-san或 @cyclic3✨
 
-Alternatively, join the Discord group and send a message there (link in [contrib file](https://github.com/Ciphey/Ciphey/wiki/Contributing)) or at the top of this README as a badge.
+或者，加入Discord群组并在那里发送消息 (链接在 [(https://github.com/Ciphey/Ciphey/wiki/Contributing)) 或在本自述文件的顶部作为徽章。
 
-Please read the [contributing file](https://github.com/Ciphey/Ciphey/wiki/Contributing) for exact details on how to contribute ✨
+请阅读[参与制作文件]](https://github.com/Ciphey/Ciphey/wiki/Contributing) 有关如何参与制作的细节 ✨
 
 By doing so, you'll get your name added to the README below and get to be apart of an ever-growing project!
 [![Stargazers over time](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)
-## 💰 Financial Contributors
-The contributions will be used to fund not only the future of Ciphey and its authors, but also Cyber Security Society at the University of Liverpool.
+## 💰 财务贡献者
+这些捐款将不仅用于资助Ciphey及其作者的未来，而且还将用于利物浦大学的网络安全协会。
 
-GitHub doesn't support "sponsor this project and we'll evenly distribute the money", so pick a link and we'll sort it out on our end 🥰
+GitHub不支持“赞助此项目，我们将平均分配资金”，因此选择一个链接，我们将对其进行最终整理 🥰
 
 ## ✨ Contributors
 感谢这些很棒的人([表情符号](https://allcontributors.org/docs/en/emoji-key)):
@@ -214,4 +214,4 @@ GitHub doesn't support "sponsor this project and we'll evenly distribute the mon
 <!-- prettier-ignore-end -->
 <!-- ALL-CONTRIBUTORS-LIST:END -->
 
-This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
+该项目遵循 [all-contributors](https://github.com/all-contributors/all-contributors) 的规范。 欢迎任何形式的捐助和帮助!
