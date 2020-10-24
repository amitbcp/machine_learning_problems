## intent:affirm
- yes
- indeed
- agreed
- agree
- that's right
- ok got it
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks a lot
- thank you
- thanks you
- of course
- ofcourse
- sure
- yeah
- ok
- cool
- go for it
- yep
- yep, will do thank you
- I'm sure I will!
- oh awesome!
- Yes
- accept
- I accept
- i accept
- ok i accept
- I changed my mind. I want to accept it
- ok cool
- alright
- i will!
- yop
- yo
- okay, that should do it
- oki doki
- yes please
- yes please!
- yep if i have to
- amayzing
- confirm
- nice
- definitely yes without a doubt
- yasss
- yup
- perfect
- sure thing
- absolutely
- Oh, ok
- Sure
- hm, i'd like that
- ja
- sure!
- yes i accept
- Sweet
- amazing!
- how nice!
- cool!
- yay
- yes accept please
- great thanks
- oh cool
- fine
- i will take that
- that sounds just right

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- goodnight
- good night
- see ya
- toodle-oo
- gotta go
- farewell
- catch you later
- bye for now
- bye
- bye was nice talking to you
- bye bye bot
- bye bot
- talk to you later
- ciao
- Bye bye
- bye!

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hello
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there bot
- hi chat bot
- hi bot
- greetings
- hello everybody
- hello robot
- hallo
- heeey
- hi hi
- hey
- hey hey
- hello there
- hi
- hello
- yo
- hola
- ola
- hi?
- hey bot!
- hello friend
- hii
- hello sweet boy
- yoo
- hey there
- hiihihi
- hello sweatheart
- hellooo
- heyo
- hello?
- Hallo
- heya
- hey bot
- howdy
- Hellllooooooo
- whats up
- Hei
- Heya
- Whats up my bot
- hiii
- heyho
- hey, let's talk
- hey let's talk
- jojojo
- hey dude
- hello it is me again
- what up
- hi there
- hi
- jop
- hi friend
- hi there it's me
- good evening
- good afternoon

## intent:get_budget
 - I want to eat at a place between 300 and 700
 - I am fine with an expensive place
 - I am looking for a dinner place at less than 300
 - I am looking for a cheap breakfast option
 - I am looking for mid range hotels to have a lunch
 - I am looking for place to eat and expensive lunch
 - expensive
 - costly
 - pricey
 - cheap
 - reasonable
 - economical

 ## intent:get_email
<!-- with 'email' entity -->
- can u mail me the information to [abc@abc.com](email)?
- can u mail to [test@tes.com](email)?
- can u mail me at [test-123.456@dom.123.co.in](email)?
- email address - [test.some@gmail.co.in](email). Mail this list.
- email me at [email-123@domina.com](email)
- mail me [emial@domain.io](email)
- my email address [email.123-abc@domain.123.com](email)
- please mail me the list to [123-email@domain.co.in](email)
- please send me the list to [123@domain.net](email)
- please send this to [email.123@123.456.com](email)
- send this to [abc-email@abc.com](email)
- send to [abc_123-email@abc123.com](email)
- this is my email address - [email-abc_123@abc.com.edu](email). send me an email.
- [email1_34-ret@host-name.123.com](email)
<!-- no entity -->
- can u share this information over email?
- can u send me an email?
- mail me the list
- email me a list of top 10 restaurants
- mail me the names of restaurants
- please send me an email
- please share this with me
- send me an email
- share some more restaurant names with me
- share this over mail
- share this information with me over email

