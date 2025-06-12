from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    handicap = models.IntegerField(default=0)

    def __str__(self):
        return self.username



class Round(models.Model):
    holes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    nine_par = models.IntegerField(default=0)
    full_par = models.IntegerField(default=0)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'id'], name='unique_round_per_user')
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save first so related holes exist
        # Recalculate scores and pars
        holes = self.hole_set.all()
        self.score = sum(h.score for h in holes)
        self.full_par = sum(h.par for h in holes)
        self.nine_par = sum(h.par for h in holes[:9])
        self.holes = holes.count()
        super().save(update_fields=['score', 'full_par', 'nine_par', 'holes'])

    def __str__(self):
        return f"Round {self.id} by {self.user.username} on {self.date}"


class Hole(models.Model):
    hole = models.IntegerField(blank=True, null=True)
    par = models.IntegerField()
    score = models.IntegerField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['round', 'hole'], name='unique_hole_per_round')
        ]

    def save(self, *args, **kwargs):
        if self.hole is None:
            existing = Hole.objects.filter(round=self.round).order_by('hole')
            if existing.exists():
                last = existing.last()
                self.hole = last.hole + 1
            else:
                self.hole = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Hole {self.hole} ({self.par} par, {self.score} strokes)"
