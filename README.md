# Secret Santa Name Generator

A text-based Python program that draws names for a group playing Secret Santa while accounting for exclusions of certain draw combinations (e.g. couples who do not want to draw each other's names). Features a file-based I/O, allowing users to input a list of names from a text file and export draw results to a text file.

## Roadmap

The following list details some ideas for further development in the future.

* Preference for cyclical combinations instead of pairings when drawing names; currently program has no preference. A cyclical pattern would make the game more inclusive for everyone participating.
* Option to send emails to every participant informing them of their gift-ee rather than simply storing names in a file. The current situation requires one moderator/bystander to know everyone's Secret Santas in order to distribute the matches. Having the matches sent directly by email makes for more anonymity.
* GUI? Could be a fun way to learn Tkinter.
