from agent.controller import AgentController

def main():
    agent = AgentController()

    print("Local Coding Agent (type 'exit' to quit)")

    while True:
        user_input = input("\nUser: ")

        if user_input.lower() == "exit":
            break

        result = agent.run(user_input)

        print("\nAgent:", result)


if __name__ == "__main__":
    main()