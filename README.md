# docassemble.CTLFinal

A docassemble extension.

## Author

Aubrie Souza, asouza@su.suffolk.edu

## Disclaimer 

This is intended for demonstration only. It produces an example document and is for demonstration only. It should not be implemented into existing interviews without refinement detailed below. 

## Watch a demo [here](https://drive.google.com/file/d/1kuxp9cIMHZ81zdmBuTUbrhzZKCH1d4bd/view?usp=sharing)

Note: This video was made prior to most testing. Some of the pages have more information or instructions on them where users asked for it. The searching mechanism works the same as in this video. 

## Watch a technical explanation [here](https://drive.google.com/file/d/1X6kBxrgeTFffkUJgtmP66jYEPYKIMaSQ/view?usp=sharing)

This project uses the python module mechanize, regex, and the yml file. This video walks through how those pieces work together to return the result.  

## Project Biography

        TLDR:

The Document Assembly Line Project is producing mobile friendly, online court forms that can be downloaded or sent directly to Massachusetts courts. This repo contains a prototype to demonstrate that the existing forms could implement a web scrapper to assist the users in filling out their form inside the interview framework rather than directing them to gather the information themselves from court websites. You will notice that this scrapes the Connecticut case look up site rather than Massachusetts; the Massachusetts site has a reCAPTCHA that presented technical challenges not within my abilities at the start of the project. 
    
        Problem:

In March 2020, the COVID-19 pandemic hit and courts around the country had to close their doors to the public. This left those already struggling with access to the court and representation with no one to turn to. In Massachusetts, there were stories of individuals calling the court clerks to fill out forms over the phone but this was not a long term solution for anyone, not the clerks nor those seeking help. 

The Document Assembly Line Project sought to address the access gap by creating mobile-friendly, online versions of court forms and pro se materials. Since March, volunteers from all over the world have jumped in to volunteer their time to bring these forms to life. The team  focused on urgent matters related to housing and domestic violence first, and is expanding to address more regular filings at the trial and appellate level. Today, the project has 19 unique interviews to help people address urgent legal issues, with more reaching production every day. Using these interviews, pro se users can produce their own legal document from their cell phones or computers. Some forms can be submitted directly to the court where others provide instructions to contact the court on how to proceed with filing. 

