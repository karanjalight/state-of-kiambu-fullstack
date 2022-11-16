from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model


# Create your models here.


TOPICS = (
    ('News', 'News'),
    ('Markets', 'Markets'),
    ('Politics', 'Politics'),
    ('Fiction-and-Poetry', 'Fiction and Poetry'),
    ('Books-and-Culture', 'Books and Culture'),
    ('Humour-and-Cartoons', 'Humour and Cartoons'),
    ('Puzzles-and-Games', 'Puzzles and Games'),
    ('Style', 'Style'),
        
)

TOPICS_CATEGORIES =(
  #markets
  ('MD', 'Market Data TSK Money'),
  ('CR', 'Commercial Real Estate'),
  ('CF', 'Commodities and Futures'),
  ('SJ', 'Stocks and Juacali'),

  #politics
  ('D', 'Diplomacy '),
  ('ES', 'Eighty-Sixed'),
  ('CL', 'Courts and Law'),

  #books and culture
  ('B', 'Books'),
  ('TM', 'TV and Music'),
  ('F', 'Food')

)

class article(models.Model):
  slug = models.CharField( primary_key=True ,max_length=50, null=False, blank=False, help_text="This is a unique identifier. It should be Unique for every article")
  menu = models.CharField(choices=TOPICS, max_length=20, help_text="This are the menu items, Be cautious as it affects how the article is displayed in the front end")
  article_category = models.CharField(choices=TOPICS_CATEGORIES, blank=True, max_length=20, null=True, help_text="if the is no article category just leave blank")
  article_name = models.CharField(max_length=250, null=False, help_text="Can be Same as the Slug" )
  image = models.ImageField(upload_to ='uploads/')
  article = models.CharField(max_length=1500, blank=False, help_text='To separate paragraphs, use the tag <br> between to represent a space between the paragraphs') 
  



  def __str__(self):
    return self.article_name
