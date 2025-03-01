import pyttsx3

engine=pyttsx3.init()
text=input("Enter a message here: ")
# with open("Text_to_Speech/sample.txt", "r", encoding="utf-8") as file:
# with open("sample.txt", "r", encoding="utf-8") as file:

#     text=file.read()
    # print(text)

# engine.say("Hello I am Python")
engine.say(text)
engine.runAndWait()
engine.stop()
