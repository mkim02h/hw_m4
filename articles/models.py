from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()
 
    def __str__(self) -> str:
        return self.title




# # CRUD

# # C - create
# #INSERT INTO (fields) VALUES (1, 2))
# num_1 = Article(title="title_1", text="text_1", rate=1)
# num_1.save()
# num_2 = Article.objects.create(title="title_2", text="text_2", rate=2)

# # R - read
# #SELECT fields FROM table_name WHERE field = expression;
# articles = Article.objects.all()    #all - все записи
# articles = Article.objects.order_by('id').all().last()   #filter - фильтр по условию
# articles = Article.objects.get(id=1)   #get - получить одну запись по условию

# # U - update
# #UPDATE table_name SET field = 'value' WHERE id = 1;
# article.text = "new_text"
# article.save()

# # D - delete
# #DELETE FROM table_name WHERE expression;
# article.delete()