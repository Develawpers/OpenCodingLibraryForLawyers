## 🔎 Intro

The [mailto protocol](http://www.faqs.org/rfcs/rfc2368.html) is an internet standard (URL scheme) that allows users to create hyperlinks that will directly launch their email client software and compose a new email message.
The mail to syntax allows you to autofill all the fields that you normally find in an email composer, such as the body, subject, senders, cc/ccn addresses. 

---

## 🍾 1. Who is the develawpeer and how to credit him/her?

[Giulio Messori](https://www.linkedin.com/in/giuliomessori/) used the code trick to automate the repetitive emails that his law firm colleagues would send during the normal GDPR privacy compliance assistance. There is no really need to credit the author as he used standard protocols to structure his flow. However, if you wish to send some kudos you can [contact him on LinkedIn](https://www.linkedin.com/in/giuliomessori/).  

**[Learn the basic 'mailto' syntax →](https://develawpers.com/How-to-use-the-mailto-command-to-automate-repetitive-emails-in-your-legal-assistance-764965c3368c4a3f81e89a355943b1e1)**

**[Go to the full use case →](https://develawpers.com/How-to-use-the-mailto-command-to-automate-repetitive-emails-in-your-legal-assistance-764965c3368c4a3f81e89a355943b1e1)**

---

## 🐜 2. Known bugs

There are no known bugs for this code trick. Want to segnalate one? [Write the author here](https://www.linkedin.com/in/giuliomessori/). 

---

## ➡️ 3. Wiki

Let’s assume you maintain the law firm website and need to create mailto links that will make it easy for prospect clients to reach one of the Partners via email.

**1.** Send an email to Mario Rossi (single recipient)

```html
<a href="mailto:mario@lawfirm.com">
```

**2.** Send an email to Mario Rossi and Lucia Bianchi (separate multiple recipients with a comma)

```html
<a href="mailto:mario@lawfirm.com,lucia@lawfirm.com">
```

**3.** Send an email to Mario Rossi but put Lucia Rossi in the CC: list and Franca Verdi in the BCC: list

```html
<a href="mailto:mario@lawfirm.com?cc=lucia@lawfirm.com&bcc=franca@lawfirm.com">
```

**4.** Send an email to Mario Rossi with the subject “Hello, I would like to have a quote for your services”

```html
<a href="mailto:mario@lawfirm.com?subject=Hello,&I&would&like&to&have&a&quote&for&your&services">
```

**5.** Send an email to Mario Rossi with the subject “Hello, I would like to have a quote for your services” and some text in the body of the email message (e.g. Thanks in advance. Regards.)

```html
<a href="mailto:mario@lawfirm.com?subject=Hello,&I&would&like&to&have&a&quote&for&your&services&body=Thanks%20in%20advance.%20ARegards.%20">
```

You may use any permutations and combinations while writing a mailto hyperlink but make sure that there’s only one `?` character.

---

## 👨🏻‍💻 4. Use case

Giulio identified several phases that occur in the privacy assistance that his law firm normally conducts when dealing with its clients. Each phase begins or ends with an email, and lawyers always take from 15 to 30 minutes every time to re-write the same email. Our developeer took the most common emails that would circulate in those cases and filled a common document with some 'mailto' links for each phase. He even agreed on the text with the management. 
Each lawyer now knows what to send, when to send and he/she can do it with a click.

### Step 1

For exemplification purposes, we only identify one phases that the author identified and that needs an email automation: 

Phase 1: Intro steps after the client signed with the law firm

What we want to do is to send **this automated text when relating to phase 1**.

To: client@test.com
cc: mario@lawfirm.com

Object: [Client name] <> Law Firm - First Steps

Dear all,
we are happy that you have decided to sign with [lawfirm] and to work with to best meet your requirements and expectations. This is to explain to you what will be the first steps of our activity and what we will need from you:
1. Setting up the data room: to facilitate the exchange of materials, a data room will be set up 
2. Upload of documentation: to facilitate the first phase of Due Diligence, we kindly ask you to upload in the input folder all the documents that can help us to understand the state of the art in data protection.
We remain at your disposal for any doubts and/or clarifications.
Best regards,
[Name Surname]

### Step 2

There are two roads that you can follow in order to automate the email message: **1)** you can insert the mailto synthax manually (not that much fun 😅) or **2)** (best choice!) you can use some free mailto links generator such as [https://mailtolink.me/](https://mailtolink.me/). Although I started with the first path to learn the syntax by myself, I then decided to go with the mailto generator. Here's the result.

[`mailto:client@test.com](mailto:client@test.com)?cc=mario@lawfirm.com&subject=%5BClient%20name%5D%20%3C%3E%20Law%20Firm%20-%20First%20Steps&body=Dear%20all%2Cwe%20are%20happy%20that%20you%20have%20decided%20to%20sign%20with%20%5Blawfirm%5D%20and%20to%20work%20with%20to%20best%20meet%20your%20requirements%20and%20expectations.%20This%20is%20to%20explain%20to%20you%20what%20will%20be%20the%20first%20steps%20of%20our%20activity%20and%20what%20we%20will%20need%20from%20you%3A1.%20Setting%20up%20the%20data%20room%3A%20to%20facilitate%20the%20exchange%20of%20materials%2C%20a%20data%20room%20will%20be%20set%20up%202.%20Upload%20of%20documentation%3A%20to%20facilitate%20the%20first%20phase%20of%20Due%20Diligence%2C%20we%20kindly%20ask%20you%20to%20upload%20in%20the%20input%20folder%20all%20the%20documents%20that%20can%20help%20us%20to%20understand%20the%20state%20of%20the%20art%20in%20data%20protection.We%20remain%20at%20your%20disposal%20for%20any%20doubts%20and%2For%20clarifications.Best%20regards%2C%5BName%20Surname%5D` 

### Step 3

Copy the code and insert it on a word that you want to use as a container by right-clicking on the selected words > insert link > paste the code. In our case the words 'Send email' are the container of the generated mailto command. You can try it!

Phase 1: Intro steps after the client signed with the law firm. [Send email →](mailto:client@test.com?cc=mario@lawfirm.com&subject=%5BClient%20name%5D%20%3C%3E%20Law%20Firm%20-%20First%20Steps&body=Dear%20all%2Cwe%20are%20happy%20that%20you%20have%20decided%20to%20sign%20with%20%5Blawfirm%5D%20and%20to%20work%20with%20to%20best%20meet%20your%20requirements%20and%20expectations.%20This%20is%20to%20explain%20to%20you%20what%20will%20be%20the%20first%20steps%20of%20our%20activity%20and%20what%20we%20will%20need%20from%20you%3A1.%20Setting%20up%20the%20data%20room%3A%20to%20facilitate%20the%20exchange%20of%20materials%2C%20a%20data%20room%20will%20be%20set%20up%202.%20Upload%20of%20documentation%3A%20to%20facilitate%20the%20first%20phase%20of%20Due%20Diligence%2C%20we%20kindly%20ask%20you%20to%20upload%20in%20the%20input%20folder%20all%20the%20documents%20that%20can%20help%20us%20to%20understand%20the%20state%20of%20the%20art%20in%20data%20protection.We%20remain%20at%20your%20disposal%20for%20any%20doubts%20and%2For%20clarifications.Best%20regards%2C%5BName%20Surname%5D)
