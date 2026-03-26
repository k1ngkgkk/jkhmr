# jkhmr

A WaCkY .png file storage system.

Jackhammer does something no one asked for:
- It jackhammers an image into thousands (or millions) of 1-bit text files.
- Then it glues the rubble back together using pure Python magic.

Video Demo for convinence:
https://youtu.be/8jY0S_f05oo?si=TdwA3B4vBFMQqlI_

Why?
Because we can.
And I have too much free time in my vacations.

---

## process

Deconstruct:
Turns every single bit of a file into its own individual `.txt` file containing either `0` or `1`.

Reconstruct:
Reads the rubble pile in order and rebuilds the original `.png`.

It is slow.
It is inefficient.
It is gloriously unnecessary.

---

## intallation

Clone the repository:

git clone https://github.com/k1ngkgkk/jkhmr.git  
cd jackhammer  

Install dependencies:

pip install -r requirements.txt  

> (Optional) Add the folder to PATH so you can run `jackhammer` globally.

---

## use

Deconstruct an image:

jkhmr deconstruct image.png  

This creates:

rubble/    (will be deleted after)

Reconstruct the image:

jackhammer reconstruct output.png
---

## WARNING

- Use small files unless you enjoy watching your terabytes evaporate.
- Do NOT attempt reconstruction before deconstruction has finished.
---

Have fun.
Do not brick your machine.
If your fan sounds like a jet engine, it is functioning as intended lol.
