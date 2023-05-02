STEP-1: Started an app using command line:

```
django-admin startapp base
```

STEP-2: Created a function to show 'Welcome to django' instaed of django's admin page.

Display:

![SS001](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS001.jpg)

STEP-3: Created app 'base' containing different routes.

STEP-4: Configuring the routing of the apps with project studybud.

Display:

Rerouting to empty route:

![SS002](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS002.jpg)

Rerouting to 'room/' route:

![SS003](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS003.jpg)

STEP-5: Rerouting using templates file.

Display:

Rerouting to empty route:

![S004](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS004.jpg)

Rerouting to 'room/' route:

![SS005](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS005.jpg)

STEP-5: Inheriting templates:

Writing a navigational bar template and inheriting it in the empty route and room route.

Display: 

Rerouting to empty route:

![SS006](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS006.jpg)

Rerouting to 'room/' route:

![SS007](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS007.jpg)

STEP-6: Using for loop

Rerouting to empty route:

![SS008](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS008.jpg)

==========================================================================================
============================================================

# ADVANCED APPLICATION:

STEP-1: Inside the application create a directory template/name_of_the_application 

Since, the application name is base thus the directory will be: **P001/base/templates/base**

STEP-2: Here there is room dictionary inside views. Using the key: name we will access the room page. As shown if I click the name then I will be getting redirected to room page:

Input: Routing to home

DISPLAY: 

![SS009](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS009.jpg)

Input: Clicking 'Let's learn python!'

DISPLAY: 

![SS010](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS010.jpg)

Input: Clicking 'Design with me'

DISPLAY: 

![SS011](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS011.jpg)

Input: Clicking 'Frontend developers'

DISPLAY: 

![SS012](https://github.com/KBhadraGIT/DJANGO-PROJECT/blob/main/P001/base/images/SS012.jpg)

STEP-3: We can route the same thing using url function.

We have changed the **href** that is **href="{% url 'room' room.id %}"**

But this works the same as above.