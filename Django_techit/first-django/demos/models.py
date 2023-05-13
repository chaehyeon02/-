from django.db import models

# Create your models here.
class Comment(models.Model) {
    content = models.TextField(verbose_name='내용')
    created_at = models.DataTimeField(verbose_name='작성일')
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=true, blank=true)
}