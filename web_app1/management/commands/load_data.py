from django.core.management.base import BaseCommand
from web_app1.models import *


class Command(BaseCommand):
    help = 'Load Animal and Breed'

    def handle(self, *args, **kwargs):

        animal_names = ['Dog', 'Cat', 'Bird', 'Rabbit']

        if not Animal.objects.count():
            for animal_name in animal_names:
                Animal.objects.create(name=animal_name)

        dog = Animal.objects.get(name="Dog")

        dog_breed = ['Labrador', 'German Shepherd', 'Golden Retriever', 'Bulldog', 'Beagle', 'Boxer', 'Dachshund',
                     'Great Dane']

        for breed in dog_breed:
            Breed.objects.create(name=breed, animal=dog)

        cat = Animal.objects.get(name="Cat")

        cat_breeds = ['Bengal', 'Bombay', 'Persian', 'Russian', 'Savannah', 'Siamese', 'Sphynx']

        for cat_breed in cat_breeds:
            Breed.objects.create(name=cat_breed, animal=cat)

        bird = Animal.objects.get(name="Bird")

        bird_breeds = ['Woodpecker', 'Pigeon', 'Peacock', 'Rooster', 'Vulture', 'Swallow', 'Seagull','Quail','Duck','Pelican','Magpie','Parrot','Turkey','Crane','Kingfisher','Hummingbird','Sparrow','Cormorant','Ostrich','Crow']

        for bird_breed in bird_breeds:
            Breed.objects.create(name=bird_breed, animal=bird)

        rabbit = Animal.objects.get(name="Rabbit")

        rabbit_breeds = ['Tan', 'Jersey Wooly', 'English Lop', 'Beveren', 'Chinchilla', 'Himalayan', 'Belgian','Sable','Silver Fox']

        for rabbit_breed in rabbit_breeds:
            Breed.objects.create(name=rabbit_breed, animal=rabbit)
