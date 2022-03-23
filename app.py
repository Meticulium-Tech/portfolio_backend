from flask import Flask, render_template, request
from models.book import Book
from models.service import Service

from models.skill import Skill
app = Flask(__name__)

# two decorators, same function


@app.route('/')
def index():
    writen_books = [
        Book("Daily Business Quotes", "quote-book.png", "lorem ipsum dolor"),
        Book("Power of Association", "power-ass.png", "lorem ipsum dolor"),
        Book("The Baby Genius", "baby-genius.png", "lorem ipsum dolor"),
        Book("Power of Association", "power-ass.png", "lorem ipsum dolor"),
        Book("Daily Business Quotes", "quote-book.png", "lorem ipsum dolor"),
        Book("The Baby Genius", "baby-genius.png", "lorem ipsum dolor"),
    ]
    offered_services = [
        Service("Team Relationship building", "This Training brings to the underline understanding of teams the importance of little droplets of energies that can illuminate productivity. Best for already established Brands to better ensure team growth for productivity", "icon flaticon-writing"),
        Service("Customer Relationship Management", "With over a decade of schooled and practical experience, an understanding of service is used to fertilize your team as they connect with your clients", "icon flaticon-focus-l"),
        Service("Brand Optimization", "Awareness using brand content will keep your business always ahead of your competitors, we help you message right", "icon flaticon-writing"),
        Service("Coaching", "The main purpose of coaching involves developing leadership, creating self-discipline, building a self-belief system, creating motivation, and improving self-awareness. Our goal is performance maximization by helping clients reach thier peak potential.", "icon flaticon-writing"),
        Service("Training", "International 24 hours online Training with over 2million attendees on transformational workplace behavior (Women in leadership Conference world) •Till date transformational Trainer at Customs Cameroon on behavioral Habits & Team Relationship Management", "icon flaticon-writing"),
        Service("Media Content Creation", "Content helps you attract, engage, and delight prospects and customers, bring new visitors to your site, and ultimately, generate revenue for your company. In other words, if you’re not creating content, then you’re behind the curve.", "icon flaticon-writing"),
    ]
    top_skills = [
        Skill("Brand Therapist", 100),
        Skill("CEO", 100),
        Skill("Transformational", 100),
        Skill("Personnal Development Expert", 100),    
        Skill("Course Producer", 100),
        Skill("Business consultant", 100),
        Skill("On Air Personality", 100),
        Skill("Keynote Speaker", 100),
        
    ]
    
    education = []
    return render_template('index.html', books=writen_books, services=offered_services, skills=top_skills)


@app.route('/post')
def post():
    return render_template('post.html', the_title='Tiger As Symbol')


@app.route('/arduino', methods = ['POST', 'GET'])
def arduino():
    if(request.method == 'POST'):
        return render_template('post.html')
    return "Hello Mboa waste"


if __name__ == '__main__':
    app.run(debug=True)
