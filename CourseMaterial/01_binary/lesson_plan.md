## Learning Objective:

- Understand how bits can represent color
- Be able to encode and decode simple bitmaps

## Essential Questions:
- Understand how computers store and represent certain types of information


Today going to talk about pictures
What do people know about how pictures are stored on a computer?

Only thing computers understand: 1's and 0's
Each picture broken down into things called pixels
	Show in preview
	Zoom in
	Just a bunch of small rectangles stuck together
Start easy
	How represent black and white?
		0 represent black (turn lights off)
		1 represent white (turn lights on)
Teacup Picture
	Ask them if they can see what it is
	First row would be encoded 1,1,1, ...
	How would next row be encoded?
		Next row is 1, 0, 0, ...
	Missing row is encoded 1, seven 0's, 1, 1, 0, 1
House Picture
	Have student come up
	decode the following for me
		Missing rows are:
			- two 1's, one 0, seven 1's, one 0, one 1
			- three 1's, seven 0's, two 1's
Pixels can be anything
	What are some examples?
		Legos
			https://9to5toys.com/wp-content/uploads/sites/5/2020/08/LEGO-Art-Marvel-Iron-Man-8.jpg?quality=82&strip=all
		Paintballs
			https://youtu.be/fKK933KK6Gg?t=84

Today going to make our own art
	Going to make your own black and white design on this paper
	Encode it and trade it with someone
	Share to see if you came up with the right thing

After the bring everyone back together
What did we learn?
What is different between what we did and real pictures?
Show real pictures in vim mode

Bonus lesson
	How do we do colors?
	More 1's and 0's!
	RGB slider in word
	Encode their own colored picture
