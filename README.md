
# Stak Suite: Cryptography and Cybersecurity Tools


## Introduction

Stak Suite is an innovative website designed to address common challenges in the field of cryptography, particularly for those participating in Capture The Flag (CTF) cybersecurity competitions. It offers a range of tools and resources for both beginners and experienced users, focusing on simplifying and streamlining the process of identifying and executing cryptographic attacks.


## Features
Visual Interface for Cryptographic Attacks: Easy-to-understand and efficient tools for various cryptographic attacks. \
Automatic Vulnerability Detector: Scans ciphertext for potential vulnerabilities, executes exploits, and decrypts ciphertext.\
Authentication System: Ensures tools are used responsibly and are not accessible to unauthorized users.\
Informative Pages: Detailed explanations of cryptographic attacks and how they work, catering to both beginners and experts.\
Targeted Tools for RSA: Specialized tools and resources for RSA cryptography, with potential future expansions to other methods like AES and elliptic curve cryptography.

## Target Audience
Stak Suite primarily caters to aspiring developers with an interest in cryptography and members of the creator's personal CTF team. The focus is on maximizing the advantages offered by the application for its users.
## Setup and Running the Project
* Clone and navigate to the repo:
    `git clone https://github.com/exponent3141/Stack-Suite-13DTP-.git`
    `cd Stack-Suite-13DTP-`\
* Install the required dependencies using the Python package manager by running\
    `pip install -r requirements.txt`
* Once the dependencies are installed, start the application by running:\
    `python app.py`

### Test Credentials
For testing purposes, you can use the following credentials to log in:

`Username: test`\
`Password: testpassword`\
These credentials will give you access to the website's features, allowing you to evaluate its functionality and user experience.

## Website Structure
### Main Pages
#### Home Page
Basic introduction and navigation to other sections.
#### About Page
Information about the creator and the project’s future aspirations.
#### Info Page
Detailed project description and target audience.
#### Login and Registration Pages
Secure user authentication system.
#### Tools Page
Access to general and RSA-specific cryptographic tools.
### Tool-Specific Pages
General Tools Page: 
* Base64 to ASCII converter
* XOR calculator
* Hex converter
RSA Tools Page: 
* Features encryption and decryption functionality
* Totient generator
* PEM file decoder
* Automatic RSA exploiter
## Additional Features
#### Inventory Page
Detailed descriptions of cryptographic attacks used.
#### Admin Page
For managing users and understanding database values.
#### Help Page
Brief guide on using the website with a FAQ section.

## Technical Aspects
### Backend
A SQL database to store user information, settings, and cryptographic data like prime and composite numbers.
Secure handling of user data and authentication details.
### Frontend
User-friendly interface with a calm, elegant, and dependable color palette.
Responsive design catering to different user roles and permissions.

## Testing and Feedback
Extensive testing has been conducted to ensure functionality, usability, data integrity, and security. Feedback from users has been incorporated to improve aesthetics, usability, and consistency across the platform.

## Conclusion
Stak Suite is a comprehensive tool that significantly simplifies the process of identifying and executing cryptographic attacks. It is an invaluable resource for those in the field of cybersecurity, especially in the context of CTF challenges and cryptographic learning.