I joined the project in June and saw the court filing required information that a user is unlikely to remember or know off the top of their hand. The Document Assembly Line has the instructions ([see example](https://github.com/SuffolkLITLab/docassemble-CTLFinal/blob/main/instructions.png)) on how to find all this necessary information. However, following these instructions requires the user leave the interview, follow the instructions to another source for information, accurately parse their information, and bring it back into the interview. This is not a seamless experience; it disrupts the user in the middle of the interview. For those who are not familiar with legal information it may be overwhelming, if you are disabled or do not have the ability to manage two consecutive tasks it is a bigger ask than we think as regular users of these systems. However, the courts often have a lot of this information already stored on their court websites. 

        This Product:

My goal was to create a tool that would allow the user to search for their relevant information if they did not have it within the interview, never leaving the page. This project is a working protype of how a web scraper can be built right into the interview so the user can look up their case without leaving the interview. 

The web scrapper takes simple search criteria, a single party's first name and last name, most likely the user themselves, and searches the CT Judicial Court site. Then, it displays on the next page all cases that have a party with that name and their corresponding docket numbers. For some, that list is short and you can quickly identify your party name. If you are John Smith, we see why the protype is just that, a demonstration, because it returns 50 This version has limitations, but it begins to build a tool that helps individuals stay within our framework, it guides them the same way, however a computer does the clicking and readings behind the scenes. They only have to read the results, rather than read the instructions, follow them accurately, capture the information properly, and bring it back into our framework as directed. It cuts out steps that are not building for the user. For this court website it takes 8 steps from opening a new tab to seeing your results to search through. Once the user encounters the tool it takes a single step, the input of the search criteria, to obtain the case information. It makes it simpler. 

        Key Stakeholders:

The Document Assembly Line, court clerks, and the users of courtformsonline.org. 

        Good things:

* It works – this scraper can be used for Connecticut civil, family, housing and small claims cases in the Superior Court. It would let a user find their case name and docket number quickly within the platform. It is a demonstration of how allowing scraping for these purposes can benefit individuals. I asked a tester how they would feel about using the results the response was that "Assuming I'm somewhat familiar with my case, this is great. I'd trust that answers were mine once I saw what I was looking for." It is true that the limited information requires that the user to have some recognition. Now that I have an understanding of how to built out a scraper I would want to build more pieces in and consider what information is pulled in more to make it most helpful. 

* You can clearly see how searching in the framework can be simple, easy, and user friendly. This prototype is a start, but can be expanded to allow for higher refinement of the search equal to the actual site. It would just take a little more time. It took about 2 months to build up my understanding to make it work, but now I feel like I can begin to reach deeper into *how* it works. It is a matter of investment. 

* An early tester provided feedback that they felt a need for instruction on what the results tell them. They weren't sure why there were dashes between sections of the docket number and if they needed them or if that was because the column returned in a weird format. I was having trouble adding test to the subquestion for id: display result because it would cause a break in formatting in the table. However, I realized that I needed to add a line break in the module rather than the yml and it allowed me to add the subquestion with information and provide more help to the user.

        Things to work on:
    
* The table is risk prone. Rather than creating sets that keeps the docket number paired with its corresponding case name, it runs two regex that separates them into categories. If there is a misalignment, all the cases below will be incorrectly matched with a docket number. Fixing this would require creating a regex that parses for both the docket and case name and then lower in the module separating the groups. 

* Edge cases in the case_name regex where there is not two formal parties, such as an *In Re* case is not captured by the regex. This would disrupt the table as described above. This would need to be resolved prior to any launch.

        Next Steps
    
Continuing to build on this exact model may not be beneficial. However, using this as a demonstration may further the conversation with the Massachusetts court. Building a more robust implementation for the Document Assembly Line based off of this model would result in a more usable task.   

        Research:

This project started off as a legal research exercise. It was necessary to address the question of whether accessing the data held on the court websites by a web scraper was legal.  The Massachusetts Trial Court Electronic Case Access site terms prohibits any data harvester from accessing the database. Additionally, the site has a RECAPTCHAs. Recently, hiQ Labs, Inc v. LinkedIn Co., held that scraping publicly available data is not illegal under the Computer Fraud and Abuse act. 938 F. 3d 985 (9th Cir. 2019). The Massachusetts court website is public: you do not need a log in to access the entire site which makes it more public than the site in hiQ Labs, however, the express prohibition against scraping and navigating around the reCAPTCHAs presented a legal challenge as well as a technical one. Where the limited legal precedent tended to say that if we handled the reCAPTCHA properly, such as displaying it to the user before running the scraper through the mass site, it was likely to withstand a legal challenge where circumventing the reCAPTCHA has been considered a violation of 17 U.S.C § 1201. However, handling the reCAPTCHA technically was a technical challenge that I was simply not prepared for. Oddly enough, an extension I have on my browsers to block online ads had hidden the reCAPTCHA from me while I was preparing to tackle the technical lift. Only when I opened it in an incognito browser did I realize I had hit a wall technically. 

Feeling confident that the reCAPTCHA presented a problem both technically and legally, I turned to think about how to build the skills necessary to someday come back to the Massachusetts site. I explored alternative jurisdictions and being familiar with the Connecticut State website, found that their site was simple to navigate and did not present the same challenge. Their [terms and conditions](https://www.jud.ct.gov/terms.htm) were less restrictive: the site prohibited bulk extraction and web harvesting aka web scraping, however this tool is not performing any task in bulk. The tools is designed to work the same as if the user is accessing the court, it reads it and then forgets the information. There is no bulk collection or mass access into the system. Additionally, if it became questionable, the court has a contact to reach out to for permission. Knowing that building the tool was a risk, I felt most comfortable using this site as tester. 

Then, I had to research how to built the tool. I started looking at [another scraper](https://github.com/SuffolkLITLab/docassemble-DVhotline/blob/master/docassemble/DVhotline/dv_hotline.py) that had been built by other members of the Assembly Line to figure out what I needed. I would be using the module "mechanize" which required reading through the documentation online. The documentation is all written in a manner that I am not familiar with – it uses technical terms that I have not encountered or have a real framework for in my coding experience. I've been informally trained so that I know how to make things work, but I'm not always able to explain why, I know what connects and how to write it but I don't have the information organized in anyway. So, the mechanize documentation was not very friendly. However, working with Michelle, she helped me understand what pieces I needed to pay attention to and what I could ignore, how to build slowly line by line, and how to see what was happening in my code by logging in the browser console. I was then able to expand upon my regex research and look into using more complicated capturing groups to extract the information. I often explored multiple options for technical solutions and presented them to Michelle who helped me understand why some would benefit me over others. Stack Overflow examples of others questions helped provide a visual example of what I was working on even if it wasn't going to look the same. The technical research is difficult to do on your own if you do not speak the language. I was lucky to have a partner who helped expand my ability to find the information for myself as I built up the skill.  

        User Feedback:

*Tester 1:*

* Look is great that it is grey and white changing, readability is good 
* Unclear whether the dashes in the docket number are supposed to be there, could use an indication about formatting and what I would need to write down if I wasn't copy/pasting with my keyboard 
* What happens if my case isn't here? 
* Feel like I can trust the information that appears if I have some recognition, but if I am coming into this blind it might be hard. 

Response: 

I added a hint with the format of the docket number for id: show results and id: docket number to help the user capture the format. I also added a search again button so they can go back and retype easily. 

*Tester 2:*

If you don't know the docket number, which I assume most people won't, I found it difficult to copy both the case name and docket number for the next two search pages. I had to copy the whole thing, paste it for docket number, then cut out the case name, click "continue", and then paste the case name in. Is there a way to make the "docket" and "case name" in the same search field? Or if not, on the same search page, rather than enter "docket" number, click continue, and then enter case name.

Response: 

I agree that copying and pasting is not the ideal interface to collect the information. If I had more time to refine the technology, I would allow the user to select which case was theirs, each line being a single choice. Then, when you moved to the next questions it would populate the case name and docket number as the default for the following questions. 

*Tester 3:*

* It asks for the docket number to search and my fake name didn't return any results, but it wasn't clear that there was no matches. It would be helpful is there were no matches it returned a message. 

Response: 

I tried to set it so that if there were no matches it would return a message rather than the table but was not successful. Added an [issue](https://github.com/SuffolkLITLab/docassemble-CTLFinal/issues/5)

*Tester 4:*

Could you get to the point where instead of writing down the docket number and case name, you could just click on them and it take you to it? Bring in the link so they can see the page? 

Response: 

Yes! I was able to capture the links to each page with my regex but it when you tap on the hyperlink it is a dead link. My experience with capturing the proper parts of the HTML was too limited to make the links work in the time frame. I was so close. It would be helpful to allow the user to check that the case information presented matches with theirs by seeing the whole page. For example, I saw plenty case names that were the same, but had different docket numbers. It is definitely a needed feature and possible in the next iteration. 

        Closing thoughts:

I have had to pivot and reassess what was possible after deciding on this project. My original idea which was to return the same results but for the Massachusetts court website because my technical abilities limited me. I explored alternative jurisdictions that have adopted this project, but met the same issue with reCAPTCHA on the sites. I explored a few paths that would have made this prototype more impressive, such as brining in the link to each page, but wasn't able to reach my stretch goals in time. However, it is clear that they are obtainable with continued work. See the regex that captures the hyperlink to each case [here](https://github.com/SuffolkLITLab/docassemble-CTLFinal/issues/3). 

That aside, I believe that if presented to the Massachusetts Court for demonstration it would progress the conversation between the Assembly Line and the Court where we have not had success convincing the court that access to masscourts.org through their API. Even if we could not build straight into their programs, permission to work around the reCAPTCHA would address the legal concerns. Additionally, permission is beneficial because it prevents the need to set a precedent. Scraping of court websites is not always a benefit. Permission in this singular use would avoid opening the doors to any and all web scraping. 

In the end, I am excited that I built the technical skill and understanding. That also means, I know its not ready for use. It is making too many assumptions, all of the search criteria should be brought in for the user to determine, and it should be parsing the case name and docket numbers together rather than making them their own lists. However, having gained enough understanding to know that it isn't ready is also a success. Its important to know where our creations fail and I certainly am ready to continue to build to eliminate as many of those failures as possible to make this a useable tool. 
