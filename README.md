# Overview

This simple Python program is a playlist manager. Users are able to create playlists, and add, update, and delete them as well. The user interacts with a menu that gives them options for interacting with the database.

I wrote this software to learn how Python can interact with a Cloud Firestore database. I've worked with other NoSQL databases in the past, like MongoDB, but it's been a while since I've written any Python code, so I figured this would be a good time to brush up.

[Software Demo Video](https://youtu.be/3JtZQZK-h9Q)

# Cloud Database

As mentioned above, this software uses Cloud Firestore, a part of Google's Firebase platform.

The database is divided into collections which can be considered playlists. Each playlist's ID is a name the user has provided. Playlists contain documents or songs, and each song has three fields: title, artist, and album. A song's ID is its title in lower case. 

# Development Environment

I used Visual Studio Code for an IDE and accessed the database through a Cloud Firestore project.

I wrote the software in Python, using a package called firebase-admin. 

# Useful Websites

- [Get started with Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart)
- [Essentials for working with Firestore in Python](https://superdataminer.com/2022/11/16/essentials-for-working-with-firestore-in-python/)

# Future Work

- Create a web-based UI
- Input validation
- User authentication