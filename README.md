## Flask Application Design for 數位錶款的錶面設計

### HTML Files

**index.html**

- **Purpose:** Main HTML file that displays the digital watch face.
- **Content:**
    - HTML markup to define the watch face's structure and appearance.
    - JavaScript code to handle the timekeeping and display logic.

### Routes

**main.py**

- **Purpose:** Flask web application logic.
- **Routes:**
    - **GET /:** Renders the `index.html` file, which displays the digital watch face.
    - **POST /set_time:** Accepts a POST request with a new time as a parameter, then updates the watch face with the new time.