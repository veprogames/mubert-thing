# Simple Mubert thingy

Generate tracks with pre existing API tokens used from https://huggingface.co/spaces/Mubert/Text-to-Music/tree/main

# Note

This might not work anymore if the Tokens get invalidated.

# How to use it

1. clone this repository
    1. make sure you have python installed
2. run `python main.py -h` (or `python3 main.py -h`) for instructions

Example:

`python3 main.py -t 'dark,dubstep,hardcore,aggressive' -T 2 -l 100`

This generates a 1:40 long track with 4 predefined tags and 2 random tags (6 tags in total)

You need an active Internet connection to run it because it uses `https://api-b2b.mubert.com` endpoints to generate music. On the upside the hardware requirements are basically nonexistent.

# How is this different from https://huggingface.co/spaces/Mubert/Text-to-Music?

While the Gradio App in the Huggingface Space turns your prompt into tags (which matter to Mubert), here you input the tags directly, giving you more control over the generations.