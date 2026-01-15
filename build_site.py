html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ENOFFMUS | Official Website</title>
<style>
body{margin:0;font-family:Arial,sans-serif;background:#000;color:#fff;}
header{display:flex;justify-content:space-between;align-items:center;padding:16px;background:rgba(0,0,0,0.85);}
header img{height:50px;}
nav a{margin-left:20px;color:#fff;text-decoration:none;font-weight:600;}
.hero{height:80vh;display:grid;place-items:center;text-align:center;background:radial-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.9)), url('background.jpg') center/cover no-repeat;}
.hero img{max-width:520px;width:80%;margin-bottom:24px;}
.btn{display:inline-block;padding:14px 26px;border:2px solid #fff;color:#fff;font-weight:700;text-decoration:none;margin:8px;}
.btn:hover{background:#fff;color:#000;}
section{padding:80px 24px;}
.card{background:#111;padding:24px;margin-bottom:24px;}
footer{padding:32px 24px;text-align:center;color:#bfbfbf;}
</style>
</head>
<body>
<header>
<img src="logo.png" alt="ENOFFMUS Logo">
<nav><a href='#music'>MUSIC</a><a href='#shop'>SHOP</a><a href='#contact'>CONTACT</a></nav>
</header>
<main>
<section class="hero"><img src="logo.png"><div><a class="btn" href="#music">LISTEN</a><a class="btn" href="https://enoffmus-ptp-shop.fourthwall.com/" target="_blank">MERCH</a></div></section>
<section id="music"><h2>VIDEOS</h2><div class="card"><iframe width="100%" height="315" src="https://www.youtube.com/embed?listType=user_uploads&list=Enoffmus" frameborder="0" allowfullscreen></iframe></div></section>
<section id="shop"><h2>SHOP</h2><div class="card"><a class="btn" href="https://enoffmus-ptp-shop.fourthwall.com/" target="_blank">GO TO SHOP</a></div></section>
<section id="contact"><h2>CONTACT</h2><div class="card"><p>Email: <a href="mailto:contact.enoffmus@gmail.com">contact.enoffmus@gmail.com</a></p></div></section>
</main>
<footer><a href="https://www.youtube.com/@Enoffmus" target="_blank">YouTube</a> | <a href="https://www.instagram.com/Enoffmus" target="_blank">Instagram</a><p>© ENOFFMUS</p></footer>
</body>
</html>
"""
with open("index.html","w") as f: f.write(html)
print("index.html created!")
