from flask import request, jsonify, send_file, render_template
from config import app
from jobspy import scrape_jobs



@app.route('/scrapejobs_csv', methods=['GET'])
def scrape_jobs_route_csv():
    try:
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "glassdoor"],
            search_term="software engineer",
            location="Dallas, TX",
            results_wanted=10,
            country_indeed='USA'  # only needed for indeed / glassdoor
        )
        print(f"Found {len(jobs)} jobs")
        print(jobs.head())
        jobs.to_csv("jobs.csv", index=False) # Save the jobs as a CSV file
        return send_file('jobs.csv', as_attachment=True)  # Return the CSV file as a download
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return the error message as a JSON responseturn the CSV file as a download



@app.route('/scrapejobs_excel', methods=['GET'])
def scrape_jobs_route_excel():
    try:
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin",  "glassdoor"],
            search_term="software engineer",
            location="Dallas, TX",
            results_wanted=10,
            country_indeed='USA'  # only needed for indeed / glassdoor
        )
        print(f"Found {len(jobs)} jobs")
        print(jobs.head())
        jobs.to_excel("jobs.xlsx", index=False)  # Save as Excel
        return send_file('jobs.xlsx', as_attachment=True)  # Return the Excel file as a download
    except Exception as e:
        return jsonify({'error': str(e)}), 500 # Return the Excel file as a download







if __name__ == "__main__":
    app.run(debug=True)