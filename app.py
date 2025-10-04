from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, os, random, secrets
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
DB_NAME = "database.db"

# ---------- Email (Gmail) Config ----------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'yourgmail@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'your_app_password_here')
mail = Mail(app)

email_otps = {}
email_tokens = {}

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ---------- Database ----------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT UNIQUE,
                    password TEXT
                )''')

    columns_to_add = {
        "phone": "TEXT",
        "phone_verified": "INTEGER DEFAULT 0",
        "email_verified": "INTEGER DEFAULT 0",
        "selfie_path": "TEXT",
        "age": "INTEGER",
        "gender": "TEXT",
        "personality": "TEXT",
        "fun_secrets": "TEXT",
        "languages": "TEXT",
        "zodiac": "TEXT",
        "spirituality": "TEXT",
        "relationship_status": "TEXT",
        "location": "TEXT"
    }

    c.execute("PRAGMA table_info(users)")
    existing_cols = [col[1] for col in c.fetchall()]
    for col, col_type in columns_to_add.items():
        if col not in existing_cols:
            c.execute(f"ALTER TABLE users ADD COLUMN {col} {col_type}")

    c.execute('''CREATE TABLE IF NOT EXISTS vibes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    vibe TEXT,
                    activity TEXT,
                    date TEXT,
                    start_time TEXT,
                    end_time TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )''')
    conn.commit()
    conn.close()

init_db()

# ---------- Helper ----------
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------- Pages ----------
@app.route('/')
def splash():
    return render_template("splash.html")

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/confirm_identity')
def confirm_identity_page():
    return render_template("confirm_identity.html")

@app.route('/confirm_success')
def confirm_success_page():
    return render_template("confirm_success.html")

@app.route('/verify_email_sent')
def verify_email_sent_page():
    return render_template("verify_email_sent.html")

@app.route('/verify_success')
def verify_success_page():
    return render_template("verify_success.html")

@app.route('/verify_otp', methods=["GET","POST"])
def verify_otp_page():
    if request.method == "POST":
        otp = request.form['otp']
        email = session.get('otp_email')
        if email in email_otps and email_otps[email] == otp:
            # Update user as verified
            conn = get_db_connection()
            c = conn.cursor()
            c.execute("UPDATE users SET email_verified = 1 WHERE email = ?", (email,))
            conn.commit()
            conn.close()
            
            # Clear OTP from memory
            del email_otps[email]
            session.pop('otp_email', None)
            
            return redirect(url_for('verify_success_page'))
        else:
            return render_template("verify_otp.html", error="Invalid OTP. Please try again.")
    return render_template("verify_otp.html")

# ---------- Auth ----------
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form.get('phone')
        conn = get_db_connection()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (name,email,password,phone) VALUES (?,?,?,?)", (name,email,password,phone))
            conn.commit()
            conn.close()
            session['temp_signup_email'] = email
            return redirect(url_for('otp'))
        except sqlite3.IntegrityError:
            conn.close()
            return "Email already exists!"
    return render_template("signup.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email,password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user_id'] = user['id']
            return redirect(url_for("vibe_form"))
        else:
            return "Invalid credentials!"
    return render_template("login.html")

@app.route('/otp', methods=["GET","POST"])
def otp():
    if request.method == "POST":
        email = request.form['email']
        otp = str(random.randint(100000,999999))
        email_otps[email] = otp
        try:
            msg = Message("Your Fiunite OTP", sender=app.config['MAIL_USERNAME'], recipients=[email])
            msg.body = f"Your Fiunite OTP is: {otp}"
            mail.send(msg)
        except Exception as e:
            print("Mail error:", e)
            return f"Error sending email: {e}"
        session['otp_email'] = email
        return redirect(url_for('verify_otp_page'))
    prefill = session.get('temp_signup_email', '')
    return render_template("otp.html", prefill=prefill)

@app.route('/vibe_form', methods=["GET","POST"])
def vibe_form():
    if 'user_id' not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        vibe = request.form['vibe']
        activity = request.form['activity']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("INSERT INTO vibes (user_id,vibe,activity,date,start_time,end_time) VALUES (?,?,?,?,?,?)",
                  (session['user_id'],vibe,activity,date,start_time,end_time))
        conn.commit()
        conn.close()
        return redirect(url_for("vibe"))
    return render_template("vibe_form.html")

@app.route('/vibe')
def vibe():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT users.name, vibes.vibe, vibes.activity, vibes.date, vibes.start_time, vibes.end_time FROM vibes JOIN users ON vibes.user_id=users.id")
    data = c.fetchall()
    conn.close()
    return render_template("vibe.html", vibes=data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("splash"))

# ---------- Run ----------
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
