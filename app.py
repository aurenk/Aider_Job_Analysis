from flask import Flask, request, render_template
import linkedin_scraper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_title = request.form.get('job-title')
        keywords = request.form.get('keywords')
        # Add code here to run the scraper and return the results
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
