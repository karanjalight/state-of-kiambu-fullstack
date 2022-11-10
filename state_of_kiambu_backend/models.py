from django.db import models

# Create your models here.


TOPICS = (
    ('N', 'News'),
    ('M', 'Markets'),
    ('P', 'Politics'),
    ('FP', 'Fiction and Poetry'),
    ('BC', 'Books and Culture'),
    ('HC', 'Humour and Cartoons'),
    ('PG', 'Puzzles and Games'),
    ('S', 'Style'),
        
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
  Menu = models.CharField(choices=TOPICS, max_length=20, help_text="This are the menu items, Be cautious as it affects how the article is displayed in the front end")
  article_category = models.CharField(choices=TOPICS_CATEGORIES, blank=True, max_length=20, null=True, help_text="if the is no article category just leave blank")
  article_name = models.CharField(max_length=250, null=False, help_text="Can be Same as the Slug" )
  image = models.ImageField(upload_to ='uploads/')
  article = models.CharField(max_length=1500, blank=False, help_text='To separate paragraphs, use the tag <br> between to represent a space between the paragraphs') 
  



  def __str__(self):
    return self.article_name
