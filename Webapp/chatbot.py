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
    'how are you':"I am good, thanks. How are you?",
    "what is your name":"My name is Shreya. What's your name?",
    "what are you working":"I am working on my compiler project.",
    "did you go to the class yesterday":"Yes, I did. It was a very interesting class. I think the professor is really good",
    "what is your phone number":"I don't have a phone. Sorry!",
    "how old are you":"I am 20 years old"
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