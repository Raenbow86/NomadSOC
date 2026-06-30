# NomadSOC

NomadSOC is a cybersecurity project designed to help travelers, van lifers, remote workers, students, and public Wi-Fi users make safer decisions before connecting to unknown networks.

## The Problem

People connect to coffee shop Wi-Fi, campground Wi-Fi, hotel Wi-Fi, library Wi-Fi, and public networks every day without knowing whether those networks are safe.

Most cybersecurity tools are built for professionals. NomadSOC is built for everyday people who need clear, simple, friendly security guidance.

## The Mission

NomadSOC helps users understand network risk through simple safety scoring, educational recommendations, and real-world cybersecurity awareness.

The goal is not to scare people.

The goal is to teach people how to protect themselves.

## What NomadSOC Does

NomadSOC is a beginner-friendly cybersecurity tool that helps users think through the risks of using public or shared Wi-Fi.

The tool asks simple yes/no questions about the user’s connection, device, and activity. Based on the answers, it calculates a risk score, gives a risk level, and explains why the score was assigned.

NomadSOC is designed to be educational, ethical, and practical. It does not scan, attack, monitor, or collect traffic from any network. Instead, it helps users make safer decisions before logging into sensitive accounts on public Wi-Fi.

## Current MVP Features

* Public/shared Wi-Fi risk check
* Wi-Fi password protection check
* Official network verification check
* VPN usage check
* Sensitive activity warning
* Device update check
* Firewall check
* Risk score result
* Plain-English explanation of why the score was assigned
* Safety recommendations based on user answers

## How to Run

NomadSOC is currently a Python command-line tool.

To run the program, open the project in a terminal and use:

```bash
python nomadsoc_mvp.py

The program will ask a series of yes/no questions about the user’s Wi-Fi connection, device security, and planned activity. It then returns a risk score, a risk level, plain-English explanations, and safety recommendations.


## Core Concepts

NomadSOC will eventually evaluate security across categories such as:

- Network Security
- Device Security
- User Behavior
- Environment
- Connection Health

## MVP Idea

The first version of NomadSOC will allow a user to enter or scan basic network information and receive a simple safety result.

Example:

- Safe for browsing
- VPN recommended
- Avoid banking
- Unknown or risky network

## Long-Term Vision

The long-term vision is to build a NomadSOC Intelligence Engine that explains why a security score changed and gives friendly, educational recommendations.

## Founder Note

NomadSOC started from real life: working, traveling, and depending on public Wi-Fi while learning cybersecurity.

This project is built for people who need cybersecurity to make sense in the real world.
