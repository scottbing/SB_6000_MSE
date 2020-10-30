Execution Instructions<br>
Application Parameters:<br>
-a author number [21, 24, 29]<br>
-s subfolder ['training', 'test]<br>
-o genuine signature file name (without file extension)<br>
-t genuine signature file name (without file extension)<br>
-f forged signature file name (without file extension<br><br><br>
Sample execution<br>
compare.py -a 021 -s training -o tinygenuine-01 -t tinygenuine-03 -f tinyforged-01<br>


Image file preprocessing<br>
1.) Al images must be identical in size and scale<br>
2.) Trim whitespace<br>
3.) Apply greyscale to images<brr>
