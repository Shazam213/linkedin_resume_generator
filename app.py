import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import PyPDF2
import openai
import io


app = Flask(__name__)
UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Ensure both the API key and the file are provided
    if 'file' not in request.files:
        return 'No file part in the request', 400
    if 'api_key' not in request.form or request.form['api_key'] == '':
        return 'No API key provided', 400
    
    file = request.files['file']
    api_key = request.form['api_key']
    
    if file.filename == '':
        return 'No file selected for uploading', 400

    # Save the uploaded file in memory
    file_in_memory = io.BytesIO(file.read())
    
    # Extract text from the uploaded PDF
    extracted_text = extract_text_from_pdf(file_in_memory)

    # Check if the job description checkbox is ticked and retrieve the job description
    include_job_description = 'add_job_description' in request.form
    job_description = request.form['job_description'] if include_job_description else None
    
    # Generate HTML resume using OpenAI API, passing job description if applicable
    html_content = generate_html_resume(extracted_text, api_key, job_description)
    
    # Convert HTML content to in-memory file-like object
    html_in_memory = io.BytesIO()
    html_in_memory.write(html_content.encode('utf-8'))
    html_in_memory.seek(0)
    
    # Send the HTML file as an attachment
    return send_file(html_in_memory, as_attachment=True, download_name='resume.html', mimetype='text/html')


def extract_text_from_pdf(file_in_memory):
    text = ""
    try:
        # Use the in-memory file instead of a path
        pdf = PyPDF2.PdfReader(file_in_memory)
        for page in pdf.pages:
            text += page.extract_text() or ""
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text


def generate_html_resume(extracted_text, api_key, job_description=None):
    openai.api_key = api_key

    prompt = f"""
    Convert the following extracted LinkedIn resume details into an HTML format, and make sure it is ATS (Applicant Tracking System) friendly.

    HTML format for the resume template:

    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0 auto;
                padding: 0;
                width: 85%;
                color: #333;
            }}
            h1, h2, h3 {{
                color: #333;
                margin: 0;
                padding-bottom: 10px;
            }}
            h1 {{
                text-align: center;
                font-size: 28px;
                text-transform: uppercase;
            }}
            h2 {{
                font-size: 20px;
                border-bottom: 1px solid #ccc;
                margin-bottom: 10px;
            }}
            h3 {{
                font-size: 18px;
                margin-bottom: 5px;
            }}
            .contact-info {{
                text-align: center;
                margin-top: 5px;
                font-size: 14px;
            }}
            .contact-info a {{
                text-decoration: none;
                color: #333;
            }}
            ul {{
                list-style: none;
                padding: 0;
                margin: 0;
            }}
            li {{
                padding-bottom: 5px;
                margin-bottom: 5px;
            }}
            .section {{
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <!-- Contact Information -->
        <h1>First Last</h1>
        <p class="contact-info">
            123 Street Name, Town, State 12345 <br>
            <a href="tel:123-456-7890">123-456-7890</a> | 
            <a href="mailto:somebody@domain.com">somebody@domain.com</a> |
            <a href="https://linkedin.com/in/username">linkedin.com/in/username</a> |
            <a href="https://github.com/username">github.com/username</a>
        </p>

        <!-- Education Section -->
        <div class="section">
            <h2>Education</h2>
            <ul>
                <li><strong>University</strong>, Degree Name, State (Jan 2021 – Current)</li>
                <li><strong>Junior College Name</strong>, HSC Board, City, State (Sep 2017 – May 2021)</li>
                <li><strong>School Name</strong>, SSC, Board, City, State (Sep 2017 – May 2021)</li>
            </ul>
        </div>

        <!-- Relevant Coursework -->
        <div class="section">
            <h2>Relevant Coursework</h2>
            <ul>
                <li>Relevant Coursework 1</li>
                <li>Relevant Coursework 2</li>
                <li>Relevant Coursework 3</li>
                <li>Relevant Coursework 4</li>
                <li>Relevant Coursework 5</li>
                <li>Relevant Coursework 6</li>
            </ul>
        </div>

        <!-- Experience/Internships Section -->
        <div class="section">
            <h2>Experience/Internships</h2>
            <ul>
                <li>
                    <strong>Company Name</strong>, Position, City, State (May 2020 – August 2020)
                    <ul>
                        <li>Description line 1.</li>
                        <li>Description line 2.</li>
                        <li>Description line 3.</li>
                    </ul>
                </li>
                <li>
                    <strong>Company Name</strong>, Position, City, State (May 2020 – August 2020)
                    <ul>
                        <li>Description line 1.</li>
                        <li>Description line 2.</li>
                        <li>Description line 3.</li>
                    </ul>
                </li>
            </ul>
        </div>

        <!-- Projects Section -->
        <div class="section">
            <h2>Projects</h2>
            <ul>
                <li>
                    <strong>Project Name</strong> | Python, Selenium, Google Cloud Console (January 2021)
                    <ul>
                        <li>Description line 1.</li>
                        <li>Description line 2.</li>
                        <li>Description line 3.</li>
                    </ul>
                </li>
                <li>
                    <strong>Project Name</strong> | Python, Selenium, Google Cloud Console (January 2021)
                    <ul>
                        <li>Description line 1.</li>
                        <li>Description line 2.</li>
                        <li>Description line 3.</li>
                    </ul>
                </li>
            </ul>
        </div>

        <!-- Technical Skills Section -->
        <div class="section">
            <h2>Technical Skills</h2>
            <ul>
                <!-- Add Technical Skills Here -->
            </ul>
        </div>

        <!-- Leadership / Extracurricular Section -->
        <div class="section">
            <h2>Leadership / Extracurricular</h2>
            <ul>
                <li>
                    <strong>Name</strong>, President, University Name (Spring 2020 – Present)
                    <ul>
                        <li>Description line 1.</li>
                        <li>Description line 2.</li>
                        <li>Description line 3.</li>
                    </ul>
                </li>
            </ul>
        </div>
    </body>
    </html>

    Using this format, generate an HTML resume from the following extracted text. Ensure that the HTML is clean, readable, and ATS-compliant. Adjust or omit irrelevant sections if needed to fit the professional resume format:

    {extracted_text}
    Note: directly give the output html code and no description for it.
    """

    if job_description:
        prompt += f"\n\nHere is the Job Description for the position candidate is applying to. Curate the resume for the specific job description so that the resume scores higher ATS score for better chances of selection:\n{job_description}"
    
    try:
       
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return "Error generating resume due to OpenAI API issue."
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "Error generating resume due to an unexpected issue."



def save_html_resume(html_content, original_filename):
    base_filename = os.path.splitext(original_filename)[0]
    html_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{base_filename}_resume.html")
    with open(html_path, "w") as html_file:
        html_file.write(html_content)
    return html_path


if __name__ == '__main__':
    app.run(debug=True)
