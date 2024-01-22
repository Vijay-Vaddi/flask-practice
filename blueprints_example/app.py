# same level as project folder, not inside. 

from adoption_site_project import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

# function to check bluprint url mapping : for debugging
# def print_registered_urls():
#     print("Registered URLs/views:")
#     for rule in app.url_map.iter_rules():
#         print(f"URL: {rule}, Endpoint: {rule.endpoint}")

if __name__ == '__main__':
    # print_registered_urls()
    app.run(debug=True)

    
