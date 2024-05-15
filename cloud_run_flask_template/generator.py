import os
import subprocess

def generate_project():
    project_name = input("Please enter your project name (Please do not add spaces): ")
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    # Create a file named main.py and write the provided code into it
    with open('main.py', 'w') as f:
        f.write('''import os
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))''')

    # Create a file named requirements.txt and write the provided code into it
    with open('requirements.txt', 'w') as f:
        f.write('''Flask==3.0.3
gunicorn==22.0.0
Werkzeug==3.0.3''')

    # Create a new directory named templates
    os.makedirs('templates', exist_ok=True)

    # Create a file named index.html in the templates directory and write the provided HTML code into it
    with open(os.path.join('templates', 'index.html'), 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Run Demo</title>
    <!-- Tailwind CSS -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
</head>
<body class="bg-gray-100 font-roboto">

<!-- Container -->
<div class="container mx-auto px-4 py-8">

    <!-- Cloud Run Card -->
    <div class="bg-white shadow-lg rounded-lg overflow-hidden">
      
        <div class="p-6">
            <h2 class="text-2xl font-bold text-gray-800 mb-2">What is Cloud Run?</h2>
            <p class="text-gray-700 text-lg mb-4">Cloud Run is a fully managed compute platform by Google Cloud that automatically scales your stateless containers.</p>
        </div>
    </div>

    <!-- How to Use Cloud Run Card -->
    <div class="bg-white shadow-lg rounded-lg overflow-hidden mt-8">
        
        <div class="p-6">
            <h2 class="text-2xl font-bold text-gray-800 mb-2">How to Use Cloud Run?</h2>
            <p class="text-gray-700 text-lg mb-4">1. Containerize your application using Docker.</p>
            <p class="text-gray-700 text-lg mb-4">2. Deploy your container to Cloud Run using the Google Cloud Console or the Cloud SDK command-line tool.</p>
        </div>
    </div>

    <!-- How to Deploy to Cloud Run Card -->
    <div class="bg-white shadow-lg rounded-lg overflow-hidden mt-8">
       
        <div class="p-6">
            <h2 class="text-2xl font-bold text-gray-800 mb-2">How to Deploy to Cloud Run?</h2>
            <p class="text-gray-700 text-lg mb-4">1. Use the following command to deploy to Cloud Run:</p>
            <code class="bg-gray-200 p-2 block rounded-md mb-4">gcloud run deploy [SERVICE_NAME] --image=[IMAGE_URL]</code>
            <p class="text-gray-700 text-lg mb-4">2. Replace [SERVICE_NAME] with the name of your service and [IMAGE_URL] with the URL of your Docker image stored in a container registry like Google Container Registry.</p>
        </div>
    </div>

    <!-- Contributor Section -->
    <div class="text-center mt-8">
        <p class="text-gray-600">Contributed by <a href="https://www.linkedin.com/in/yashkavaiya/" class="text-blue-500">Yash Kavaiya</a></p>
    </div>

</div> <!-- End Container -->

</body>
</html>
''')

    # Install the required packages
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"])
        print("Required packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing packages: {e}")

if __name__ == "__main__":
    generate_project()
