import tkinter as tk

# Simple rule-based response logic
def get_bot_response(user_message):
    user_message = user_message.lower()
    if "hello" in user_message or "hi" in user_message:
        return "Hello! How can I help you today?"
    elif "name" in user_message:
        return "I'm your friendly chatbot app."
    elif "bye" in user_message:
        return "Goodbye! Have a nice day."
    elif "help" in user_message:
        return "Sure! Ask me anything about this project."
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

# GUI logic
def send():
    user_message = user_entry.get()
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_message + "\n")
    bot_response = get_bot_response(user_message)
    chat_window.insert(tk.END, "Bot: " + bot_response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Python Chatbot App")
app.geometry("400x500")

chat_window = tk.Text(app, bd=1, bg="white", width=50, height=20, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10)

user_entry = tk.Entry(app, bd=1, width=30)
user_entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))

send_button = tk.Button(app, text="Send", width=8, command=send)
send_button.pack(side=tk.LEFT, padx=(5,10), pady=(0,10))

def on_enter(event):
    send()
user_entry.bind('<Return>', on_enter)

app.mainloop()