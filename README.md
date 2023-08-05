### This Code Is Demonstrate Amazon Polly Text To Speech Using Node.js and Python

## Requirements

- Node.js
- Python 3.6
- Amazon Web Services Account (AWS)

## Installation

- Clone the repository
- Create a Bucket in AWS S3 give with public access
- Create a iam Role With These Policies
  1. Select For lambda Then add a following role
  2. Add a lambda basic execution role
  3. Amazon Polly Full Access
  4. Amazon Api Gateway Invoke Full Access

## Usage

- Create a lambda function in AWS
- Then go to Lambda folder in a repository And copy a code from lambda_function.py and paste it in lambda function
- Then Create a API Gateway in AWS with a POST method
  1. Create a Rest Api give a name
  2. Create a POST method and selet lambda function above created
  3. Then go to action a enable CORS
  4. Then Deploy API
- Then go to the node.js folder and updated a code with your API Gateway URL

## Run

- Copy url from API Gateway and paste to the browser and add a query string with text and voice
  1. Example: https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com
  2. Add a text in text query string
  3. Then play a audio in browser

## Demo of Running Code

- [Demo](http://txt2speechbucket.s3-website.us-east-2.amazonaws.com/)

## Contributing

- Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
- Please make sure to update tests as appropriate.
- Please don't forget to give a star
- Thank You
- Happy Coding
