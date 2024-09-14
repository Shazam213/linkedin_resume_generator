# LinkedIn Resume Generator

## Description

The **LinkedIn Resume Generator** is a web application designed to streamline the process of creating professional, ATS (Applicant Tracking System) friendly resumes from LinkedIn PDF profiles. Leveraging the power of OpenAI's GPT-4 model, this tool extracts text from uploaded LinkedIn PDF resumes and converts it into a well-structured HTML resume.

### Key Features

1. **PDF Upload and Text Extraction**: Users can upload their LinkedIn resumes in PDF format. The application uses PyPDF2 to extract the text from the PDF.

2. **OpenAI Integration for Resume Generation**: The extracted text is then processed using OpenAI's GPT-4 model. The application uses prompt engineering to convert the raw text into a polished, ATS-friendly HTML resume.

3. **ATS-Friendly HTML Format**: The HTML resume follows a default format that is widely recognized and recommended by top companies for ATS compatibility. This format ensures that the resume is structured in a way that maximizes its chances of passing through automated resume screening systems.

4. **Custom Job Description Feature**: An **additional feature** allows users to input a job description. The resume is then tailored to match the job requirements, increasing its relevance and improving the chances of landing an interview.

## Approach and Steps

### 1. **Project Setup**

1. **Flask Application Initialization**: Created a Flask application to handle the web server and routing for the resume generation process.

2. **File Upload Handling**: Implemented functionality to handle PDF file uploads. The `/upload` route processes the file and extracts the text using PyPDF2.

3. **Text Extraction**: Extracted text from the uploaded PDF using PyPDF2, ensuring clean and accurate extraction.

4. **OpenAI API Integration**: Integrated OpenAI's GPT-4 model to generate an HTML resume from the extracted text. Used prompt engineering techniques to craft a detailed and effective prompt for resume generation.

5. **ATS-Friendly HTML Resume Generation**: Developed an HTML resume format that adheres to best practices for ATS compatibility. This format includes sections for contact information, education, experience, projects, skills, and leadership.

6. **Custom Job Description Feature**: Added functionality to include a job description, allowing users to tailor their resumes for specific job applications. This feature enhances the resume's relevance to the job requirements.

7. **File Saving and Download**: Saved the generated HTML resume to a file and provided it as a downloadable attachment for the user.

### 2. **Code Details**

- **`app.py`**: The main application file containing Flask routes and functions.
  - **Home Route (`/`)**: Renders the homepage where users can upload their resumes.
  - **Upload Route (`/upload`)**: Processes the uploaded PDF, extracts text, generates an HTML resume, and provides it for download.
  - **Text Extraction**: Utilizes PyPDF2 to read and extract text from the PDF.
  - **Resume Generation**: Uses OpenAI's GPT-4 model to convert extracted text into an HTML resume using a well-defined prompt.
  - **Custom Job Description**: If provided, the job description is included in the prompt to tailor the resume for specific job applications.
  - **File Handling**: Saves the HTML resume and serves it to the user.
### 3. **File Structure**

        .
        └── linkedin_resume_generator/
            ├── app.py
            ├── static/
            │       ├── style.css
            ├── templates/
            │       ├── index.html
            ├── __pycache__
            ├── uploads
            ├── LICENSE
            ├── README.md
            └── requirements.txt
    
### 4. **Dependencies**

- **Flask**: For creating the web application.
- **PyPDF2**: For extracting text from PDF files.
- **OpenAI**: For generating HTML resume content.
- **Werkzeug**: For secure file handling.

### 5. **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shazam213/linkedin_resume_generator.git
   cd linkedin_resume_generator
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
3. **Run the application**:
    ```bash
    flask run
    ```
The application is also deployed on vercel. [Click Here](https://linkedin-resume-generator-7d5pu04yi-shazam213s-projects.vercel.app/)
### 6. **Implementation**
1. **Home Screen**:
![Home screen](./resources/Screenshot%20from%202024-09-14%2021-15-45.png)

2. **Examples:**
- First PDF:

![soham_pdf](./resources/Screenshot%20from%202024-09-14%2021-18-53.png)

[Link to pdf](./resources/soham_linkedin.pdf)

- Generated Resume:

![soham](./resources/Screenshot%20from%202024-09-14%2021-18-28.png)

[Link to resume](./resources/soham_linkedin_resume.html)

- Second PDF:

![siddhesh_pdf](./resources/Screenshot%20from%202024-09-14%2021-19-12.png)

![siddhesh_pdf2](./resources/Screenshot%20from%202024-09-14%2021-19-19.png)

[Link to pdf](./resources/siddhesh_linkedin.pdf)

- Generated Resume:

![soham](./resources/Screenshot%20from%202024-09-14%2021-19-28.png)

[Link to resume](./resources/siddhesh_linkedin_resume.html)

### Note: The outputs were generated using Llama's API key because the OpenAI API Key was not available at the time of project creation.