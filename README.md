# cineplusnao
A movie ticket purchasing application created in Python using wxGlade. It contains 4 windows: Login, Box Office, Concession, and Ticket

Description of my “Naomy CinePlus” 

Login 

This is the very first window I designed for my system.
with a clean black background and the cinema logo at the top.

I added two fields: 
username and password, 

along with two buttons:
Exit, to close the application
Enter, to validate the login

I placed the text " Welcome  a CinePlus " at the top.

Ticket Booth Window

This window is where the user selects the movie and purchases tickets.

At the top, I placed two cinema logos and a large title that says Taquilla 
I included a dropdown menu so the user can choose a movie, and depending on the selection, the corresponding image is displayed (for example, Spiderman).

I also added controls for selecting:

Ticket type
Quantity
Movie room
And the total price is calculated automatically

When the user confirms, a dialog box appears summarizing everything:

Movie
Room
Number of tickets
Total cost

I designed it so it would be clear, fast to use, and visually pleasant.

Stand Window 

This is the most colorful window, because I wanted it to feel fun and lively—just like a real movie theater concession stand.

I used a bright pink background, and arranged the different combos and products into sections:

Combos

On the left side, I placed the basic combos with small popcorn and drinks.
On the right side, I added larger combos like “Cuates” and “Familiar,” each with its own image.

Individual Products

On the lower center of the window, I added options for individual items:

* Popcorn (small, medium, large)
* Drinks (size and flavor)
* Quantity selector

Each product comes with its own image.

On the right, a confirmation dialog appears summarizing everything the user chose—how many combos, drinks, and popcorn—followed by the subtotal.
There is also a "Next" button to continue with the purchase.

I wanted this window to be very visual, with bright colors and large elements, to make it more eye-catching.

Ticket Window 
For this window, I wanted everything to look very clear and organized, so the user can review the entire purchase before completing it.The background is bright pink, with the colorful design of the window, and it is divided into two main sections: Ticket Booth and Concession Stand

Ticket Booth (Taquilla) Section
In this part of the window, I display all the ticket-related details the user selected earlier:
 Movie: Spiderman
 Room: 2
 Time: 18:00
 Tickets: 4 adults, 9 children under 12
 Subtotal: $950

I designed this summary to ensure the user can quickly verify the movie, the room, and the number of tickets before finalizing.

Concession Stand (Dulcería) Section
Below the ticket summary, I included everything the user picked from the concession window. This section lists all the combos and items added to the order, such as:
 Basic Combos
 Family Combo
 Popcorn Combos
 “Cuates” Combos
And one drink:
 Tamarindo, small size

These items appear just like in the confirmation pop-ups I designed earlier. The ticket booth subtotal is repeated for clarity, although the Dulcería subtotal is included within the final total.

Final Amount
At the bottom of the summary, the complete total is shown:
 Total: $1900

This represents the combined cost of tickets and concession items.

Buttons
To finish the interface, I added two buttons so the user can make the final decision:
- CANCELAR – Cancels the entire operation
- FINALIZAR – It confirms the purchase and takes you to the Ticket window.

  
Technologies Used

- Python
- wxPython
- wxGlade
- Visual Studio Code
- Python 3.13
- PNG/JPG files
- Windows 10/11

  Team Members

- Naomy Arely Ramirez Nepamuceno

  Instructions to Run the Project
  
To open the application, you need to have Python installed on your computer, as well as the wxPython library. Open Visual Studio Code, then in the top-left corner, open the terminal and PRESS "NEW TERMINAL." Type the following:

cd C:\Users\PC\Downloads\wxGlade
python wx.glade.py

Next, in the top-right corner, click on "FILE", select "OPEN", find the file "naocine", and run the project from the top-right corner. The Login window will appear.


The application works as follows:

Login: Enter your username and password.

Box Office: Select the movie, time, room, and ticket type.

Concession Stand: Add products to purchase.

Ticket: A complete summary and the total amount to pay will be displayed.
