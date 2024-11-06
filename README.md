# 3D-cube
This is a cube I made in python which has yaw rotation. For anyone who doesn't know what yaw rotation is, it's the type of rotation you see in a microwave. Here's an image to help you understand:<br><br>
![image](https://github.com/user-attachments/assets/3ee70d99-20a3-4190-a8bb-0096f5b176cb)

# How I got inspired
When I was young, I saw the donut.c program and I was fascinated. I wanted to understand how it worked so I checked out the blog and I couldn't understand anything. There was so much math! So fast forward to like a week ago, I randomly remembered that program and I thought maybe I could understand it now. So I opened it up and couldn't understand much. There was 1 thing I understood though which was that it used different 3D rotation matrices to rotate the 3D coordinates of various points and get new coordinates. Now I was familiar with the 2D rotation matrix because of a book I had read and thought to myself, "Why don't I make a rotating square?". And so I did. I wrote a simple algorithm to create a grid(a list containing multiple lists) and I generated coordinates for a square. Then I applied the rotation matrix, got the new set of coordinates and I rounded them off. Then after clearing the grid, I stored the character "." in the new coordinates to get the new rotated square. I did this many times with small rotations and printed each frame in my terminal to get an animation of a rotating square. 

# How I made it 3D
So after making the 2d rotating square, I wanted to make it 3D. I derived a 3d rotation matrix for the yaw rotation. I used an algorithm to make 3d coordinates for points of a cube. I knew how I would calculate the new coordinates, but I didn't know how I could plot it on a 2d grid. I tried the donut.c blog but I couldn't understand much. However after playing around on a 3D graphing calculator, I realised that I just had to plot the x and y coordinate of the 3d point and just take the one with the greater z value and put it instead of any other point with a lower z value. This is what they meant by "z-buffer" in the donut.c blog I think. And I was so satisfied with this that I didn't think about perspective. While typing the code, I realised that just a z-buffer would not be sufficient. So I visited the donut.c blog again and saw the following diagram:<br><br>
<img width="479" alt="Screenshot" src="https://github.com/user-attachments/assets/24e64876-7739-4fc8-a5f8-6a72e402e48b"><br><br>
Now I didn't use this diagram directly. Instead I tried to make a different type of diagram with similar thinking but later I realised it wasn't correct. So I used this thinking itself. If you don't know what I'm talking about you could check out donut.c's blog and scroll down to the part about perspective. So I wrote the code for everything and it still gave me problems. The reason is because my derivation of the 3d rotation matrix was slightly wrong and I realised that after looking it up on google. The thing is I used the same logic used in derivation of the 2D rotation matrix. Instead of XY plane I did it for the XZ' plane(because we're talking about the yaw rotation here) where Z' is the negative Z axis. I chose the negative z axis because the cube I made was in the XZ' region. It was towards the negative z axis. But this thinking was wrong. I was supposed to do it for the XZ plane and not the XZ' plane because the value of the trigonometric functions would be negative automatically when we feed it negative z values. Adding a few minuses to the trigonometric functions could end up giving you the wrong coordinates that you don't want. So I fixed it and derived it for the XZ plane and the program worked! Here's an image of my derivation:<br><br>
![image](https://github.com/user-attachments/assets/364e2e56-1b01-4beb-8ac3-551e01d5e0e7)<br>
It's not very neat and there's not much explanation but yeah.

# How can the 2D rotation matrix be derived
Well if you look it up you'll probably see a different method used than what I'll be explaining here. The method I'm going to be explaining is the one I learnt from a book I had read(SMP advance mathematics, it's a really old book I got from my school library). So when you have any normal set of coordinates, say (x, y) in a unit circle, you can write it in the form of a matrix being multiplied by a vector. 
[1  0] [x]
[0  1] [y]
This is also called an identity matrix. Upon expanding it, it will give you the same x and y coordinates as before. Now you can also write it in another form:
x(1), y(0)
 (0),  (1)
Here, (1 0) is the x axis' coordinates and (0 1) is the y axis' coordinates.
Now if you rotate the x and y axis by a common angle, let's say θ. You will get new coordinates of the x and y axis:
x axis :- (cos θ   sin θ)
y axis :- (-sin θ   cos θ)
So if you make this change in the identity matrix, you will get:
[cos θ   -sin θ] [x]
[sin θ    cos θ] [y]
Expand this and you will get the new x and y coordinates after rotation of θ:
[xcosθ - ysinθ]
[xsinθ + ycosθ]

# What about 3D rotation matrix?
Now apply the same logic as in the 2d rotation matrix but for a different plane in the 3d world and you can derive your own 3D rotation matrix.

# Result
![image](https://github.com/user-attachments/assets/bb368f47-d783-40b7-aca1-92895911ecd0)<br>
After running the code many frames like this will be printed creating an animation of a rotating cube. Of course some pixels might be off because the coordinates are rounded off.

It's been a wonderful experience learning about all this stuff and I've really developed an interest in 3D graphics. I've only scratched its surface and there's so much to learn. There might be many things I could change in this program too. I haven't attempted to improve the quality of this program so there might be some changes that could improve this by a lot. Maybe there might be a change which could avoid some of the minor errors in the result. If maybe I've made some mistake in the program or maybe I'm wrong about something or there's something I could have done to make the program more efficient or any observation you've made at all, please do let me know. I'm an absolute beginner in this field and I'll continue learning and sharing some more projects of mine in the future :)

Edit: Through a few very small and easy changes, I added cube2.py in which the cube spins around its own axis instead of revolving around a different fixed axis (which makes it do a yaw rotation). Basically I just shifted the origin to the center of the cube instead of in front of the cube.

Another edit: I added another direction of rotation to cube2.py<br>
Here's my derivation of the new coordinates:<br>
![image](https://github.com/user-attachments/assets/5b465989-b7aa-4adc-a5c0-b3cfdd0ba276)

# Result of cube2.py with rotation in 2 directions
![image](https://github.com/user-attachments/assets/2d144c40-6bf5-4a05-96cc-5ca9985df809)<br><br>
Again, many frames like this are printed to create an animation. Run this code in your command prompt/terminal to see it for yourself
