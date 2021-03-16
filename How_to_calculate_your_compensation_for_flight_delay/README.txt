## 🍾 1. Who is the develawpeer and how to credit him/hr?

[Giacomo Bertelli](https://www.linkedin.com/in/giacomo-bertelli-2209753b/) used this simple and easy code trick to automate the calculation of the amount of the compensation for flight delays in accordance with [Regulation (EC)261/04](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32004R0261) . 

**[Learn the basic syntax →](https://develawpers.com/How-to-calculate-speeding-fines-under-Italian-law-a803201b6b954d11a59b7c0df4739f3f)**

## 🐜 2. Known bugs

There are no known bugs for this code trick. Want to segnalate one? [Write the author here](https://www.linkedin.com/in/giacomo-bertelli-2209753b/). 

---

## ➡️ 3. Wiki

Let’s assume you would like to automate the amount of the compensation for flight delays for yourself or for your clients. Following you may find the complete Code Strings.

```python
def my_func():
    print("How much can you claim in compensation for your delayed flight? Type here the delay and the distance to find out")
   
    delay = float(input("How many hours of delay?: "))
    distance = float(input("How many kilometers away?: "))
   
    if delay<3:
        print("You are not entitled to any compensation, sorry")
    elif delay>=3:
        if distance<1500:
            print("You shall receive a compensation amounting to 250€")
        elif distance>3500:
            if delay<4:
                print("You shall receive a compensation amounting to 300€")
            else:
                print("Great, you are entitled to a compensation amounting to 600€")
        else:
            print("That's right, your compensation shall be 400€")
    answer = str(input("Would you like to calculate your compensation again?"))
    if ((answer == "yes") or ( answer == "Yes")):
      my_func()
    else:
      print("Have a good day!")          

my_func()
```

### Let's go more in depth

1**.** First of all, you want to set the following. This is basically the starting point of the program generally known as main function.

```python
def my_func():

	my_func ()
```

2. Let's print out the "welcome" message and the request for the user's input. 
Please note that we only need print() to print out a blank line.  

```python
  print("How much can you claim in compensation for your delayed flight? Type here the delay and the distance to find out")
  print()
   
  delay = float(input("ow many hours of delay?: "))
  distance = float(input("How many kilometers away?: "))
```

3. Let's set our if-elif-else statements. This is not rocket science and it is very basic. We are saying that if the two variables called "delay" and "distance" - which is provided by the user - are smaller or bigger compared to a pre-established number the code strings will print different things accordingly (in accordance with [Regulation (EC)261/04](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32004R0261)  compensation policies).

```python
  if delay<3:
        print("You are not entitled to any compensation, sorry")
    elif delay>=3:
        if distance<1500:
            print("You shall receive a compensation amounting to 250€")
        elif distance>3500:
            if delay<4:
                print("You shall receive a compensation amounting to 300€")
            else:
                print("Great, you are entitled to a compensation amounting to 600€")
        else:
            print("That's right, your compensation shall be 400€")
```

4. Now let's set our restart function which will allow the user to restart the entire script **if** he ****answers the question positively, otherwise (**else**) it will end. 

```python
  answer = str(input("Would you like to calculate your compensation again?"))
    if ((answer == "yes") or ( answer == "Yes")):
      my_func()
    else:
      print("Have a good day!") 

```

---

## 👨🏻‍💻 4. Use cases

This simple code trick allows the user, whether a jurist or a citizen, to know with just a few clicks the amount - if any - of the compensation for flight delay. Please note that this code trick is applicable only to subject matter that falls within the scope of application of [Regulation (EC)261/04](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32004R0261) . Further guidelines regarding its territorial and material scope can be found here: 

[https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52016XC0615(01)&rid=1](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52016XC0615(01)&rid=1).

In addition, this could also be adapted based on other jurisdiction and services and to automate and streamline similar processes.
