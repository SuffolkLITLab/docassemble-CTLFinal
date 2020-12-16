# docassemble.CTLFinal

A docassemble extension.

## Author

Aubrie Souza, asouza@su.suffolk.edu

## Project Biography

**About the Document Assembly Line Project** 

The Document Assembly Line Project is producing mobile friendly, online court forms that can be downloaded or sent directly to Massachusetts courts. The project builds an expert tool that presents to the user questions that will collect the answers for their legal document. 

**TLDR:**

The Document Assembly Line run out of Suffolk University Law School's Legal Innovation and Technology Lab set out to address the access to justice gap created by the COVID-19 pandemic. The website scraper is intended as a prototype for a future scraper that could be built into existing interviews rather than as a standalone. 

**Problem:**

In March 2020, the COVID-19 pandemic hit and courts around the country had to close their doors to the public. This left those already struggling with access to the court and representation with no one to turn to. In Massachusetts, there were stories of individuals calling the court clerks to fill out forms over the phone but not solution for anyone seeking help.
The Document Assembly Line Project sought to address the gap by creating mobile-friendly, online versions of court forms and pro se materials. Since March, volunteers from all over the world have jumped in to volunteer their time to bring these forms to life, focusing first on urgent matters related to housing and domestic violence. Today, the project has 19 unique interviews to help people address urgent legal issues, with more reaching production every day. Using these interviews, pro se users can produce their own legal document from their cell phones or computers and submit the work directly to the court or provide instructions for filing where direct filing is not available.  

**Key Stakeholders:**

The Document Assembly Line, court clerks, and the users of courtformsonline.org. 

**The Idea:**

I joined the project in June and saw that consistently, the court filing required information that a user is unlikely to remember or know off hand. The Document Assembly Line has the instructions ([see example](https://github.com/SuffolkLITLab/docassemble-CTLFinal/blob/main/instructions.png))on how to find all this necessary information. However, following these instructions requires the user leave the interview, follow the instructions to another source for information, accurately parse their information, and bring it back into the interview. This is far from a seamless experience; it is a disruption in the middle of the interview. However, the courts often have a lot of this information already stored on their court websites. 
  My goal was to create a tool that would allow the user to search for their relevant information if they did not have it within the same interview. This project is a working protype of how a web scraper can be built right into the interview so the user can look up their case without leaving the interview. 
	The web scrapper takes simple search criteria, a single party's first name and last name, most likely the user themselves, and searches the CT Judicial Court site. It then, returns all cases that have a party with that name and their corresponding docket numbers. For some, that list is short and you can quickly identify your party name. If you are John Smith, we see why the protype is just that, a demonstration. This version has limitations, but it begins to build a tool that helps individuals stay within our framework, it guides them the same way, however a computer does the clicking and readings behind the scenes. They only have to read the results, rather than read the instructions, follow them accurately, capture the information properly, and bring it back into our framework as directed. It cuts out steps that are not building for the user. For this court website it takes 8 steps from opening a new tab to seeing your results to search through. Once the user encounters the tool it takes a single step, the input of the search criteria, to obtain the case information. It makes it simpler. 

**What works:** 

  It works – this scraper can be used for Connecticut civil, family, housing and small claims cases in the Superior Court. It would let a user find their case name and docket number quickly within the platform. It is a demonstration of how allowing scrapping for these purposes can benefit individuals. I asked a tester how they would feel about using the results the response was that "Assuming I'm somewhat familiar with my case, this is great. I'd trust that answers were mine once I saw what I was looking for." It is true that the limited information requires that the user 

**Things to work on:**
	The search criteria assumes that the user wants to search exactly what is input for first and last name. Hidden from the user is that you can choose to search as "Starts with", "Contains", "Is Equal to" or "Sounds Like". The default choice on the site is "Starts with", but I have the computer selecting 

An early tester provided feedback that they need a little instruction on what the results tell them. They weren't sure why there were dashes between sections of the docket number and if they needed them or if that was because the column returned in a weird format.  


**Research:**

**User Feedback:** 

Tester 1: 

* Look is great that it is grey and white changing, readability is good 
* Unclear whether the dashes in the docket number are supposed to be there, could use an indication about formatting and what I would need to write down if I wasn't copy/pasting with my keyboard 
* What happens if my case isn't here? 
* Feel like I can trust the information that appears if I have some recognition, but if I am coming into this blind it might be hard. 

Response: 

I added a hint with the format of the docket number for id: show results and id: docket number to help the user capture the format. I also added a search again button so they can go back and retype easily. 

Tester 2: 

If you don't know the docket number, which I assume most people won't, I found it difficult to copy both the case name and docket number for the next two search pages. I had to copy the whole thing, paste it for docket number, then cut out the case name, click "continue", and then paste the case name in. Is there a way to make the "docket" and "case name" in the same search field? Or if not, on the same search page, rather than enter "docket" number, click continue, and then enter case name.

Response: 

I agree that copying and pasting is not the ideal interface to collect the information. If I had more time to refine the technology, I would allow the user to select which case was theirs, each line being a single choice. Then, when you moved to the next questions it would populate the case name and docket number as the default for the following questions. 

Tester 3: 

* It asks for the docket number to search and my fake name didn't return any results, but it wasn't clear that there was no matches. It would be helpful is there were no matches it returned a message. 



