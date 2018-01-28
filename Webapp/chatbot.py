#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:03:26 2018

@author: aravind_
"""

import os

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

hard_coded = {
    'hey': 'hi there',
    'hi': 'hi there',
    'hello': 'hi there',
    'how are you': 'I am good, thanks. How are you?',
    'how are things': 'I am good, thanks. How are you?',
    'how are you doing': 'I am good, thanks. How are you?',

    'Hi, how are you': 'hey I am good.',
    'Hi how are you': 'hey I am good.',
    "Hi, how're you": "hey I am good.",
    'Hi': 'hi there',
    'Hello': 'hi there',
    'My name is Manish':'My name is Shreya ',
    'How are things': 'I am good, thanks. How are you?',
    'How are you doing': 'I am good, thanks. How are you?',
    'What is your name': 'My name is Shreya. What is your name?',
    'what are you working on': 'I am working on my compiler project.',
    'what are you doing': 'I am working on my compiler project.', 
    'That is really interesting': 'Thank you.', 
    'did you go to the class yesterday': 'Yes, I did. It was a very interesting class. I think the professor is really good',
    'How old are you': 'I am 20 years old'
    'That sounds really boring.': 'I know. Tell me about it.', 
    'You should take a break.': 'Yeah you are probably right.', 
    'Do you want to get coffee?': 'I will let you know.'
    'What is your phone number': 'I don not have a phone. Sorry!',
    'Come let us go for drinks.': 'Ok, let me pack up. Yay!'
}

def set_bot():
    chatterbot = ChatBot("Date")
    
    chatterbot.set_trainer(ListTrainer)

    chatterbot.train([
        "Hey!",
        "Hello",
    ])

    chatterbot.train([
        "How are you?",
        "I am good, thanks. How are you?",
    ])

    chatterbot.train([
        "What's your name?",
        "My name is Shreya. What's your name?",
    ])

    chatterbot.train([
        "My name is Manish. What are you working?",
        "I am working on my compiler project.",
    ])

    chatterbot.train([
        "Oh that's soo cool!",
        "Eh, thanks I guess.",
    ])

    chatterbot.train([
        "Where are you from?",
        "I am from London. Where are you from?",
        "I am from Ireland. Have you ever been?",
        "No I have never been there. That's so cool.",
    ])

    chatterbot.train([
        "Want to get coffee someday?",
        "Hmm, I will let you know.",
    ])

    chatterbot.train([
        "Ok, cool. I will see you around then.",
        "Bye!"
    ])

    chatterbot.train([
        "What is your phone number?",    
        "I don't have a phone. Sorry!",
    ])

    chatterbot.train([
        "What's your digits? I will call you.",    
        "Haha, ok. Here you go.",
    ])

    chatterbot.train([
        "You look very pretty.",    
        "Why, thank you. Same to you.",
    ])

    chatterbot.train([
        "What course are you studying?",    
        "I am in first year computing. What about you?",
    ])

    chatterbot.train([
        "I am doing a masters in Machine Learning.",    
        "Oh, that's so cool. Tell me more!",
    ])

    chatterbot.train([
        "How old are you?",    
        "I am 19. What about you?",
    ])
    
    chatterbot.set_trainer(ChatterBotCorpusTrainer)

    # Train based on english greetings corpus
    chatterbot.train("chatterbot.corpus.english.greetings")

    # Train based on the english conversations corpus
    chatterbot.train("chatterbot.corpus.english.conversations")

    return chatterbot

def bot():
    chatterbot = ChatBot("Date")
    return chatterbot