from agents.simple_agent import run_agent

def main():
    while True:
        user=input("You: ")

        if user=="exit":
            break
        response=run_agent(user)
        print("Agent:", response)


if __name__ == "__main__":
    main()