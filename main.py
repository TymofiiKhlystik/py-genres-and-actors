import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    name_genres = "Western", "Action", "Dramma"
    name_actor = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for item  in name_genres:
        Genre.objects.create(name=item)

    for item_first, item_last in name_actor:
        Actor.objects.create(
            first_name=item_first,
            last_name=item_last
        )




if __name__ == "__main__":
    main()
    print(main())
    # <QuerySet [<Actor: Jaden Smith>, <Actor: Will Smith>]>

    print(Genre.objects.all())
    # <QuerySet [<Genre: Western>, <Genre: Drama>]>

    print(Actor.objects.all())