# 👉 Day 39 Challenge

Once the word has been picked, the following things need to happen:

1. Prompt the user to type in a letter.
2. Check if the letter is in the word.
3. If it does, output the word with all blanks apart from the letter(s) they've already guessed.
4. Keep a running list of the letters they've used.
5. Count how many times they've picked a letter that **isn't** in the word - more than 6 and they lose.
6. Output a 'win' message if they reveal all the letters.


🥳 Extra points for using [ASCII art](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) to draw the hangman as the player makes incorrect guesses.

Example:

```
🌟Hangman🌟

Choose a letter: i
Nope, not in there.
5 left.

Choose a letter: a
Correct!
__a__

Choose a letter: s
Correct!
s_a__

Choose a letter: u
Correct!
sua__

# Repeat until.....
# If user wins
You won with 5 lives left.

# Loses
You lost!
```

<details> <summary> 💡 Hints </summary>
  
- Check if a letter is in the string: `if inputLetter in string`.
- Try using underscores to show blanks to let the user know how many more letters there are to guess.
- Keep track of letters used.  Try adding each letter chosen to a new list, then checking this list for each subsequent choice.
- Check out our [100 Days of Code forum](https://ask.replit.com/c/100-days-of-code/30) for help.


</details>