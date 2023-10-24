import json

class Idea:
    def __init__(self, title, description, tags):
        self.title = title
        self.description = description
        self.tags = tags

class IdeaOrganizer:
    def __init__(self):
        self.ideas = []

    def add_idea(self, title, description, tags):
        idea = Idea(title, description, tags)
        self.ideas.append(idea)

    def list_ideas(self):
        for i, idea in enumerate(self.ideas, start=1):
            print(f"{i}. Title: {idea.title}")
            print(f"   Description: {idea.description}")
            print(f"   Tags: {', '.join(idea.tags)}")
            print()

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            data = [{"title": idea.title, "description": idea.description, "tags": idea.tags} for idea in self.ideas]
            json.dump(data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.ideas = [Idea(item["title"], item["description"], item["tags"]) for item in data]
        except FileNotFoundError:
            pass

def main():
    organizer = IdeaOrganizer()
    organizer.load_from_file("ideas.json")

    while True:
        print("Idea Organizer Menu:")
        print("1. Add Idea")
        print("2. List Ideas")
        print("3. Save Ideas")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the idea title: ")
            description = input("Enter the idea description: ")
            tags = input("Enter tags (comma-separated): ").split(",")
            organizer.add_idea(title, description, tags)

        elif choice == "2":
            print("List of Ideas:")
            organizer.list_ideas()

        elif choice == "3":
            organizer.save_to_file("ideas.json")
            print("Ideas saved to 'ideas.json'")

        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

