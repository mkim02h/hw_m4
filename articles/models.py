from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    image = models.ImageField(null=True, upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
 
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('-created_at', 'id')

class Category(models.Model):
    name = models.CharField(max_length = 255)

class Comment(models.Model):
    article = models.ForeignKey("Article", on_delete=models.SET_NULL, null=True, related_name='comments')
    author_name = models.CharField(max_length = 255, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.author_name}: {self.text[:30]}"



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