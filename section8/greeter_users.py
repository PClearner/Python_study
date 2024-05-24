#test
def show_massages(messages):
    for x in messages:
        print(x)
messages = ['hello','damn','kill','happy']
show_massages(messages)

def send_messages(messages):
    send_message = []
    while messages:
        send_message.append(messages.pop())
    return send_message

ss = send_messages(messages)
print(f"this is ss:{ss}")
print(f"this is messages:{messages}")

messages = ['hello','damn','kill','happy']
ss = send_messages(messages[:])
print(f"this is ss:{ss}")
print(f"this is messages:{messages}")