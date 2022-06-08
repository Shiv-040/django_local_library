from django.contrib import admin

#Register your models here.
#Import models from the models.py file
from .models import Author, Book, Genre, BookInstance, Language
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

#Admin Class definition for Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]    

#Register the Admin Class with the associated model
#admin.site.register(Author, AuthorAdmin)



#Inline class to provide a BookInstance form inline with the BookAdmin
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

#Admin Class definition for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


#Register the Admin Class with the associated model
#admin.site.register(Book, BookAdmin)

#Admin Class definition for BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter=('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


