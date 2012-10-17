# -*- coding: cp1252 -*-
# Name: Fabien Toune
# Section: MOOC
# Date: 06 Oct 2012
# homework_1.py

##### Template for Homework 1, exercises 1.2-1.4 ######

print "********** Exercise 1.2 **********"

# Do your work for Exercise 1.2 here

print "  |  |  "
print "--------"
print "  |  |  "
print "--------"
print "  |  |  "



print "********** Exercise 1.3 **********"

# Do your work for Excercise 1.3 here. Hint - how many different
# variables will you need?

v = "  |  |  "
h = "--------"
print v
print h
print v
print h
print v

print "********** Exercise 1.4 **********"

# Do your work for Exercise 1.4 here.

c1 = 3 * 5/(2+3)
c2 = (7 + 9)**0.5 * 2
c3 = (4-7)**3
c4 = (-19+100)**0.25
c5 = 6%4
print c1
print c2
print c3
print c4
print c5

nom = raw_input("Entrez votre nom: ")
prenom = raw_input("Entrez votre prénom: ")
mois = raw_input("Entrez votre date de naissance:\nMois? ")
jour = raw_input("Jour? ")
annee = raw_input("Année? ")
print prenom, nom, "est né le", jour, mois, annee
