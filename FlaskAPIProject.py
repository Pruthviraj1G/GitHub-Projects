from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pruthviraj Girase — Resume</title>
  <style>
    :root{--accent:#0ea5a4;--muted:#6b7280;font-family:Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial}
    *{box-sizing:border-box}
    body{font-family:var(--font, Inter), sans-serif;margin:0;background:#f7fafc;color:#0f172a;line-height:1.45}
    .container{max-width:900px;margin:32px auto;background:#fff;border-radius:12px;box-shadow:0 8px 30px rgba(2,6,23,.07);overflow:hidden}
    header{display:flex;gap:20px;padding:28px;border-bottom:1px solid #eef2f7}
    .avatar{flex:0 0 110px;height:110px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#60a5fa);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:28px}
    .head-info{flex:1}
    h1{margin:0;font-size:22px}
    .meta{color:var(--muted);margin-top:6px;font-size:14px}
    .layout{display:grid;grid-template-columns:1fr 320px}
    main{padding:28px}
    aside{background:#fbfdff;border-left:1px solid #eef2f7;padding:28px}
    section{margin-bottom:20px}
    h2{font-size:14px;margin:0 0 10px 0;color:#0f172a}
    p.lead{margin:0;color:var(--muted)}
    .detail-list{list-style:none;padding:0;margin:0}
    .detail-list li{margin:6px 0;color:var(--muted);font-size:14px}
    .edu-item{margin-bottom:12px}
    .skill-badge{display:inline-block;padding:6px 10px;border-radius:999px;border:1px solid #e6eef2;margin:6px 6px 0 0;font-size:13px;background:#fff}
    .project{padding:12px;border-radius:8px;border:1px solid #f1f5f9;margin-bottom:10px}
    .contact a{color:var(--accent);text-decoration:none}
    .print-hide{display:inline-block}
    @media(max-width:880px){.layout{grid-template-columns:1fr}.avatar{display:none}.print-hide{display:none}}
    @media print{body{background:#fff} .container{box-shadow:none;border-radius:0} aside{display:none}}
  </style>
</head>
<body>
  <div class="container" role="document">
    <header>
      <div class="avatar">PG</div>
      <div class="head-info">
        <h1>Pruthviraj Girase</h1>
        <div class="meta">Pursuing B.Tech — CSE (AIML) • Email: pruthvirajgirase108@gmail.com • • Vivekananda Global University • Age 19</div>
        <p class="lead" style="margin-top:12px">Motivated CSE (AIML) undergraduate with foundational knowledge in algorithms, data structures and machine learning basics. Interested in practical AI projects, coding and problem solving. Seeking internships and hands-on learning opportunities.</p>
      </div>
    </header>

    <div class="layout">
      <main>
        <section>
          <h2>Education</h2>
          <div class="edu-item">
            <strong>B.Tech — Computer Science & Engineering (AIML)</strong>
            <div class="meta">Vivekananda Global University</div>
            <div class="meta">Currently pursuing</div>
          </div>
        </section>

        <section>
          <h2>Skills</h2>
          <div>
            <span class="skill-badge">Python</span>
            <span class="skill-badge">C / C++</span>
            <span class="skill-badge">Machine Learning (basics)</span>
            <span class="skill-badge">Data Structures</span>
            <span class="skill-badge">SQL</span>
            <span class="skill-badge">Git</span>
          </div>
        </section>

        <section>
          <h2>Projects</h2>
          <div class="project">
            <strong>Project Title — Short Description</strong>
            <div class="meta">Technologies: Python, (add libraries)</div>
            <p style="margin:8px 0 0">A short 1–2 line summary of a project you worked on. Replace this placeholder with your real project details.</p>
          </div>
          <div class="project">
            <strong>Project Title — Short Description</strong>
            <div class="meta">Technologies: (list)</div>
            <p style="margin:8px 0 0">Another brief description. Add links or GitHub repos in the contact section if you have them.</p>
          </div>
        </section>

        <section>
          <h2>Achievements & Activities</h2>
          <ul class="detail-list">
            <li>Participated in CodeRed Hackathon</li>
            <li>Participated in Metaminds Hackathon</li>
            <li>Participated in National Project Exhibition</li>
          </ul>
        </section>

      </main>

      <aside>
        <section class="contact">
          <h2>Contact</h2>
          <ul class="detail-list">
            <li>Email: <a href="mailto:pruthvirajgirase108@gmail.com">your.email@example.com</a></li>
            <li>Phone: +91-9373954253</li>
            <li>Location: India</li>
            <li>LinkedIn: linkedin.com/in/yourprofile</li>
            <li>GitHub: github.com/yourusername</li>
          </ul>
        </section>

        <section>
          <h2>Profile</h2>
          <p class="meta">A concise professional summary that you can edit — mention strengths, career objective or the kind of internships you're seeking.</p>
        </section>

        <section>
          <h2>Languages</h2>
          <ul class="detail-list">
            <li>English — Fluent</li>
            <li>Hindi / Marathi — Native</li>
          </ul>
        </section>

        <section>
          <h2>Interests</h2>
          <p class="meta">AI / Machine Learning, Competitive Programming, Open Source, Robotics</p>
        </section>
         <section>
                      <h2>More</h2>
                      <button onclick="window.location.href='http://localhost:8888/notebooks/Project.ipynb'">
                        View My Codes
                      </button>
                    </section>

      </aside>
    </div>
  </div>
                     

</body>
</html>

    """
@app.route("/about")
def about():
    return """
    <h1> I am About page </h1>
    <h2> I am running in flask</h2>
    """
if __name__=='__main__':
    app.run()