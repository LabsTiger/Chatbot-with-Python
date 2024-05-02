import json

def load_data():
     try:
          with open("data.json", "r") as file:
               data = json.load(file)
     except FileNotFoundError:
          data = {}
     return data

def save_data(data):
     with open("data.json", "w") as file:
          json.dump(data, file)

def get_response(question, data):
     if question in data:
          return data[question]
     else:
          return None

def main():
     print("Hello. I am a chatbot!")
     data = load_data()

     while True:
          user_input = input("> ")

          if user_input.lower() == "exit":
               break

          response = get_response(user_input, data)

          if response:
               print(response)
          else:
               print("I'm sorry! I don't know the answer to that!")
               teach_response = input("Please teach me: ")
               data[user_input] = teach_response
               save_data(data)
               print("Thanks! Now I get it!")

if __name__ == "__main__":
     main()
