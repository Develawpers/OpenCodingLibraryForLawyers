def my_func1():
    print("Is your firm/company compelled to appoint a DPO? Answer Yes or No to the three questions below to find out.")
    print ("\nIs your firm a public authority or body?")

    qInput = input("")
    qInput = qInput.lower()

    if qInput == "yes":
        print("Condition 1 is met, so yes, you must appoint a DPO under the GDPR.")
        ans()

    elif qInput == "no":
        print ("Do your firm's core activities consist of data processing operations that require regular and systematic monitoring of data subjects on a large scale?")
        qInput2 = input("")
        qInput2 = qInput2.lower()

        if qInput2 == "yes":
            print("Condition 2 is met, so yes, you must appoin a DPO under the GDPR.")
        elif qInput2 == "no":
            print("Do your firm's core activities consist of large-scale processing of special categories of data (sensitive data such as personal information on health, religion, race or sexual orientation) and/or personal data relating to criminal convictions and offences?")
            qInput3 = input("")
            qInput3 = qInput3.lower()
            ans()

            if qInput3 == "yes":
                print("Condition 3 is met, so yes, you must appoint a DPO under the GDPR.")
            elif qInput3 == "no":
                print("No, you do not have an obligation to appoint a DPO under the GDPR. Please note that even where the GDPR does not specifically require a DPO to be appointed, it is highly encouraged by the European Data Protection Board as a matter of good practice")
                ans()

            else:
                print(f'{qInput3} is invalid, please try again...')
                return my_func1()
        else :
            print(f'{qInput2} is invalid, please try again...')
            return my_func1()
    else :
        print(f'{qInput} is invalid, please try again...')
        return my_func1()

def ans():
    answer = str(input("Would you like to check again?"))
    if ((answer == "yes") or ( answer == "Yes")):
            my_func1()
    elif((answer == "no") or (answer == "No")):
        print("Have a good day!")
    else:
        print(answer, "is invalid")
        return ans()

my_func1()