## regex:email
- ([\w\.-]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- Find me a place to eat in [Bangalore](location)
- I need a new restaurant in [Bengaluru](location)
- [Bhopal](location)
- help me find restaurant in [Bngalore](location)
- Could you find me a restaurant to eat at [bngalore](location)?
- [Bhubaneshwar](location)
- Can you find me a restaurant in [Bombay](location)?
- [Amritsar](location)
- [erode](location)
- [Jammu](location)
- [Kurnool](location)
- Hey, help me find a restaurant in [Mumbai](location)
- I need to find a restaurant in [Kolkata](location)
- [Pune](location)
- [Cyberabad](location)
- [calcuta](location)
- Find a restaurant for me in [Calcutta](location)
- Where should I eat in [Delhi](location)?
- [Delhi NCR](location)
- Suggest me a good restaurant around [New Delhi](location)
- [Bengaluru](location)
- [Amratsar](location)
- I need to find this restaurant in [Delhi](location)
- [Dilli](location)
- Show me the closest open restaurant in [Chennai](location)
- [Indore](location)
- [Jodhpur](location)
- Hey help me find a restaurant in [Madras](location)
- Help me find a restaurant in [Surat](location)
- Recommend me a restaurant around [Pune](location)
- [Goa](location)
- Could you find a restaurant for me in [Belgaum](location)? 
- [Chandigarh](location)
- [Rajahmundry](location)
- [Ujjain](location)
- Could you find a restaurant for me in [Bengaluru](location)? 
- Would you find me a restaurant in [Allahabad](location)??
- [vadodara](location)
- [Srinagar](location)
- Could you find me a restaurant in [Agra](location)? 
- Pick a restaurant for me, please in [Kochi](location)
- [Mysuru](location)
- How can you help me find a restaurant in [Jamshedpur](location)?
- [Thrissur](location)
- Can you find a restaurant for me in [Chandigarh](location)?
- [Lucknow](location)
- Would you find me a restaurant in [Visakhapatnam](location)??
- Could you find me a restaurant to eat at [Gurgaon](location)?
- [NewDelhi](location)
- [Surat](location)
- [Jamshedpur](location)
- Would you find me a restaurant in [calcutta](location)??
- Okay. Show me some in [bengaluru](location)
- Recommend me a restaurant around [Prayagraj](location)
- [Rourkela](location)
- [Vijayawada](location)
- [Ajmer](location)
- [Allahabad](location)
- [raurkela](location)
- Can you suggest some good restaurants in [bombay](location)
<!-- only 'cuisine' entity : 26 training samples -->
- I'm gonna need help finding a [indian](cuisine) restaurant
- [american](cuisine)
- i'm looking for a [Chinese](cuisine) restaurant
- Hey, can you help me with locating a [mexican](cuisine) restaurant
- i want a [french](cuisine) restaurant
- [chinese](cuisine)
- What's a good place to eat [mexican](cuisine) food
- Find a restaurant for me where I can eat [north indian](cuisine)
- Find a restaurant for me to eat [mexican](cuisine)
- [italian](cuisine)
- I am hungry, find me some place to go eat [italian](cuisine)
- Would you find a [south indian](cuisine) restaurant for me?
- Would you find a [american](cuisine) restaurant
- [north indian](cuisine)
- A place to eat [chinase](cuisine)
- I want to eat [italian](cuisine) food
- Please find me a [south-indian](cuisine) restaurant
- [south indian](cuisine)
- Quickly get me a [northindian](cuisine) place
- Where can i get [south-indina](cuisine) food?
- I need to find a restaurant [southindian](cuisine)
- [mexican](cuisine)
- A place to have [italian](cuisine) food
- Suggest me a good [mexican](cuisine) restaurant
- how can you help me find a [french](cuisine) restaurant?
- [italian](cuisine)
<!-- location + cuisine entities : 50 training samples -->
- I'm gonna need help finding a [indian](cuisine) restaurant in [Mysore](location)
- i'm looking for a [Chinese](cuisine) restaurant in [Lucknow](location)
- Hey, can you help me with locating a [mexican](cuisine) restaurant in [Lakhanpur](location)
- i want a [french](cuisine) restaurant in [Vizag](location)
- What's a good place to eat [mexican](cuisine) food in [Bangalore](location)
- Find a restaurant for me where I can eat [north indian](cuisine) in [Jaipur](location)
- Find a restaurant for me to eat [mexican](cuisine) at [Faridabad](location)
- I am hungry, find me some place to go eat [italian](cuisine) in [Goa](location)
- Would you find a [south indian](cuisine) restaurant for me in [Kozhikode](location)?
- Would you find a [american](cuisine) restaurant for me in [Trivandrum](location)?
- A place to eat [chinase](cuisine) in [Mysuru](location)
- Hey, can you help me with locating a [north indian](cuisine) restaurant in [calcuta](location)
- I want to eat [italian](cuisine) food in [cochin](location)
- Please find me a [south-indian](cuisine) restaurant in [madras](location)
- Quickly get me a [northindian](cuisine) place in [New Delhi](location)
- Where can i get [south-indina](cuisine) food in [Mangaluru](location)
- i'm looking for a [Chinese](cuisine) restaurant in [cyberabad](location)
- [chinese](cuisine) eating place in [mumbai](location)
- I want to eat [italian](cuisine) food in [Prayagraj](location)
- Okay. I want to eat [south indian](cuisine) in [allahabad](location)
- Okay. Show me some [north indian](cuisine) restaurants in [prayagraj](location)
- What's a good place to eat [mexican](cuisine) food in [chandighar](location)
<!-- no entity : 50 training samples -->
- I need to find a restaurant
- Can you find me a good restaurant?
- Would you be able to search a place to eat?
- A place to have food
- Feeling hungry, can you help
- I am hungry, find a restaurant
- Get me some food quickly
- Pick some place for me to eat quickly
- Where can i get some food to eat
- i'm looking for a restaurant
- how can you help me find a restaurant
- pick a restaurant for me
- please find a restaurant for me
- I'm hungry. Looking out for some good restaurants
- I want to eat
- I am feeling hungry
- I need a new restaurant
- Suggest me a good restaurant
- where should i eat?
- I'm gonna need help finding a restaurant
- Show me an open restaurant
- Find a restaurant for me to eat


## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## intent:ask_restaurant
<!-- only 'location' entity : 58 training samples-->


## lookup:location
<!-- tier 1 cities -->
- Bangalore
- Chennai
- Delhi
- Hyderabad
- Kolkata
- Mumbai
<!-- tier 2 cities -->
- Agra 
- Ajmer 
- Aligarh
- Allahabad
- Amravati 
- Amritsar 
- Asansol 
- Ahmedabad 
- Bareilly 
- Belgaum 
- Bhavnagar 
- Bhiwandi 
- Bhopal 
- Bhubaneswar 
- Bikaner 
- Chandigarh 
- Coimbatore 
- Nagpur 
- Cuttack 
- Dehradun 
- Dhanbad 
- Durgapur 
- Erode 
- Faridabad 
- Firozabad 
- Gulbarga 
- Guntur 
- Gwalior 
- Gurgaon 
- Guwahati 
- Indore 
- Jabalpur 
- Jaipur 
- Jalandhar 
- Jammu 
- Jamnagar 
- Jamshedpur 
- Jhansi 
- Jodhpur 
- Kakinada 
- Kannur 
- Kanpur 
- Kochi 
- Kottayam 
- Kolhapur 
- Kollam 
- Kozhikode 
- Kurnool 
- Lucknow
- Ludhiana 
- Madurai 
- Malappuram 
- Mathura 
- Goa 
- Mangalore 
- Meerut 
- Moradabad 
- Mysore 
- Nanded 
- Nashik 
- Nellore 
- Noida 
- Palakkad 
- Patna 
- Pondicherry 
- Pune 
- Raipur 
- Rajkot 
- Rajahmundry 
- Ranchi 
- Rourkela 
- Sangli 
- Siliguri 
- Solapur 
- Srinagar 
- Surat 
- Thiruvananthapuram 
- Thrissur 
- Tiruchirappalli 
- Tirunelveli 
- Tiruppur 
- Tiruvannamalai 
- Ujjain 
- Bijapur 
- Vadodara 
- Varanasi 
- Vijayawada 
- Visakhapatnam 
- Vellore 
- Warangal

## lookup:cuisine
- american
- chinese
- italian
- mexican
- north indian
- south indian

## synonym:chinese
- Chinese
- Chinase

## synonym:south indian
- south-indian
- southindian
- south-indina
- South Indian

## synonym:north indian
- north-indian
- northindian
- north-indina
- North Indian

## synonym:Bengaluru
- Bangalore
- bngalore
- bengalluru
- Bangalor
- bangalore
- bengaluru

## synonym:Delhi
- New Delhi
- Delhi
- NewDelhi
- Dilli
- Dellhi
- newdelhi
- Newdelhi
- new delhi
- new Delhi

## synonym:Mumbai
- Bombay
- mumbai
- bombay

## synonym:Kolkata
- Calcutta
- kolkata
- kolkatta
- calcutta
- calcuta

## synonym:Chennai
- chennai
- madras
- Madras

## synonym:Hyderabad
- hyderabad
- Secunderabad
- secunderabad
- cyberabad
- Cyberabad

## synonym:Lucknow
- Lakhanpur

## synonym:Mysore
- mysore
- mysuru
- Mysuru

## synonym Kochi
- kochi
- cochin
- Cochin

## synonym:Mangalore
- mangalore
- mangaluru
- Mangaluru

## synonym:Visakhapatnam
- visakhapatnam
- Vizag
- vizag

## synonym:Thiruvananthapuram
- thiruvananthapuram
- trivandrum
- Trivandrum
- Travancore
- travancore

## synonym:Vadodara
- vadodara
- Vadodra
- vadodra

## synonym:Jamshedpur
- jamshedpur
- Jamsedpur
- jamsedpur

## synonym:Rajahmundry
- rajahmundry
- Rajahmundri
- rajahmundri
- Rajamundry
- rajamundry
- Rajamundri
- rajamundri

## synonym:Rourkela
- rourkela
- Raurkela
- raurkela

## synonym:Amritsar
- amritsar
- Amratsar
- amratsar

## synonym:Chandigarh
- chandigarh
- Chandighar
- chandighar

## synonym:Allahabad
- prayagraj
- Prayagraj
- Allahabad
- allahabad

## synonym:Nashik
- nashik
- Nasik
- nasik

## synonym:Pondicherry
- pondicherry
- puducherry
- Puducherry
