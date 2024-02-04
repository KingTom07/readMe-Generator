def prompt_for_information():
    print("Welcome to the GitHub README Generator!")

    # Prompt for information
    title = input("Enter the title of your project/repository: ")
    description = input("Enter a brief description: ")
    running_instructions = input("Provide running instructions: ")
    author_name = input("Enter the author's name: ")
    screenshot_image = input("Enter the screenshot image file name: ")

    # Create README content
    readme_content = f"# {title}\n\n"
    readme_content += f"## Description\n{description}\n\n"
    readme_content += f"## Running Instructions\n{running_instructions}\n\n"
    readme_content += f"## Author\n{author_name}\n\n"
    readme_content += f"## Screenshot\n![Screenshot]({screenshot_image})"

    # Write content to README.md file
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

    print("README.md file created successfully!")

if __name__ == "__main__":
    prompt_for_information()
