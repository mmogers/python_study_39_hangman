# Hangman

This simple game is actually pretty complex. This hangman project combines lists, string manipulation, and slicing, along with other concepts.

It's a bit of a step up, so don't be afraid to check hints and solutions if you're getting stuck. Also, check out our [100 Days of Code forum](https://ask.replit.com/c/100-days-of-code/30) for help.

## Picking from a list randomly

👉 `random.choice()` picks a random item from a list.

Here's a list of words:

`listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]`

To select randomly from this list, we assign `random.choice()` to a variable.  We give `random.choice()` the name of the list in the brackets.

```python
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = random.choice(listOfWords)
```
There's **lots** of other stuff needed to make this program work, but, we'll break that down in the _challenge_ section of today's tutorial.

### Try it out and get randomizing!