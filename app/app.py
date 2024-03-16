from flask import Flask, render_template, request, send_file, flash, redirect, url_for, send_from_directory, session
from flask_cors import CORS
from faker import Faker
from PIL import Image
import uuid
import os
import json

app = Flask(__name__)
CORS(app)
app.secret_key = 'a_very_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/')
def index():
    instructions = {
        'Dataset Generator': 'Use /generate_data to generate fake data in JSON format. Choose a dataset and quantity.',
        'Image Converter': 'Use /convert to convert JPEG images to PNG or BMP format. Upload an image and select the desired output format.'
    }
    return render_template('index.html', instructions=instructions)


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    # Check if coming from a POST redirect and if the image should still be shown
    if request.method == 'GET' and not session.get('show_image', False):
        # Clear the session if not coming from a POST redirect
        session.pop('converted_image', None)
        session.pop('output_format', None)
    
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No image file provided.')
            return redirect(request.url)
        file = request.files['image']
        output_format = request.form['output_format'].upper()
        if file.filename == '':
            flash('No selected file.')
            return redirect(request.url)

        # Generate a unique filename for the output file
        output_filename = f"{uuid.uuid4()}.{output_format.lower()}"

        try:
            # Convert the image using Pillow
            image = Image.open(file.stream)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            # Make sure the directory exists
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            image.save(image_path)

            flash('Image successfully converted.')
            session['converted_image'] = output_filename
            session['output_format'] = output_format.lower()
            # Indicate that the image should be shown (used for GET request logic)
            session['show_image'] = True
        except Exception as e:
            flash(f'Failed to convert image: {e}')

        return redirect(url_for('convert'))

    # Render the page, showing the image if it was just converted
    converted_image_url = ''
    if 'converted_image' in session:
        converted_image = session['converted_image']
        converted_image_url = url_for('static', filename=f'uploads/{converted_image}')
        # Clear the flag so the image won't be shown after a reload
        session.pop('show_image', None)

    return render_template('convert.html', converted_image=converted_image_url)





def generate_dataset(dataset, quantity):
    faker = Faker()
    data = []
    for _ in range(quantity):
        if dataset == 'personal_info':
            data.append({
                "Name": faker.name(),
                "Email": faker.email(),
                "Phone Number": faker.phone_number(),
                "Address": faker.address()
            })
        elif dataset == 'employment_data':
            data.append({
                "Job": faker.job(),
                "Company": faker.company(),
                "Job Title": faker.job()
            })
        elif dataset == 'contact_details':
            data.append({
                "Email": faker.email(),
                "Phone Number": faker.phone_number(),
                "Address": faker.address()
            })
        elif dataset == 'online_activity':
            data.append({
                "Username": faker.user_name(),
                "Email": faker.safe_email(),
                "Website": faker.url()
            })
        elif dataset == 'financial_information':
            data.append({
                "Bank Account": faker.bban(),
                "Credit Card Number": faker.credit_card_number()
            })
    return data

@app.route('/generate_data', methods=['GET', 'POST'])
def generate_data():
    if request.method == 'POST':
        dataset = request.form['dataset']
        quantity = int(request.form.get('quantity', 1))
        data = generate_dataset(dataset, quantity)
        
        filename = f"{dataset}_data.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        flash('Your dataset is ready for download.')
        return redirect(url_for('download_file', filename=filename))
    
    return render_template('generate_data.html')

@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(app.root_path, filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
