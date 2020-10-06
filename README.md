# transcription-api
Transcribes text in images for accessibility purposes.

## Motivation
There is a community on reddit that is committed to transcribing image posts for those who are browsing using an e-reader. This, at times, includes transcribing lengthy screenshots of text conversations. I saw a demo using the tesseract library transcribing an image with text into string text and thought it might be useful to have the ability to pass in an image URL and transcribe that.

## How to run
After cloning the project and `cd`ing into the transcription-api directory, run the following:

Build the image and tag as `transcribe-api` (or anything you want):

```docker build . -t transcribe-api```

Run the image, mapping the container's port 5000 to your machine's port 5000 (or any port you want):

```docker run -p 5000:5000 transcribe```

From there, running this:

```curl -X GET -F 'image_url=https://i.redd.it/or0w5iujxbr51.jpg' localhost:5000/transcribe```

should return:

```
Hey girl! Soooo I'm sure you've been
asked before but | was curious if you
would like to be a product model for
me bs | think you'll love all of my
different challenges with over 50
natural health and wellness products
to choose from! Of course I'll give you
my huge discount too & you’re NOT
promoting anything © Can | give ya
some info on what you’d be doing?

No worries love!! €3
3:37 PM

Hey girl! | know you might not be
interested in my products but | was
wondering if you'd be willing to help
me spread the word about my
business by throwing a post up on
your story, tagging me, & I'll enter you
into my $100 Amazon gift card
giveaway for this month?!

| literally don’t know you lol. Do you
not feel embarrassed that you are

sending the same copy and paste
message to strangers asking for a
aol larg
```

You _should_ be able to pass in any direct link to an image and get a transcript. Is it perfect? Not in the slightest. However, I would think it would be easier to fix this up rather than transcribing from scratch.

## Future steps
There are a few more things I'd like to do with this:
- [ ] Support for imgur links
- [ ] Lambda function with API gateway
- [ ] Simple, accessible frontend

## Suggestions & Contributing
Feel free to create an issue with any suggestions or feedback you might have. To contribute, just make a fork and submit a PR! 
