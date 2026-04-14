from agent import Agent

agent = Agent()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = agent.run(user_input)
    print("Agent:", response)
