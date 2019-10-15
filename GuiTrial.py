from guizero import TextBox, App, Text, PushButton
import time

app = App(title="Security Program")

user_box = TextBox(app, text="Enter Username")
pass_box = TextBox(app, text="Enter Password")

user_wrong = Text(app, text="Incorrect Username", visible=False)
pass_wrong = Text(app, text="Incorrect Password", visible=False)
correct_text = Text(app, text="Correct", visible=False)
false_text = Text(app, text="Incorrect", visible=False)

start_time = time.time()
capture_duration = 10


def test_input():
    if user_box.value == "Finn":
        if pass_box.value == "P@ssword#1":
            correct_text.show()
        else:
            pass_wrong.show()
    elif pass_box.value == "P@ssword#1":
        if user_box.value != "Finn":
            user_wrong.show()
    else:
        false_text.show()
        #while (int(time.time() - start_time) < capture_duration):


submit_butt = PushButton(app, text="Enter", command=test_input())

app.display()
