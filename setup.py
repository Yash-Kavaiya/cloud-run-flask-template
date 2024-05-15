from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cloud_run_flask_template',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cloud_run_flask_template = cloud_run_flask_template.generator:generate_project'
        ]
    },
    install_requires=[
        'Flask==3.0.3',
        'gunicorn==22.0.0',
        'Werkzeug==3.0.3'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A template for Google Cloud Run Flask development',
    long_description=long_description,  # Set the long description here
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cloud_run_flask_template',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
