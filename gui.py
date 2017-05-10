from Tkinter import *
from functions import *
import glob
import urllib2
import logging
import json
import requests
import pyautogui
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

master = Tk()

#Titles the application
Label(text="Mr. Owl Branch Creator App").grid(row=0)

#User input Branch Title
Label(text="Enter your Branch Title here").grid(row=1, column=0)
branchTitle = StringVar()
e = Entry(master, textvariable=branchTitle, width=85)
e.grid(row=1, column=1)

b = branchTitle.get()

#User input Branch Description
Label(text="Enter your Branch Description here").grid(row=2, column=0)
branchDescrip = StringVar()
e = Entry(master, textvariable=branchDescrip, width=85)
e.grid(row=2, column=1)

#User input Google Sheets Link
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
Label(text="Paste your Google Sheets link here").grid(row=3, column=0)
sheetsLink = StringVar()
e = Entry(master, textvariable=sheetsLink, width=85)
e.grid(row=3, column=1)

s = sheetsLink.get()

#User input number of Sub-Topics
Label(text="Number of sub-topics to be created").grid(row=4, column=0)
enteredNumSubtopics = StringVar()
e = Entry(master, textvariable=enteredNumSubtopics, width=85)
e.grid(row=4, column=1)

#Iterates though Google Sheets
def sheetsIterate():
    num = enteredNumSubtopics.get()
    trueNumSubtopics = int(num)
    urllib2.urlopen(sheetsLink.get())
    for x in range (0, trueNumSubtopics):
        subTopicTitles = []
        subTopicTitles.append(sheetsLink.get())
        print subTopicTitles

#Mr Owl username and password entry
Label(text="Mr. Owl Username").grid(row=5, column=0)
owlUser = StringVar()
e = Entry(master, textvariable=owlUser, width=85)
e.grid(row=5, column=1)
Label(text="Mr. Owl Password").grid(row=6, column=0)
owlPass = StringVar()
e = Entry(master, show='*', textvariable=owlPass, width=85)
e.grid(row=6, column=1)

subTopicTitles = []
#Signs in to mrowl.com
def mrOwlLogin():
    #Makes folder on desktop
    #os.makedirs("C:\Users\Marila\Desktop\\" + branchTitle.get() )
    driver=webdriver.Chrome("C:\Python27\Scripts\chromedriver")
    driver.get("http://www.mrowl.com")
    driver.find_element_by_id("username").send_keys(owlUser.get())
    driver.find_element_by_id("userpass").send_keys(owlPass.get())
    driver.implicitly_wait(3)
    driver.find_element_by_id("login").click()
    #Creates a branch
    driver.find_element_by_id("applet-create-branch").click()
    driver.find_element_by_id("branchName").send_keys(branchTitle.get())
    driver.find_element_by_id("branchDescription").send_keys(branchDescrip.get())
    driver.implicitly_wait(3)
    #Gets the Google Sheets JSON
    urlShorten = sheetsLink.get()
    start = urlShorten.find("/d/") + 3
    end = urlShorten.find("/ed", start)
    urlShortened = urlShorten[start:end]
    sheetsJson = "https://spreadsheets.google.com/feeds/list/" + urlShortened + "/od6/public/basic?prettyprint=true&alt=json"
    response = urllib2.urlopen(sheetsJson)
    data = json.load(response)
    i = 0
    numBranch = int(enteredNumSubtopics.get())
    for x in range (0, numBranch):
        subTopicTitles.append(data['feed']['entry'][i]['title']['$t'])
        print SubTopicTitles[i]
        i += 1

    #Posts to Mr. Owl
    i = 0
    driver.find_element_by_name("AddBranch").click()
    for x in range (0, numBranch):
        driver.find_element_by_id("editSubTopicDetails").click()
        driver.find_element_by_id("newSubtopicname").send_keys(subTopicTitles[i])
        driver.find_element_by_id("newSubtopicdescription").send_keys(subTopicTitles[i])
        driver.implicitly_wait(7)
        driver.find_element_by_name("addTopic").click()
        i += 1


#Creates Help and Submit buttons
helpButton = Button(master, text="Help", width=10, command=openReadMe).grid(row=7, column=1, sticky=E)
submitButton = Button(master, text="Submit", width=10, command=mrOwlLogin).grid(row=7, column=2, sticky=E)


mainloop()
